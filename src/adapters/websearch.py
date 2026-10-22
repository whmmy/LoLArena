"""Unified web_search tool — mounted on EVERY model.

Fairness contract: all models call the SAME tool backed by the SAME search
engine. The engine is a single GLOBAL choice — never a per-model setting:

  * ``deepseek`` (default) — DeepSeek's in-house Search API
    (``POST https://api.deepseek.com/v1/tools/search``), ~1s/query, billed per
    successful request. Key: ``DEEPSEEK_WEBSEARCH_API_KEY`` or ``DEEPSEEK_API_KEY``.
  * ``zhipu`` (legacy) — Zhipu / Z.AI ``/paas/v4/web_search`` (``search_pro``
    engine). Kept for A/B comparison and as a fallback.

Pick the engine with ``LOLA_WEBSEARCH_PROVIDER`` (or ``web_search.provider`` in
``configs/policy.yaml``). Both backends are normalised to the same compact
result shape, so the tool schema the models see, the digest fed back into the
conversation, and the provenance log are identical regardless of engine.

This module exposes:
  - WebSearchTool: executes a query against the configured engine
  - TOOL_OPENAI / TOOL_ANTHROPIC / TOOL_GEMINI: provider-specific schemas
"""

from __future__ import annotations

import json
import re
import time
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any

import httpx

from .. import config as cfg

# Tool name every model sees.
TOOL_NAME = "web_search"
TOOL_DESC = (
    "Search the live web for up-to-date esports news, match results, team form, "
    "roster changes, patch/meta analysis, and head-to-head history. Returns a list "
    "of results each with title, summary (content), link, source site, and publish "
    "date. Use this to gather evidence you cannot derive from the injected match "
    "data. Issue focused queries (team + opponent + context), e.g. "
    "'T1 vs Gen.G LCK 2026 Spring final prediction'. Search operators work inside "
    "the query: site:liquipedia.net, -site:example.com, \"exact phrase\", "
    "lang:zh,en, after:2026-01-01, before:2026-06-01."
)

# JSON-schema for the tool arguments (provider-agnostic).
ARGS_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "query": {
            "type": "string",
            "description": "The search query. Keep under 70 characters; be specific.",
        },
        "count": {
            "type": "integer",
            "description": "Number of results to return (1-50). Default 8.",
            "default": 8,
            "minimum": 1,
            "maximum": 50,
        },
        "recency": {
            "type": "string",
            "description": (
                "Optional publication-date filter. 'noLimit' (default) searches "
                "all time and gives the best recall; a narrower window drops "
                "pages whose publish date is unknown (forums, wikis, tier "
                "lists), so use one only when you need breaking news."
            ),
            "enum": ["oneDay", "oneWeek", "oneMonth", "oneYear", "noLimit"],
            "default": "noLimit",
        },
    },
    "required": ["query"],
}

# ---------- provider-specific tool declarations ----------

TOOL_OPENAI = {  # OpenAI / DeepSeek / Qwen / Kimi / GLM / Moonshot (function-calling)
    "type": "function",
    "function": {
        "name": TOOL_NAME,
        "description": TOOL_DESC,
        "parameters": ARGS_SCHEMA,
    },
}

TOOL_ANTHROPIC = {  # Claude
    "name": TOOL_NAME,
    "description": TOOL_DESC,
    "input_schema": ARGS_SCHEMA,
}

TOOL_GEMINI = {  # Gemini (functionDeclarations item)
    "name": TOOL_NAME,
    "description": TOOL_DESC,
    "parameters": ARGS_SCHEMA,
}

# ---------- engine constants ----------

PROVIDER_DEEPSEEK = "deepseek"
PROVIDER_ZHIPU = "zhipu"
PROVIDERS = (PROVIDER_DEEPSEEK, PROVIDER_ZHIPU)
DEFAULT_PROVIDER = PROVIDER_DEEPSEEK

# How many chars of each result's summary we feed back to the model. DeepSeek's
# "summary" is 600-2600 chars; Zhipu's "content" is already ~600. Keeping the
# cap identical across engines keeps the prompt budget stable.
CONTENT_CHARS = 600

# Max query length accepted by each engine (includes any date operator we add).
_MAX_QUERY_LEN = {PROVIDER_DEEPSEEK: 128, PROVIDER_ZHIPU: 70}

# recency enum -> lookback window for the engine-side date filter.
_RECENCY_DAYS = {"oneDay": 1, "oneWeek": 7, "oneMonth": 30, "oneYear": 365}

# A query that already carries an explicit date operator keeps it; we never
# append a second (conflicting) one.
_DATE_OP_RE = re.compile(r"\b(?:after|before):\s*\d{4}", re.IGNORECASE)

# Transient HTTP statuses worth one retry (search is read-only, so retrying is safe).
_RETRY_STATUS = {408, 429, 500, 502, 503, 504}


class WebSearchTool:
    """Executes a web_search query via the configured engine (one per run).

    Records every call (query, params, full results, timestamp) into ``self.log``
    so the run can persist it for provenance / audit. Also memoizes within a
    run: an identical (query, count) is served from cache instead of hitting the
    engine twice.
    """

    def __init__(self, api_key: str | None = None, base_url: str | None = None,
                 engine: str | None = None, timeout: float = 30.0,
                 provider: str | None = None, proxy: str | None = None,
                 transport: httpx.BaseTransport | None = None):
        cfg.load_env()
        self.provider = self._resolve_provider(provider)
        self.timeout = timeout
        self.transport = transport
        # Explicit proxy wins; otherwise proxies.yaml / env (websearch block).
        # trust_env is disabled so ambient HTTP(S)_PROXY settings never silently
        # reroute the search backend.
        self.proxy = proxy or cfg.proxy_for("websearch")

        if self.provider == PROVIDER_DEEPSEEK:
            self.api_key = (api_key or cfg.env("DEEPSEEK_WEBSEARCH_API_KEY")
                            or cfg.env("DEEPSEEK_API_KEY"))
            base = (base_url or cfg.env("DEEPSEEK_WEBSEARCH_BASE_URL")
                    or "https://api.deepseek.com/v1").rstrip("/")
            if not base.endswith("/v1"):
                base += "/v1"
            self.base_url = base
            self.engine = engine or "deepseek_search"
            key_hint = "DEEPSEEK_WEBSEARCH_API_KEY (or DEEPSEEK_API_KEY)"
        else:
            self.api_key = (api_key or cfg.env("ZHIPU_WEBSEARCH_API_KEY")
                            or cfg.env("ZHIPU_API_KEY"))
            self.base_url = (base_url or cfg.env("ZHIPU_WEBSEARCH_BASE_URL")
                             or "https://open.bigmodel.cn/api").rstrip("/")
            self.engine = engine or cfg.env("ZHIPU_WEBSEARCH_ENGINE") or "search_pro"
            key_hint = "ZHIPU_WEBSEARCH_API_KEY (or ZHIPU_API_KEY)"

        if not self.api_key:
            raise RuntimeError(
                f"{key_hint} is not set. The shared web_search tool requires it. "
                f"(provider={self.provider}; set LOLA_WEBSEARCH_PROVIDER=zhipu "
                f"to switch to the legacy Zhipu backend.)"
            )
        self.call_count = 0
        self.queries: list[str] = []
        self.log: list[dict[str, Any]] = []     # provenance log (every call)
        self._memo: dict[str, list[dict[str, Any]]] = {}
        self._http: httpx.Client | None = None

    # ---------- setup helpers ----------

    @staticmethod
    def _resolve_provider(provider: str | None) -> str:
        """Explicit arg > LOLA_WEBSEARCH_PROVIDER > policy.yaml > default."""
        candidates = [
            provider,
            cfg.env("LOLA_WEBSEARCH_PROVIDER"),
            ((cfg.policy().get("web_search") or {}).get("provider")),
            DEFAULT_PROVIDER,
        ]
        for name in candidates:
            if name and str(name).strip():
                value = str(name).strip().lower()
                if value not in PROVIDERS:
                    raise ValueError(
                        f"Unknown web_search provider {value!r}; "
                        f"expected one of {PROVIDERS}."
                    )
                return value
        return DEFAULT_PROVIDER

    def _client(self) -> httpx.Client:
        """Lazily create ONE keep-alive client per tool (one per model run).

        Reusing the connection pool removes a TCP+TLS handshake from every
        search (up to max_calls_per_prediction per model per match).
        """
        if self._http is None:
            kwargs: dict[str, Any] = {"timeout": self.timeout, "trust_env": False}
            if self.transport is not None:
                kwargs["transport"] = self.transport
            elif self.proxy:
                kwargs["proxy"] = self.proxy
            self._http = httpx.Client(**kwargs)
        return self._http

    def close(self) -> None:
        """Release the connection pool. Safe to call more than once."""
        if self._http is not None:
            self._http.close()
            self._http = None

    def __enter__(self) -> "WebSearchTool":
        return self

    def __exit__(self, *exc: Any) -> None:
        self.close()

    # ---------- query construction ----------

    def build_query(self, query: str, recency: str) -> str:
        """Normalise + cap a query, adding an engine date filter when requested.

        DeepSeek's Search API has no ``recency`` parameter; its query language
        supports ``after:YYYY-MM-DD`` instead. We only add the operator when the
        model explicitly asked for a window (recency != noLimit) and the query
        does not already contain a date operator. Default searches stay
        unfiltered on purpose: ``after:`` drops every page whose publish date is
        unknown (forums, wikis), which measurably lowers result quality.
        """
        limit = _MAX_QUERY_LEN[self.provider]
        q = " ".join((query or "").split())[:limit]
        if not q or self.provider != PROVIDER_DEEPSEEK:
            return q
        days = _RECENCY_DAYS.get(recency or "noLimit")
        if not days or _DATE_OP_RE.search(q):
            return q
        since = datetime.now(timezone.utc) - timedelta(days=days)
        operator = f" after:{since:%Y-%m-%d}"
        room = limit - len(operator)
        if room < 16:  # no useful query left -> fall back to an unfiltered search
            return q
        return q[:room].rstrip() + operator

    # ---------- one search ----------

    def __call__(self, query: str, count: int = 8,
                 recency: str = "noLimit") -> list[dict[str, Any]]:
        """Run a single search. Returns compact result dicts.

        Compact shape (stable across providers, extra keys optional):
            [{title, content, link, media, publish_date, score?, authority?}]
        """
        query = (query or "").strip()
        if not query:
            return []

        recency = (recency or "noLimit").strip()
        if recency not in _RECENCY_DAYS:
            recency = "noLimit"
        n = max(1, min(50, int(count or 8)))
        sent_query = self.build_query(query, recency)
        if not sent_query:
            return []

        # Recency is part of the key: for Zhipu it is a request field (not folded
        # into the query), and cached results must not leak across windows.
        memo_key = f"{sent_query}|{n}|{recency}"
        if memo_key in self._memo:
            # repeated query in the same run -> serve cached, still log it
            cached = self._memo[memo_key]
            self._record(sent_query, n, recency, cached, cached=True)
            return cached

        self.queries.append(sent_query)
        self.call_count += 1

        headers = {"Authorization": f"Bearer {self.api_key}",
                   "Content-Type": "application/json"}
        payload = self._payload(sent_query, n, recency)
        error_note: str | None = None
        try:
            resp = self._post(self._url(), payload, headers)
            compact, error_note = self._parse(resp)
        except httpx.HTTPError as e:
            # Soft-fail: a flaky search must never take down the whole prediction.
            note = f"network: {type(e).__name__}: {e}"
            compact = [self._error_hit(note)]
            error_note = note[:300]

        # Only cache successful results: caching an error (429, network blip)
        # would poison every later attempt at the same query in this run.
        if error_note is None:
            self._memo[memo_key] = compact
        self._record(sent_query, n, recency, compact, error=error_note)
        return compact

    def _url(self) -> str:
        if self.provider == PROVIDER_DEEPSEEK:
            return f"{self.base_url}/tools/search"
        return f"{self.base_url}/paas/v4/web_search"

    def _payload(self, query: str, count: int, recency: str) -> dict[str, Any]:
        if self.provider == PROVIDER_DEEPSEEK:
            # need_content=False: the structured `summary` (600-800 chars, written
            # for models) is what we feed back; full page markdown would blow up
            # the prompt budget without adding signal.
            return {"query": query, "count": count, "need_content": False}
        return {
            "search_query": query,
            "search_engine": self.engine,
            "search_intent": True,
            "count": count,
            "search_recency_filter": recency or "noLimit",
            "content_size": "medium",
            "request_id": uuid.uuid4().hex,
        }

    def _post(self, url: str, payload: dict[str, Any],
              headers: dict[str, str], *, attempts: int = 2) -> httpx.Response:
        """POST with one retry on transient failures (timeouts / 429 / 5xx)."""
        last_exc: httpx.HTTPError | None = None
        for attempt in range(attempts):
            try:
                resp = self._client().post(url, json=payload, headers=headers)
            except httpx.HTTPError as e:
                last_exc = e
                if attempt + 1 >= attempts:
                    raise
                time.sleep(0.8)
                continue
            if resp.status_code in _RETRY_STATUS and attempt + 1 < attempts:
                delay = _retry_after_seconds(resp)
                time.sleep(min(delay if delay is not None else 0.8, 3.0))
                continue
            return resp
        raise last_exc or RuntimeError("web_search request failed")

    # ---------- response normalisation ----------

    def _parse(self, resp: httpx.Response) -> tuple[list[dict[str, Any]], str | None]:
        if resp.status_code != 200:
            note = f"http {resp.status_code}: {resp.text[:300]}"
            return [self._error_hit(note, f"[web_search error {resp.status_code}]")], note

        try:
            data = resp.json()
        except ValueError:
            note = f"http 200 with non-JSON body: {resp.text[:300]}"
            return [self._error_hit(note)], note

        if isinstance(data, dict) and data.get("error"):
            err = data["error"]
            message = err.get("message") if isinstance(err, dict) else err
            note = str(message or err)[:300]
            return [self._error_hit(note)], note

        if self.provider == PROVIDER_DEEPSEEK:
            raw = (data or {}).get("results") or []
            compact = [self._compact_deepseek(r) for r in raw if isinstance(r, dict)]
        else:
            raw = (data or {}).get("search_result") or []
            compact = [{
                "title": r.get("title", ""),
                "content": (r.get("content") or "")[:CONTENT_CHARS],
                "link": r.get("link", ""),
                "media": r.get("media", ""),
                "publish_date": r.get("publish_date", ""),
            } for r in raw if isinstance(r, dict)]
        return compact, None

    @staticmethod
    def _compact_deepseek(r: dict[str, Any]) -> dict[str, Any]:
        content = (r.get("summary") or r.get("snippet") or r.get("content") or "").strip()
        out: dict[str, Any] = {
            "title": r.get("title") or "",
            "content": content[:CONTENT_CHARS],
            "link": r.get("url") or "",
            "media": r.get("site_name") or "",
            "publish_date": (r.get("date") or "")[:10],
        }
        # Extra provenance (ignored by format_results_for_model, kept in the log
        # so search quality can be audited / compared across engines later).
        if r.get("rerank_score") is not None:
            out["score"] = round(float(r["rerank_score"]), 3)
        if r.get("authority") is not None:
            out["authority"] = r["authority"]
        return out

    @staticmethod
    def _error_hit(note: str, title: str = "[web_search error]") -> dict[str, Any]:
        return {"title": title, "content": note[:300], "link": "",
                "media": "", "publish_date": ""}

    def _record(self, query: str, count: int, recency: str,
                results: list[dict[str, Any]], *,
                error: str | None = None, cached: bool = False) -> None:
        self.log.append({
            "query": query,
            "count": count,
            "recency": recency,
            "provider": self.provider,
            "engine": self.engine,
            "result_count": len(results),
            "results": results,
            "error": error,
            "cached": cached,
            "accessed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        })

    def dump_log(self) -> list[dict[str, Any]]:
        """Return the full provenance log (one entry per tool call)."""
        return self.log

    # ---------- invocation adapters (normalize a model's tool-call args) ----------

    def invoke_raw(self, raw_args: Any) -> list[dict[str, Any]]:
        """Accept args as dict OR JSON string (models send both)."""
        if isinstance(raw_args, str):
            try:
                raw_args = json.loads(raw_args)
            except json.JSONDecodeError:
                raw_args = {"query": raw_args}
        if not isinstance(raw_args, dict):
            return []
        return self.__call__(
            query=raw_args.get("query", ""),
            count=raw_args.get("count", 8),
            recency=raw_args.get("recency", "noLimit"),
        )


def format_results_for_model(results: list[dict[str, Any]], query: str) -> str:
    """Render search results as a compact text block to feed back into the model."""
    if not results:
        return f"[web_search '{query}']: no results."
    lines = [f"[web_search '{query}' — {len(results)} results]"]
    for i, r in enumerate(results, 1):
        bits = [f"#{i} {r.get('title','')}"]
        if r.get("publish_date"):
            bits.append(f"({r['publish_date']})")
        lines.append(" ".join(bits))
        if r.get("media"):
            lines.append(f"   source: {r['media']}")
        if r.get("content"):
            lines.append(f"   {r['content']}")
        if r.get("link"):
            lines.append(f"   {r['link']}")
    return "\n".join(lines)


def sources_from_tool(tool: WebSearchTool) -> list[dict[str, str]]:
    """Build the prediction's sources[] log from the tool's per-call log.

    One entry per executed tool call (cache hits included), with the call's own
    timestamp — so repeated queries are never duplicated exponentially and the
    leakage audit sees when each query actually ran.
    """
    return [{
        "query": entry.get("query", ""),
        "engine": entry.get("engine", tool.engine),
        "accessed_at": entry.get("accessed_at", ""),
    } for entry in tool.log]


def _retry_after_seconds(resp: httpx.Response) -> float | None:
    raw = resp.headers.get("retry-after") or resp.headers.get("Retry-After")
    if not raw:
        return None
    try:
        return float(raw)
    except ValueError:
        return None

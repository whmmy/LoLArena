"""Unified web_search tool — mounted on EVERY model.

Fairness contract: all models call the SAME tool backed by the SAME engine
(Zhipu web_search). The only thing that differs between models is *what* they
choose to search for.

This module exposes:
  - WebSearchTool: executes a query against Zhipu, returns compact results
  - TOOL_OPENAI:   tool schema in OpenAI function-calling format
  - TOOL_ANTHROPIC: tool schema in Anthropic tool-use format
  - TOOL_GEMINI:   tool schema in Gemini functionDeclarations format
"""

from __future__ import annotations

import json
import time
import uuid
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
    "'T1 vs Gen.G LCK 2026 Spring final prediction'."
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
            "description": "Time window for results.",
            "enum": ["oneDay", "oneWeek", "oneMonth", "oneYear", "noLimit"],
            "default": "oneMonth",
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


class WebSearchTool:
    """Executes a web_search query via Zhipu. One instance is reused per run.

    Records every call (query, params, full results, timestamp) into self.log
    so the run can persist it for provenance / audit. Also memoizes within a
    run: an identical (query, count, recency) is served from cache instead of
    hitting Zhipu twice.
    """

    def __init__(self, api_key: str | None = None, base_url: str | None = None,
                 engine: str | None = None, timeout: float = 30.0):
        cfg.load_env()
        self.api_key = api_key or cfg.env("ZHIPU_WEBSEARCH_API_KEY") or cfg.env("ZHIPU_API_KEY")
        self.base_url = (base_url or cfg.env("ZHIPU_WEBSEARCH_BASE_URL")
                         or "https://open.bigmodel.cn/api").rstrip("/")
        self.engine = engine or cfg.env("ZHIPU_WEBSEARCH_ENGINE") or "search_pro"
        self.timeout = timeout
        if not self.api_key:
            raise RuntimeError(
                "ZHIPU_WEBSEARCH_API_KEY (or ZHIPU_API_KEY) not set. "
                "web_search tool requires it."
            )
        self.call_count = 0
        self.queries: list[str] = []
        self.log: list[dict[str, Any]] = []     # provenance log (every call)
        self._memo: dict[str, list[dict[str, Any]]] = {}

    def __call__(self, query: str, count: int = 8,
                 recency: str = "oneMonth") -> list[dict[str, Any]]:
        """Run a single search. Returns compact result dicts.

        Compact shape (stable across providers):
            [{title, content, link, media, publish_date}]
        """
        query = (query or "").strip()[:70]
        if not query:
            return []

        memo_key = f"{query}|{count}|{recency}"
        if memo_key in self._memo:
            # repeated query in the same run -> serve cached, still log it
            cached = self._memo[memo_key]
            self._record(query, count, recency, cached, cached=True)
            return cached

        self.queries.append(query)
        self.call_count += 1

        payload = {
            "search_query": query,
            "search_engine": self.engine,
            "search_intent": True,
            "count": max(1, min(50, int(count))),
            "search_recency_filter": recency or "oneMonth",
            "content_size": "medium",
            "request_id": uuid.uuid4().hex,
        }
        headers = {"Authorization": f"Bearer {self.api_key}",
                   "Content-Type": "application/json"}
        url = f"{self.base_url}/paas/v4/web_search"

        error_note: str | None = None
        with httpx.Client(timeout=self.timeout) as client:
            resp = client.post(url, json=payload, headers=headers)

        if resp.status_code != 200:
            # Soft-fail: return an error note the model can read, never crash the run.
            error_note = f"http {resp.status_code}: {resp.text[:300]}"
            compact = [{
                "title": f"[web_search error {resp.status_code}]",
                "content": resp.text[:300],
                "link": "", "media": "", "publish_date": "",
            }]
        else:
            data = resp.json()
            if isinstance(data, dict) and data.get("error"):
                error_note = json.dumps(data["error"], ensure_ascii=False)[:300]
                compact = [{
                    "title": "[web_search error]",
                    "content": error_note,
                    "link": "", "media": "", "publish_date": "",
                }]
            else:
                results = (data or {}).get("search_result") or []
                compact = [{
                    "title": r.get("title", ""),
                    "content": (r.get("content") or "")[:600],
                    "link": r.get("link", ""),
                    "media": r.get("media", ""),
                    "publish_date": r.get("publish_date", ""),
                } for r in results]

        self._memo[memo_key] = compact
        self._record(query, count, recency, compact, error=error_note)
        return compact

    def _record(self, query: str, count: int, recency: str,
                results: list[dict[str, Any]], *,
                error: str | None = None, cached: bool = False) -> None:
        self.log.append({
            "query": query,
            "count": count,
            "recency": recency,
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
            recency=raw_args.get("recency", "oneMonth"),
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
    """Build the prediction's sources[] log (accessed_at = now, for leakage audit)."""
    return [{
        "query": q,
        "engine": tool.engine,
        "accessed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    } for q in tool.queries]

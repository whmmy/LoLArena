"""Base runner with a unified agent loop + web_search tool.

Every model mounts the SAME web_search tool (Zhipu backend). The agent loop:
  model -> emits JSON OR a web_search tool_call
       -> if tool_call: runner executes web_search, feeds results back
       -> repeat until model emits final JSON (no more tool calls)

Fairness: identical tool, identical backend. Only the model's *choice* of queries differs.
"""

from __future__ import annotations

import abc
import dataclasses
import datetime as dt
import json
import os
import re
import time
from typing import Any, Callable, Iterator

from .. import config as cfg


@dataclasses.dataclass
class RunnerResult:
    model_id: str
    scope: str                      # "match" | "game"
    target_id: str                  # match slug or "<match_slug>/g<pos>"
    submitted_at: str
    prediction: dict[str, Any]
    raw_text: str                   # final assistant text (JSON)
    thinking_text: str | None
    sources: list[dict[str, Any]]   # web_search query log
    input_tokens: int
    output_tokens: int
    tool_calls: int
    cost_usd: float
    wall_seconds: float
    error: str | None = None
    search_log: list[dict[str, Any]] = dataclasses.field(default_factory=list)  # full provenance
    rounds: list[dict[str, Any]] = dataclasses.field(default_factory=list)  # full per-turn transcript


ProgressCallback = Callable[[dict[str, Any]], None]


class BaseRunner(abc.ABC):
    """One subclass per provider protocol. All share the agent loop in run()."""

    def __init__(self, model_cfg: dict[str, Any], search_tool):
        self.cfg = model_cfg
        self.model_id = model_cfg["id"]
        self.search = search_tool
        self.max_tool_calls = int(
            cfg.policy().get("web_search", {}).get("max_calls_per_prediction", 12)
        )

    # ---- to implement per provider ----

    @abc.abstractmethod
    def _chat(self, messages: list[dict[str, Any]], *, allow_tools: bool = True) -> dict[str, Any]:
        """One provider call. messages already include system + history.

        Return:
            text        : str        final assistant text (or '' if tool_calls)
            thinking    : str|None
            tool_calls  : list[dict] normalized tool-call requests (see below)
            input_tokens: int
            output_tokens: int

        Each tool_call dict MUST be normalized to:
            { "id": str, "name": "web_search", "args": <dict|json-str> }
        """

    # ---- streaming variant (used by the betting-advice path) ----
    # The betting path is a single-turn, tool-free chat that we stream token
    # by token to the browser. Providers that support native streaming override
    # this (see OpenAICompatRunner). This default falls back to the non-stream
    # _chat() and emits the whole text in one delta — so ANY runner can be used
    # for betting, even without a streaming implementation.

    def stream_chat(self, messages: list[dict[str, Any]], *,
                    allow_tools: bool = False) -> Iterator[dict[str, Any]]:
        """Yield streaming events for one chat turn.

        Event shapes:
            {"type": "delta",  "text": str}            # incremental text chunk
            {"type": "done",   "text": str,            # full accumulated text
                               "thinking": str|None,
                               "input_tokens": int,
                               "output_tokens": int,
                               "error": str|None}
        """
        out = self._chat(messages, allow_tools=allow_tools)
        full = out.get("text") or ""
        if full:
            yield {"type": "delta", "text": full}
        yield {
            "type": "done",
            "text": full,
            "thinking": out.get("thinking"),
            "input_tokens": out.get("input_tokens", 0),
            "output_tokens": out.get("output_tokens", 0),
            "error": None,
        }

    # ---- the unified agent loop ----

    def run(self, system_prompt: str, user_prompt: str, *, scope: str,
            target_id: str, validate_fn: Callable[[dict], list[str]] | None = None,
            max_format_retries: int = 2,
            progress: ProgressCallback | None = None) -> RunnerResult:
        t0 = time.time()
        totals = {"in": 0, "out": 0, "calls": 0, "cost": 0.0}
        sources: list[dict[str, Any]] = []
        thinking_parts: list[str] = []
        rounds: list[dict[str, Any]] = []
        raw = ""
        err: str | None = None
        pred: dict[str, Any] = {}

        # Seed messages. Sub-classes that need a different message shape
        # (Anthropic system block, Gemini contents) override _seed_messages.
        messages = self._seed_messages(system_prompt, user_prompt)

        try:
            self._emit(progress, "start", scope=scope, target_id=target_id)
            # 1) the search-and-reason loop until JSON or budget exhausted
            self._agent_loop(messages, totals, sources, thinking_parts, rounds, progress)

            # 2) extract + validate JSON, with up to N repair retries
            for attempt in range(max_format_retries + 1):
                raw = self._last_assistant_text(messages)
                self._emit(progress, "parse", attempt=attempt + 1, raw_chars=len(raw))
                pred = parse_json(raw)
                if isinstance(pred, dict):
                    errs = validate_fn(pred) if validate_fn else []
                    if not errs:
                        self._emit(progress, "validated", attempt=attempt + 1)
                        break
                    # ask the model to fix it (one more round, no tools)
                    self._emit(progress, "repair", attempt=attempt + 1, errors=errs)
                    fix_msg = self._repair_message(errs)
                    messages.append(fix_msg)
                    out = self._chat(messages, allow_tools=False)
                    totals["in"] += out.get("input_tokens", 0)
                    totals["out"] += out.get("output_tokens", 0)
                    self._emit(progress, "chat_end", round=f"repair_{attempt + 1}",
                               input_tokens=out.get("input_tokens", 0),
                               output_tokens=out.get("output_tokens", 0),
                               text_chars=len(out.get("text") or ""),
                               text=out.get("text") or "",
                               thinking=out.get("thinking"),
                               tool_calls=0,
                               provider_thinking_chars=len(out.get("thinking") or ""))
                    self._record_turn(rounds, "repair", out, round_no=None)
                    self._append_assistant(messages, out)
                else:
                    pred = {}
                    self._emit(progress, "repair", attempt=attempt + 1,
                               errors=["Output was not valid JSON."])
                    messages.append(self._repair_message(
                        ["Output was not valid JSON. Return ONLY the JSON object."]
                    ))
                    out = self._chat(messages, allow_tools=False)
                    totals["in"] += out.get("input_tokens", 0)
                    totals["out"] += out.get("output_tokens", 0)
                    self._emit(progress, "chat_end", round=f"repair_{attempt + 1}",
                               input_tokens=out.get("input_tokens", 0),
                               output_tokens=out.get("output_tokens", 0),
                               text_chars=len(out.get("text") or ""),
                               text=out.get("text") or "",
                               thinking=out.get("thinking"),
                               tool_calls=0,
                               provider_thinking_chars=len(out.get("thinking") or ""))
                    self._record_turn(rounds, "repair", out, round_no=None)
                    self._append_assistant(messages, out)
        except Exception as e:  # noqa: BLE001
            err = f"{type(e).__name__}: {e}"
            self._emit(progress, "error", error=err)

        if isinstance(pred, dict) and not pred.get("sources"):
            pred["sources"] = sources

        result = RunnerResult(
            model_id=self.model_id, scope=scope, target_id=target_id,
            submitted_at=now_iso(), prediction=pred, raw_text=raw,
            thinking_text="\n".join(thinking_parts) or None,
            sources=sources,
            input_tokens=totals["in"], output_tokens=totals["out"],
            tool_calls=totals["calls"],
            cost_usd=totals["cost"] + self._price(totals["in"], totals["out"]),
            wall_seconds=time.time() - t0, error=err,
            search_log=getattr(self.search, "log", []),
            rounds=rounds,
        )
        self._emit(progress, "finish", ok=bool(result.prediction and not result.error),
                   tool_calls=result.tool_calls, input_tokens=result.input_tokens,
                   output_tokens=result.output_tokens,
                   cost_usd=round(result.cost_usd, 6),
                   wall_seconds=round(result.wall_seconds, 2))
        return result

    # ---- agent loop shared by all providers ----

    def _agent_loop(self, messages, totals, sources, thinking_parts,
                    rounds: list[dict[str, Any]],
                    progress: ProgressCallback | None = None) -> None:
        from ..adapters.websearch import format_results_for_model, sources_from_tool

        round_no = 0
        while True:
            round_no += 1
            self._emit(progress, "chat_start", round=round_no)
            out = self._chat(messages)
            totals["in"] += out.get("input_tokens", 0)
            totals["out"] += out.get("output_tokens", 0)
            if out.get("thinking"):
                thinking_parts.append(out["thinking"])
            self._ensure_tool_call_ids(out, round_no)
            self._append_assistant(messages, out)

            calls = out.get("tool_calls") or []
            self._emit(progress, "chat_end", round=round_no,
                       input_tokens=out.get("input_tokens", 0),
                       output_tokens=out.get("output_tokens", 0),
                       text_chars=len(out.get("text") or ""),
                       text=out.get("text") or "",
                       thinking=out.get("thinking"),
                       tool_calls=len(calls),
                       provider_thinking_chars=len(out.get("thinking") or ""))
            if not calls:
                self._record_turn(rounds, "agent_final", out, round_no=round_no)
                return  # model emitted plain text (hopefully JSON) -> done

            # execute each web_search call and feed results back as a tool response
            tool_results = []
            budget_exhausted = False
            for c in calls:
                call_id = c.get("id") or f"call_{round_no}_{len(tool_results)}"
                if c.get("name") != "web_search":
                    tool_results.append({
                        "id": call_id,
                        "text": "Tool call rejected: only web_search is available.",
                    })
                    continue
                query = _q(c.get("args"))
                if totals["calls"] >= self.max_tool_calls:
                    budget_exhausted = True
                    tool_results.append({
                        "id": call_id,
                        "text": (
                            "Search budget exhausted; no search was executed for "
                            f"query: {query}. Use earlier search results and output the final JSON."
                        ),
                    })
                    continue
                self._emit(progress, "tool_start", round=round_no,
                           call_no=totals["calls"] + 1, query=query)
                results = self.search.invoke_raw(c.get("args"))
                totals["calls"] += 1
                sources.extend(sources_from_tool(self.search))
                self._emit(progress, "tool_end", round=round_no,
                           call_no=totals["calls"], query=query,
                           result_count=len(results))
                tool_results.append({
                    "id": call_id,
                    "text": format_results_for_model(results, query),
                })
            # record this reasoning turn: model text + thinking + the tool calls it
            # made + the results we fed back, so the full chain is traceable.
            self._record_turn(rounds, "agent", out, tool_results, round_no=round_no)
            if tool_results:
                # Providers may return either a single message dict (Anthropic/Gemini
                # bundle results into one user turn) or a list of OpenAI-style
                # {role:"tool", tool_call_id} messages (one per call_id).
                tool_msgs = self._tool_results_message(tool_results)
                if isinstance(tool_msgs, list):
                    messages.extend(tool_msgs)
                else:
                    messages.append(tool_msgs)
            if budget_exhausted or totals["calls"] >= self.max_tool_calls:
                # The just-appended tool messages close every tool_call_id before
                # we ask for a final answer, which strict OpenAI-compatible APIs require.
                self._emit(progress, "budget_hit", max_tool_calls=self.max_tool_calls)
                messages.append(self._user_message(
                    "You've reached the search budget. Now output the final JSON only."
                ))
                self._emit(progress, "chat_start", round=round_no + 1, final_after_budget=True)
                out2 = self._chat(messages, allow_tools=False)
                totals["in"] += out2.get("input_tokens", 0)
                totals["out"] += out2.get("output_tokens", 0)
                if out2.get("thinking"):
                    thinking_parts.append(out2["thinking"])
                self._ensure_tool_call_ids(out2, round_no + 1)
                self._append_assistant(messages, out2)
                self._emit(progress, "chat_end", round=round_no + 1,
                           input_tokens=out2.get("input_tokens", 0),
                           output_tokens=out2.get("output_tokens", 0),
                           text_chars=len(out2.get("text") or ""),
                           text=out2.get("text") or "",
                           thinking=out2.get("thinking"),
                           tool_calls=len(out2.get("tool_calls") or []),
                           provider_thinking_chars=len(out2.get("thinking") or ""))
                self._record_turn(rounds, "final_after_budget", out2, round_no=round_no + 1)
                return
            # loop continues -> model reasons again

    def _ensure_tool_call_ids(self, out: dict, round_no: int) -> None:
        for i, c in enumerate(out.get("tool_calls") or []):
            if not c.get("id"):
                c["id"] = f"call_{round_no}_{i}"

    def _emit(self, progress: ProgressCallback | None, event: str, **data: Any) -> None:
        if progress is None:
            return
        progress({"model_id": self.model_id, "event": event, **data})

    def _record_turn(self, rounds: list[dict[str, Any]], kind: str,
                     out: dict[str, Any],
                     tool_results: list[dict[str, Any]] | None = None,
                     *, round_no: int | None = None) -> None:
        """Append the full product of one _chat() call to the transcript:
        assistant text, thinking, normalized tool calls (with args), the tool
        results fed back, and per-turn token counts. Persisted for audit."""
        rounds.append({
            "seq": len(rounds) + 1,
            "kind": kind,            # agent | agent_final | final_after_budget | repair
            "round": round_no,       # agent-loop round number; None for repair turns
            "text": out.get("text") or "",
            "thinking": out.get("thinking"),
            "tool_calls": [
                {"id": c.get("id"), "name": c.get("name"), "args": c.get("args")}
                for c in (out.get("tool_calls") or [])
            ],
            "tool_results": [
                {"id": r.get("id"), "text": r.get("text")}
                for r in (tool_results or [])
            ],
            "input_tokens": out.get("input_tokens", 0),
            "output_tokens": out.get("output_tokens", 0),
        })

    # ---- provider-overridable message normalization ----
    # Default shape = OpenAI chat-completions style. Anthropic/Gemini override.

    def _seed_messages(self, system_prompt: str, user_prompt: str) -> list[dict]:
        return [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]

    def _append_assistant(self, messages: list[dict], out: dict) -> None:
        """Append the assistant turn returned by _chat into the message list."""
        msg: dict[str, Any] = {"role": "assistant"}
        if out.get("text"):
            msg["content"] = out["text"]
        if out.get("tool_calls"):
            msg["tool_calls"] = [
                {"id": c.get("id") or f"call_{i}", "type": "function",
                 "function": {"name": c["name"], "arguments": _argstr(c.get("args"))}}
                for i, c in enumerate(out["tool_calls"])
            ]
        messages.append(msg)

    def _user_message(self, text: str) -> dict:
        return {"role": "user", "content": text}

    def _repair_message(self, errors: list[str]) -> dict:
        return self._user_message(
            "Your previous output had these problems:\n- "
            + "\n- ".join(errors)
            + "\n\nRe-output the COMPLETE JSON object only, no extra text."
        )

    def _tool_results_message(self, results: list[dict]) -> dict:
        """results: [{id, text}] -> OpenAI-style tool role messages are one per id,
        but for simplicity we return a single user-role digest that all providers
        can consume. Providers needing strict tool-role messages override this."""
        digest = "\n\n".join(r["text"] for r in results)
        return {"role": "user", "content": f"Web search results:\n\n{digest}"}

    def _last_assistant_text(self, messages: list[dict]) -> str:
        for m in reversed(messages):
            if m.get("role") == "assistant" and isinstance(m.get("content"), str) and m["content"]:
                return m["content"]
        return ""

    # ---- key / base_url resolution (shared, proxy-aware) ----
    def _resolve_key(self) -> str:
        import os
        from .. import config as cfg
        proxy = cfg.env("LOLA_MODEL_PROXY")
        key_env = self.cfg.get("api_key_env", "")
        key = os.environ.get(key_env, "") if key_env else ""
        if not key and proxy:
            key = os.environ.get("OPENAI_API_KEY", "")
        if not key:
            raise RuntimeError(
                f"{self.model_id}: env var {key_env or 'OPENAI_API_KEY'} is not set."
            )
        return key

    def _resolve_base_url(self) -> str | None:
        import os
        from .. import config as cfg
        proxy = cfg.env("LOLA_MODEL_PROXY")
        if proxy:
            return proxy.rstrip("/")
        env_name = self.cfg.get("base_url_env", "")
        if env_name:
            override = os.environ.get(env_name, "")
            if override:
                return override.rstrip("/")
        return (self.cfg.get("base_url") or None)

    # ---- pricing ----
    def _price(self, in_tok: int, out_tok: int) -> float:
        p = self.cfg.get("price_per_mtok") or {}
        return (in_tok * p.get("input", 0) + out_tok * p.get("output", 0)) / 1_000_000


# ---------------- helpers ----------------

def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def parse_json(text: str) -> dict | None:
    """Best-effort JSON extraction from model text (handles fences, prose)."""
    text = (text or "").strip()
    if text.startswith("```"):
        text = text.strip("`")
        if text[:4].lower() == "json":
            text = text[4:]
        text = text.strip()
        if "```" in text:
            text = text.split("```", 1)[0]
    try:
        obj = json.loads(text)
        return obj if isinstance(obj, dict) else None
    except json.JSONDecodeError:
        start, end = text.find("{"), text.rfind("}")
        if start != -1 and end > start:
            try:
                obj = json.loads(text[start: end + 1])
                return obj if isinstance(obj, dict) else None
            except json.JSONDecodeError:
                return None
        return None


def _q(args: Any) -> str:
    if isinstance(args, dict):
        return str(args.get("query", ""))
    try:
        return str(json.loads(args).get("query", ""))
    except Exception:
        return str(args)


def _argstr(args: Any) -> str:
    if isinstance(args, str):
        return args
    return json.dumps(args, ensure_ascii=False)


def parse_markdown_picks(text: str) -> list[dict[str, Any]]:
    """Best-effort parse of the betting-advice recommendation table.

    Expects a markdown table with a fixed header:
        | 市场 | 选择 | 赔率 | 模型概率 | 隐含概率 | 价值 | 信心 | 理由 |
    Returns one dict per data row (keys: market, pick, odds, model_prob,
    implied_prob, value, confidence, reason). On any failure returns [] — the
    caller falls back to showing the raw markdown.
    """
    if not text:
        return []
    lines = text.splitlines()
    # find the header row by its required columns
    header_idx = None
    for i, ln in enumerate(lines):
        cells = _split_md_row(ln)
        if len(cells) >= 8 and "市场" in cells[0] and "选择" in cells[1] and "价值" in cells[5]:
            header_idx = i
            break
    if header_idx is None:
        return []
    picks: list[dict[str, Any]] = []
    for ln in lines[header_idx + 1:]:
        cells = _split_md_row(ln)
        # a separator row like |---|---|...| yields non-text cells; skip
        if not cells or all(set(c) <= set("-: ") for c in cells):
            continue
        if len(cells) < 8:
            break  # table ended
        try:
            picks.append({
                "market": cells[0].strip(),
                "pick": cells[1].strip(),
                "odds": _to_num(cells[2]),
                "model_prob": _to_num(cells[3]),
                "implied_prob": _to_num(cells[4]),
                "value": cells[5].strip(),       # 有 / 无
                "confidence": cells[6].strip(),  # 高 / 中 / 低
                "reason": cells[7].strip(),
            })
        except Exception:  # noqa: BLE001
            break
    return picks


def _split_md_row(line: str) -> list[str]:
    s = line.strip()
    if not s.startswith("|"):
        return []
    s = s.strip("|")
    return [c.strip() for c in s.split("|")]


def _to_num(cell: str) -> float | str:
    """Strip % and parse to float; keep original string if not numeric."""
    v = cell.strip().replace("%", "").replace("，", ",").strip()
    try:
        return float(v)
    except (TypeError, ValueError):
        return cell.strip()

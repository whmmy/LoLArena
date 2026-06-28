"""OpenAI-compatible runner.

Covers every model whose API speaks POST /chat/completions with tools:
GPT, DeepSeek, Qwen, Kimi, GLM, Moonshot, Doubao (via OpenRouter or native).

Supports the LOLA_MODEL_PROXY env: if set, ALL models route through that single
base_url (and OPENAI_API_KEY if the per-model key is empty) — handy for a 中转.
"""

from __future__ import annotations

from typing import Any, Iterator

from openai import OpenAI

from .base import BaseRunner
from .retry import chat_retry
from ..adapters import websearch as ws


class OpenAICompatRunner(BaseRunner):
    def __init__(self, model_cfg: dict, search_tool):
        super().__init__(model_cfg, search_tool)
        self.client = OpenAI(
            api_key=self._resolve_key(),
            base_url=self._resolve_base_url(),
            # Default raised from 180 -> 300: reasoning models (MiniMax M3 etc.)
            # plus the multi-round agent loop can exceed 180s on a single call.
            # Per-model overrides in models.yaml still win.
            timeout=float(model_cfg.get("timeout_seconds", 300)),
        )

    # ---- one chat-completions call ----
    @chat_retry
    def _chat(self, messages: list[dict[str, Any]], *, allow_tools: bool = True) -> dict[str, Any]:
        kwargs: dict[str, Any] = {
            "model": self.cfg["model"],
            "messages": messages,
            "temperature": 0.3,
        }
        if allow_tools:
            kwargs["tools"] = [ws.TOOL_OPENAI]
            kwargs["tool_choice"] = "auto"
        if self.cfg.get("max_tokens"):
            kwargs["max_tokens"] = self.cfg["max_tokens"]

        resp = self.client.chat.completions.create(**kwargs)
        msg = resp.choices[0].message

        tool_calls = []
        for tc in (msg.tool_calls or []):
            fn = tc.function or {}
            tool_calls.append({
                "id": tc.id,
                "name": fn.name,
                "args": fn.arguments,   # JSON string from OpenAI
            })

        usage = resp.usage
        return {
            "text": msg.content or "",
            "thinking": getattr(msg, "reasoning_content", None),
            "tool_calls": tool_calls,
            "input_tokens": getattr(usage, "prompt_tokens", 0) if usage else 0,
            "output_tokens": getattr(usage, "completion_tokens", 0) if usage else 0,
        }

    # ---- streaming variant (betting-advice path: single-turn, no tools) ----
    def stream_chat(self, messages: list[dict[str, Any]], *,
                    allow_tools: bool = False) -> "Iterator[dict[str, Any]]":
        """Stream one chat turn token-by-token (OpenAI stream=True).

        Yields the same event shapes as BaseRunner.stream_chat, plus:
            {"type": "thinking", "text": str}   # incremental reasoning chunk
        so callers can show live activity during the (sometimes multi-minute)
        thinking phase of reasoning models. Transient errors are wrapped by
        chat_retry on the non-stream path; here we run streaming directly and
        surface failures as a done event with `error`.
        """
        kwargs: dict[str, Any] = {
            "model": self.cfg["model"],
            "messages": messages,
            "temperature": 0.3,
            "stream": True,
            "stream_options": {"include_usage": True},
        }
        if allow_tools:
            kwargs["tools"] = [ws.TOOL_OPENAI]
            kwargs["tool_choice"] = "auto"
        if self.cfg.get("max_tokens"):
            kwargs["max_tokens"] = self.cfg["max_tokens"]

        full_parts: list[str] = []
        thinking_parts: list[str] = []
        in_tok = 0
        out_tok = 0
        err: str | None = None
        # Some providers (e.g. MiniMax M3) stream reasoning inline in `content`
        # wrapped in <think>...</think> rather than via a separate
        # `reasoning_content` field. We split such a stream live: text inside
        # <think> is routed to a `thinking` event, text outside to `delta`.
        # `in_think` tracks whether we're currently inside a <think> block, and
        # `buf` holds trailing chars that might be a partial tag boundary so we
        # don't emit a half tag.
        in_think = False
        buf = ""
        OPEN = "<think>"
        CLOSE = "</think>"

        def _route(text: str):
            """Append `text` to the right accumulator and return its events."""
            if not text:
                return []
            if in_think:
                thinking_parts.append(text)
                return [{"type": "thinking", "text": text}]
            full_parts.append(text)
            return [{"type": "delta", "text": text}]

        try:
            stream = self.client.chat.completions.create(**kwargs)
            for chunk in stream:
                if not getattr(chunk, "choices", None):
                    # final usage-only chunk (choices == []) carries the totals
                    u = getattr(chunk, "usage", None)
                    if u is not None:
                        in_tok = getattr(u, "prompt_tokens", 0) or 0
                        out_tok = getattr(u, "completion_tokens", 0) or 0
                    continue
                delta = chunk.choices[0].delta
                piece = getattr(delta, "content", None)
                if piece:
                    buf += piece
                    events: list[dict[str, Any]] = []
                    while True:
                        tag = CLOSE if in_think else OPEN
                        idx = buf.find(tag)
                        if idx == -1:
                            # No full tag boundary in buffer. Emit everything
                            # except a tail that could be the start of a tag,
                            # which we hold back for the next chunk.
                            safe = len(buf) - (len(tag) - 1)
                            if safe > 0:
                                events.extend(_route(buf[:safe]))
                                buf = buf[safe:]
                            break
                        # Emit text up to the tag, then flip the think state.
                        if idx > 0:
                            events.extend(_route(buf[:idx]))
                        in_think = not in_think
                        buf = buf[idx + len(tag):]
                    for e in events:
                        yield e
                rcontent = getattr(delta, "reasoning_content", None)
                if rcontent:
                    thinking_parts.append(rcontent)
                    # Forward reasoning live (not just in the final `done` event)
                    # so the browser shows activity during the long thinking phase
                    # instead of looking frozen.
                    yield {"type": "thinking", "text": rcontent}
                u = getattr(chunk, "usage", None)
                if u is not None:
                    in_tok = getattr(u, "prompt_tokens", 0) or in_tok
                    out_tok = getattr(u, "completion_tokens", 0) or out_tok
            # Flush any remainder after the stream ends.
            if buf:
                for e in _route(buf):
                    yield e
        except Exception as e:  # noqa: BLE001
            err = f"{type(e).__name__}: {e}"

        yield {
            "type": "done",
            "text": "".join(full_parts),
            "thinking": "".join(thinking_parts) or None,
            "input_tokens": in_tok,
            "output_tokens": out_tok,
            "error": err,
        }

    # ---- tool results: OpenAI requires one {role:"tool"} message per call_id ----
    def _tool_results_message(self, results: list[dict]) -> list[dict]:
        """Return OpenAI-spec tool messages — one per tool_call_id.

        DeepSeek (and strict OpenAI servers) reject a `tool_calls` assistant turn
        that is followed by anything other than matching `role:"tool"` messages.
        Returning a list here triggers the extend() path in BaseRunner._agent_loop.
        """
        return [
            {"role": "tool", "tool_call_id": r["id"], "content": r["text"]}
            for r in results
        ]

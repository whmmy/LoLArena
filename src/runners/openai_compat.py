"""OpenAI-compatible runner.

Covers every model whose API speaks POST /chat/completions with tools:
GPT, DeepSeek, Qwen, Kimi, GLM, Moonshot, Doubao (via OpenRouter or native).

Supports the LOLA_MODEL_PROXY env: if set, ALL models route through that single
base_url (and OPENAI_API_KEY if the per-model key is empty) — handy for a 中转.
"""

from __future__ import annotations

from typing import Any

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

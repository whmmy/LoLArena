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
from ..adapters import websearch as ws


class OpenAICompatRunner(BaseRunner):
    def __init__(self, model_cfg: dict, search_tool):
        super().__init__(model_cfg, search_tool)
        self.client = OpenAI(
            api_key=self._resolve_key(),
            base_url=self._resolve_base_url(),
            timeout=float(model_cfg.get("timeout_seconds", 180)),
        )

    # ---- one chat-completions call ----
    def _chat(self, messages: list[dict[str, Any]]) -> dict[str, Any]:
        kwargs: dict[str, Any] = {
            "model": self.cfg["model"],
            "messages": messages,
            "tools": [ws.TOOL_OPENAI],
            "tool_choice": "auto",
            "temperature": 0.3,
        }
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

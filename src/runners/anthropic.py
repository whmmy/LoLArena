"""Anthropic Claude runner.

Uses our UNIFIED web_search tool (Zhipu backend), NOT Anthropic's built-in
server-side web_search — so every model has identical tool capability. We hand
Claude a normal `tool_use` tool and execute it ourselves in the agent loop.

Anthropic message shape differs from OpenAI, so we override the message
normalization hooks (_seed_messages, _append_assistant, _tool_results_message,
_last_assistant_text) and translate.
"""

from __future__ import annotations

import os
from typing import Any

import anthropic

from .base import BaseRunner
from ..adapters import websearch as ws


class AnthropicRunner(BaseRunner):
    def __init__(self, model_cfg: dict, search_tool):
        super().__init__(model_cfg, search_tool)
        self.client = anthropic.Anthropic(
            api_key=self._resolve_key(),
            base_url=self._resolve_base_url(),
            timeout=float(model_cfg.get("timeout_seconds", 180)),
        )

    # ---- one messages.create call ----
    def _chat(self, messages: list[dict[str, Any]], *, allow_tools: bool = True) -> dict[str, Any]:
        system = self._pop_system(messages)
        kwargs: dict[str, Any] = {
            "model": self.cfg["model"],
            "system": system,
            "messages": messages,
            "max_tokens": self.cfg.get("max_tokens", 16000),
            "temperature": 0.3,
        }
        if allow_tools:
            kwargs["tools"] = [ws.TOOL_ANTHROPIC]
        resp = self.client.messages.create(**kwargs)

        text = ""
        thinking = None
        tool_calls: list[dict[str, Any]] = []
        for block in resp.content:
            btype = getattr(block, "type", None)
            if btype == "text":
                text += block.text
            elif btype == "thinking":
                thinking = (thinking or "") + getattr(block, "thinking", "")
            elif btype == "tool_use":
                tool_calls.append({
                    "id": block.id,
                    "name": block.name,
                    "args": block.input,   # already a dict in Anthropic SDK
                })
        return {
            "text": text,
            "thinking": thinking,
            "tool_calls": tool_calls,
            "input_tokens": resp.usage.input_tokens,
            "output_tokens": resp.usage.output_tokens,
        }

    # ---- Anthropic message normalization (overrides base defaults) ----

    def _seed_messages(self, system_prompt: str, user_prompt: str) -> list[dict]:
        # system is popped at call time by _pop_system
        self._system_prompt = system_prompt
        return [{"role": "user", "content": user_prompt}]

    def _pop_system(self, messages: list[dict]) -> str:
        return getattr(self, "_system_prompt", "")

    def _append_assistant(self, messages: list[dict], out: dict) -> None:
        content: list[dict[str, Any]] = []
        if out.get("text"):
            content.append({"type": "text", "text": out["text"]})
        for c in out.get("tool_calls") or []:
            content.append({
                "type": "tool_use",
                "id": c.get("id") or f"toolu_{id(c)}",
                "name": c["name"],
                "input": _as_dict(c.get("args")),
            })
        messages.append({"role": "assistant", "content": content or [{"type": "text", "text": ""}]})

    def _tool_results_message(self, results: list[dict]) -> dict:
        # Anthropic wants tool_result blocks inside a user message.
        content = []
        for r in results:
            content.append({
                "type": "tool_result",
                "tool_use_id": r["id"],
                "content": r["text"],
            })
        return {"role": "user", "content": content}

    def _repair_message(self, errors: list[str]) -> dict:
        return {"role": "user", "content":
                "Your previous output had these problems:\n- " + "\n- ".join(errors)
                + "\n\nRe-output the COMPLETE JSON object only."}

    def _last_assistant_text(self, messages: list[dict]) -> str:
        for m in reversed(messages):
            if m.get("role") == "assistant":
                content = m.get("content")
                if isinstance(content, str) and content:
                    return content
                if isinstance(content, list):
                    texts = [b.get("text", "") for b in content if b.get("type") == "text"]
                    joined = "".join(texts)
                    if joined:
                        return joined
        return ""

    # The base _agent_loop calls _user_message for the budget message — Anthropic
    # is fine with {role:user, content:str}, so the default works.


def _as_dict(args: Any) -> dict:
    if isinstance(args, dict):
        return args
    import json
    try:
        return json.loads(args) if args else {}
    except json.JSONDecodeError:
        return {"query": str(args)}

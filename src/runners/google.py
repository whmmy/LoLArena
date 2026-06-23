"""Google Gemini runner (native genai SDK).

Uses our UNIFIED web_search tool (Zhipu backend) via Gemini function-calling,
NOT Gemini's built-in google_search — so every model has identical tool
capability. We drive the function-calling loop manually in the agent loop.

Gemini's message shape is its own (contents list with parts, role 'user'/'model',
functionCall/functionResponse parts). We keep our internal message list in the
OpenAI-ish shape and translate to Gemini Content objects at each _chat call.
"""

from __future__ import annotations

from typing import Any

from google import genai
from google.genai import types

from .base import BaseRunner
from ..adapters import websearch as ws


class GeminiRunner(BaseRunner):
    def __init__(self, model_cfg: dict, search_tool):
        super().__init__(model_cfg, search_tool)
        self.client = genai.Client(
            api_key=self._resolve_key(),
            http_options=self._http_options(),
        )
        self._system_prompt = ""

    # ---- HTTP options: respect base_url override / proxy ----
    def _http_options(self) -> types.HttpOptions:
        from urllib.parse import urlparse, urlunparse
        url = (self._resolve_base_url()
               or "https://generativelanguage.googleapis.com/v1beta").rstrip("/")
        parsed = urlparse(url)
        path = parsed.path.rstrip("/")
        api_version = "v1beta"
        for version in ("/v1beta", "/v1", "/v1alpha"):
            if path.endswith(version):
                api_version = version.lstrip("/")
                path = path[: -len(version)]
                break
        is_official = parsed.netloc == "generativelanguage.googleapis.com"
        if is_official:
            return types.HttpOptions(api_version=api_version)
        base_url = urlunparse(parsed._replace(path=path or "", params="", query="", fragment=""))
        return types.HttpOptions(base_url=base_url, api_version=api_version)

    # ---- config (no automatic_function_calling — we drive the loop) ----
    def _config(self, *, allow_tools: bool = True) -> types.GenerateContentConfig:
        kwargs: dict[str, Any] = {
            "system_instruction": self._system_prompt or None,
            "temperature": 0.3,
            "max_output_tokens": self.cfg.get("max_tokens", 8192),
            "automatic_function_calling": types.AutomaticFunctionCallingConfig(disable=True),
        }
        if allow_tools:
            kwargs["tools"] = [types.Tool(function_declarations=[ws.TOOL_GEMINI])]
        return types.GenerateContentConfig(
            **kwargs,
        )

    # ---- one generate_content call ----
    def _chat(self, messages: list[dict[str, Any]], *, allow_tools: bool = True) -> dict[str, Any]:
        contents = self._to_contents(messages)
        resp = self.client.models.generate_content(
            model=self.cfg["model"], contents=contents, config=self._config(allow_tools=allow_tools),
        )

        text_parts: list[str] = []
        thinking_parts: list[str] = []
        tool_calls: list[dict[str, Any]] = []
        for cand in resp.candidates or []:
            content = cand.content
            for part in (content.parts if content and content.parts else []):
                if getattr(part, "thought", False) and part.text:
                    thinking_parts.append(part.text)
                elif getattr(part, "function_call", None):
                    fc = part.function_call
                    tool_calls.append({
                        "id": getattr(fc, "id", None) or f"fc_{id(part)}",
                        "name": fc.name,
                        "args": dict(fc.args or {}),
                    })
                elif part.text:
                    text_parts.append(part.text)

        usage = resp.usage_metadata
        in_tok = usage.prompt_token_count if usage else 0
        if usage and usage.total_token_count is not None and in_tok is not None:
            out_tok = max(0, usage.total_token_count - in_tok)
        elif usage:
            out_tok = (usage.candidates_token_count or 0) + (usage.thoughts_token_count or 0)
        else:
            out_tok = 0

        return {
            "text": "".join(text_parts) or "",
            "thinking": "".join(thinking_parts) or None,
            "tool_calls": tool_calls,
            "input_tokens": in_tok or 0,
            "output_tokens": out_tok or 0,
        }

    # ---- message normalization overrides (OpenAI-ish -> Gemini contents) ----

    def _seed_messages(self, system_prompt: str, user_prompt: str) -> list[dict]:
        self._system_prompt = system_prompt
        return [{"role": "user", "content": user_prompt}]

    def _append_assistant(self, messages: list[dict], out: dict) -> None:
        msg: dict[str, Any] = {"role": "assistant"}
        if out.get("text"):
            msg["content"] = out["text"]
        if out.get("tool_calls"):
            msg["tool_calls"] = [
                {"id": c.get("id") or f"fc_{i}", "name": c["name"], "args": c.get("args")}
                for i, c in enumerate(out["tool_calls"])
            ]
        messages.append(msg)

    def _tool_results_message(self, results: list[dict]) -> dict:
        # stored opaquely; translated to functionResponse parts in _to_contents
        return {"role": "user", "tool_results": results}

    def _last_assistant_text(self, messages: list[dict]) -> str:
        for m in reversed(messages):
            if m.get("role") == "assistant" and isinstance(m.get("content"), str) and m["content"]:
                return m["content"]
        return ""

    # ---- translate internal messages -> Gemini Content list ----
    def _to_contents(self, messages: list[dict[str, Any]]) -> list[types.Content]:
        contents: list[types.Content] = []
        for m in messages:
            role = "model" if m.get("role") == "assistant" else "user"
            parts: list[types.Part] = []

            if m.get("tool_results"):
                for r in m["tool_results"]:
                    parts.append(types.Part(
                        function_response=types.FunctionResponse(
                            name="web_search", id=r["id"], response={"result": r["text"]},
                        )
                    ))
                contents.append(types.Content(role="user", parts=parts))
                continue

            if m.get("content"):
                parts.append(types.Part(text=m["content"]))
            for tc in m.get("tool_calls") or []:
                import json
                args = tc.get("args")
                if isinstance(args, str):
                    try:
                        args = json.loads(args)
                    except json.JSONDecodeError:
                        args = {"query": args}
                parts.append(types.Part(function_call=types.FunctionCall(
                    name=tc["name"], args=args or {}, id=tc.get("id"),
                )))
            if parts:
                contents.append(types.Content(role=role, parts=parts))
        return contents

"""Runner factory: build the right runner for a model's `provider` field."""

from __future__ import annotations

from typing import Any

from .base import BaseRunner, RunnerResult  # noqa: F401  (re-export)


_PROVIDER_MAP = {
    "openai": "openai_compat",
    "openrouter": "openai_compat",
    "deepseek": "openai_compat",
    "dashscope": "openai_compat",
    "zhipu": "openai_compat",
    "moonshot": "openai_compat",
    "minimax": "openai_compat",
    "anthropic": "anthropic",
    "google": "google",
}


def build_runner(model_cfg: dict[str, Any], search_tool) -> BaseRunner:
    provider = model_cfg.get("provider", "")
    kind = _PROVIDER_MAP.get(provider)
    if not kind:
        raise ValueError(
            f"Unknown provider '{provider}' for model '{model_cfg.get('id')}'. "
            f"Known: {sorted(set(_PROVIDER_MAP))}"
        )
    if kind == "openai_compat":
        from .openai_compat import OpenAICompatRunner
        return OpenAICompatRunner(model_cfg, search_tool)
    if kind == "anthropic":
        from .anthropic import AnthropicRunner
        return AnthropicRunner(model_cfg, search_tool)
    if kind == "google":
        from .google import GeminiRunner
        return GeminiRunner(model_cfg, search_tool)
    raise ValueError(f"No runner class for kind '{kind}'")

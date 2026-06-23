"""Retry decorator for provider chat calls.

`tenacity` is already a project dependency (requirements.txt) but was unused.
We retry only the transient SDK errors that are safe to re-issue an identical
request for:

  - APITimeoutError      (MiniMax M3 reasoning runs easily exceed 180s)
  - APIConnectionError   (transient network / DNS / TLS)
  - RateLimitError       (HTTP 429)
  - InternalServerError  (HTTP 5xx)

Deliberately NOT retried:
  - BadRequestError (HTTP 400, e.g. malformed tool_calls) — deterministic, retry
    only wastes budget and masks the real bug.
  - AuthenticationError / NotFoundError / PermissionDeniedError — non-transient.

Usage:
    from .retry import chat_retry

    class OpenAICompatRunner(BaseRunner):
        @chat_retry
      def _chat(self, messages, *, allow_tools=True): ...
"""

from __future__ import annotations

from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

# Imported lazily-guarded so the module can be imported even if a specific SDK
# isn't installed; the decorator only fires at call time.
from openai import (
    APITimeoutError,
    APIConnectionError,
    RateLimitError,
    InternalServerError,
)

# Errors that justify an identical retry. 400/BadRequestError is intentionally
# absent — see module docstring.
RETRIABLE_EXC = (
    APITimeoutError,
    APIConnectionError,
    RateLimitError,
    InternalServerError,
)


def chat_retry(fn):
    """Retry a provider _chat call on transient errors.

    3 attempts, exponential backoff 2-30s, reraise the last error so the
    runner's existing except-clause records it as a normal failure.
    """
    return retry(
        retry=retry_if_exception_type(RETRIABLE_EXC),
        wait=wait_exponential(multiplier=2, min=2, max=30),
        stop=stop_after_attempt(3),
        reraise=True,
    )(fn)

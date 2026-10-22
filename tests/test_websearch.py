"""Offline tests for the unified web_search adapter.

Run with:  python -m unittest discover -s tests -v
No network and no API keys needed — httpx.MockTransport stands in for the engine.
"""

from __future__ import annotations

import json
import unittest
from datetime import datetime, timedelta, timezone
from unittest import mock

import httpx

from src.adapters.websearch import WebSearchTool, sources_from_tool

SEARCH_URL = "https://api.deepseek.com/v1/tools/search"


def _deepseek_tool(handler) -> WebSearchTool:
    return WebSearchTool(provider="deepseek", api_key="test-key",
                         transport=httpx.MockTransport(handler))


def _zhipu_tool(handler) -> WebSearchTool:
    return WebSearchTool(provider="zhipu", api_key="test-key",
                         transport=httpx.MockTransport(handler))


class DeepSeekBackendTests(unittest.TestCase):
    def test_request_shape_and_compact_result(self):
        seen: dict = {}

        def handler(request: httpx.Request) -> httpx.Response:
            seen["url"] = str(request.url)
            seen["auth"] = request.headers.get("authorization")
            seen["body"] = json.loads(request.content)
            return httpx.Response(200, json={"results": [{
                "title": "T1 beat Gen.G",
                "url": "https://example.com/a",
                "site_name": "Example",
                "date": "2026-08-15T16:00:00+00:00",
                "summary": "s" * 900,
                "snippet": "short",
                "rerank_score": 2.1234,
                "authority": 3,
            }]})

        tool = _deepseek_tool(handler)
        results = tool("T1 vs Gen.G", count=3)

        self.assertEqual(seen["url"], SEARCH_URL)
        self.assertEqual(seen["auth"], "Bearer test-key")
        self.assertEqual(seen["body"],
                         {"query": "T1 vs Gen.G", "count": 3, "need_content": False})
        self.assertEqual(len(results), 1)
        hit = results[0]
        self.assertEqual(hit["title"], "T1 beat Gen.G")
        self.assertEqual(hit["link"], "https://example.com/a")
        self.assertEqual(hit["media"], "Example")
        self.assertEqual(hit["publish_date"], "2026-08-15")
        self.assertEqual(len(hit["content"]), 600)  # capped for token budget
        self.assertEqual(hit["score"], 2.123)
        self.assertEqual(hit["authority"], 3)
        # provenance log
        self.assertEqual(tool.log[0]["provider"], "deepseek")
        self.assertEqual(tool.log[0]["engine"], "deepseek_search")
        self.assertEqual(tool.log[0]["result_count"], 1)
        self.assertIsNone(tool.log[0]["error"])

    def test_memoized_query_hits_engine_once_but_is_logged(self):
        calls: list[int] = []

        def handler(request: httpx.Request) -> httpx.Response:
            calls.append(1)
            return httpx.Response(200, json={"results": [
                {"title": "a", "url": "u", "summary": "x"}]})

        tool = _deepseek_tool(handler)
        tool("same query")
        tool("same query")

        self.assertEqual(len(calls), 1)
        self.assertEqual(tool.call_count, 1)
        self.assertEqual(len(tool.log), 2)
        self.assertTrue(tool.log[1]["cached"])
        # sources: one entry per actual tool call, no quadratic duplication
        self.assertEqual(len(sources_from_tool(tool)), 2)

    def test_recency_maps_to_date_operator(self):
        bodies: list[dict] = []

        def handler(request: httpx.Request) -> httpx.Response:
            bodies.append(json.loads(request.content))
            return httpx.Response(200, json={"results": []})

        tool = _deepseek_tool(handler)
        tool("T1 news", recency="oneWeek")
        expected = (datetime.now(timezone.utc) - timedelta(days=7)).strftime("%Y-%m-%d")
        self.assertEqual(bodies[0]["query"], f"T1 news after:{expected}")

        tool("T1 news", recency="noLimit")
        self.assertEqual(bodies[1]["query"], "T1 news")

    def test_explicit_date_operator_is_not_duplicated(self):
        bodies: list[dict] = []

        def handler(request: httpx.Request) -> httpx.Response:
            bodies.append(json.loads(request.content))
            return httpx.Response(200, json={"results": []})

        tool = _deepseek_tool(handler)
        tool("T1 news after:2025-01-01", recency="oneMonth")
        self.assertEqual(bodies[0]["query"], "T1 news after:2025-01-01")
        self.assertEqual(bodies[0]["query"].count("after:"), 1)

    def test_query_is_capped_at_engine_limit_after_operator(self):
        bodies: list[dict] = []

        def handler(request: httpx.Request) -> httpx.Response:
            bodies.append(json.loads(request.content))
            return httpx.Response(200, json={"results": []})

        tool = _deepseek_tool(handler)
        tool("x" * 500, recency="oneMonth")
        sent = bodies[0]["query"]
        self.assertLessEqual(len(sent), 128)
        self.assertRegex(sent, r" after:\d{4}-\d{2}-\d{2}$")

    @mock.patch("src.adapters.websearch.time.sleep")
    def test_transient_429_is_retried_then_soft_fails(self, _sleep):
        calls: list[int] = []

        def handler(request: httpx.Request) -> httpx.Response:
            calls.append(1)
            return httpx.Response(429, text="qps exceeded")

        tool = _deepseek_tool(handler)
        results = tool("q")

        self.assertEqual(len(calls), 2)  # one retry
        self.assertIn("429", results[0]["title"])
        self.assertIn("429", tool.log[0]["error"] or "")
        # errors are not memoized: a later retry of the same query hits the engine
        tool("q")
        self.assertEqual(len(calls), 4)

    @mock.patch("src.adapters.websearch.time.sleep")
    def test_network_error_soft_fails(self, _sleep):
        def handler(request: httpx.Request) -> httpx.Response:
            raise httpx.ConnectError("boom", request=request)

        tool = _deepseek_tool(handler)
        results = tool("q")
        self.assertIn("error", results[0]["title"])
        self.assertIn("network", tool.log[0]["error"] or "")

    def test_invoke_raw_accepts_json_string(self):
        def handler(request: httpx.Request) -> httpx.Response:
            return httpx.Response(200, json={"results": []})

        tool = _deepseek_tool(handler)
        tool.invoke_raw(json.dumps({"query": "T1", "count": 2}))
        self.assertEqual(tool.call_count, 1)


class ZhipuBackendTests(unittest.TestCase):
    def test_legacy_backend_still_works(self):
        seen: dict = {}

        def handler(request: httpx.Request) -> httpx.Response:
            seen["url"] = str(request.url)
            seen["body"] = json.loads(request.content)
            return httpx.Response(200, json={"search_result": [{
                "title": "t", "content": "c" * 800, "link": "l",
                "media": "m", "publish_date": "2026-01-02",
            }]})

        tool = _zhipu_tool(handler)
        results = tool("q", count=5, recency="oneDay")

        self.assertEqual(seen["url"], "https://open.bigmodel.cn/api/paas/v4/web_search")
        self.assertEqual(seen["body"]["search_recency_filter"], "oneDay")
        self.assertEqual(seen["body"]["count"], 5)
        self.assertEqual(len(results[0]["content"]), 600)
        self.assertEqual(results[0]["publish_date"], "2026-01-02")
        self.assertEqual(tool.log[0]["engine"], "search_pro")

    def test_cache_does_not_leak_across_recency_windows(self):
        calls: list[dict] = []

        def handler(request: httpx.Request) -> httpx.Response:
            calls.append(json.loads(request.content))
            return httpx.Response(200, json={"search_result": []})

        tool = _zhipu_tool(handler)
        tool("q", recency="noLimit")
        tool("q", recency="oneDay")
        self.assertEqual(len(calls), 2)
        self.assertEqual(calls[1]["search_recency_filter"], "oneDay")


class ProviderResolutionTests(unittest.TestCase):
    def test_unknown_provider_is_rejected(self):
        with self.assertRaises(ValueError):
            WebSearchTool(provider="google", api_key="k")

    def test_env_selects_provider(self):
        with mock.patch.dict("os.environ", {"LOLA_WEBSEARCH_PROVIDER": "zhipu"}):
            tool = WebSearchTool(api_key="k", transport=httpx.MockTransport(
                lambda r: httpx.Response(200, json={"search_result": []})))
            self.assertEqual(tool.provider, "zhipu")


if __name__ == "__main__":
    unittest.main()

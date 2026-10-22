"""Offline test for the shared agent loop + web_search wiring.

A scripted runner stands in for a real provider, so the test exercises the
tool-call -> execute -> feed-back -> final-JSON path without any model API call.
"""

from __future__ import annotations

import json
import unittest

import httpx

from src.adapters.websearch import WebSearchTool
from src.runners.base import BaseRunner


class ScriptedRunner(BaseRunner):
    """Replays a fixed list of _chat() responses."""

    def __init__(self, model_cfg, search_tool, script):
        super().__init__(model_cfg, search_tool)
        self.script = list(script)

    def _chat(self, messages, *, allow_tools=True):
        return dict(self.script.pop(0), input_tokens=10, output_tokens=5)


FINAL = {"winner": "T1", "win_prob": 0.6, "score": "3-1", "sources": []}


class AgentLoopTests(unittest.TestCase):
    def test_tool_call_is_executed_and_sources_are_not_duplicated(self):
        requests: list[dict] = []

        def handler(request: httpx.Request) -> httpx.Response:
            requests.append(json.loads(request.content))
            return httpx.Response(200, json={"results": [
                {"title": "hit", "url": "https://example.com", "summary": "ok",
                 "site_name": "Example", "date": "2026-10-01T00:00:00+00:00"}]})

        tool = WebSearchTool(provider="deepseek", api_key="test-key",
                             transport=httpx.MockTransport(handler))
        runner = ScriptedRunner(
            {"id": "fake-model", "price_per_mtok": {"input": 0, "output": 0}},
            tool,
            script=[
                {"text": "", "tool_calls": [
                    {"id": "c1", "name": "web_search",
                     "args": json.dumps({"query": "T1 vs Gen.G"})}]},
                {"text": json.dumps(FINAL), "tool_calls": []},
            ],
        )

        result = runner.run("system", "user", scope="match", target_id="slug")

        self.assertIsNone(result.error)
        self.assertEqual(result.prediction["winner"], "T1")
        self.assertEqual(result.tool_calls, 1)
        self.assertEqual(len(requests), 1)
        self.assertEqual(requests[0]["query"], "T1 vs Gen.G")
        # one source entry per actual tool call (regression: used to grow O(n^2))
        self.assertEqual(len(result.sources), 1)
        self.assertEqual(result.sources[0]["engine"], "deepseek_search")
        self.assertEqual(len(result.search_log), 1)
        # the full transcript records the tool call and its results
        self.assertEqual(result.rounds[0]["tool_calls"][0]["name"], "web_search")
        self.assertIn("hit", result.rounds[0]["tool_results"][0]["text"])
        tool.close()

    def test_unknown_tool_is_rejected_without_crashing(self):
        tool = WebSearchTool(provider="deepseek", api_key="test-key",
                             transport=httpx.MockTransport(
                                 lambda r: httpx.Response(200, json={"results": []})))
        runner = ScriptedRunner(
            {"id": "fake-model"},
            tool,
            script=[
                {"text": "", "tool_calls": [
                    {"id": "c1", "name": "browse", "args": {"query": "x"}}]},
                {"text": json.dumps(FINAL), "tool_calls": []},
            ],
        )
        result = runner.run("system", "user", scope="match", target_id="slug")
        self.assertIsNone(result.error)
        self.assertEqual(result.tool_calls, 0)
        self.assertIn("only web_search", result.rounds[0]["tool_results"][0]["text"])
        tool.close()


if __name__ == "__main__":
    unittest.main()

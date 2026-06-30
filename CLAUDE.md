# CLAUDE.md — dev context for LoLArena

## What this is
A benchmark that scores frontier + Chinese LLMs on real League-of-Legends match
prediction. Two scopes: **series** (auto, T-3h before kickoff) and **single
game** (manual, after BP). Models are ranked by post-match accuracy.

## The fairness invariant (DO NOT break it)
**Every model gets the SAME context_pack AND the SAME `web_search` tool.**
The tool backend is always Zhipu (see `src/adapters/websearch.py`). Never wire
a model to its native search tool (Gemini `google_search`, Anthropic's built-in
`web_search_20250305`, OpenAI's hosted browsing) — that would make tool
capability differ between models and ruin the comparison. Differences between
models must come ONLY from what they choose to search and how they reason.

## Layout cheat-sheet
- `src/adapters/cito.py` — LoL data source (PRIMARY) + multi-key pool + disk cache. Normalises Cito responses into PandaScore-shaped match objects so the pipeline barely changed.
- `src/adapters/pandascore.py` — legacy LoL client, kept as fallback (not called by default)
- `src/adapters/websearch.py` — the ONE search tool + provider-specific schemas
- `src/pipeline/collect.py` — builds context_pack.json (rosters/form/objectives/standings/player_form/champion_pool/h2h/meta)
- `src/pipeline/prompt_build.py` — renders system + user prompts
- `src/pipeline/validate.py` — JSON Schema + semantic checks (probs sum, winner agrees, etc.)
- `src/pipeline/orchestrator.py` — cmd_* entrypoints; runs all models in parallel
- `src/runners/base.py` — the agent loop (tool_call -> execute -> feed back -> repeat)
- `src/runners/{openai_compat,anthropic,google}.py` — provider-specific `_chat` + message normalization
- `src/graders/` — grade_match / grade_game + domain-agnostic metrics
- `src/server/main.py` — FastAPI: static site + /api/refresh-bp + /api/predict
- `src/pipeline/scheduler.py` — APScheduler predict_tick (5min) + grade_tick (15min)

## Adding a model
Add one entry to `configs/models.yaml`. Set `provider` to one of:
`openai|openrouter|deepseek|dashscope|zhipu|moonshot` (all → OpenAICompatRunner),
`anthropic`, or `google`. If its API speaks OpenAI chat-completions with
function-calling, use `openai_compat`. Done — it auto-mounts web_search.

## When editing prompts
`prompts/*.md` are read fresh on every prediction (no restart needed). The
required `reasoning.*` subfield names are enforced by BOTH the schema
(`schemas/*.schema.json` minLength) and the grader
(`graders/grade_match.py` reasoning_completeness). Keep them in sync.

## Running tests
No formal test suite yet — verify via:
- `python -c "..."` snippets against `validate` and `graders` (see commits)
- `python -m src --help` (CLI wiring)
- `python -m src build-site` (site builder on empty data)
- FastAPI `TestClient` for routes

## Env required to actually predict
`CITO_API_KEY` (or `CITO_API_KEYS` comma-separated for a key pool) +
`ZHIPU_WEBSEARCH_API_KEY` + at least one model key.
Without keys, `cmd_predict` fails fast with a clear message (by design).

## Data source notes (Cito)
- `team_id` is the Cito **slug** (e.g. `t1`/`gen`); `match_id` is the Riot
  `officialEventId` (bare numeric, stored as int). Both flow through the
  normalised match object unchanged, so blue/red side and score comparisons in
  collect/orchestrator/grade work as-is.
- Response envelopes vary per endpoint (7 shapes) — `CitoClient._unwrap()`
  strips them so callers always see a list or object.
- Free tier is **500 req/month/key**. Player-level blocks (`player_form`,
  `player_champion_pool`) cost ~2 req/player; toggle them in
  `configs/policy.yaml` when quota is tight.
- **`team_objectives` has kills/gold/objectives but NO game duration.** The
  duration + series-sweep anchors come from a separate `team_series_history`
  block (`/lol/teams/{slug}/matches`, ~1 req/team) which is the ONLY source of
  per-game `duration` and real series scores. This block feeds both the
  single-game duration anchor and the series-score (sweep) anchor — keep it on
  or those predictions revert to league-mean priors. Note: very recent matches
  (last ~1-2 days) often have `duration: null` until Cito back-fills, so the
  anchor uses older games.
- **Scoring scales are task-config-driven** (`scale:` in `configs/tasks.yaml`).
  The MAE default `max(2, |truth|)` is far too tight for game duration (~2min
  miss -> 0), so duration/kills tasks set an explicit `scale`. Changing it
  changes how much a BP-specific call is rewarded vs a risk-free mean guess.

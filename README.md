# 🎮 LoLArena — Frontier LLM League-of-Legends Prediction Arena

A benchmark that scores frontier LLMs on **real** League-of-Legends
match prediction. Two scopes: **series** (auto, T-3h before kickoff) and
**single game** (manual, after champion select). Models are ranked by
post-match accuracy.

> 🌏 中文版本: [README.zh-CN.md](README.zh-CN.md)

## The fairness invariant

> **Every model gets the SAME `context_pack` AND the SAME `web_search` tool.**
> Differences between models must come ONLY from what they choose to search
> and how they reason.

- All models ingest the **same aggregated `context_pack`** built from
  **PandaScore** (free tier) — rosters, recent form, hero pools, head-to-head,
  meta signals.
- All models are mounted with the **same `web_search` tool** (backend:
  **Zhipu web_search API**, `search_pro` engine with intent recognition).
  Each model decides what to search and how many rounds.
- Tool capability is identical across models — the only differentiator is
  analytical judgment.
- Each model produces one prediction per match, persisted and graded
  independently.

## Two prediction scopes

| Type        | Trigger                                                        | What the model predicts                                                                                          |
| ----------- | -------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Series**  | Automatic (APScheduler) — T-3h before kickoff                  | Win probability (e.g. TES 55% – G2 45%), series score (3-1), total games, upset flag, key players                |
| **Single game** | Manual "Refresh BP" button on the web UI after pick/ban     | Single-game win + probability, game length (minutes), kills per team, total kills                                |

Every prediction must cover **four dimensions**:
1️⃣ Team fundamentals · 2️⃣ Lane matchup (top/jungle/mid/bot/support) ·
3️⃣ Patch adaptation & playstyle · 4️⃣ Historical head-to-head & psychology

## Repository layout

```
lolArena/
├─ configs/        models.yaml (model registry) · policy.yaml (strategy) · tasks.yaml (grading) · leagues.yaml (tracked leagues)
├─ prompts/        system.md · task_match.md · task_game.md
├─ schemas/        match_prediction / game_prediction (JSON Schema)
├─ src/
│   ├─ adapters/   pandascore.py (LoL API) · websearch.py (unified search tool)
│   ├─ pipeline/   collect · prompt_build · validate · orchestrator · scheduler
│   ├─ runners/    base (agent loop) · openai_compat · anthropic · google
│   ├─ graders/    grade_match · grade_game · metrics/
│   ├─ server/     main.py (FastAPI)
│   └─ leaderboard/build_site.py
├─ data/           matches/<slug>/  ·  games/<slug>/g<pos>/
└─ docs/site/      index.html + data.json (single-page leaderboard)
```

## Quick start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Configure keys
cp .env.example .env
#   Required: PANDASCORE_API_KEY, ZHIPU_WEBSEARCH_API_KEY
#   Per-model: <PROVIDER>_API_KEY (enable/disable entries in configs/models.yaml)

# 3. Start the service (FastAPI + scheduler together)
python -m src serve
#   Open http://127.0.0.1:8000
```

## CLI (manual operations)

```bash
python -m src scan                          # Scan near-future matches due for prediction
python -m src collect <match_id>            # Build context_pack for a match
python -m src predict <match_id>            # Run every enabled model on a match (series prediction)
python -m src refresh-bp <match_id> <pos>   # Fetch champion select for a single game
python -m src predict-game <match_id> <pos> # Run every model on a single game after BP completes
python -m src grade <match_id>              # Grade series predictions after the match
python -m src grade-game <match_id> <pos>   # Grade single-game predictions after the game
python -m src build-site                    # Rebuild data.json for the leaderboard
python -m src scheduler                     # Run scheduler only (no web UI)
```

## Workflow

```
T-3h before kickoff ── scheduler.predict_tick ──► build context_pack ──► run all models in parallel
                                                                                (agent loop: web_search as needed)

Single-game BP published ──► web "Refresh BP" (/api/refresh-bp)
                                └─ BP complete ──► run all models in parallel (task_game)

Post-match ── scheduler.grade_tick ──► pull real results ──► grade_match / grade_game ──► build_site
```

## Scoring (configs/tasks.yaml)

**Series** — weighted composite, 0–100:

- T1_result **0.45** — win-prob Brier + score similarity + total-games MAE
- T2_matchup **0.25** — key-player recall + swing-factor completeness
- T3_reasoning **0.15** — four-dimension reasoning completeness
- T4_meta **0.15** — patch/meta signal citations

**Single game**:

- G1_result **0.50** — win-prob Brier
- G2_duration **0.25** — game-length MAE
- G3_kills **0.25** — per-team-kill MAE + total-kill sMAPE

## Configuration

- **Add/remove models**: edit `configs/models.yaml` only. Each entry has a
  `provider` field that picks the runner (`openai|openrouter|deepseek|dashscope|zhipu|moonshot`
  → `OpenAICompatRunner`; `anthropic` → `AnthropicRunner`; `google` →
  `GoogleRunner`). The same `web_search` tool is auto-mounted on every model.
- **Tracked leagues**: `configs/leagues.yaml` (slugs come from PandaScore
  `/lol/leagues`).
- **Prediction lead time**: env var `LOLA_PREDICT_LEAD_H` (default `3`).
- **Shared proxy / gateway**: set `LOLA_MODEL_PROXY=https://your-proxy/v1`
  and every model routes through it.

## Data sources & limits

- **LoL data**: PandaScore free tier. Free endpoints cover fixtures, teams,
  rosters, recent form, static hero/item data, post-match scores and per-game
  BP (picks). The **paid** Historical tier adds per-game KDA / gold / CS / damage
  — **not** available on free. Any deeper stats must be supplemented by the
  model's own `web_search` calls.
- **Search**: Zhipu `web_search` API (`search_pro` engine, with intent
  recognition). Every model uses the same backend.

## Adding a new model

1. Add one entry to `configs/models.yaml` with the right `provider`.
2. Provide the corresponding `*_API_KEY` env var (or route through
   `LOLA_MODEL_PROXY`).
3. If the API speaks OpenAI chat-completions with function-calling, use
   `openai_compat` as the provider — `web_search` is auto-mounted.
4. That's it. No code changes needed.

## Reference implementation

Methodology, prompt structure, cached data shapes, and orchestration patterns
are adapted from [`WorldCupArena`](../WorldCupArena) (the soccer counterpart).
Three key differences in this project:

1. Dropped ICS — fixtures come directly from PandaScore
   `/lol/matches/upcoming`.
2. **All models share one unified `web_search` tool** (WorldCupArena split
   injected vs. self-search across two stages).
3. Added **single-game prediction** triggered manually after BP completes,
   exposed via a FastAPI endpoint.

## Development notes

- `prompts/*.md` are re-read on every prediction — no restart needed.
- The required `reasoning.*` subfield names are enforced by **both** the
  schema (`schemas/*.schema.json` `minLength`) and the grader
  (`graders/grade_match.py` `reasoning_completeness`). Keep them in sync.
- No formal test suite yet — verify with ad-hoc `python -c "..."` snippets
  against `validate` and `graders`, plus `python -m src --help` and
  `python -m src build-site` (the site builder works on empty data).

## License

TBD.
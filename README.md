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
  **Cito API** — rosters, recent form + objective control, league standings,
  player form & champion pools, head-to-head, and per-game BP / kills.
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

## Betting advice (post-prediction, value-betting)

For any match that **already has model predictions**, the web UI gains a
**🎲 下注建议** button on the match card, opening a streaming betting-advice
panel — an arena where models are compared on their **betting judgment**:

- **Input** — the user fills in the open odds: moneyline, correct score (3-0 /
  0-3 / 1-3 …), handicap (-1.5 / +1.5), total games over/under. An odds of `0`
  or blank means the market is **not open** and is dropped from analysis.
- **Reasoning source** — the chosen model reasons **only** over the match's
  already-collected `context_pack` + every model's prediction (win probs,
  predicted score, key players, swing factors). It does **not** web_search —
  no new information is fetched.
- **Output** — streams token-by-token into a chat panel (SSE, marked.js
  live-render), first a per-market value narrative, then a fixed-header
  markdown recommendation table that the backend parses into structured picks.

The recommendation table is parsed and persisted to
`data/matches/<slug>/betting_advice/<model>_<timestamp>.json`, so running the
panel for several models yields a **side-by-side comparison** of their
betting acumen (who found the real value bets). This path reuses the runners'
new `stream_chat()` streaming interface (native on OpenAI-compatible models,
one-shot fallback elsewhere).

## Repository layout

```
lolArena/
├─ configs/        models.yaml (model registry) · policy.yaml (strategy) · tasks.yaml (grading)
│                  · leagues.yaml (tracked leagues) · proxies.yaml (outbound HTTP/SOCKS proxies)
├─ prompts/        system.md · task_match.md · task_game.md · betting_system.md · task_betting.md
├─ schemas/        match_prediction / game_prediction (JSON Schema)
├─ src/
│   ├─ adapters/   cito.py (LoL data source, primary) · pandascore.py (fallback) · websearch.py (unified search tool)
│   ├─ pipeline/   collect · prompt_build · validate · orchestrator · scheduler · betting
│   ├─ runners/    base (agent loop + streaming) · openai_compat · anthropic · google · retry (transient-error backoff)
│   ├─ graders/    grade_match · grade_game · metrics/ (Brier, MAE, sMAPE, recall, structural checks)
│   ├─ server/     main.py (FastAPI)
│   └─ leaderboard/build_site.py
├─ data/           matches/<slug>/ (predictions/, betting_advice/)  ·  games/<slug>/g<pos>/  ·  _cito_cache/
├─ doc/            citoapi-lol/ (primary API reference) · pandaScoreApi/ (fallback) · webSearch/ (Zhipu tool docs)
└─ docs/site/      index.html + data.json (single-page leaderboard)
```

## Quick start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Configure keys
cp .env.example .env
#   Required: CITO_API_KEY (or CITO_API_KEYS multi-key pool), ZHIPU_WEBSEARCH_API_KEY
#   Per-model: <PROVIDER>_API_KEY (enable/disable entries in configs/models.yaml)

# 3. Start the service (FastAPI + scheduler together)
python -m src serve
#   Open http://127.0.0.1:8000
```

## CLI (manual operations)

```bash
python -m src scan                          # Scan near-future matches due for prediction
python -m src collect <match_id>            # Build context_pack for a match
python -m src predict <match_id> [--models a,b]   # Run models on a match (series prediction)
python -m src refresh-bp <match_id> <pos>   # Fetch champion select for a single game
python -m src predict-game <match_id> <pos> # Run every model on a single game after BP completes
python -m src grade <match_id>              # Grade series predictions after the match
python -m src grade-game <match_id> <pos>   # Grade single-game predictions after the game
python -m src serve                         # Start FastAPI + scheduler (open http://127.0.0.1:8000)
python -m src build-site                    # Rebuild data.json for the leaderboard
python -m src scheduler                     # Run scheduler only (no web UI)
```

`predict --models glm-5.2,gpt-5` runs a subset; omit the flag to run every
enabled model in `models.yaml`.

## HTTP API (src/server/main.py)

| Method & path            | Purpose                                                        |
| ------------------------ | -------------------------------------------------------------- |
| `GET  /`                 | Single-page leaderboard (`docs/site/index.html`)               |
| `GET  /data.json`        | Leaderboard data (empty payload if site not built yet)         |
| `GET  /api/matches`      | List tracked matches under `data/matches/` with status         |
| `POST /api/refresh-bp`   | Fetch BP for one game; auto-runs single-game prediction if complete |
| `POST /api/predict`      | Manually trigger series prediction for a match                 |
| `POST /api/rebuild`      | Regenerate `data.json` after predictions land                  |
| `POST /api/betting-advice` | **(SSE)** Stream one model's betting analysis for a predicted match |
| `GET  /api/betting-advice/list?slug=` | List all betting-advice runs for a match (model comparison) |

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

## Model registry (configs/models.yaml)

| Model ID          | Display name     | Provider    | Runner             |
| ----------------- | ---------------- | ----------- | ------------------ |
| `gpt-5`           | GPT-5            | openai      | OpenAICompatRunner |
| `claude-opus-4`   | Claude Opus 4    | anthropic   | AnthropicRunner    |
| `gemini-3-pro`    | Gemini 3 Pro     | google      | GeminiRunner       |
| `glm-5.2`         | GLM-5.2          | zhipu       | OpenAICompatRunner |
| `deepseek-v4-pro` | DeepSeek V3 pro  | deepseek    | OpenAICompatRunner |
| `qwen-max`        | Qwen Max         | dashscope   | OpenAICompatRunner |
| `kimi-k2`         | Kimi K2          | moonshot    | OpenAICompatRunner |
| `minimax-m3`      | MiniMax M3       | minimax     | OpenAICompatRunner |

Every entry auto-mounts the same `web_search` tool. `minimax-m3` is a reasoning
model (interleaved thinking) and ships with a longer `timeout_seconds: 600`.

## Configuration

- **Add/remove models**: edit `configs/models.yaml` only. Each entry has a
  `provider` field that picks the runner (`openai|openrouter|deepseek|dashscope|zhipu|moonshot|minimax`
  → `OpenAICompatRunner`; `anthropic` → `AnthropicRunner`; `google` →
  `GeminiRunner`). The same `web_search` tool is auto-mounted on every model.
- **Tracked leagues**: `configs/leagues.yaml` (`cito_league_id` maps to a Cito
  league id like `lol-lck`; the legacy PandaScore `slug`/`id` are kept as fallback).
- **Per-model proxy / gateway**: set `LOLA_MODEL_PROXY=https://your-proxy/v1`
  and every model routes through it. Or override one model only by setting its
  `<PROVIDER>_BASE_URL` (or the `base_url_env` named in its entry).
- **Per-service HTTP/SOCKS proxy**: `configs/proxies.yaml` (e.g. route Cito
  through `socks5://127.0.0.1:1080`). Env overrides: `LOLA_CITO_PROXY_URL`
  and `LOLA_CITO_PROXY_ENABLED` (PandaScore likewise). socks5 needs
  `pip install httpx[socks]`.
- **Retries**: provider `_chat` calls are wrapped by `src/runners/retry.py`
  (tenacity, 3 attempts, 2–30s exponential backoff) on transient errors only —
  timeouts, 429, 5xx. `400/BadRequestError` is deliberately not retried.

### Environment variables

| Variable                 | Purpose                                                          | Default                         |
| ------------------------ | ---------------------------------------------------------------- | ------------------------------- |
| `CITO_API_KEY`           | LoL data, primary source (single key; backward compatible)       | —                               |
| `CITO_API_KEYS`          | LoL data, primary source (comma-separated multi-key pool; auto-rotates, switches on rate-limit/quota) | — |
| `PANDASCORE_API_KEY`     | LoL data, fallback (not called by default)                       | —                               |
| `ZHIPU_WEBSEARCH_API_KEY`| Unified search backend (required to predict)                     | —                               |
| `<PROVIDER>_API_KEY`     | Per-model key (enable entries in `models.yaml`)                  | —                               |
| `LOLA_PREDICT_LEAD_H`    | Hours before kickoff to run series prediction                    | `3`                             |
| `LOLA_RESULT_GRACE_H`    | Result-fetch grace window after scheduled end                    | `2`                             |
| `LOLA_HOST` / `LOLA_PORT`| FastAPI bind address                                             | `127.0.0.1` / `8000`            |
| `LOLA_MODEL_PROXY`       | Route ALL models through one OpenAI-compatible base_url          | (unset = each model's own url)  |

## Data sources & limits

- **LoL data**: Cito API (primary). The free tier covers fixtures, rosters,
  recent form + objective control, league standings, player form & champion
  pools, and per-game BP (picks) + kills — including the per-game detail the
  PandaScore free tier gated behind its paid Historical plan. Free-tier quota
  is **500 req/month/key**; set `CITO_API_KEYS` (comma-separated) to form a key
  pool that multiplies the quota and auto-switches on rate-limit/quota errors.
- `context_pack` blocks are individually toggleable under `context_pack:` in
  `configs/policy.yaml`. Player-level data (`player_form` /
  `player_champion_pool`) is the heaviest (~2 req/player); turn it off when
  quota is tight and let models supplement via `web_search`.
- The PandaScore client (`src/adapters/pandascore.py`) is kept as a fallback
  and is not called by default.
- **Search**: Zhipu `web_search` API (`search_pro` engine, with intent
  recognition). Every model uses the same backend.

## Adding a new model

1. Add one entry to `configs/models.yaml` with the right `provider`
   (`openai|openrouter|deepseek|dashscope|zhipu|moonshot|minimax` all map to
   `OpenAICompatRunner`; also `anthropic`, `google`).
2. Provide the corresponding `*_API_KEY` env var (or route through
   `LOLA_MODEL_PROXY`, or set its `base_url_env`).
3. If the API speaks OpenAI chat-completions with function-calling, use one of
   the OpenAI-compatible providers above — `web_search` is auto-mounted.
4. That's it. No code changes needed.

## Reference implementation

Methodology, prompt structure, cached data shapes, and orchestration patterns
are adapted from [`WorldCupArena`](https://github.com/wzk1015/WorldCupArena/) (the soccer counterpart).
Three key differences in this project:

1. fixtures come directly from the Cito API
   `/lol/schedule/upcoming` (multi-key pool + disk cache to manage free-tier quota).
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

## Deployment (Linux / CentOS + uv)

项目自带一键部署脚本，systemd 守护，开机自启 + 崩溃自动重启，监听 `0.0.0.0:8000`。

### 1. 把代码放到服务器

```bash
sudo mkdir -p /opt/lolArena
sudo chown $USER:$USER /opt/lolArena
cd /opt
git clone https://github.com/你的用户名/lolArena.git
cd lolArena
```

### 2. 装系统依赖 + uv

```bash
sudo yum install -y git curl tar
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env   # 让 uv 进 PATH
```

### 3. 一键安装

```bash
bash deploy/install.sh
```

脚本会：用 uv 建虚拟环境并装依赖 → 生成 `.env`（自动把 `LOLA_HOST` 改成 `0.0.0.0`，`LOLA_PORT` 改成 `8000`）→ 安装并启用 systemd service → 开放 8000 端口 → 做一次模块导入的 sanity check。

> **首次部署必读**：`src/cli.py` 的 `serve` 命令同时启动 FastAPI 和 APScheduler（`predict_tick` / `grade_tick`），所以 `ExecStart` 是 `python -m src serve` 而不是裸 `uvicorn`，否则定时跑分会失效。

### 4. 填 API key 并启动

```bash
vi .env                       # 填 CITO_API_KEY + ZHIPU_WEBSEARCH_API_KEY + 至少一个模型 key
sudo systemctl restart lolarena
```

### 5. 放行云厂商安全组

去云厂商控制台，在「安全组」里放行 **8000/tcp**（脚本只处理服务器本机防火墙）。

### 可调环境变量（install.sh）

| 变量 | 默认 | 说明 |
|------|------|------|
| `PYTHON_VERSION` | `3.11` | uv 用的 Python 版本 |
| `LOLA_HOST` | `0.0.0.0` | 监听地址（部署到服务器必须改 0.0.0.0） |
| `LOLA_PORT` | `8000` | 监听端口 |
| `SKIP_FIREWALL` | `0` | 设 `1` 跳过 firewalld/iptables |
| `SKIP_ENV_EDIT` | `0` | 设 `1` 不动 `.env`（自己手配） |

例：换端口 `LOLA_PORT=8888 bash deploy/install.sh`。

### 常用运维命令

```bash
sudo systemctl start lolarena          # 启动
sudo systemctl status lolarena         # 状态
sudo journalctl -u lolarena -f         # 实时日志
sudo systemctl restart lolarena        # 重启（改代码/改 .env 后）
sudo systemctl stop lolarena           # 停止
```

### 更新代码

```bash
cd /opt/lolArena
git pull
uv sync                                # 依赖有变时, 走 pyproject.toml (无锁文件时生成 uv.lock)
sudo systemctl restart lolarena
```

> **依赖改动**：优先改 `pyproject.toml`（uv sync 的事实源），保持与 `requirements.txt` 同步即可。

## License

TBD.
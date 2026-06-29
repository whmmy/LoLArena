# 06 — Live(实时 / 覆盖)

Cito 的"实时"分三层:
1. **`/lol/coverage`** — 联赛级覆盖矩阵(就算 LCK、LCP 这种"主路径",也别假设)
2. **`/lol/live`** — 当前进行中的比赛(任何时候都可能为空)
3. **`/lol/matches/{id}/coverage`** + **`/lol/live/{gameId}/visual-state`** — 单场实时预检与游戏内推流读取

> ⚠️ **官方明确**:"LCK CL / Academy 视为机会主义数据,直到 `numeric_live_state: true` 才可信赖"。这在 `/lol/coverage` 的响应里有原文。

---

## `GET /lol/coverage`

联赛级覆盖矩阵。**包装 D-ish:`{ success, product, data: [...], definitions, precheck_endpoint, docs }`**。

```bash
curl "https://api.citoapi.com/api/v1/lol/coverage" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

### 实测响应(部分)

```json
{
  "success": true,
  "product": "League of Legends API",
  "data": [
    {
      "league_id": "lol-lck",
      "slug": "lck",
      "name": "LCK",
      "aliases": ["lck-main", "league-of-legends-champions-korea"],
      "schedule_rows": "supported",
      "live_rows": "supported",
      "numeric_live_state": "supported_when_live",
      "webhook_coverage": "fires_when_numeric_live_state_present",
      "production_policy": "primary_live_state_path",
      "note": "Use as the primary live-state path once the match appears in /lol/live and numeric_live_state is true."
    },
    {
      "league_id": "lol-lpl",
      "slug": "lpl",
      "name": "LPL",
      "aliases": ["league-of-legends-pro-league"],
      "schedule_rows": "supported",
      "live_rows": "supported",
      "numeric_live_state": "supported_when_live",
      "webhook_coverage": "fires_when_numeric_live_state_present",
      "production_policy": "primary_live_state_path",
      "note": "..."
    },
    {
      "league_id": "lol-lck-challengers",
      "slug": "lck_challengers",
      "name": "LCK Challengers / Academy",
      "aliases": ["lck-cl", "lck challengers", "academy", "t1-challengers", "dwg-kia-challengers", "ns-challengers", "kt-challengers"],
      "schedule_rows": "supported",
      "live_rows": "opportunistic",
      "numeric_live_state": "opportunistic_when_live",
      "webhook_coverage": "fires_when_numeric_live_state_present",
      "production_policy": "opportunistic_live_state",
      "note": "Treat as opportunistic until schedule metadata, a live row, and numeric live state are all present."
    },
    {
      "league_id": "minor-regional",
      "slug": "minor_regional",
      "name": "Minor / Regional Leagues",
      "aliases": ["academy", "regional", "minor"],
      "schedule_rows": "supported",
      "live_rows": "opportunistic",
      "numeric_live_state": "not_guaranteed",
      "webhook_coverage": "not_guaranteed",
      "production_policy": "opportunistic_live_state",
      "note": "Use schedule data for metadata. Gate automated live decisions on numeric_live_state: true."
    }
  ],
  "definitions": {
    "schedule_metadata": "A stored schedule/match row exists in Cito.",
    "live_row": "The match is currently present in Cito live discovery or live cache.",
    "numeric_live_state": "Current kills, gold, towers, objectives, player stats, or game clock are present.",
    "webhook_event": "Cito has enough numeric live-state data to emit lol.live.state webhooks for subscribed users.",
    "recommended_rule": "For production decisions, require schedule_metadata + live_row + numeric_live_state. For LCK CL / Academy, never assume live state before this pre-check confirms it."
  },
  "precheck_endpoint": "/api/v1/lol/matches/{matchId}/coverage",
  "docs": "https://citoapi.com/docs/api/league-of-legends"
}
```

### 字段

**`data[]` 每条**:

| 字段 | 值 | 含义 |
|---|---|---|
| `league_id` | string | Cito 内部 id(`lol-lck` / `lol-lck-challengers` / `minor-regional`) |
| `slug` / `name` / `aliases[]` | | 标识 |
| `schedule_rows` | `"supported"` / `"opportunistic"` | 赛程数据是否始终可用 |
| `live_rows` | `"supported"` / `"opportunistic"` | 直播行是否稳定 |
| `numeric_live_state` | `"supported_when_live"` / `"opportunistic_when_live"` / `"not_guaranteed"` | 实时数值(经济 / 击杀等)是否可信 |
| `webhook_coverage` | `"fires_when_numeric_live_state_present"` / `"not_guaranteed"` | webhook 是否会触发 |
| `production_policy` | `"primary_live_state_path"` / `"opportunistic_live_state"` | 生产策略标记 |
| `note` | string | 人读说明 |

**`definitions`** 提供了 4 个核心概念的官方定义,务必看。

**`recommended_rule`(摘录)**:

> For production decisions, require schedule_metadata + live_row + numeric_live_state. For LCK CL / Academy, **never assume live state before this pre-check confirms it**.

---

## `GET /lol/live`

当前进行中的 LoL 比赛。**包装 E:** `{ success, status, count, data, coverage, lastKnown, lastCheckedAt, retryAfterSeconds, message, liveOnly, try_instead, alternatives, scheduleEndpoints, docs, developer_help }`。

```bash
curl "https://api.citoapi.com/api/v1/lol/live" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

### 实测响应(无进行中比赛)

```json
{
  "success": true,
  "status": "no_match",
  "count": 0,
  "data": [],
  "coverage": {
    "schedule_metadata": false,
    "live_row": false,
    "numeric_live_state": false,
    "webhook_event": false,
    "coverage_level": "not_found",
    "expected_live_state": false,
    "expected_webhooks": false,
    "message": "No stored schedule metadata or live row was found for this ID."
  },
  "lastKnown": [],
  "lastCheckedAt": "2026-06-29T02:00:57.002Z",
  "retryAfterSeconds": 60,
  "message": "No LoL match is live right now. /lol/live only returns in-progress games; scheduled and upcoming matches are available from /api/v1/lol/schedule/today and /api/v1/lol/schedule/upcoming.",
  "liveOnly": true,
  "try_instead": "/api/v1/lol/schedule/upcoming",
  "alternatives": [
    "/api/v1/lol/schedule/today",
    "/api/v1/lol/schedule/upcoming"
  ],
  "scheduleEndpoints": {
    "today": "/api/v1/lol/schedule/today",
    "upcoming": "/api/v1/lol/schedule/upcoming"
  },
  "docs": "https://citoapi.com/docs/api/league-of-legends",
  "developer_help": {
    "docs": "https://citoapi.com/docs/api/league-of-legends",
    "ai_agent_context": "https://citoapi.com/llms.txt",
    "ai_agent_instruction": "If you are using Cursor, Claude Code, ChatGPT, Codex, or another AI coding agent, give it the ai_agent_context URL plus this response.",
    "copy_paste_prompt": "..."
  }
}
```

### 字段

| 字段 | 说明 |
|---|---|
| `success` / `status` | `"ok"` / `"no_match"` / 其他 |
| `count` | `data[]` 长度 |
| `data[]` | 当前进行中的比赛,结构同 `schedule/upcoming` 的 `data[]`(`matchId`, `team1`, `team2`, `strategy`, `startTime`, `state: "inProgress"`, ...) |
| `coverage` | 当前整体覆盖状态 |
| `lastKnown[]` | 最近一次有直播时的快照(空状态时为 `[]`) |
| `lastCheckedAt` | 上次巡检时间 |
| `retryAfterSeconds` | 客户端建议的轮询间隔 |
| `message` | 人类可读状态说明 |
| `liveOnly` | bool,这个端点**只返回 in-progress** |
| `try_instead` / `alternatives[]` | 没直播时的备选端点 |
| `scheduleEndpoints.today` / `.upcoming` | 自描述的赛程端点 |
| `developer_help` | AI agent 提示块 |

> 💡 **客户端轮询策略**:遵守 `retryAfterSeconds`(本次实测为 60s),不要自作主张 5s 轮询。

### 别名

| 方法 | 路径 |
|---|---|
| GET | `/lol/matches/live`(`/lol/live` 的别名) |
| GET | `/lol/tournaments/live`(`/lol/live` 的别名,标注为 "Live Tournament Matches") |

---

## `GET /lol/matches/{matchId}/coverage`

单场比赛覆盖预检。**包装 D-ish(裸对象)**

```bash
curl "https://api.citoapi.com/api/v1/lol/matches/lol-match-116520394663535912/coverage" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

### 官方示例

```json
{
  "match_id": "lol-match-116520394663535912",
  "coverage": {
    "schedule_metadata": true,
    "live_row": false,
    "numeric_live_state": false,
    "webhook_event": false,
    "coverage_level": "metadata_only",
    "expected_live_state": false,
    "expected_webhooks": false
  },
  "league": {
    "slug": "lck_challengers",
    "live_state_policy": "opportunistic_live_state"
  }
}
```

### 字段

| 字段 | 说明 |
|---|---|
| `match_id` | 比赛 id |
| `coverage.schedule_metadata` | bool,赛程行存在 |
| `coverage.live_row` | bool,live discovery 命中 |
| `coverage.numeric_live_state` | bool,有数值状态(kills/gold/towers 等) |
| `coverage.webhook_event` | bool,有数值状态即可发 webhook |
| `coverage.coverage_level` | `"metadata_only"` / `"live"` / `"not_found"` |
| `coverage.expected_live_state` | bool |
| `coverage.expected_webhooks` | bool |
| `league.slug` | 联赛短 slug |
| `league.live_state_policy` | `"primary_live_state_path"` / `"opportunistic_live_state"` |

> **生产决策铁律**:`schedule_metadata && live_row && numeric_live_state` 三个都为 true 才可以信赖实时数据。

---

## `GET /lol/live/{matchId}/series`

系列赛实时状态(已完成局数 / 当前比分 / 当前 game 上下文)。

```bash
curl "https://api.citoapi.com/api/v1/lol/live/{matchId}/series" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

未实测。响应应包含:
- 已完成的 games(每条含 winner / duration / patch / 双方比分增量)
- 当前比分(team1 score / team2 score)
- 当前 game 上下文(若正在进行)

---

## `GET /lol/live/{gameId}/visual-state`

实时可视化推流读取(高置信度的"准"实时数据)。

```bash
curl "https://api.citoapi.com/api/v1/lol/live/{gameId}/visual-state" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

未实测。根据 webhooks `lol.live.state` payload 推断字段:
- `gameId` / `matchId` / `league`
- `gameTime`(秒)
- `blueTeam` / `redTeam`:各自 `{tag, kills, gold, towers, dragons, barons}`
- `source`(通常是 `"vision"`)

---

## 隐藏端点(`ai/endpoints.json` 有,官方 docs 未列)

| 方法 | 路径 | 说明 |
|---|---|---|
| GET | `/lol/live/{matchId}` | 单个直播比赛 |
| GET | `/lol/live/{gameId}/stats` | 单局直播统计 |
| GET | `/lol/live/{gameId}/window` | 直播数据窗口(滑动) |
| GET | `/lol/live/{gameId}/details` | 直播详情 |
| GET | `/lol/live/{gameId}/events` | 直播事件流 |

---

## Quick reference

| 用途 | 推荐端点 |
|---|---|
| 联赛级实时能力 | `/lol/coverage` |
| 当前正在直播的比赛 | `/lol/live` |
| 单场直播预检 | `/lol/matches/{id}/coverage` |
| 系列赛实时比分 | `/lol/live/{matchId}/series` |
| 单局实时数值 | `/lol/live/{gameId}/visual-state` |
| 实时事件推送(优于轮询) | [09-webhooks.md](./09-webhooks.md) |
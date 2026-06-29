# 01 — 概览 / 认证 / 区域 / 限流 / 错误

## Base URL

```
https://api.citoapi.com/api/v1
```

所有 LoL 端点都挂在这个前缀下(例:`/lol/players/...`、`/lol/matches/...`)。

---

## 认证

每个请求必须带 `x-api-key` 请求头。

```bash
curl "https://api.citoapi.com/api/v1/lol/live" \
  -H "x-api-key: YOUR_CITO_API_KEY" \
  -H "Content-Type: application/json"
```

### Key 类型

| 前缀 | 用途 |
|---|---|
| `cito_live_...` | 正式账户 key,部署应用时用 |
| `pk_demo_...` | 公共只读 demo key,注册前快速试用 |

> ⚠️ Key 只能服务端使用,不要进浏览器 JS;用环境变量存取,定期轮换。

---

## 通用响应结构(实测)

> ⚠️ 官方 docs/reference 描述的 `{ data, pagination }` 在 LoL 接口里**基本不适用**。LoL 接口用自己一套包装。**以下为实测结果**。

### 包装类型枚举(7 种,均已实测)

| 包装类型 | 真实示例接口 | JSON shape |
|---|---|---|
| **A. 裸数组** | `players/{id}/earnings`、`players/{id}/teams` | `[ {...}, {...} ]` |
| **B. 裸对象** | `players/{id}/stats`、`players/{id}/earnings/summary`、`games/{id}`、`matches/{id}` | `{ ... }` |
| **C. `{ success, count, data: [...] }`** | `leagues`、`schedule/upcoming`、`schedule/today`、`leagues/{id}/schedule` | 见下 |
| **D. `{ success, data: {...} }`(单资源)** | `leagues/{id}/standings` → `data.rankings`、`players/{id}/form` → `data.windows` | 见下 |
| **E. `{ success, status, count, data: [...], meta, developer_help }`** | `live`、`schedule/upcoming`、`transfers/player/{id}`(空状态时) | 见下 |
| **F. `{ value: [...], Count }`(注意大小写)** | `transfers`、`transfers/team/{slug}`、`matches/{id}/games` | 见下 |
| **G. `{ gameId, source, section, data, lastUpdated }`** | `games/{id}/plates`、`games/{id}/distributions`、`games/{id}/vision`、`games/{id}/jungle-share` | 见下 |

### 各包装的实测示例

**A. 裸数组** — `GET /lol/players/{id}/earnings`

```json
[
  {
    "tournamentId": "lol-2026-01-09-lck-2026-season-opening",
    "tournamentName": "LCK 2026 Season Opening",
    "tournamentDate": { /* ... */ },
    "placement": 1,
    "earnings": 0,
    "prizePool": 0,
    "tier": null,
    "league": "LCK",
    "teamSize": 5,
    "teammates": null,
    "orgSlugAtTime": "east-3"
  }
]
```

**B. 裸对象** — `GET /lol/players/{id}/stats`

```json
{
  "gamesPlayed": 62, "wins": 39, "losses": 23,
  "winRate": 0.6290322580645161,
  "avgKills": 3.61, "avgDeaths": 3.10, "avgAssists": 6.39,
  "avgKda": 3.23, "avgCs": 273.16, "avgCsPerMin": 8.76,
  "avgGold": 12981.32, "avgGoldPerMin": 416.38,
  "avgDamage": 21086.40, "avgDamagePerMin": 676.35,
  "avgVisionScore": 42.31, "killParticipation": 0.55,
  "firstBloodRate": 0.0645,
  "pentaKills": 0, "quadraKills": 0, "tripleKills": 3
}
```

**C. `{ success, count, data: [...] }`** — `GET /lol/leagues`

```json
{
  "success": true,
  "count": 27,
  "data": [
    {
      "leagueId": "lol-lpl",
      "esportsApiId": "98767991314006698",
      "name": "LPL", "slug": "lpl", "shortName": "LPL",
      "region": "CHINA", "tier": "1",
      "imageUrl": "http://...",
      "priority": 1, "isActive": true,
      "createdAt": "2026-01-14T04:55:53.287Z",
      "lastUpdated": "2026-06-29T01:55:01.169Z",
      "_count": { "tournaments": 20, "teams": 16 },
      "aliases": ["lol-lpl", "lol_lpl", "lpl", "98767991314006698"],
      "endpoints": {
        "detail": "/api/v1/lol/leagues/lol-lpl",
        "schedule": "/api/v1/lol/leagues/lol-lpl/schedule",
        "scheduleBySlug": "/api/v1/lol/leagues/lpl/schedule",
        "standings": "/api/v1/lol/leagues/lol-lpl/standings",
        "teams": "/api/v1/lol/leagues/lol-lpl/teams"
      }
    }
  ]
}
```

**D. `{ success, data: {...} }`** — `GET /lol/leagues/{id}/standings`

```json
{
  "success": true,
  "data": {
    "leagueId": "lol-lck", "leagueName": "LCK",
    "tournamentId": "lol-lck_split_3_2026", "stage": "Groups",
    "rankings": [
      { "rank": 1, "orgSlug": "t1", "teamName": "T1",
        "wins": 0, "losses": 0, "winRate": 0,
        "gameWins": 0, "gameLosses": 0, "gameWinRate": 0 }
    ]
  }
}
```

**E. `{ success, status, count, data: [...], ..., developer_help }`** — `GET /lol/live`(空状态)

```json
{
  "success": true,
  "status": "no_match",
  "count": 0,
  "data": [],
  "coverage": {
    "schedule_metadata": false, "live_row": false,
    "numeric_live_state": false, "webhook_event": false,
    "coverage_level": "not_found",
    "expected_live_state": false, "expected_webhooks": false,
    "message": "No stored schedule metadata or live row was found for this ID."
  },
  "lastKnown": [], "lastCheckedAt": "2026-06-29T02:00:57.002Z",
  "retryAfterSeconds": 60,
  "message": "No LoL match is live right now. ...",
  "liveOnly": true,
  "try_instead": "/api/v1/lol/schedule/upcoming",
  "alternatives": ["/api/v1/lol/schedule/today", "/api/v1/lol/schedule/upcoming"],
  "scheduleEndpoints": { "today": "..", "upcoming": ".." },
  "docs": "https://citoapi.com/docs/api/league-of-legends",
  "developer_help": {
    "docs": "https://citoapi.com/docs/api/league-of-legends",
    "ai_agent_context": "https://citoapi.com/llms.txt",
    "ai_agent_instruction": "If you are using Cursor, Claude Code, ChatGPT, Codex, or another AI coding agent, give it the ai_agent_context URL plus this response.",
    "copy_paste_prompt": "Use the Cito API docs (https://citoapi.com/docs/api/league-of-legends) and the Cito AI agent context (https://citoapi.com/llms.txt). Fix this API request and show the correct endpoint, headers, and example code: /api/v1/lol/live"
  }
}
```

> 💡 `developer_help` 字段在大多数响应里都会出现——Cito 在明确告诉你:**"如果你(或你的 AI 助手)不知道怎么调对,把上面那段 copy_paste_prompt 复制给 LLM"**。这本身是个产品设计亮点。

**F. `{ value: [...], Count }`** — `GET /lol/transfers`(注意 `value` 不是 `data`、`Count` 首字母大写)

```json
{
  "value": [
    {
      "id": "ae924f85-9a3d-4e29-8bdf-7ef6e37733ae",
      "playerName": "Cody Sun",
      "fromOrg": { "slug": "ccg", "name": "CCG Esports", "logoUrl": "...", "region": "NORTH_AMERICA" },
      "toOrg": null,
      "transferDate": { /* ... */ },
      "transferType": "released", "role": "Bot",
      "announcementUrl": "https://lol.fandom.com/wiki/Data%3ANews%2F2026-06-27",
      "details": "Cody Sun leaves.",
      "player": {
        "lolPlayerId": "4cd09091-f8c2-4c76-be75-a4472aa77bbb",
        "currentIgn": "Cody Sun", "realName": "Liyu Sun",
        "nationality": "CA", "imageUrl": "..."
      }
    }
  ],
  "Count": 3
}
```

**G. `{ gameId, source, section, data, lastUpdated }`** — `GET /lol/games/{id}/distributions`

```json
{
  "gameId": "lol-game-115548128963037570",
  "source": "cito_postgame_enrichment",
  "section": "distributions",
  "data": { "gold": null, "damage": null },
  "lastUpdated": "2026-06-14T16:56:27.804Z"
}
```

> postgame 系列接口(`plates` / `distributions` / `vision` / `jungle-share`)在数据未生成时 `data` 整体为 `null`。

### `players/{id}/form` / `champion-pool` 的特殊包装

这两个有"选手档案 + 内容"的复合包装:

`/lol/players/{id}/form`:

```json
{
  "player": { "lolPlayerId": "...", "currentIgn": "Faker", "role": "Mid", "currentTeam": "East 3", "currentTeamSlug": "east-3" },
  "windows": [
    {
      "window": 20, "sampleComplete": false,
      "matchesAnalyzed": 20, "gamesAnalyzed": 59,
      "wins": 39, "losses": 20, "winRate": 0.661,
      "avgKills": 3.8, "avgDeaths": 3.25, "avgAssists": 6.71,
      "avgKda": 3.23, "kdaVariance": 19.05,
      "consistencyScore": 56.35,
      "avgCs": 287.05, "avgCsPerMin": 8.76,
      "avgGold": 13641.39, "avgGoldPerMin": 416.38,
      "avgDamage": 22158.59, "avgDamagePerMin": 676.35,
      "avgVisionScore": 44.46,
      "killParticipation": 0.564, "firstBloodRate": 0.0678,
      "championPool": [
        { "championId": 34, "championName": "Anivia", "gamesPlayed": 10, "wins": 8, "winRate": 0.8 },
        ...
      ],
      "dateRange": { "from": {}, "to": {} }
    }
  ]
}
```

`/lol/players/{id}/champion-pool`:

```json
{
  "player": { ... },
  "filters": { "last": 14, "league": null },
  "matchesAnalyzed": 14, "gamesAnalyzed": 41,
  "championPool": [
    { "championId": 34, "championName": "Anivia",
      "picks": 9, "wins": 7, "losses": 2,
      "unknownResults": 0, "lastPickedAt": {},
      "decidedGames": 9, "winRate": 0.7778, "pickRate": 0.2195 }
  ],
  "picks": [
    { "matchId": "...", "gameId": "...", "gameNumber": 5,
      "startTime": "...", "league": "lck", "tournamentName": "Summer 2024",
      "teamSlug": "t1", "championId": 13, "championName": "Ryze",
      "result": "win" }
  ]
}
```

### 分页参数(适用列表型)

多数列表端点接受 `page` / `limit`(部分接受 `cursor`)。具体参数在每个接口章节列出。

---

## 区域端点

默认 `api.citoapi.com` 自动就近路由。延迟敏感场景可显式用区域端点:

| Code | Endpoint | 延迟 |
|---|---|---|
| `NA-EAST` | `na-east.api.citoapi.com` | ~20ms |
| `NA-WEST` | `na-west.api.citoapi.com` | ~25ms |
| `EU` | `eu.api.citoapi.com` | ~30ms |
| `ASIA` | `asia.api.citoapi.com` | ~45ms |
| `OCE` | `oce.api.citoapi.com` | ~50ms |
| `BR` | `br.api.citoapi.com` | ~40ms |
| `ME` | `me.api.citoapi.com` | ~55ms |

或直接用 `?region=EU` query 参数过滤(默认端点也支持)。

**建议**:跨区数据(选手档案、转会历史)用默认端点;实时直播数据用离你最近的区域端点。

---

## 限流

按 key 计费,按月 + 按分钟双限。

| 计划 | 月配额 | 每分钟 | Burst |
|---|---:|---:|---:|
| Free | 500 | 10 | 20 |
| One Game Starter | 10k–250k | 30 | 60 |
| Basic | 50,000 | 30 | 60 |
| Pro | 250,000 | 100 | 200 |
| Business | 2,000,000 | 500 | 1,000 |
| Enterprise | 协商 | 协商 | 协商 |

### 响应头

```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 87
X-RateLimit-Reset: 1705348800
```

| Header | 说明 |
|---|---|
| `X-RateLimit-Limit` | 当前窗口最大请求数 |
| `X-RateLimit-Remaining` | 剩余请求数 |
| `X-RateLimit-Reset` | 窗口重置的 Unix 时间戳 |

### 429 响应体

```json
{
  "success": false,
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "You hit your current request limit. ... Use webhooks for real-time updates.",
    "docs": "https://citoapi.com/docs/rate-limits",
    "actions": [
      { "label": "Upgrade plan", "url": "https://citoapi.com/dashboard/billing/plans" },
      { "label": "Learn about webhooks", "url": "https://citoapi.com/webhooks/" }
    ],
    "upgradeUrl": "https://citoapi.com/dashboard/billing/plans",
    "webhooksUrl": "https://citoapi.com/webhooks/"
  }
}
```

→ 客户端应尊重响应里的 `retry_after`(秒)做退避。

---

## 错误码

| HTTP | 含义 |
|---|---|
| 400 | 参数非法 / 请求格式错 |
| 401 | key 缺失或失效 |
| 403 | key 没权限访问该资源 |
| 404 | 资源不存在 |
| 429 | 触发限流 |
| 500 | 服务端内部错 |
| 503 | 服务暂不可用(查 status 页) |

错误响应体:

```json
{
  "error": {
    "type": "invalid_request",
    "message": "Player 'Bugha123' not found",
    "param": "username",
    "code": "player_not_found"
  }
}
```

| 字段 | 说明 |
|---|---|
| `type` | 错误类型(下表) |
| `message` | 人类可读 |
| `param` | 触发错误的参数(如适用) |
| `code` | 机器可读错误码 |

### 错误 type 枚举

| type | 说明 |
|---|---|
| `invalid_request` | 请求非法 |
| `authentication_error` | key 无效或过期 |
| `authorization_error` | key 没权限 |
| `not_found` | 资源不存在 |
| `rate_limit_exceeded` | 触发限流 |
| `validation_error` | 参数校验失败 |
| `internal_error` | 服务端异常 |

---

## 字段可信度标记约定

本目录里所有响应字段使用统一标记:

- ✅ **已验证** — 来自官方文档示例(目前仅 Player Earnings / Org and Roster History 两个);或拿到 API key 后实测确认
- 🟡 **推断** — 基于接口 summary、字段语义、通用响应约定推断,实际可能有差异
- ⚪ **通用结构** — 分页 / 包装层

拿到 key 后,推断会逐步升级为已验证。
# 07 — Transfers

转会数据。3 个核心接口(按时间 / 按选手 / 按队伍),全部实测。

---

## `GET /lol/transfers`

最近转会列表。**包装 F:`{ value: [...], Count }`**。

```bash
curl "https://api.citoapi.com/api/v1/lol/transfers?limit=20" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

可选 query:
- `limit` — 最大返回数
- `team` / `teamSlug` — 过滤队伍
- `league` — 过滤联赛
- `since` — 起始时间

### 实测响应

```json
{
  "value": [
    {
      "id": "ae924f85-9a3d-4e29-8bdf-7ef6e37733ae",
      "playerName": "Cody Sun",
      "fromOrg": {
        "slug": "ccg",
        "name": "CCG Esports",
        "logoUrl": "http://static.lolesports.com/teams/1743818097778__CCGIcon_Main.png",
        "region": "NORTH_AMERICA"
      },
      "toOrg": null,
      "transferDate": { /* ISO datetime */ },
      "transferType": "released",
      "role": "Bot",
      "announcementUrl": "https://lol.fandom.com/wiki/Data%3ANews%2F2026-06-27",
      "details": "Cody Sun leaves.",
      "player": {
        "lolPlayerId": "4cd09091-f8c2-4c76-be75-a4472aa77bbb",
        "currentIgn": "Cody Sun",
        "realName": "Liyu Sun",
        "nationality": "CA",
        "imageUrl": "http://static.lolesports.com/players/1655828053256_MIRAGEELYANDRA_CODYSUN-picture.png"
      }
    },
    {
      "id": "f3954df1-eacb-4f1b-9158-807e55fc4387",
      "playerName": "Rafal",
      "fromOrg": null,
      "toOrg": {
        "slug": "the-paradox-invaders",
        "name": "The ParadOx Invaders",
        "logoUrl": null,
        "region": "EMEA"
      },
      "transferDate": {},
      "transferType": "signed",
      "role": "Support",
      "announcementUrl": "https://lol.fandom.com/wiki/Data%3ANews%2F2026-06-27",
      "details": "Rafal joins from academy roster.",
      "player": {
        "lolPlayerId": "61a63634-ff68-483a-a7a6-fe2da1bbc196",
        "currentIgn": "RaFaL",
        "realName": "Rafail Kyriakakis",
        "nationality": null,
        "imageUrl": null
      }
    }
  ],
  "Count": 3
}
```

### 字段

| 字段 | 类型 | 说明 |
|---|---|---|
| `id` | string(UUID) | 转会记录 id,可用作 `transfers/{id}` 查询 |
| `playerName` | string | 当时显示名 |
| `fromOrg` | object/null | 来源组织,`null` 表示无(新签或复出) |
| `toOrg` | object/null | 去向组织,`null` 表示无(被裁或退役) |
| `transferDate` | object | 转会日期(实测有时为空 `{}`) |
| `transferType` | string | `"signed"` / `"released"` / `"contract_extension"` / `"trade"` 等 |
| `role` | string | `"Top"` / `"Jungle"` / `"Mid"` / `"Bot"` / `"Support"` |
| `announcementUrl` | string | 公告链接(通常 lol.fandom.com Data:News) |
| `details` | string | 简短文字描述 |
| `player.lolPlayerId` | UUID | Cito 选手 id,可用于 `players/{id}/*` |
| `player.currentIgn` | string | 当前 ID |
| `player.realName` | string | 真实姓名 |
| `player.nationality` | string/null | 国籍(ISO 3166-1 alpha-2,如 `"CA"`、`"KR"`) |
| `player.imageUrl` | string/null | 选手头像 |

### `org` 子对象

| 字段 | 说明 |
|---|---|
| `slug` | 组织短 slug |
| `name` | 显示名 |
| `logoUrl` | 队徽 URL(可能为 null) |
| `region` | Riot 区域枚举 |

---

## `GET /lol/transfers/player/{playerId}`

单个选手的转会历史。空状态走**包装 E**(成功但 `data: []`)。

```bash
curl "https://api.citoapi.com/api/v1/lol/transfers/player/{playerId}" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

### 实测响应(空)

```json
{
  "success": true,
  "status": "no_results",
  "count": 0,
  "data": [],
  "message": "No results were found for this request.",
  "try_instead": "/api/v1/lol/transfers",
  "docs": "https://citoapi.com/docs/api/league-of-legends",
  "meta": {
    "requestedAt": "2026-06-29T02:02:34.237Z",
    "filters": { "limit": "3" }
  },
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
| `success` / `status` | `"no_results"` 时 count=0、data=[] |
| `count` / `data[]` | 命中时为转会记录数组,元素结构同 `/lol/transfers` |
| `message` | 人类可读 |
| `try_instead` | 建议改调的端点 |
| `meta` | `{ requestedAt, filters }` |
| `developer_help` | AI agent 提示 |

### 注意

实测 Faker(`/lol/transfers/player/c76dc4df-...`)返回空——这意味着:
- **Cito 的 transfers 表只追踪近期显著转会**,不保留完整生涯转会流水
- 需要生涯转会的,得自己从 `players/{id}/teams` 推导(每条 team 记录 = 一次换队)

---

## `GET /lol/transfers/team/{slug}`

单个队伍的转会动态。**包装 F:`{ value: [...], Count }`**。

```bash
curl "https://api.citoapi.com/api/v1/lol/transfers/team/t1?limit=20" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

### 实测响应(T1,部分)

```json
{
  "value": [
    {
      "id": "03f1b8d9-8894-4e04-ab5b-2028f6e6c392",
      "playerName": "Keria",
      "fromOrg": {
        "slug": "t1-rookies",
        "name": "T1 Rookies",
        "logoUrl": "http://static.lolesports.com/teams/1651078718919_download99.png",
        "region": "KOREA"
      },
      "toOrg": null,
      "transferDate": {},
      "transferType": "contract_extension",
      "role": "Support",
      "announcementUrl": "https://lol.fandom.com/wiki/Data%3ANews%2F2026-04-26",
      "details": "Keria's contract is extended through 2029.",
      "player": {
        "lolPlayerId": "ce9fd881-9cce-4dc7-b253-99286f6da8f8",
        "currentIgn": "Keria",
        "realName": "Minseok Ryu",
        "nationality": "KR",
        "imageUrl": "http://static.lolesports.com/players/1769087515444_LCK_T1_Keria_F.PNG"
      }
    }
  ],
  "Count": 2
}
```

### 字段

同 `/lol/transfers`(包装 F)。每条元素结构完全一致。

---

## 隐藏端点(`ai/endpoints.json` 有,官方 docs 未列)

| 方法 | 路径 | 说明 |
|---|---|---|
| GET | `/lol/transfers/{transferId}` | 单条转会详情(用 `/lol/transfers` 列表里的 `id` 字段) |
| GET | `/lol/transfers/window/{season}` | 按转会窗(如 `2025-spring` / `2025-summer`)批量拉取 |

---

## Quick reference

| 用途 | 推荐端点 |
|---|---|
| 最近所有转会 | `/lol/transfers?limit=20` |
| 单个选手的转会 | `/lol/transfers/player/{id}` |
| 单个队伍的转会 | `/lol/transfers/team/{slug}` |
| 单条转会详情 | `/lol/transfers/{transferId}` |
| 某赛季转会窗 | `/lol/transfers/window/2025-summer` |
| 选手生涯队伍流水 | `/lol/players/{id}/teams`(裸数组,每条是一次任期) |
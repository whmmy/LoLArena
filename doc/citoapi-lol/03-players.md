# 03 — Players

选手档案、收益、状态、英雄池、组织履历。覆盖官方 markdown 列出的 6 个 + `ai/endpoints.json` 中未列在 markdown 的隐藏端点。

> ⚠️ **重要**:官方 docs 给的示例 `/lol/players/{id}/teams` 用的是 `{ success, data: { teams: [...] } }` 包装。**实测是裸数组**。本文档以实测为准。

---

## `GET /lol/players/{playerId}/earnings`

选手历次奖金明细。**裸数组**(包装 A)。

```bash
curl "https://api.citoapi.com/api/v1/lol/players/{playerId}/earnings" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

### 实测响应

```json
[
  {
    "tournamentId": "lol-2026-01-09-lck-2026-season-opening",
    "tournamentName": "LCK 2026 Season Opening",
    "tournamentDate": { /* ISO datetime 对象,有时为空 */ },
    "placement": 1,
    "earnings": 0,
    "prizePool": 0,
    "tier": null,
    "league": "LCK",
    "teamSize": 5,
    "teammates": null,
    "orgSlugAtTime": "east-3"
  },
  {
    "tournamentId": "lol-2025-11-09-2025-world-championship",
    "tournamentName": "2025 World Championship",
    "tournamentDate": {},
    "placement": 1,
    "earnings": 200000,
    "prizePool": 1000000,
    "tier": "S-Tier",
    "league": "Worlds",
    "teamSize": 5,
    "teammates": null,
    "orgSlugAtTime": "east-3"
  }
]
```

### 字段

| 字段 | 类型 | 说明 |
|---|---|---|
| `tournamentId` | string | 赛事 id |
| `tournamentName` | string | 赛事名 |
| `tournamentDate` | object/string | 赛事日期(实测有时为空 `{}`) |
| `placement` | int | 名次,`1` = 冠军。`999` 表示参与但无成绩 |
| `earnings` | int | 该选手实际奖金(USD) |
| `prizePool` | int | 赛事总奖金池 |
| `tier` | string | `"S-Tier"` / `"A-Tier"` / `"Qualifier"` / `null` |
| `league` | string | 所属联赛显示名(如 `"LCK"`、`"MSI"`、`"Worlds"`)。**非国际赛时为 null** |
| `teamSize` | int | 队伍人数,LoL 固定 5 |
| `teammates` | string[]/null | 队友名单(仅部分赛事填充,实测多为 null) |
| `orgSlugAtTime` | string | 当时所在组织 slug |

> 💡 官方 docs 给的示例(`tournamentName` / `tournamentDate` / `placement` / `earnings` / `league` / `orgSlugAtTime`)只是该接口**真实字段的子集**——实测多了 `tournamentId` / `prizePool` / `tier` / `teamSize` / `teammates`。

---

## `GET /lol/players/{playerId}/earnings/summary`

选手奖金汇总。**裸对象**(包装 B)。

```bash
curl "https://api.citoapi.com/api/v1/lol/players/{playerId}/earnings/summary" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

### 实测响应(Faker)

```json
{
  "totalEarnings": 1922084.56,
  "tournamentCount": 80,
  "firstPlaceCount": 30,
  "top3Count": 63,
  "avgPlacement": 27.73,
  "bestPlacement": 1,
  "highestEarning": 405600,
  "earningsByYear": {
    "2013": 218666.8, "2014": 30188.2, "2015": 247291.6,
    "2016": 490139.2, "2017": 298855, "2018": 6416,
    "2019": 85255.8, "2020": 24495.8, "2021": 57267.2,
    "2022": 124444.2, "2023": 125115.8, "2024": 196956,
    "2025": 319458.4, "2026": 0
  },
  "earningsByLeague": {
    "LCK": 271781.8, "MSI": 301200, "Worlds": 1460668.2
  },
  "worldsAppearances": 12,
  "worldsWins": 7,
  "msiAppearances": 9,
  "msiWins": 2
}
```

### 字段

| 字段 | 说明 |
|---|---|
| `totalEarnings` | 生涯总奖金(USD) |
| `tournamentCount` | 参赛场次 |
| `firstPlaceCount` | 冠军次数 |
| `top3Count` | 前 3 次数 |
| `avgPlacement` | 平均名次(数字越低越好) |
| `bestPlacement` | 历史最好名次,通常是 1 |
| `highestEarning` | 单届最高奖金 |
| `earningsByYear` | 按年份分布,**当前年(如 2026)可能为 0** |
| `earningsByLeague` | 按联赛分布 |
| `worldsAppearances` / `worldsWins` | 全球总决赛出场/夺冠次数 |
| `msiAppearances` / `msiWins` | MSI 出场/夺冠次数 |

---

## `GET /lol/players/{playerId}/stats`

选手场均聚合统计。**裸对象**(包装 B)。

```bash
curl "https://api.citoapi.com/api/v1/lol/players/{playerId}/stats" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

### 实测响应(Faker)

```json
{
  "gamesPlayed": 62,
  "wins": 39,
  "losses": 23,
  "winRate": 0.6290322580645161,
  "avgKills": 3.6129032258064515,
  "avgDeaths": 3.096774193548387,
  "avgAssists": 6.387096774193548,
  "avgKda": 3.2291666666666665,
  "avgCs": 273.16129032258067,
  "avgCsPerMin": 8.761661694459294,
  "avgGold": 12981.322580645161,
  "avgGoldPerMin": 416.3765541740675,
  "avgDamage": 21086.40322580645,
  "avgDamagePerMin": 676.3474107158254,
  "avgVisionScore": 42.306451612903224,
  "killParticipation": 0.5495410256410255,
  "firstBloodRate": 0.06451612903225806,
  "pentaKills": 0,
  "quadraKills": 0,
  "tripleKills": 3
}
```

### 字段

| 字段 | 说明 |
|---|---|
| `gamesPlayed` / `wins` / `losses` / `winRate` | 基础胜负 |
| `avgKills` / `avgDeaths` / `avgAssists` / `avgKda` | 场均 KDA,avgKda = (kills+assists)/deaths |
| `avgCs` / `avgCsPerMin` | 场均补刀 + 每分钟补刀 |
| `avgGold` / `avgGoldPerMin` | 场均金币 + 每分钟金币(GPM) |
| `avgDamage` / `avgDamagePerMin` | 场均伤害 + DPM |
| `avgVisionScore` | 场均视野分 |
| `killParticipation` | 参团率(0–1) |
| `firstBloodRate` | 一血率 |
| `pentaKills` / `quadraKills` / `tripleKills` | 五杀/四杀/三杀次数 |

> 这是**赛季聚合**(不是生涯)。换赛季或换 league 过滤参数会改变数据。

---

## `GET /lol/players/{playerId}/form`

选手滑动窗口状态,3 个 window 并列。包装 `{ player, windows: [...] }`。

```bash
curl "https://api.citoapi.com/api/v1/lol/players/{playerId}/form" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

可选 query:
- `windows` — 自定义窗口,如 `?windows=10,20,50`(默认 10/20/50)
- `league` — 过滤联赛,如 `?league=lck`
- `role` — 过滤位置,如 `?role=Mid`

### 实测响应(部分,Faker 20-window)

```json
{
  "player": {
    "lolPlayerId": "c76dc4df-1a6f-4c83-b7ba-44cf213e0291",
    "currentIgn": "Faker",
    "role": "Mid",
    "currentTeam": "East 3",
    "currentTeamSlug": "east-3"
  },
  "windows": [
    {
      "window": 20,
      "sampleComplete": false,
      "matchesAnalyzed": 20,
      "gamesAnalyzed": 59,
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
        { "championId": 268, "championName": "Azir", "gamesPlayed": 8, "wins": 6, "winRate": 0.75 }
      ],
      "dateRange": { "from": {}, "to": {} }
    }
  ]
}
```

### 字段

**`player`(选手快照)**:`{ lolPlayerId, currentIgn, role, currentTeam, currentTeamSlug }`

**`windows[]`(每个窗口)**:

| 字段 | 说明 |
|---|---|
| `window` | 窗口大小(10/20/50) |
| `sampleComplete` | bool,该选手历史是否够填满 window。`false` 表示样本不足,数字会偏 |
| `matchesAnalyzed` / `gamesAnalyzed` | 实际取的 series 数和 game 数 |
| `wins` / `losses` / `winRate` | 该窗口胜负 |
| `avgKills/Deaths/Assists/Kda` | 场均数据 |
| `kdaVariance` | KDA 方差,数值越低越稳定 |
| `consistencyScore` | 综合稳定度分数(0-100?) |
| `avgCs/avgCsPerMin` `avgGold/avgGoldPerMin` `avgDamage/avgDamagePerMin` `avgVisionScore` `killParticipation` `firstBloodRate` | 场均聚合指标 |
| `championPool[]` | 该窗口内使用的英雄,`{ championId, championName, gamesPlayed, wins, winRate }` |
| `dateRange.from` / `dateRange.to` | 时间范围(实测常为 `{}`) |

---

## `GET /lol/players/{playerId}/champion-pool`

选手英雄池(近 N 场),带 picks 明细。包装 `{ player, filters, ..., championPool, picks }`。

```bash
curl "https://api.citoapi.com/api/v1/lol/players/{playerId}/champion-pool?last=14" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

可选 query:
- `last` — 取最近 N 场,默认 14
- `league` — 过滤联赛

### 实测响应(部分,Faker)

```json
{
  "player": {
    "lolPlayerId": "c76dc4df-1a6f-4c83-b7ba-44cf213e0291",
    "currentIgn": "Faker",
    "role": "Mid",
    "currentTeam": "East 3",
    "currentTeamSlug": "east-3"
  },
  "filters": { "last": 14, "league": null },
  "matchesAnalyzed": 14,
  "gamesAnalyzed": 41,
  "championPool": [
    {
      "championId": 34, "championName": "Anivia",
      "picks": 9, "wins": 7, "losses": 2,
      "unknownResults": 0, "lastPickedAt": {},
      "decidedGames": 9, "winRate": 0.7778, "pickRate": 0.2195
    },
    {
      "championId": 4, "championName": "Twisted Fate",
      "picks": 7, "wins": 4, "losses": 3,
      "unknownResults": 0, "lastPickedAt": {},
      "decidedGames": 7, "winRate": 0.5714, "pickRate": 0.1707
    }
  ],
  "picks": [
    {
      "matchId": "lol-match-115548128963037587",
      "gameId": "lol-game-115548128963037592",
      "gameNumber": 5,
      "startTime": "2026-06-14T06:00:00.000Z",
      "league": "lck",
      "tournamentName": "Summer 2024",
      "teamSlug": "t1",
      "championId": 13, "championName": "Ryze",
      "result": "win"
    }
  ]
}
```

### 字段

| 字段 | 说明 |
|---|---|
| `player` | 选手快照 |
| `filters.last` / `filters.league` | 当前应用的过滤 |
| `matchesAnalyzed` / `gamesAnalyzed` | 实际取的样本 |
| `championPool[]` | 英雄聚合:`{ championId, championName, picks, wins, losses, unknownResults, lastPickedAt, decidedGames, winRate, pickRate }` |
| `picks[]` | 每次 pick 一条:`{ matchId, gameId, gameNumber, startTime, league, tournamentName, teamSlug, championId, championName, result }` |

> `picks` 里 `result` 是该选手对局胜负(`"win"` / `"loss"`);`league` 用小写 slug(`"lck"` / `"worlds"`)。

---

## `GET /lol/players/{playerId}/teams`

选手组织 / 队伍履历。**裸数组**(包装 A)。

> ⚠️ **官方 docs 示例**:`{ success, true, data: { playerId, playerName, teams: [...] } }` —— **与实测不符**。实测是裸数组,每条 = 一次加入某组织的记录。

```bash
curl "https://api.citoapi.com/api/v1/lol/players/{playerId}/teams" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

### 实测响应(Faker,部分)

```json
[
  {
    "orgSlug": "t1",
    "teamName": "T1",
    "role": "MID",
    "status": "current",
    "joinDate": "2026-02-01T00:00:00.000Z",
    "leaveDate": null,
    "leaveReason": null,
    "isStarter": false,
    "logoUrl": "http://static.lolesports.com/teams/1726801573959_539px-T1_2019_full_allmode.png"
  },
  {
    "orgSlug": "t1-challengers",
    "teamName": "T1 Esports Academy",
    "role": "MID",
    "status": "current",
    "joinDate": "2026-02-01T00:00:00.000Z",
    "leaveDate": null,
    "leaveReason": null,
    "isStarter": true,
    "logoUrl": "http://static.lolesports.com/teams/T1-FullonDark.png"
  },
  {
    "orgSlug": "lck-allstars",
    "teamName": "LCK All-Stars",
    "role": "MID",
    "status": "current",
    "joinDate": "2026-02-01T00:00:00.000Z",
    "leaveDate": null,
    "leaveReason": null,
    "isStarter": true,
    "logoUrl": "http://static.lolesports.com/teams/LCK.png"
  }
]
```

### 字段

| 字段 | 类型 | 说明 |
|---|---|---|
| `orgSlug` | string | 组织短 slug(如 `t1`、`t1-challengers`) |
| `teamName` | string | 队伍显示名 |
| `role` | string | `"TOP"` / `"JUG"` / `"MID"` / `"BOT"` / `"SUP"` |
| `status` | string | `"current"` / 历史状态 |
| `joinDate` | ISO datetime | 加入日期 |
| `leaveDate` | ISO datetime/null | 离开日期,仍在队为 null |
| `leaveReason` | string/null | 离开原因(如 `"contract_ended"`) |
| `isStarter` | bool | 是否首发 |
| `logoUrl` | string | 队徽 URL |

> 一个选手可能同时挂在多个 org(`isStarter=false` 的 T1 + `isStarter=true` 的 T1 Esports Academy + LCK All-Stars 等)。

---

## 隐藏端点(`ai/endpoints.json` 有,官方 docs 未列)

> ⚠️ 以下接口**未实测**,字段结构请以官方为准。

### 选手档案 / 搜索

| 方法 | 路径 | 说明 | 关键 query params |
|---|---|---|---|
| GET | `/lol/players` | 全部选手列表 | — |
| GET | `/lol/players/search` | 选手搜索(autocomplete) | `q`(必填) |
| GET | `/lol/players/{playerId}` | 单个选手档案 | — |
| GET | `/lol/players/{playerId}/matches` | 选手参赛历史 | — |
| GET | `/lol/players/{playerId}/champions` | 选手英雄池(汇总) | — |
| GET | `/lol/players/{playerId}/achievements` | 选手成就与头衔 | — |
| GET | `/lol/players/{playerId}/stats/career` | 选手生涯统计 | — |
| GET | `/lol/players/{playerId}/compare/{otherPlayerId}` | 两选手对比 | — |
| GET | `/lol/players/{playerId}/peers` | 相似选手 | — |

### Leaderboards(8 个全局排行)

| 方法 | 路径 | 维度 |
|---|---|---|
| GET | `/lol/leaderboards/earnings` | 奖金榜 |
| GET | `/lol/leaderboards/kda` | KDA 榜 |
| GET | `/lol/leaderboards/cs` | 补刀榜(每分钟) |
| GET | `/lol/leaderboards/winrate` | 胜率榜 |
| GET | `/lol/leaderboards/vision` | 视野榜 |
| GET | `/lol/leaderboards/firstblood` | 一血率榜 |
| GET | `/lol/leaderboards/damage` | 伤害榜(每分钟) |
| GET | `/lol/leaderboards/championships` | 冠军数榜 |

### Search / Autocomplete / Trending(Postman Collection)

| 方法 | 路径 | 说明 |
|---|---|---|
| GET | `/lol/search` | 统一搜索(选手/队/赛事) | `q`(必填) |
| GET | `/lol/autocomplete` | 搜索自动补全 | `q`(必填) |
| GET | `/lol/trending` | 热门选手/队/话题 | — |

### Player trend(Analytics)

| 方法 | 路径 |
|---|---|
| GET | `/lol/analytics/players/{playerId}/trend` |

---

## Quick reference

| 用途 | 推荐端点 |
|---|---|
| 选手生涯奖金 | `/lol/players/{id}/earnings` + `/earnings/summary` |
| 选手场均数据 | `/lol/players/{id}/stats` |
| 近期状态(多窗口) | `/lol/players/{id}/form?windows=10,20,50` |
| 英雄池(含每 pick) | `/lol/players/{id}/champion-pool?last=N` |
| 组织履历 | `/lol/players/{id}/teams` |
| 找选手 ID | `/lol/players/search?q=faker` |
| 全局排行 | `/lol/leaderboards/{dimension}` |
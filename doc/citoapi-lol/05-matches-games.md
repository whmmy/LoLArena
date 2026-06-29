# 05 — Matches & Games

比赛元数据 + 对局 + 赛后数据(plates / distributions / vision / jungle-share / gold graph)。

---

## `GET /lol/matches/{id}`

单场比赛详情。**裸对象**(包装 B)。`{id}` 兼容两种形态:
- 完整前缀:`lol-match-115548128963037587`
- 裸数字:`115548128963037587`(今日赛程里就是这种)

```bash
curl "https://api.citoapi.com/api/v1/lol/matches/lol-match-115548128963037587" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

### 实测响应

```json
{
  "matchId": "lol-match-115548128963037587",
  "esportsApiId": "115548128963037587",
  "tournamentId": "lol-lck_summer_2024",
  "blockName": "Knockouts",
  "round": null,
  "team1": {
    "slug": "gen",
    "name": "Gen.G Esports",
    "shortName": "GEN",
    "logoUrl": "https://static.lolesports.com/teams/1773829250929_GENGLOGO_GOLD.png",
    "score": 2
  },
  "team2": {
    "slug": "t1",
    "name": "T1",
    "shortName": "T1",
    "logoUrl": "https://static.lolesports.com/teams/1726801573959_539px-T1_2019_full_allmode.png",
    "score": 3
  },
  "winnerSlug": "t1",
  "strategy": "Bo5",
  "startTime": "2026-06-14T06:00:00.000Z",
  "endTime": "2026-06-26T19:35:05.532Z",
  "state": "completed",
  "vodUrl": "https://www.youtube.com/watch?v=0UG_SZpo750",
  "gameCount": 5,
  "coverage": {
    "schedule_metadata": true,
    "live_row": false,
    "numeric_live_state": false,
    "webhook_event": false,
    "coverage_level": "metadata_only",
    "expected_live_state": false,
    "expected_webhooks": false,
    "precheck_endpoint": "/api/v1/lol/matches/lol-match-115548128963037587/coverage",
    "message": "Stored schedule or post-game data exists, but this is not an active numeric live-state feed."
  },
  "coverage_details_endpoint": "/api/v1/lol/matches/lol-match-115548128963037587/coverage"
}
```

### 字段

| 字段 | 说明 |
|---|---|
| `matchId` | Cito 完整 id |
| `esportsApiId` | Riot 原始 id |
| `tournamentId` | 赛事 id |
| `blockName` | 阶段名(如 `"Knockouts"`、`"Week 9"`) |
| `round` | 轮次,Bo 阶段常为 null |
| `team1` / `team2` | `{slug, name, shortName, logoUrl, score}` |
| `winnerSlug` | 胜者 slug |
| `strategy` | `"Bo3"` / `"Bo5"` |
| `startTime` / `endTime` | 开始/结束时间 |
| `state` | `"unstarted"` / `"inProgress"` / `"completed"` |
| `vodUrl` | VOD 链接 |
| `gameCount` | 实际局数(Bo5 完成时常为 5) |
| `coverage` | 实时数据覆盖状态(详见 [06-live.md](./06-live.md)) |
| `coverage_details_endpoint` | `/matches/{id}/coverage` 的预检端点 |

---

## `GET /lol/matches/{id}/games`

该比赛包含的所有对局。**包装 F:`{ value: [...], Count }`**。

```bash
curl "https://api.citoapi.com/api/v1/lol/matches/lol-match-115548128963037587/games" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

### 实测响应(部分)

```json
{
  "value": [
    {
      "gameId": "lol-game-115548128963037588",
      "esportsApiId": "115548128963037588",
      "matchId": "lol-match-115548128963037587",
      "gameNumber": 1,
      "blueTeam": {
        "slug": "t1", "name": "T1", "shortName": "T1", "logoUrl": "...",
        "kills": 10, "gold": 56400,
        "towers": 1, "dragons": 1, "barons": 0,
        "heralds": null, "inhibitors": null, "bans": null
      },
      "redTeam": {
        "slug": "gen", "name": "Gen.G Esports", "shortName": "GEN", "logoUrl": "...",
        "kills": 30, "gold": 69700,
        "towers": 11, "dragons": 4, "barons": 1,
        "heralds": null, "inhibitors": null, "bans": null
      },
      "winnerSlug": "gen",
      "winningSide": "red",
      "duration": 1875,
      "patch": "16.11",
      "lastUpdated": "2026-06-28T02:08:13.053Z",
      "firstObjectives": {
        "firstBlood": "red",
        "firstTower": "red",
        "firstDragon": "red",
        "firstBaron": "red",
        "firstHerald": "red"
      }
    }
  ],
  "Count": 5
}
```

### 字段

每条 game:

| 字段 | 说明 |
|---|---|
| `gameId` / `esportsApiId` / `matchId` / `gameNumber` | id 三元组 + 局号 |
| `blueTeam` / `redTeam` | 双方队伍 + 各自 `{kills, gold, towers, dragons, barons, heralds, inhibitors, bans}` |
| `winnerSlug` | 胜者 slug |
| `winningSide` | `"blue"` / `"red"` |
| `duration` | int,秒 |
| `patch` | 比赛版本(如 `"16.11"`) |
| `lastUpdated` | 上次更新时间 |
| `firstObjectives` | 首资源归属方:`{firstBlood, firstTower, firstDragon, firstBaron, firstHerald}` 各自为 `"blue"` / `"red"` |

> ⚠️ 当前 games 列表里的 `kills/gold/towers/dragons/barons` 是**赛后最终值**;`heralds/inhibitors/bans` 实测大多为 `null`,可能在 live 阶段填充。

---

## `GET /lol/games/{gameId}`

单个对局详情。**裸对象**(包装 B)。

```bash
curl "https://api.citoapi.com/api/v1/lol/games/lol-game-115548128963037588" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

字段结构与 `/matches/{id}/games` 数组里的单条 game 基本一致(matchId / blueTeam / redTeam / winnerSlug / winningSide / duration / patch / firstObjectives / lastUpdated 等)。`{gameId}` 也兼容 `lol-game-<numeric>` 和裸数字两种。

---

## `GET /lol/games/{gameId}/stats`

对局每位选手详细数据。**包装 F:`{ value: [...], meta }`**。

```bash
curl "https://api.citoapi.com/api/v1/lol/games/lol-game-115548128963037570/stats" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

### 实测响应(部分)

```json
{
  "value": [
    {
      "id": "3645d905-bbfb-4baf-9b2a-d4fe48b66556",
      "playerName": "KT Bdd",
      "imageUrl": "...",
      "player": {
        "lolPlayerId": "27796c82-2b9c-4291-a967-fc94245ae4d6",
        "currentIgn": "Bdd",
        "realName": "Bo seong Gwak",
        "imageUrl": "..."
      },
      "teamSlug": "dk",
      "teamName": "DK Challengers",
      "teamLogoUrl": "...",
      "team": {
        "slug": "dwg-kia-challengers",
        "name": "DK Challengers",
        "shortName": "DK",
        "logoUrl": "..."
      },
      "side": "blue",
      "role": "Mid",
      "championId": 112,
      "championName": "Viktor",
      "champion": "Viktor",
      "position": "Mid",
      "kills": 0, "deaths": 0, "assists": 0,
      "kda": 0,
      "killParticipation": null,
      "cs": 0, "csPerMin": null,
      "gold": 0, "goldPerMin": null, "goldShare": null,
      "damageDealt": null, "damage": null, "damageTaken": null,
      "damagePerMin": null, "damageShare": null,
      "visionScore": null,
      "wardsPlaced": null, "wardsKilled": null, "wardsDestroyed": null,
      "firstBlood": false,
      "items": null,
      "primaryRune": null, "secondaryRune": null,
      "summonerSpell1": null, "summonerSpell2": null,
      "source": "riot_live_feed",
      "statsStatus": "metadata_only",
      "finalStatsAvailable": false,
      "gd15": null, "goldDiffAt15": null,
      "csd15": null, "csDiffAt15": null,
      "xpd15": null, "xpDiffAt15": null,
      "soloKills": null, "solo_kills": null,
      "campsStolen": null,
      "monsterKillsEnemyJungle": null,
      "jungleProximity": null,
      "advancedMetrics": {
        "gd15": null, "csd15": null, "xpd15": null,
        "soloKills": null, "campsStolen": null
      },
      "advancedMetricCoverage": {
        "hasLaningAt15": false,
        "hasSoloKills": false,
        "hasCampsStolen": false
      },
      "derivedStatsStatus": {
        "source": "stored rows with controller-derived fallbacks",
        "durationSeconds": null,
        "explanations": {
          "kda": "KDA is zero because kills plus assists are zero, or the source row explicitly stored zero.",
          "csPerMin": "csPerMin could not be calculated because game duration is missing.",
          "goldPerMin": "goldPerMin could not be calculated because game duration is missing.",
          "damagePerMin": "damagePerMin could not be calculated because game duration is missing."
        }
      }
    }
  ],
  "meta": {
    "source": "Cito stored game player stats",
    "lastCheckedAt": "2026-06-29T02:02:36.511Z",
    "freshness": "stored",
    "lastUpdated": "2026-06-14T16:56:27.804Z",
    "durationSeconds": null,
    "derivedStats": "csPerMin, goldPerMin, damagePerMin, and kda are calculated when source fields and duration are available; otherwise null with explanation."
  }
}
```

### 字段

**`value[]` 每位选手一行**:

| 字段 | 说明 |
|---|---|
| `id` | UUID,该选手在本局的记录 id |
| `playerName` | 当时显示名 |
| `imageUrl` | 选手头像 |
| `player` | 当前档案快照(`lolPlayerId`, `currentIgn`, `realName`, `imageUrl`) |
| `teamSlug` / `teamName` / `teamLogoUrl` / `team` | 队伍短 slug + 显示名 + logo + 完整 `{slug, name, shortName, logoUrl}` |
| `side` | `"blue"` / `"red"` |
| `role` / `position` | 实测值相同(`"Top"` / `"Jungle"` / `"Mid"` / `"ADC"` / `"Support"`) |
| `championId` / `championName` / `champion` | 英雄 id + 名字,实测 `champion` 与 `championName` 相同 |
| `kills` / `deaths` / `assists` / `kda` | KDA 三件套 + KDA |
| `killParticipation` / `cs` / `csPerMin` / `gold` / `goldPerMin` / `goldShare` | 资源数据 |
| `damageDealt` / `damage` / `damageTaken` / `damagePerMin` / `damageShare` | 伤害数据(`damage` 与 `damageDealt` 等价) |
| `visionScore` / `wardsPlaced` / `wardsKilled` / `wardsDestroyed` | 视野数据 |
| `firstBlood` | bool |
| `items[]` / `primaryRune` / `secondaryRune` / `summonerSpell1` / `summonerSpell2` | 出装 / 符文 / 召唤师技能。实测常为 `null`(需要 live 阶段或 Riot 详细数据才有) |
| `source` | 数据来源,实测 `"riot_live_feed"` |
| `statsStatus` | `"metadata_only"` / `"complete"` 等。空数据时为 `"metadata_only"` |
| `finalStatsAvailable` | bool,最终统计是否齐全 |
| `gd15` / `goldDiffAt15` | 15 分钟金币差 |
| `csd15` / `csDiffAt15` | 15 分钟补刀差 |
| `xpd15` / `xpDiffAt15` | 15 分钟经验差 |
| `soloKills` / `solo_kills` | 单杀数(两个等价字段) |
| `campsStolen` | 偷野数(打野位) |
| `monsterKillsEnemyJungle` | 反野数 |
| `jungleProximity` | 打野邻近度 |
| `advancedMetrics` | 同名字段的简化结构 |
| `advancedMetricCoverage` | 是否有这些高级数据 |
| `derivedStatsStatus` | 派生数据来源 + 解释(`explanations` 字段解释每个 null) |

**`meta`**:

| 字段 | 说明 |
|---|---|
| `source` | `"Cito stored game player stats"` |
| `lastCheckedAt` | 服务端校验时间 |
| `freshness` | `"stored"` / `"live"` |
| `lastUpdated` | 数据源更新时间 |
| `durationSeconds` | 游戏时长(实测常为 null) |
| `derivedStats` | 派生字段说明文字 |

### 别名

| 方法 | 路径 |
|---|---|
| GET | `/lol/games/{gameId}/player-stats`(`/stats` 的别名) |

---

## `GET /lol/games/{gameId}/postgame`

赛后综合包(经济图 + 时间线 + 镀层 + 视野 + 打野分配)。**包装 F-ish**(`{ gameId, source, coverageLevel, availableSections, missingSections, dataQuality, goldGraph, timeline, plates, ..., lastUpdated }`)。

```bash
curl "https://api.citoapi.com/api/v1/lol/games/lol-game-115548128963037570/postgame" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

### 实测响应(部分)

```json
{
  "gameId": "lol-game-115548128963037570",
  "source": "cito_postgame_enrichment",
  "coverageLevel": "partial",
  "availableSections": ["goldGraph"],
  "missingSections": ["timeline", "plates", "vision", "jungleShare", "distributions"],
  "dataQuality": {
    "fullPostgameAvailable": false,
    "goldGraphAvailable": true,
    "timelineAvailable": false,
    "platesAvailable": false,
    "visionAvailable": false,
    "jungleShareAvailable": false,
    "distributionsAvailable": false,
    "allZeroGoldGraphSuppressed": false
  },
  "goldGraph": [
    { "timestamp": 53000, "blueGold": 2500, "redGold": 2500, "goldDiff": 0 },
    { "timestamp": 71000, "blueGold": 2700, "redGold": 2600, "goldDiff": 100 },
    { "timestamp": 1270000, "blueGold": 34800, "redGold": 44900, "goldDiff": -10100 }
  ],
  "timeline": [],
  "plates": null,
  "goldDistribution": null,
  "damageDistribution": null,
  "vision": null,
  "jungleShare": null,
  "rawAdvancedStats": null,
  "lastUpdated": "2026-06-14T16:56:27.804Z"
}
```

### 字段

| 字段 | 说明 |
|---|---|
| `gameId` | 对局 id |
| `source` | `"cito_postgame_enrichment"` |
| `coverageLevel` | `"full"` / `"partial"` |
| `availableSections[]` | 本场已可用的板块名 |
| `missingSections[]` | 本场缺失的板块名 |
| `dataQuality.*` | 各板块是否可用的细粒度 bool |
| `goldGraph[]` | 经济图采样点:`{timestamp(ms), blueGold, redGold, goldDiff}` |
| `timeline[]` | 事件时间线(实测本场为空数组) |
| `plates` / `goldDistribution` / `damageDistribution` / `vision` / `jungleShare` / `rawAdvancedStats` | 各板块数据(未生成时为 null) |
| `lastUpdated` | 数据源时间 |

> ⚠️ 即使 games/stats 字段齐全,postgame 包也**未必**齐全——很多板块(`timeline` / `plates` / `distributions` / `vision` / `jungleShare`)需要 Cito 额外的赛后处理流水线。客户端必须先看 `availableSections` 和 `dataQuality` 再用。

---

## `GET /lol/games/{gameId}/plates`

镀层 / 虚空虫 / 分路塔皮。**包装 G:** `{ gameId, source, section, data, lastUpdated }`。

```bash
curl "https://api.citoapi.com/api/v1/lol/games/lol-game-115548128963037570/plates" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

### 实测响应(本场数据未生成)

```json
{
  "gameId": "lol-game-115548128963037570",
  "source": "cito_postgame_enrichment",
  "section": "plates",
  "data": null,
  "lastUpdated": "2026-06-14T16:56:27.804Z"
}
```

`data` 数据生成时按官方说明应含:`voidgrubs`(虚空虫)、`towerPlates`(塔皮)、`lanePlates`(分路塔皮)。

---

## `GET /lol/games/{gameId}/distributions`

金币 / 伤害按位置分布。**包装 G**。

```bash
curl "https://api.citoapi.com/api/v1/lol/games/lol-game-115548128963037570/distributions" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

### 实测响应

```json
{
  "gameId": "lol-game-115548128963037570",
  "source": "cito_postgame_enrichment",
  "section": "distributions",
  "data": {
    "gold": null,
    "damage": null
  },
  "lastUpdated": "2026-06-14T16:56:27.804Z"
}
```

`data.gold` / `data.damage` 在数据齐全时按 Top/Jungle/Mid/ADC/Support 给出占比(0–1)。

---

## `GET /lol/games/{gameId}/vision`

队伍视野统计。**包装 G**。

```json
{
  "gameId": "...",
  "source": "cito_postgame_enrichment",
  "section": "vision",
  "data": null,
  "lastUpdated": "..."
}
```

---

## `GET /lol/games/{gameId}/jungle-share`

打野资源按位置占比。**包装 G**。

```json
{
  "gameId": "...",
  "source": "cito_postgame_enrichment",
  "section": "jungle-share",
  "data": null,
  "lastUpdated": "..."
}
```

---

## 隐藏端点(`ai/endpoints.json` 有,官方 docs 未列)

| 方法 | 路径 | 说明 |
|---|---|---|
| GET | `/lol/matches` | match 列表 |
| GET | `/lol/matches/past` | 已完成 match |
| GET | `/lol/matches/{id}/stats` | match 聚合统计 |
| GET | `/lol/matches/{id}/player-stats` | match 所有 game 的选手 stats |
| GET | `/lol/matches/{id}/timeline` | match 事件时间线 |
| GET | `/lol/games/{id}/timeline` | 单 game 时间线 |
| GET | `/lol/games/{id}/builds` | 出装数据 |
| GET | `/lol/games/{id}/gold` | 经济图(单端点,等同 postgame.goldGraph) |
| GET | `/lol/games/{id}/objectives` | 单 game 客观元素(双方) |

---

## Quick reference

| 用途 | 推荐端点 |
|---|---|
| 比赛元信息(双方 / 比分 / 状态) | `/lol/matches/{id}` |
| 比赛所有 game 列表 | `/lol/matches/{id}/games` |
| 单 game 元信息 | `/lol/games/{id}` |
| 单 game 选手数据 | `/lol/games/{id}/stats` |
| 单 game 赛后综合包 | `/lol/games/{id}/postgame` |
| 单 game 经济图 | `/lol/games/{id}/gold` |
| 单 game 客观元素 | `/lol/games/{id}/objectives` |
| 镀层 / 塔皮 | `/lol/games/{id}/plates` |
| 金币 / 伤害按位置 | `/lol/games/{id}/distributions` |
| 视野 | `/lol/games/{id}/vision` |
| 打野分配 | `/lol/games/{id}/jungle-share` |
| 时间线 | `/lol/matches/{id}/timeline` 或 `/lol/games/{id}/timeline` |
| 出装 | `/lol/games/{id}/builds` |
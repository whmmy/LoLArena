# 02 — Leagues / Schedule / Standings

联赛元数据 + 赛程 + 积分。覆盖 8 个接口,全部基于实测响应。

---

## `GET /lol/leagues`

获取全部 LoL 联赛列表,带 slug / aliases / endpoints 自描述。

```bash
curl "https://api.citoapi.com/api/v1/lol/leagues" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

### 实测响应(包装类型 C)

```json
{
  "success": true,
  "count": 27,
  "data": [
    {
      "leagueId": "lol-lck",
      "esportsApiId": "98767991310889156",
      "name": "LCK", "slug": "lck", "shortName": "LCK",
      "region": "KOREA", "tier": "1",
      "imageUrl": "http://static.lolesports.com/leagues/1703076867943_LCK_1png.png",
      "priority": 1, "isActive": true,
      "createdAt": "2026-01-14T04:55:53.120Z",
      "lastUpdated": "2026-06-29T01:55:00.951Z",
      "_count": { "tournaments": 24, "teams": 10 },
      "aliases": ["lol-lck", "lol_lck", "lck", "98767991310889156"],
      "endpoints": {
        "detail": "/api/v1/lol/leagues/lol-lck",
        "schedule": "/api/v1/lol/leagues/lol-lck/schedule",
        "scheduleBySlug": "/api/v1/lol/leagues/lck/schedule",
        "standings": "/api/v1/lol/leagues/lol-lck/standings",
        "teams": "/api/v1/lol/leagues/lol-lck/teams"
      }
    },
    { "leagueId": "lol-lpl", ... },
    { "leagueId": "lol-worlds", ... },
    { "leagueId": "lol-msi", ... }
    /* 共 27 条,涵盖 LCK/LPL/LEC/LCS/LTA/LFL/PCS/VCS/LCP/CBLOL 等 */
  ]
}
```

### `data[]` 字段

| 字段 | 类型 | 说明 |
|---|---|---|
| `leagueId` | string | 标准 id,`lol-<slug>` 格式,如 `lol-lck`、`lol-worlds` |
| `esportsApiId` | string | Riot LoL Esports API 原始 id |
| `name` | string | 显示名 |
| `slug` | string | 短 slug,如 `lck`、`lpl` |
| `shortName` | string | 缩写,如 `LCK`、`LPL` |
| `region` | string | Riot 区域枚举,值如 `KOREA` / `CHINA` / `EMEA` / `NORTH_AMERICA` / `BRAZIL` / `LATIN_AMERICA` / `ASIA_PACIFIC` / `INTERNATIONAL` / `JAPAN` / `VIETNAM` / `HONG_KONG, MACAU, TAIWAN` / `LATIN_AMERICA NORTH` / `LATIN_AMERICA SOUTH` / `AMERICAS` |
| `tier` | string | `"1"`(顶级联赛)/ `"2"`(次级)/ `"3"`(地区)/ `"international"`(国际赛) |
| `imageUrl` | string | 联赛 logo |
| `priority` | int | 显示优先级,数字越小越靠前(本次实测全部为 1) |
| `isActive` | bool | 是否活跃 |
| `createdAt` / `lastUpdated` | ISO datetime | 同步时间 |
| `_count.tournaments` | int | 该联赛下赛事数 |
| `_count.teams` | int | 该联赛下队伍数 |
| `aliases[]` | string[] | 全部等价 slug(可用于 search 兼容) |
| `endpoints.detail/schedule/scheduleBySlug/standings/teams` | string | 自描述的子端点路径,直接可用 |

### 使用建议

- 客户端缓存这一份即可,**不需要硬编码 slug**
- `endpoints.scheduleBySlug` 给的就是 `/lol/leagues/lck/schedule` 这种**短 slug 形式**,可以直接拼

---

## `GET /lol/schedule/upcoming`

即将开始的 LoL 比赛列表。

```bash
curl "https://api.citoapi.com/api/v1/lol/schedule/upcoming" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

### 实测响应(包装类型 C + meta)

```json
{
  "success": true,
  "status": "ok",
  "count": 2,
  "data": [
    {
      "matchId": "lol-match-115846993721104369",
      "tournamentId": "lol-tournament-115570934354631452",
      "tournamentEsportsApiId": "115570934354631452",
      "tournamentName": "2026",
      "leagueId": "lol-msi",
      "leagueEsportsApiId": "98767991325878492",
      "leagueName": "MSI",
      "leagueSlug": "msi",
      "blockName": "Play In Knockouts",
      "round": null,
      "team1": {
        "slug": "dcg", "name": "Relove Deep Cross Gaming",
        "code": "DCG",
        "logoUrl": "http://...",
        "score": 0
      },
      "team2": { "slug": "team-liquid", "name": "Team Liquid Alienware", "code": "TLAW", "logoUrl": "...", "score": 0 },
      "winnerSlug": null,
      "strategy": "Bo5",
      "startTime": "2026-06-29T03:00:00.000Z",
      "endTime": null,
      "state": "unstarted",
      "source": "Riot LoL Esports API",
      "officialEventId": "115846993721104369",
      "officialTournamentId": "115570934354631452",
      "metadataWarning": null,
      "metadataWarnings": []
    }
  ],
  "meta": {
    "source": "Cito schedule monitor + Riot LoL Esports API verification",
    "lastCheckedAt": "2026-06-29T02:00:57.800Z",
    "dataCompleteness": "complete",
    "warnings": []
  }
}
```

### `data[]` 字段

| 字段 | 类型 | 说明 |
|---|---|---|
| `matchId` | string | **Cito 完整 id**,`lol-match-<numeric>` 格式 |
| `tournamentId` / `tournamentEsportsApiId` | string | 赛事 id(两种形式) |
| `tournamentName` | string | 赛事名 |
| `leagueId` / `leagueEsportsApiId` / `leagueName` / `leagueSlug` | string | 联赛 4 元组 |
| `blockName` | string | 阶段名,如 `Play In Knockouts` / `Week 9` |
| `round` | string/null | 轮次,Bo 阶段常见为 null |
| `team1` / `team2` | object | `{slug, name, code, logoUrl, score}` |
| `winnerSlug` | string/null | 胜者 slug,未开始为 null |
| `strategy` | string | `"Bo3"` / `"Bo5"` |
| `startTime` / `endTime` | ISO datetime | 开始/结束时间,未结束 endTime 为 null |
| `state` | string | `"unstarted"` / `"inProgress"` / `"completed"` |
| `source` | string | 数据源,实测为 `"Riot LoL Esports API"` |
| `officialEventId` / `officialTournamentId` | string | Riot 原始 id,可用于对账 |
| `metadataWarning` / `metadataWarnings[]` | string | 元数据警告(如某字段未对齐),通常为 null/[] |

### `meta`

| 字段 | 说明 |
|---|---|
| `source` | 内部来源描述 |
| `lastCheckedAt` | 实时同步时间 |
| `dataCompleteness` | `"complete"` / `"partial"` 等 |
| `warnings[]` | 全局警告 |

---

## `GET /lol/schedule/today`

今日赛程。**结构跟 upcoming 略有不同**——`teams` 用数组 + `strategy` 用对象 + 带 `outcome/record`。

```bash
curl "https://api.citoapi.com/api/v1/lol/schedule/today" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

### 实测响应(包装类型 C)

```json
{
  "success": true,
  "count": 22,
  "data": [
    {
      "startTime": "2026-06-14T06:00:00.000Z",
      "state": "completed",
      "type": "match",
      "blockName": "Week 9",
      "matchId": "115548128963037547",
      "teams": [
        { "name": "Dplus KIA", "code": "DK",
          "imageUrl": "...",
          "score": 2, "outcome": "win",
          "record": { "wins": 11, "losses": 7 } },
        { "name": "KIWOOM DRX", "code": "KRX",
          "imageUrl": "...",
          "score": 1, "outcome": "loss",
          "record": { "wins": 5, "losses": 13 } }
      ],
      "strategy": { "type": "bestOf", "count": 3 },
      "leagueId": "lol-lck", "leagueName": "LCK"
    }
  ],
  "pages": {
    "older": "b2xkZXI6OjExNTU0ODEyODk2Mjg0MDU5OQ==",
    "newer": null
  }
}
```

### 字段差异(对比 upcoming)

| 字段 | today | upcoming |
|---|---|---|
| 队伍结构 | `teams: [team1, team2]` 数组,带 `outcome` 和 `record` | `team1` / `team2` 两个对象 |
| `strategy` | `{type: "bestOf", count: 3}` 对象 | `"Bo5"` 字符串 |
| `matchId` | 纯数字 id(如 `"115548128963037547"`) | `"lol-match-115548128963037587"`(带前缀) |
| 是否有 `tournamentId` / `tournamentName` | ❌ | ✅ |
| `state` | `"completed"` 常见 | `"unstarted"` 常见 |
| 分页 | `pages.older/newer`(base64 游标) | 无 |

> ⚠️ 同一场比赛在不同接口可能给不同形态的 matchId(裸数字 vs 带 `lol-match-` 前缀)。`matches/{id}` 端点对两种都接受。

### `pages` 翻页

- `pages.older` / `pages.newer`:base64 编码的游标
- 用法:`GET /lol/schedule/today?cursor=<base64>`

---

## `GET /lol/leagues/lol-lck/schedule`(及 `GET /lol/leagues/lck/schedule`)

LCK 联赛专属赛程。两种 slug 都通。

```bash
curl "https://api.citoapi.com/api/v1/lol/leagues/lol-lck/schedule" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

响应结构与 `/lol/schedule/today` 一致(包装类型 C,带 `teams` 数组 + `pages` 游标)。

### 别名

| 完整 slug | 短 slug |
|---|---|
| `lol-lck` | `lck` |
| `lol-lpl` | `lpl` |

其他联赛无短别名,**只能用 `lol-<slug>` 形式**。

### 通用方法

任何联赛都行,只要你拿到 `leagueId`:

```bash
curl "https://api.citoapi.com/api/v1/lol/leagues/{leagueId}/schedule" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

---

## `GET /lol/leagues/{leagueId}/standings`

联赛积分榜。

```bash
curl "https://api.citoapi.com/api/v1/lol/leagues/lol-lck/standings" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

### 实测响应(包装类型 D:`{ success, data: {...} }`)

```json
{
  "success": true,
  "data": {
    "leagueId": "lol-lck",
    "leagueName": "LCK",
    "tournamentId": "lol-lck_split_3_2026",
    "stage": "Groups",
    "rankings": [
      { "rank": 1, "orgSlug": "t1", "teamName": "T1",
        "wins": 0, "losses": 0, "winRate": 0,
        "gameWins": 0, "gameLosses": 0, "gameWinRate": 0 },
      { "rank": 1, "orgSlug": "gen", "teamName": "Gen.G Esports", ... },
      { "rank": 1, "orgSlug": "hle", "teamName": "Hanwha Life Esports", ... }
      /* 10 支 LCK 队 */
    ]
  }
}
```

### `data` 字段

| 字段 | 说明 |
|---|---|
| `leagueId` / `leagueName` | 联赛标识 |
| `tournamentId` | 当前积分对应的赛事 |
| `stage` | 当前阶段,实测 `"Groups"`(分组赛) |
| `rankings[]` | 排名数组 |

### `rankings[]` 字段

| 字段 | 说明 |
|---|---|
| `rank` | 当前排名 |
| `orgSlug` | 队伍短 slug(如 `t1`、`gen`) |
| `teamName` | 队伍显示名 |
| `wins` / `losses` | 系列赛胜负(Bo 维度) |
| `winRate` | 系列胜率 |
| `gameWins` / `gameLosses` | 单场胜负(Game 维度) |
| `gameWinRate` | 单场胜率 |

> ⚠️ 新赛季初(如本次 Split 3 开赛)所有数字都是 0,`rank` 也都并列 1。客户端必须能处理 `rank` 重复的情况。

---

## 其他 schedule 相关端点(实测但本次未取数据)

| 方法 | 路径 | 说明 |
|---|---|---|
| GET | `/lol/schedule` | 全量赛程(带过滤器) |
| GET | `/lol/schedule/week` | 本周赛程 |
| GET | `/lol/schedule/past` | 已结束比赛(别名) |
| GET | `/lol/schedule/results` | 跨联赛最近结果 |
| GET | `/lol/matches` | match 列表(支持过滤器) |
| GET | `/lol/matches/past` | 已完成 match |

未实测,响应结构推断同 today/upcoming 之一,具体包装以官方为准。

---

## Quick reference

| 用途 | 推荐端点 |
|---|---|
| 列出所有支持的联赛 | `GET /lol/leagues` |
| 找 LCK/LPL 赛程 | `GET /lol/leagues/lck/schedule` |
| 今日比赛 | `GET /lol/schedule/today` |
| 未来比赛 | `GET /lol/schedule/upcoming` |
| 联赛积分榜 | `GET /lol/leagues/{leagueId}/standings` |
| 联赛队伍列表 | `GET /lol/leagues/{leagueId}/teams`(未实测) |
| 联赛历史 | `GET /lol/leagues/{leagueId}/history`(未实测) |
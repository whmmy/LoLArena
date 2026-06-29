# 04 — Teams

队伍元数据、阵容、阵容历史、目标控制、对阵、收益、成就。

---

## `GET /lol/teams`

全部职业队伍列表。未实测响应,基于 `ai/endpoints.json` 路径存在。

```bash
curl "https://api.citoapi.com/api/v1/lol/teams" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

可选 query(推断):
- `limit` / `page` 分页
- `league` 过滤联赛
- `region` 过滤区域

> ⚠️ 未实测,响应包装和字段命名请以官方为准。

---

## `GET /lol/teams/{slug}`(未实测)

单个队伍详情。

---

## `GET /lol/teams/{slug}/roster/history`

队伍阵容历史(含日期区间)。

```bash
curl "https://api.citoapi.com/api/v1/lol/teams/t1/roster/history" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

### 实测响应(摘要)

T1 阵容历史返回了一长串 roster entries,**每条 ≈ 选手在该队的一段任期**,字段与 `players/{id}/teams` 类似:

```json
[
  {
    "lolPlayerId": "...",
    "playerName": "Faker",
    "realName": "...",
    "role": "MID",
    "joinDate": "...",
    "leaveDate": null,
    "isStarter": true,
    "logoUrl": "..."
  }
]
```

> ⚠️ 完整字段未逐字段确认,但响应是**裸数组**(包装 A),每条是一个任期。`leaveDate=null` 表示仍在队。

---

## `GET /lol/teams/{slug}/roster`(未实测)

**当前**阵容(不带历史)。

```bash
curl "https://api.citoapi.com/api/v1/lol/teams/{slug}/roster" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

---

## `GET /lol/teams/{slug}/objectives`

队伍近期客观元素控制率(每场 vs 对手)。

```bash
curl "https://api.citoapi.com/api/v1/lol/teams/t1/objectives?last=20&league=lck" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

### 实测响应(部分,T1)

```json
[
  {
    "matchId": "lol-match-115548128962971887",
    "gameId": "lol-game-115548128962971889",
    "gameNumber": 2,
    "startTime": "2026-05-08T08:00:00.000Z",
    "league": "lck",
    "tournamentName": "Summer 2024",
    "opponentSlug": "kwangdong-freecs",
    "side": "blue",
    "result": "win",
    "objectives": {
      "kills": 18,
      "opponentKills": 4,
      "gold": 54947,
      "opponentGold": 40385,
      "towers": 9,
      "opponentTowers": 0,
      "dragons": 4,
      "opponentDragons": 0,
      "barons": 0,
      "opponentBarons": 0,
      "firstBlood": true,
      "firstTower": true,
      "firstDragon": true,
      "firstBaron": null
    }
  }
]
```

### 字段

**每条记录**:

| 字段 | 说明 |
|---|---|
| `matchId` / `gameId` / `gameNumber` | 比赛与对局标识 |
| `startTime` | 开赛时间 |
| `league` / `tournamentName` | 联赛(slug 小写)/ 赛事 |
| `opponentSlug` | 对手短 slug |
| `side` | 队伍这边打的方(`"blue"` / `"red"`) |
| `result` | `"win"` / `"loss"` |

**`objectives`**(T1 这一边的数据 + 对手的数据并列):

| 字段 | 说明 |
|---|---|
| `kills` / `opponentKills` | 双方击杀总数 |
| `gold` / `opponentGold` | 双方最终金币 |
| `towers` / `opponentTowers` | 推塔数 |
| `dragons` / `opponentDragons` | 小龙数 |
| `barons` / `opponentBarons` | 大龙数 |
| `firstBlood` / `firstTower` / `firstDragon` / `firstBaron` | bool/null,T1 是否抢到对应首资源 |

> ⚠️ 此接口的 `objectives` 是**game 级**(单场),不是 series 级。

### Query

- `last` — 最近 N 场
- `league` — 过滤联赛

---

## `GET /lol/teams/{slug}/h2h/{opponentSlug}`(未实测)

两队历史对阵。

```bash
curl "https://api.citoapi.com/api/v1/lol/teams/{slug}/h2h/{opponentSlug}" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

---

## 隐藏端点(`ai/endpoints.json` 有,官方 docs 未列)

| 方法 | 路径 | 说明 |
|---|---|---|
| GET | `/lol/teams` | 全部队伍列表 |
| GET | `/lol/teams/{slug}` | 单个队伍详情 |
| GET | `/lol/teams/{slug}/roster` | 当前阵容 |
| GET | `/lol/teams/{slug}/matches` | 队伍比赛历史 |
| GET | `/lol/teams/{slug}/stats` | 队伍聚合统计 |
| GET | `/lol/teams/{slug}/earnings` | 队伍组织级奖金 |
| GET | `/lol/teams/{slug}/achievements` | 队伍成就 / 头衔 |
| GET | `/lol/teams/{slug}/champions` | 队伍英雄池 + 选用率 |
| GET | `/lol/teams/{slug}/ranking-history` | 排名历史 |
| GET | `/lol/teams/{slug}/h2h/{opponent}` | 两队对阵 |
| GET | `/lol/teams/{slug}/h2h/{opponent}` | 同上 |
| GET | `/lol/leagues/{leagueId}/teams` | 联赛下队伍 |

### Rankings(GPR — Global Power Rankings)

官方 Esports GPR 榜。

```bash
curl "https://api.citoapi.com/api/v1/lol/rankings?league=lck&season=2026&includeHistory=true" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

| 方法 | 路径 | 说明 |
|---|---|---|
| GET | `/lol/rankings` | GPR 总榜(按 team) |
| GET | `/lol/rankings/teams` | `/lol/rankings` 的别名 |

可选 query:
- `league` — `lck` / `lpl` / `lec` / `lcs` / 任意 leagueId
- `season` — `2026` 等
- `includeHistory` — bool,是否含历史变动

### Team Trend(Analytics)

| 方法 | 路径 |
|---|---|
| GET | `/lol/analytics/teams/{slug}/trend` |
| GET | `/lol/analytics/teams/{slug}/win-conditions` |

### Role Analytics

| 方法 | 路径 | 说明 |
|---|---|---|
| GET | `/lol/analytics/roles/{role}` | 单一位置分析(`mid` / `top` / `jungle` 等) |

---

## Quick reference

| 用途 | 推荐端点 |
|---|---|
| 当前队伍列表 | `/lol/teams` |
| 当前阵容 | `/lol/teams/{slug}/roster` |
| 阵容历史 | `/lol/teams/{slug}/roster/history` |
| 队伍客观元素控制 | `/lol/teams/{slug}/objectives?last=20` |
| 与对手历史对阵 | `/lol/teams/{slug}/h2h/{opponent}` |
| 队伍奖金 | `/lol/teams/{slug}/earnings` |
| 队伍成就 | `/lol/teams/{slug}/achievements` |
| 队伍英雄池 | `/lol/teams/{slug}/champions` |
| 队伍战绩走势 | `/lol/analytics/teams/{slug}/trend` |
| GPR 排名 | `/lol/rankings?league=lck` |
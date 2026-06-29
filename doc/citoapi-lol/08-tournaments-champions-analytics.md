# 08 — Tournaments / Champions / Analytics / Rankings(隐藏端点)

> ⚠️ **本文档是"目录型"章节**——这些端点在官方 markdown 文档里**完全没有列出**,但在 `ai/endpoints.json`(官方 AI agent 端点清单)和 Postman Collection 里全部存在。Cito 显然是为 AI coding agent 准备的(详见每个端点对应路径的说明)。
>
> **为节省 API 配额,这些端点的响应结构未实测验证**。本文档仅列路径、官方描述和官方 params。
>
> 客户端拿到字段时如有疑问,建议直接用真实 key 调一次验证。

---

## Tournaments(赛事)

```bash
# 全部赛事
curl "https://api.citoapi.com/api/v1/lol/tournaments" \
  -H "x-api-key: YOUR_CITO_API_KEY"

# 单个赛事
curl "https://api.citoapi.com/api/v1/lol/tournaments/{tournamentId}" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

| 方法 | 路径 | 描述 |
|---|---|---|
| GET | `/lol/tournaments` | 全部赛事列表 |
| GET | `/lol/tournaments/live` | 直播赛事比赛(`/lol/live` 的别名) |
| GET | `/lol/tournaments/{tournamentId}` | 单个赛事详情 |
| GET | `/lol/tournaments/{tournamentId}/standings` | 赛事积分 |
| GET | `/lol/tournaments/{tournamentId}/bracket` | 赛事对阵图 |
| GET | `/lol/tournaments/{tournamentId}/matches` | 赛事所有比赛 |
| GET | `/lol/tournaments/{tournamentId}/results` | 赛事最终结果 |
| GET | `/lol/tournaments/{tournamentId}/stats` | 赛事统计 |
| GET | `/lol/tournaments/{tournamentId}/mvp` | 赛事 MVP |

`tournamentId` 实测占位符,如 `worlds-2025` / `lol-lck_split_3_2026`。

---

## Champions(英雄)

```bash
curl "https://api.citoapi.com/api/v1/lol/champions/stats" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

| 方法 | 路径 | 描述 | 关键 query |
|---|---|---|---|
| GET | `/lol/champions/stats` | 全英雄聚合统计 | — |
| GET | `/lol/champions/meta` | 当前版本 tier list | — |
| GET | `/lol/champions/patches/{patch}` | 指定 patch 的英雄改动 | `patch` 必填,如 `14.10` |
| GET | `/lol/champions/{championId}/stats` | 单英雄详细统计 | — |
| GET | `/lol/champions/{championId}/players` | 单英雄的代表选手 | — |
| GET | `/lol/champions/{championId}/matchups` | 单英雄的对位数据 | — |

`championId` 用 Riot champion key,如 `azir` / `leesin` / `ahri`。

---

## Analytics(分析)

```bash
curl "https://api.citoapi.com/api/v1/lol/analytics/players/faker/trend" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

| 方法 | 路径 | 描述 | 关键 query |
|---|---|---|---|
| GET | `/lol/analytics/players/{playerId}/trend` | 选手长期趋势 | — |
| GET | `/lol/analytics/teams/{slug}/trend` | 队伍长期趋势 | — |
| GET | `/lol/analytics/roles/{role}` | 单位置分析 | `role` 必填,如 `mid` / `top` / `jungle` / `adc` / `support` |
| GET | `/lol/analytics/regions/compare` | 跨区域对比 | — |
| GET | `/lol/analytics/drafts/{matchId}` | 单比赛 BP 分析 | `matchId` 必填 |
| GET | `/lol/analytics/teams/{slug}/win-conditions` | 队伍胜负条件 | — |

---

## Rankings(GPR — Global Power Rankings)

官方 Esports GPR 榜,Riot 联合评分。

```bash
curl "https://api.citoapi.com/api/v1/lol/rankings?league=lck&season=2026&includeHistory=true" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

| 方法 | 路径 | 描述 | 关键 query |
|---|---|---|---|
| GET | `/lol/rankings` | GPR 总榜(按 team) | `league` / `season` / `includeHistory` |
| GET | `/lol/rankings/teams` | `/lol/rankings` 的别名 | 同上 |

GPR 字段(官方描述,未实测):`league` / `GPR score` / `Elo` / `rank change` / `match records`。

---

## Leaderboards(全局排行)

```bash
curl "https://api.citoapi.com/api/v1/lol/leaderboards/earnings" \
  -H "x-api-key: YOUR_CITO_API_KEY"
```

| 方法 | 路径 | 维度 |
|---|---|---|
| GET | `/lol/leaderboards/earnings` | 奖金榜 |
| GET | `/lol/leaderboards/kda` | KDA 榜 |
| GET | `/lol/leaderboards/cs` | 每分钟补刀榜 |
| GET | `/lol/leaderboards/winrate` | 胜率榜 |
| GET | `/lol/leaderboards/vision` | 视野榜 |
| GET | `/lol/leaderboards/firstblood` | 一血率榜 |
| GET | `/lol/leaderboards/damage` | 每分钟伤害榜 |
| GET | `/lol/leaderboards/championships` | 冠军数榜 |

---

## Search / Discovery(Postman Collection 出现)

| 方法 | 路径 | 描述 | 关键 query |
|---|---|---|---|
| GET | `/lol/search` | 统一搜索(选手/队/赛事) | `q`(必填) |
| GET | `/lol/autocomplete` | 搜索自动补全 | `q`(必填) |
| GET | `/lol/trending` | 热门选手/队/话题 | — |

---

## Matches / Games 扩展

| 方法 | 路径 | 描述 |
|---|---|---|
| GET | `/lol/matches` | 全部比赛列表(带过滤) |
| GET | `/lol/matches/past` | 已完成比赛 |
| GET | `/lol/matches/{id}/stats` | match 聚合统计 |
| GET | `/lol/matches/{id}/player-stats` | match 所有 game 的选手 stats |
| GET | `/lol/matches/{id}/timeline` | match 事件时间线 |
| GET | `/lol/games/{id}/timeline` | 单 game 事件时间线 |
| GET | `/lol/games/{id}/builds` | 出装数据 |
| GET | `/lol/games/{id}/gold` | 经济图(等价于 postgame.goldGraph 单端点) |
| GET | `/lol/games/{id}/objectives` | 单 game 双方客观元素 |

---

## Schedule 扩展

| 方法 | 路径 | 描述 |
|---|---|---|
| GET | `/lol/schedule` | 全量赛程(带过滤) |
| GET | `/lol/schedule/week` | 本周赛程 |
| GET | `/lol/schedule/past` | 已结束比赛别名 |
| GET | `/lol/schedule/results` | 跨联赛最近结果 |

---

## Live 扩展

| 方法 | 路径 | 描述 |
|---|---|---|
| GET | `/lol/live/{matchId}` | 单个直播比赛 |
| GET | `/lol/live/{gameId}/stats` | 单局直播统计 |
| GET | `/lol/live/{gameId}/window` | 直播数据窗口 |
| GET | `/lol/live/{gameId}/details` | 直播详情 |
| GET | `/lol/live/{gameId}/events` | 直播事件流 |

---

## Teams 扩展

| 方法 | 路径 | 描述 |
|---|---|---|
| GET | `/lol/teams` | 全部队伍列表 |
| GET | `/lol/teams/{slug}` | 单个队伍详情 |
| GET | `/lol/teams/{slug}/roster` | 当前阵容 |
| GET | `/lol/teams/{slug}/matches` | 队伍比赛历史 |
| GET | `/lol/teams/{slug}/stats` | 队伍聚合统计 |
| GET | `/lol/teams/{slug}/earnings` | 队伍组织级奖金 |
| GET | `/lol/teams/{slug}/achievements` | 队伍成就 |
| GET | `/lol/teams/{slug}/champions` | 队伍英雄池 |
| GET | `/lol/teams/{slug}/ranking-history` | 排名历史 |
| GET | `/lol/teams/{slug}/h2h/{opponent}` | 两队对阵 |

---

## Players 扩展

| 方法 | 路径 | 描述 |
|---|---|---|
| GET | `/lol/players` | 全部选手列表 |
| GET | `/lol/players/search` | 选手搜索(autocomplete) |
| GET | `/lol/players/{playerId}` | 单个选手档案 |
| GET | `/lol/players/{playerId}/matches` | 选手参赛历史 |
| GET | `/lol/players/{playerId}/champions` | 选手英雄池(汇总) |
| GET | `/lol/players/{playerId}/achievements` | 选手成就 |
| GET | `/lol/players/{playerId}/stats/career` | 选手生涯统计 |
| GET | `/lol/players/{playerId}/compare/{otherPlayerId}` | 两选手对比 |
| GET | `/lol/players/{playerId}/peers` | 相似选手 |

---

## Leagues 扩展

| 方法 | 路径 | 描述 |
|---|---|---|
| GET | `/lol/leagues/{leagueId}` | 单联赛详情 |
| GET | `/lol/leagues/{leagueId}/history` | 联赛历史 |
| GET | `/lol/leagues/{leagueId}/teams` | 联赛下队伍 |

---

## Quick reference(常用隐藏端点)

| 用途 | 推荐端点 |
|---|---|
| 全英雄 meta tier | `/lol/champions/meta` |
| 单英雄的代表选手 | `/lol/champions/{championId}/players` |
| 选手长期趋势 | `/lol/analytics/players/{id}/trend` |
| BP 分析 | `/lol/analytics/drafts/{matchId}` |
| GPR 排名 | `/lol/rankings?league=lck&season=2026` |
| 奖金 / KDA / 视野榜 | `/lol/leaderboards/{dimension}` |
| 搜索选手 | `/lol/players/search?q=faker` |
| 出装 | `/lol/games/{id}/builds` |
| 时间线 | `/lol/matches/{id}/timeline` |
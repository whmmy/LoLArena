# Cito API — League of Legends 文档

Cito API(https://citoapi.com)是面向 LoL / Fortnite / COD / Apex / Dota2 / UFC 等电竞项目的 REST + Webhook 数据服务。本目录是 **LoL 接口**的完整中文参考。

数据来源:
- 官方 docs(https://citoapi.com/docs/api/league-of-legends/)— 调用方式 + 官方示例
- 官方隐藏的 AI agent 端点清单 `https://citoapi.com/ai/endpoints.json` — **官方 markdown 没列出的全部端点**(tournaments / champions / analytics / rankings / leaderboards / h2h / roster 等)
- 官方 `https://citoapi.com/llms.txt` 和 Postman Collection — 端点索引冗余确认
- **实测响应**:本文档作者用 CitoAPI key 对 25+ 个核心接口做了真实调用,所有响应结构均来自实测,**不靠推断**

---

## 文档目录

| 文件 | 内容 |
|---|---|
| [01-overview.md](./01-overview.md) | Base URL、认证、响应包装(实测)、分页、错误码、限流、区域端点 |
| [02-leagues-schedule-standings.md](./02-leagues-schedule-standings.md) | 联赛列表/赛程/积分(leagues / schedule/* / standings) |
| [03-players.md](./03-players.md) | 选手档案/收益/组织履历/状态/英雄池(stats / earnings / form / champion-pool / teams) |
| [04-teams.md](./04-teams.md) | 队伍列表/阵容/阵容历史/目标控制/对阵(teams + roster + objectives + h2h + 隐藏端点) |
| [05-matches-games.md](./05-matches-games.md) | 比赛/对局/赛后数据(matches / games / postgame / plates / distributions / vision / jungle-share) |
| [06-live.md](./06-live.md) | 实时比赛 + 覆盖预检(/live + /coverage + visual-state) |
| [07-transfers.md](./07-transfers.md) | 转会(/transfers + 按选手 + 按队伍 + transferId) |
| [08-tournaments-champions-analytics.md](./08-tournaments-champions-analytics.md) | 隐藏端点(tournaments / champions / analytics / rankings / leaderboards) |
| [09-webhooks.md](./09-webhooks.md) | 11 个 LoL webhook 事件、HMAC-SHA256 签名、payload、过滤、重试 |

---

## 端点总数:100+ LoL 接口

### 官方 docs 列出(35 个)

覆盖联赛 / 选手 / 队伍 / 转会 / 直播 / 比赛 / 赛程 / webhook。

### 官方 docs **没**列出,但 `ai/endpoints.json` 有(`★` 标记)

- **Tournaments(8 个)**:list / live / detail / standings / bracket / matches / results / stats / mvp
- **Champions(6 个)**:stats / meta / patches/{patch} / {id}/stats / {id}/players / {id}/matchups
- **Analytics(5 个)**:players/{id}/trend / teams/{slug}/trend / roles/{role} / regions/compare / drafts/{matchId} / teams/{slug}/win-conditions
- **Rankings(GPR,2 个)**:/lol/rankings、/lol/rankings/teams(支持 league/season/includeHistory)
- **Leaderboards(8 个)**:earnings / kda / cs / winrate / vision / firstblood / damage / championships
- **Team h2h**:`/lol/teams/{slug}/h2h/{opponent}`
- **Player compare/peers**:`/lol/players/{id}/compare/{otherId}`、`/lol/players/{id}/peers`
- **Search 集成**:`/lol/search`、`/lol/autocomplete`、`/lol/trending`(在 Postman collection 里)
- **Match/Games 扩展**:`/lol/matches/{id}/stats`、`/lol/matches/{id}/player-stats`、`/lol/matches/{id}/timeline`、`/lol/games/{id}/timeline`、`/lol/games/{id}/builds`、`/lol/games/{id}/gold`、`/lol/games/{id}/objectives`
- **Live 扩展**:`/lol/live/{matchId}`、`/lol/live/{gameId}/stats`、`/lol/live/{gameId}/window`、`/lol/live/{gameId}/details`、`/lol/live/{gameId}/events`
- **Schedule 扩展**:`/lol/schedule`、`/lol/schedule/week`、`/lol/schedule/past`、`/lol/schedule/results`、`/lol/matches`、`/lol/matches/past`

> 隐藏端点的响应结构**本文档未实测验证**(为节省 API 配额)。详见 [08-tournaments-champions-analytics.md](./08-tournaments-champions-analytics.md),里面只列路径、官方描述和官方 `ai/endpoints.json` 提供的 params,**不写响应字段**。

---

## 字段可信度标记约定

- ✅ **已实测** — 文档作者用真实 API key 打过,有完整 JSON 示例
- 🟡 **官方 markdown 文档示例** — 仅 2 个接口官方给了示例(`players/{id}/earnings`、`players/{id}/teams`)
- ⚪ **官方端点清单** — `ai/endpoints.json` 列出端点存在,但响应结构未实测(节省 API 配额)

> **重要发现**:官方 markdown 文档示例与实际响应有出入(下文会指出)。本文档**以实测为准**。

---

## 计划限制(quick ref)

- 免费:500 req/月,10 req/min,burst 20
- One Game Starter(LoL live 起点):10k–250k req/月,30 req/min,burst 60
- Basic:50k/月,30 req/min,burst 60
- Pro:250k/月,100 req/min,burst 200
- Business:2M/月,500 req/min,burst 1000

详细限流见 [01-overview.md](./01-overview.md)。
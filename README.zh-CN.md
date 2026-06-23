# 🎮 LoLArena — 大模型英雄联盟比赛预测竞技场

用真实英雄联盟比赛评测多个大模型的预测能力。每场比赛在开赛前 **3 小时**自动触发预测；每小局在 **BP 完成后**手动刷新触发。赛后按真实结果打分，模型间排行比拼谁更准。

> 🌏 English version: [README.md](README.md)

## 公平性核心

> **所有模型拿相同的「数据合集」+ 相同的「web_search 工具」，各自决定怎么搜索。**

- 系统统一从 **PandaScore**（免费端点）取数 → 聚合成同一份 `context_pack` 注入给每个模型
- 每个模型都挂上 **同一个 `web_search` 工具**（后端统一为 **智谱 web_search API**）—— 模型自己决定查什么、查几次
- 模型间工具能力完全相同，差异纯粹来自「分析判断力」
- 每个模型每场只产一份预测，独立落盘，独立打分

## 两种预测

| 类型 | 触发 | 预测内容 |
|---|---|---|
| **系列赛** | 开赛前 3h 自动（APScheduler） | 胜负概率（如 TES 55% - G2 45%）、比分（3-1）、总局数、让胜/让负、关键选手 |
| **单局** | BP 完成后网页手动「刷新 BP」 | 单局胜负 + 概率、时长（分钟）、双方击杀数、总击杀 |

每类分析都要求模型覆盖 **四维**：
1️⃣ 战队基本面 · 2️⃣ 对位分析（上中野下辅）· 3️⃣ 版本适应度与打法 · 4️⃣ 历史交手与心理

## 目录结构

```
lolArena/
├─ configs/        models.yaml(模型注册) · policy.yaml(策略) · tasks.yaml(评分) · leagues.yaml(关注联赛)
├─ prompts/        system.md · task_match.md · task_game.md
├─ schemas/        match_prediction / game_prediction (JSON Schema)
├─ src/
│   ├─ adapters/   pandascore.py(LoL API) · websearch.py(统一搜索工具)
│   ├─ pipeline/   collect · prompt_build · validate · orchestrator · scheduler
│   ├─ runners/    base(agent loop) · openai_compat · anthropic · google
│   ├─ graders/    grade_match · grade_game · metrics/
│   ├─ server/     main.py(FastAPI)
│   └─ leaderboard/build_site.py
├─ data/           matches/<slug>/  ·  games/<slug>/g<pos>/
└─ docs/site/      index.html + data.json (排行榜单页应用)
```

## 快速开始

```bash
# 1. 装依赖
pip install -r requirements.txt

# 2. 配置密钥
cp .env.example .env
#   必填：PANDASCORE_API_KEY、ZHIPU_WEBSEARCH_API_KEY
#   按需：各模型 *_API_KEY（在 configs/models.yaml 里启用/注释）

# 3. 启动服务（FastAPI + 调度器一起跑）
python -m src serve
#   打开 http://127.0.0.1:8000
```

## 命令行（手动操作）

```bash
python -m src scan                       # 扫描近期待预测比赛
python -m src collect <match_id>         # 构建某场比赛的 context_pack
python -m src predict <match_id>         # 对一场比赛跑全部模型（系列赛预测）
python -m src refresh-bp <match_id> <pos>     # 拉取某局 BP
python -m src predict-game <match_id> <pos>   # BP 完成后跑全部模型（单局预测）
python -m src grade <match_id>           # 赛后对系列赛预测打分
python -m src grade-game <match_id> <pos>     # 赛后对单局预测打分
python -m src build-site                 # 重新生成 data.json
python -m src scheduler                  # 仅启动调度器（不开 Web）
```

## 工作流

```
开赛前 3h ── scheduler.predict_tick ──► collect context_pack ──► 并行跑所有模型
                                                                        (agent loop: 模型自搜 web_search)
        单局 BP 公开后 ──► 网页「刷新 BP」(/api/refresh-bp)
                            └─ BP 完整 ──► 并行跑所有模型 (task_game)

赛后 ── scheduler.grade_tick ──► 拉真实结果 ──► grade_match / grade_game ──► build_site
```

## 评分（configs/tasks.yaml）

**系列赛**（四层加权综合，0-100）：
- T1_result 0.45（胜负概率 brier + 比分相似度 + 总局数 MAE）
- T2_matchup 0.25（关键选手召回 + 摇摆因素完整性）
- T3_reasoning 0.15（四维推理完整性）
- T4_meta 0.15（版本信号引用）

**单局**：
- G1_result 0.50（胜负 brier）· G2_duration 0.25（时长 MAE）· G3_kills 0.25（双方击杀 MAE + 总击杀 sMAPE）

## 配置

- **增删模型**：只改 `configs/models.yaml`（每条带 `provider`，决定走哪个 runner）。所有模型自动挂上同一个 `web_search`。
- **关注联赛**：`configs/leagues.yaml`（slug 来自 PandaScore `/lol/leagues`）。
- **预测提前量**：环境变量 `LOLA_PREDICT_LEAD_H`（默认 3）。
- **代理/中转**：设 `LOLA_MODEL_PROXY=https://your-proxy/v1` 即让所有模型走同一中转。

## 数据来源与限制

- LoL 数据：**PandaScore 免费版**。免费端点覆盖赛程、队伍、选手名单、最近战绩、英雄/装备静态数据、赛后比分与单局 BP(picks)。Historical 付费版的 KDA/金币/补刀/伤害等深度统计**不在免费版**——这部分由模型的 `web_search` 自行补足。
- 搜索：**智谱 web_search API**（`search_pro` 引擎，带意图识别）。

## 添加新模型

1. 在 `configs/models.yaml` 加一条带正确 `provider` 的条目。
2. 提供对应的 `*_API_KEY` 环境变量（或通过 `LOLA_MODEL_PROXY` 中转）。
3. 如果 API 走 OpenAI chat-completions 并支持 function-calling，`provider` 设为 `openai_compat` —— `web_search` 自动挂上。
4. 搞定，不需要改代码。

## 参考实现

方法论、提示语结构、缓存数据格式、编排模式参考了 [`WorldCupArena`](../WorldCupArena)（足球版）。本项目相对它的三点关键差异：
1. 放弃 ICS，赛程直接来自 PandaScore `/lol/matches/upcoming`
2. **所有模型统一挂同一个 web_search 工具**（参考项目分 S1 注入 / S2 自搜两套）
3. 新增单局预测（BP 后手动触发 + FastAPI 接口）

## 开发备忘

- `prompts/*.md` 每次预测都重读，无需重启。
- 必填的 `reasoning.*` 子字段名由 **schema**（`schemas/*.schema.json` 的 `minLength`）和 **grader**（`graders/grade_match.py` 的 `reasoning_completeness`）双重约束，改动时要保持同步。
- 暂无正式测试套件 —— 验证手段：`python -c "..."` 跑 `validate` 和 `graders`、`python -m src --help` 看 CLI 连通、`python -m src build-site` 验证站点构建（空数据也能跑通）。
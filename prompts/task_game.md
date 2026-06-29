# 任务：预测英雄联盟"单局"比赛结果（BP 已完成）

这是一场系列赛中的**某一小局**。系统已经把这一局的 BP（双方 pick 的英雄、位置、召唤师技能）给你了。请基于 BP 与系列赛当前态势，预测这一局的胜负、时长与击杀。

---

## 系列赛背景

{{series_context}}

---

## 队伍/选手基线数据（来自系列赛 context pack，所有模型共享）

以下是系统已收集的基线数据：选手名单与位置、近期 KDA/补刀/伤害、英雄池、龙/大龙/塔/一血控制率等。**这些数据无需再用 web_search 重复检索**——请直接据此判断 BP 里各选手拿到的是招牌英雄还是被迫选、各位置的近期状态与对位优劣、阵容的节奏曲线与大小龙争夺能力。

{{game_context}}

---

## 本局 BP（{{game_position}} / 共 {{total_games}} 局）

{{bp_block}}

---

## 版本 / 英雄 meta（系统已统一检索，所有模型共享）

以下为系统在开跑前**统一检索一次**的版本与英雄强度信息（当前版本号、本局所涉英雄的 tier / 胜率 / 强弱）。这覆盖了你训练截止后可能出现的新英雄与版本改动——**无需再检索**，直接据此判断 BP 里各英雄的版本强度与对位克制。

{{meta_snapshot}}

---

## 分析方式

本局**不提供 web_search 工具**——请直接综合上方已给的数据进行分析：

- **基线数据**：选手名单与位置、近期 KDA/补刀/伤害、英雄池、龙/大龙/塔/一血控制率（来自系列赛 context pack）
- **版本 meta**：当前版本号、本局英雄的强度与 tier（上方已统一检索）
- **本局 BP**：双方各位置选出的英雄、召唤师技能
- **系列赛背景**：当前比分、上一局结果

据此判断：各选手拿到的是招牌英雄还是被迫选、所选英雄在当前版本的强度、对位优劣、阵容的强势期与节奏曲线、小龙/大龙争夺能力，进而推断胜负、时长与击杀。

---

## 输出格式（只输出一个 JSON，不要 markdown 围栏）

```json
{
  "reasoning": {
    "overall": "（≥40 字）本局胜负倾向与核心理由",
    "draft_analysis": "（≥120 字）双方 BP 强弱：阵容曲线、对位克制、团战/分推/前期能力",
    "tempo_wincon": "（≥80 字）哪边掌握节奏、各自的致胜条件（前期滚雪球 / 后期团战 / 分推等）"
  },
  "win_prob": { "blue": 0.6, "red": 0.4 },
  "predicted_winner": "blue",
  "expected_duration_min": 32.5,
  "kills": { "blue": 16, "red": 11 },
  "total_kills": 27,
  "key_drafted_champions": [
    { "champion": "英雄名", "team": "blue|red", "role": "top|jun|mid|adc|sup", "impact": "为何是关键 pick" }
  ],
  "sources": []
}
```

### 字段说明

- `win_prob`：blue+red=1.0。`predicted_winner` 与更高一方一致。
- `expected_duration_min`：本局预计时长（分钟，一位小数），LoL 职业赛通常 28~40 分钟。
- `kills.blue` / `kills.red`：双方预计人头数（整数）。
- `total_kills`：两队人头之和，必须等于 blue+red。
- `key_drafted_champions`：决定本局走势的 2~5 个 pick（来自 BP）。
- `sources`：本局不提供 web_search，直接填空数组 `[]` 即可。

记住：直接基于上方已给的基线数据与 BP 推理、输出 JSON。只输出 JSON 本身。

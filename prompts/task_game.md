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

## 检索指引（用 web_search 工具，可选）

上面的基线数据已覆盖队伍名单、选手状态、英雄池与控制率，**这些不必再查**。web_search 只需补基线里没有、且随版本快速变化的信息：

- 双方所选英雄在当前版本（{{patch_version}}）的强度梯度、对线/团战定位
- 关键对位的克制关系（如某打野 gank 能力 vs 某上单逃生、某中单推线 vs 某刺客）
- 该版本主流阵容的强势期与节奏

保持精炼，单局分析通常 **1~3 条**检索足够，重点查版本英雄强度与具体对位克制。

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
  "sources": [
    { "query": "你发出的检索词", "accessed_at": "2026-06-23T12:00:00Z" }
  ]
}
```

### 字段说明

- `win_prob`：blue+red=1.0。`predicted_winner` 与更高一方一致。
- `expected_duration_min`：本局预计时长（分钟，一位小数），LoL 职业赛通常 28~40 分钟。
- `kills.blue` / `kills.red`：双方预计人头数（整数）。
- `total_kills`：两队人头之和，必须等于 blue+red。
- `key_drafted_champions`：决定本局走势的 2~5 个 pick（来自 BP）。

记住：先检索、再推理、最后输出 JSON。只输出 JSON 本身。

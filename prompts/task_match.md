# 任务：预测一场英雄联盟系列赛（Bo3 / Bo5）的最终结果

下面是系统为你准备的比赛数据合集。先用 `web_search` 工具检索补充证据，再给出严格 JSON 预测。

---

## 比赛数据合集（context_pack）

{{context_pack}}

---

## 赛前检索指引（用 web_search 工具）

合集里已有队伍名单、最近战绩、英雄池、版本号等基线信息。请你**主动发起检索**补齐以下方向（建议至少 4~6 条查询，覆盖四个分析维度）：

- 两队近期真实状态、连败/连胜、关键选手起伏（fundamentals）
- 五个位置的具体对位强弱、近期交锋中的对线数据（matchups）
- 当前版本（{{patch_version}}）的强势英雄、主流阵容、两队的版本契合度（meta_style）
- 两队历史交手、大赛/世界赛经验、赛程体力与心理（h2h_psych）
- 若有换人、首发变动、教练/BP 风格新闻，务必检索确认

查询示例：`"{{blue_name}} vs {{red_name}} {{league}} {{serie}} prediction"`、`"{{blue_name}} recent form LCK 2026"`、`"LoL patch {{patch_version}} meta tier list"` 等。具体查什么由你判断。

---

## 比分预测必须锚定历史、敢于给横扫（关键）

`series_score` / `series_length` 是本任务最容易失分的字段。**最常见的错误是无论实力差距多大都保守给 `3-1` / `2-1`**，而跨赛区/强弱悬殊局里横扫（`3-0` / `0-3`）非常常见。请按以下方法锚定：

- **横扫锚点**：`team_series_history.{side}.sweep_rate` 是该队近 25 场系列赛里**主动横扫**（`3-0`/`2-0`）的比例；`swept_rate` 是**被横扫**比例。若强队 `sweep_rate` 高（如 ≥0.35）且对手 `swept_rate` 不低，**应优先考虑 `3-0`**，不要默认 `3-1`。
- **系列长度锚点**：`team_series_history.{side}.avg_series_length` 是该队系列赛场均打满几局。两队该值都接近 3 → 倾向 `3-0`；接近 4~5 → 倾向打到 BoX 上限。
- **win_probs 与比分要自洽**：`win_probs` 高的那一方决定了比分里大数给谁；力度越大、越要敢给短比分。参考映射（仅作起点，最终以实力差 + 横扫率修正）：

  | 强队 win_probs | 跨赛区/明显实力差 | 同级别胶着 |
  |---|---|---|
  | ≥ 0.80 | 优先 `3-0`，次选 `3-1` | `3-1` |
  | 0.65~0.80 | `3-1`，横扫率高时可 `3-0` | `3-1` / `3-2` |
  | 0.55~0.65 | `3-2` | `3-2` |

- **判据**：实力档差大（如世界冠军 vs 外卡/新军）、强队近期连胜且横扫率高、BP 储备深 → 敢给 `3-0`。不要因为"留一线"而把所有局都给 `3-1`。

---

## 输出格式（只输出一个 JSON，不要 markdown 围栏）

```json
{
  "reasoning": {
    "overall": "（≥40 字）总体判断：胜负倾向 + 核心理由",
    "fundamentals": "（≥120 字）两队近10场胜率/状态、运营稳定性、关键选手状态与英雄池健康度",
    "matchups": "（≥150 字）上/中/野/下/辅逐位置对位分析，关键对局，团战/边线控制力",
    "meta_style": "（≥100 字）版本主流阵容特征、哪队更契合强势英雄与节奏",
    "h2h_psych": "（≥80 字）历史交手、心理/体力、大赛经验、临场调整"
  },
  "win_probs": {
    "blue": 0.55,
    "red": 0.45
  },
  "predicted_winner": "blue",
  "series_score": "3-1",
  "series_length": 4,
  "favored_side": "blue_strong",
  "key_players": [
    { "player": "选手名", "team": "blue|red", "role": "top|jun|mid|adc|sup", "reason": "为什么是关键先生" }
  ],
  "swing_factors": [
    "影响胜负的具体变量（如：蓝色方前期节奏、某选手英雄池被针对、BP 主动权等）"
  ],
  "meta_style_signals": [
    "本次预测中考虑到的版本/阵容信号（供事后校验）"
  ],
  "sources": [
    { "query": "你发出的检索词", "accessed_at": "2026-06-23T10:00:00Z" }
  ]
}
```

### 字段说明

- `win_probs`：两队胜率，blue+red=1.0（精确到两位小数）。
- `predicted_winner`：`blue` 或 `red`，必须与 `win_probs` 中更高的一方一致。
- `series_score`：最终比分字符串，如 `"3-1"`（蓝-红）。Bo3 用 `"2-1"` 这类，Bo5 用 `"3-2"` 这类。**必须锚定 `team_series_history` 的 sweep_rate / avg_series_length 与两队实力差**；实力悬殊且强队横扫率高时敢于给 `3-0`/`0-3`，不要默认 `3-1`。
- `series_length`：总局数（整数，如 4 或 5）。必须与 `series_score` 的两数之和一致。
- `favored_side`：胜负倾向标签，取值 `blue_strong` / `blue_slight` / `even` / `red_slight` / `red_strong`（"让胜/让负"的力度）。
- `key_players`：你认为将决定比赛走向的 3~6 名选手（可来自两队），每条注明位置与理由。
- `swing_factors`：3~6 条具体的关键变量。
- `meta_style_signals`：1~4 条你在推理中考虑到的版本/阵容信号（用于事后版本契合度校验）。
- `sources`：你本次检索的全部查询记录（每条带访问时间）。

记住：先检索、再推理、最后输出 JSON。**比分要锚定历史横扫率、敢于给短比分**。只输出 JSON 本身。

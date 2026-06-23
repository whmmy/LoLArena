"""Series (match) grader.

Walks configs/tasks.yaml#match, invokes the right metric per task, and rolls
up a weighted composite in [0, 100].
"""

from __future__ import annotations

from typing import Any

from .. import config as cfg
from . import metrics as M


def grade_match(prediction: dict[str, Any], truth: dict[str, Any]) -> dict[str, Any]:
    spec = cfg.tasks_cfg()["match"]
    layer_weights = spec["layer_weights"]
    tasks = spec["tasks"]

    truth_side = truth.get("winner_side")  # "blue" | "red"
    blue_players = truth.get("blue_players", [])   # optional, fed from roster
    red_players = truth.get("red_players", [])

    layers: dict[str, float] = {}
    task_scores: dict[str, dict[str, Any]] = {}

    for t in tasks:
        layer = t["layer"]
        w_in = float(t["weight_in_layer"])
        score = _score_task(t, prediction, truth, truth_side, blue_players + red_players)
        task_scores[t["id"]] = {"score": round(score, 2), "metric": t["metric"]}
        layers[layer] = layers.get(layer, 0.0) + score * w_in

    composite = sum(layers.get(L, 0.0) * w for L, w in layer_weights.items())
    return {
        "tasks": task_scores,
        "layers": {L: round(v, 2) for L, v in layers.items()},
        "composite": round(composite, 2),
    }


def _score_task(task: dict, pred: dict, truth: dict,
                truth_side: str | None, all_players: list[dict]) -> float:
    metric = task["metric"]
    field = task["output_field"]
    try:
        if metric == "brier_binary":
            probs = pred.get(field) or {}
            # win_probs is {blue,red}; the "truth" is which side won
            if not truth_side:
                return 50.0
            return M.brier_binary(probs, truth_side)
        if metric == "scoreline_similarity":
            return M.scoreline_similarity(pred.get(field, ""), truth.get("series_score", ""))
        if metric == "mae":
            return M.mae(pred.get(field, 0), truth.get("series_length", 0))
        if metric == "key_players_recall":
            return M.key_players_recall(pred.get(field, []), all_players)
        if metric == "structural_completeness":
            return M.structural_completeness(pred.get(field), min_items=1, min_str_len=3)
        if metric == "reasoning_completeness":
            req = ["overall", "fundamentals", "matchups", "meta_style", "h2h_psych"]
            mins = {"overall": 40, "fundamentals": 120, "matchups": 150,
                    "meta_style": 100, "h2h_psych": 80}
            return M.reasoning_completeness(pred.get(field), req, mins)
    except Exception as e:  # noqa: BLE001
        return 0.0
    return 0.0

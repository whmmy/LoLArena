"""Single-game grader.

Truth (from orchestrator._truth_for_game):
  {winner_side, length_min, kills:{blue,red}, total_kills, status}
"""

from __future__ import annotations

from typing import Any

from .. import config as cfg
from . import metrics as M


def grade_game(prediction: dict[str, Any], truth: dict[str, Any]) -> dict[str, Any]:
    spec = cfg.tasks_cfg()["game"]
    layer_weights = spec["layer_weights"]
    tasks = spec["tasks"]

    layers: dict[str, float] = {}
    task_scores: dict[str, dict[str, Any]] = {}

    for t in tasks:
        layer = t["layer"]
        w_in = float(t["weight_in_layer"])
        score = _score_task(t, prediction, truth)
        task_scores[t["id"]] = {"score": round(score, 2), "metric": t["metric"]}
        layers[layer] = layers.get(layer, 0.0) + score * w_in

    composite = sum(layers.get(L, 0.0) * w for L, w in layer_weights.items())
    return {
        "tasks": task_scores,
        "layers": {L: round(v, 2) for L, v in layers.items()},
        "composite": round(composite, 2),
    }


def _score_task(task: dict, pred: dict, truth: dict) -> float:
    metric = task["metric"]
    field = task["output_field"]
    truth_side = truth.get("winner_side")
    try:
        if metric == "brier_binary":
            probs = pred.get(field) or {}
            if not truth_side:
                return 50.0
            return M.brier_binary(probs, truth_side)
        if metric == "mae":
            if field == "expected_duration_min":
                return M.mae(pred.get(field, 0), truth.get("length_min", 0))
            # kills.blue / kills.red -> nested
            if field == "kills.blue":
                return M.mae((pred.get("kills") or {}).get("blue", 0),
                             (truth.get("kills") or {}).get("blue", 0))
            if field == "kills.red":
                return M.mae((pred.get("kills") or {}).get("red", 0),
                             (truth.get("kills") or {}).get("red", 0))
        if metric == "smape":
            return M.smape(pred.get(field, 0), truth.get("total_kills", 0))
    except Exception:  # noqa: BLE001
        return 0.0
    return 0.0

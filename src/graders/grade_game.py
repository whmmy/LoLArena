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
    # per-layer sum of weights actually applied (tasks can return None to opt
    # out — e.g. duration when truth.length_min is missing/0 — so the layer is
    # renormalized over the tasks that DID score, rather than dragging in a
    # garbage 0 from a missing truth value).
    layer_w_used: dict[str, float] = {}
    task_scores: dict[str, dict[str, Any]] = {}

    for t in tasks:
        layer = t["layer"]
        w_in = float(t["weight_in_layer"])
        score = _score_task(t, prediction, truth)
        if score is None:
            # truth unavailable for this task — record as skipped, don't score it
            task_scores[t["id"]] = {"score": None, "metric": t["metric"],
                                    "skipped": "truth unavailable"}
            continue
        task_scores[t["id"]] = {"score": round(score, 2), "metric": t["metric"]}
        layers[layer] = layers.get(layer, 0.0) + score * w_in
        layer_w_used[layer] = layer_w_used.get(layer, 0.0) + w_in

    # renormalize each layer to its configured weight over the tasks that scored
    weighted_layers: dict[str, float] = {}
    for layer, raw in layers.items():
        used = layer_w_used.get(layer, 0.0)
        weighted_layers[layer] = (raw / used) if used > 0 else 0.0

    composite = sum(weighted_layers.get(L, 0.0) * w
                    for L, w in layer_weights.items()) if layer_weights else 0.0
    return {
        "tasks": task_scores,
        "layers": {L: round(v, 2) for L, v in weighted_layers.items()},
        "composite": round(composite, 2),
    }


def _score_task(task: dict, pred: dict, truth: dict) -> float:
    metric = task["metric"]
    field = task["output_field"]
    truth_side = truth.get("winner_side")
    # optional per-task MAE scale (the |error| that scores 0). Default in metrics
    # is max(2, |truth|), which is far too tight for game duration (~2min -> 0),
    # so tasks.yaml can override it (e.g. duration: 8) to stop rewarding risk-free
    # convergence to the league mean.
    scale = task.get("scale")
    mae_kwargs = {"scale": float(scale)} if scale is not None else {}
    try:
        if metric == "brier_binary":
            probs = pred.get(field) or {}
            if not truth_side:
                return 50.0
            return M.brier_binary(probs, truth_side)
        if metric == "mae":
            if field == "expected_duration_min":
                # truth.length_min is 0.0 when Cito hasn't backfilled it (every
                # game in the current dataset). Scoring against 0 would either
                # hand out near-0 to every model or reward convergence to 0,
                # polluting the leaderboard. Skip instead — the layer renormalizes
                # over the kills tasks that DO have truth.
                truth_len = truth.get("length_min")
                if not truth_len:
                    return None
                return M.mae(pred.get(field, 0), truth_len, **mae_kwargs)
            # kills.blue / kills.red -> nested
            if field == "kills.blue":
                return M.mae((pred.get("kills") or {}).get("blue", 0),
                             (truth.get("kills") or {}).get("blue", 0), **mae_kwargs)
            if field == "kills.red":
                return M.mae((pred.get("kills") or {}).get("red", 0),
                             (truth.get("kills") or {}).get("red", 0), **mae_kwargs)
        if metric == "smape":
            return M.smape(pred.get(field, 0), truth.get("total_kills", 0))
    except Exception:  # noqa: BLE001
        return 0.0
    return 0.0

"""Prediction validation: JSON Schema + semantic checks.

Returns a list of human-readable error strings. Empty list == valid.
The runner uses this as its validate_fn; on failure it asks the model to repair.
"""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any

import jsonschema

from .. import config as cfg

SCHEMAS = cfg.SCHEMAS
_TOL = 0.02  # probability sum tolerance (a bit looser than schema, repaired after)


@lru_cache(maxsize=4)
def _schema(name: str) -> dict:
    return json.loads((SCHEMAS / f"{name}.schema.json").read_text(encoding="utf-8"))


def validate_match(pred: dict[str, Any]) -> list[str]:
    return _validate(pred, "match_prediction")


def validate_game(pred: dict[str, Any]) -> list[str]:
    return _validate(pred, "game_prediction")


def _validate(pred: dict[str, Any], schema_name: str) -> list[str]:
    errors: list[str] = []

    # 1) JSON Schema (structure, required fields, types, enum, minLength)
    try:
        jsonschema.validate(pred, _schema(schema_name))
    except jsonschema.ValidationError as e:
        path = ".".join(str(p) for p in e.absolute_path) or "<root>"
        errors.append(f"Schema [{path}]: {e.message}")
        return errors  # structural failure -> skip semantic checks

    # 2) Semantic checks common to both
    errors.extend(_check_probs(pred))

    # 3) Scope-specific
    if schema_name == "match_prediction":
        errors.extend(_check_series_score(pred))
    else:
        errors.extend(_check_total_kills(pred))

    return errors


def _check_probs(pred: dict[str, Any]) -> list[str]:
    """win_probs/win_prob must sum to ~1 and predicted_winner must pick the max."""
    probs = pred.get("win_probs") or pred.get("win_prob")
    if not isinstance(probs, dict):
        return []
    b = probs.get("blue"); r = probs.get("red")
    out = []
    if isinstance(b, (int, float)) and isinstance(r, (int, float)):
        if abs((b + r) - 1.0) > _TOL:
            out.append(f"win_probs must sum to 1.0 (got {b + r:.3f}).")
    winner = pred.get("predicted_winner")
    if winner and isinstance(b, (int, float)) and isinstance(r, (int, float)):
        higher = "blue" if b >= r else "red"
        if winner != higher:
            out.append(
                f"predicted_winner='{winner}' but the higher probability is "
                f"'{higher}' (blue={b}, red={r}). They must agree."
            )
    return out


def _check_series_score(pred: dict[str, Any]) -> list[str]:
    """series_length must equal the sum of series_score's two numbers."""
    score = pred.get("series_score", "")
    length = pred.get("series_length")
    parts = str(score).split("-")
    if len(parts) != 2:
        return [f"series_score must look like '3-1' (got '{score}')."]
    try:
        a, b = int(parts[0]), int(parts[1])
    except ValueError:
        return [f"series_score numbers must be integers (got '{score}')."]
    if isinstance(length, int) and length != (a + b):
        return [
            f"series_length={length} but series_score '{score}' sums to {a + b}. "
            f"They must be consistent."
        ]
    return []


def _check_total_kills(pred: dict[str, Any]) -> list[str]:
    """total_kills must equal kills.blue + kills.red."""
    kills = pred.get("kills") or {}
    b = kills.get("blue"); r = kills.get("red"); total = pred.get("total_kills")
    if isinstance(b, int) and isinstance(r, int) and isinstance(total, int):
        if total != b + r:
            return [f"total_kills={total} but kills.blue+kills.red={b + r}. They must match."]
    return []

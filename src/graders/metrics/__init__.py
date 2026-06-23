"""Domain-agnostic scoring metrics.

All functions return a score in [0, 100] where 100 = perfect, 0 = worst.
This keeps every task comparable and the composite a simple weighted sum.

Conventions:
  - probabilities: dict like {"blue": p, "red": 1-p}
  - truth side:    "blue" | "red"
  - scalars:       numbers (ints/floats)
"""

from __future__ import annotations

from typing import Any, Iterable

import numpy as np


def _clamp01(x: float) -> float:
    return max(0.0, min(1.0, float(x)))


# ----------------------------- probability -----------------------------

def brier_binary(probs: dict[str, float], truth_side: str) -> float:
    """Brier score for a binary outcome, converted to a 0-100 goodness score.

    brier = (p_true - 1)^2 + (p_false - 0)^2  in [0, 2]
    goodness = 100 * (1 - brier/2)            in [0, 100]
    """
    p_true = _clamp01(probs.get(truth_side, 0.5))
    brier = (p_true - 1.0) ** 2 + (1.0 - p_true) ** 2
    return 100.0 * (1.0 - brier / 2.0)


def brier_multiclass(probs: dict[str, float], truth_label: str) -> float:
    """Multiclass Brier -> 0-100 goodness. probs need not be normalized."""
    items = list(probs.items())
    if not items:
        return 0.0
    total = sum(max(0.0, float(p)) for _, p in items) or 1.0
    brier = 0.0
    for label, p in items:
        target = 1.0 if label == truth_label else 0.0
        brier += (float(p) / total - target) ** 2
    n = len(items)
    worst = 2.0 * (1.0 - 1.0 / n)  # max brier for uniform-wrong
    return 100.0 * max(0.0, 1.0 - brier / worst) if worst else 0.0


# ----------------------------- scalar error -----------------------------

def mae(pred: float, truth: float, *, scale: float | None = None) -> float:
    """Mean absolute error -> goodness. scale = |error| that scores 0.

    Default scale = max(2, |truth|) so a 2-unit miss already near-fails.
    """
    err = abs(float(pred) - float(truth))
    s = scale if scale is not None else max(2.0, abs(float(truth)))
    return 100.0 * max(0.0, 1.0 - err / s)


def smape(pred: float, truth: float) -> float:
    """Symmetric MAPE -> 0-100 goodness. Good for kills (relative scale)."""
    p, t = float(pred), float(truth)
    denom = (abs(p) + abs(t)) / 2.0
    if denom == 0:
        return 100.0 if p == t else 0.0
    smape_val = abs(p - t) / denom  # in [0, 1] (can exceed for wild preds)
    return 100.0 * max(0.0, 1.0 - min(1.0, smape_val))


# ----------------------------- set / ranking -----------------------------

def f1_set(pred: Iterable, truth: Iterable) -> float:
    """F1 over two sets of strings -> 0-100."""
    P, T = {str(x) for x in (pred or [])}, {str(x) for x in (truth or [])}
    if not P and not T:
        return 100.0
    tp = len(P & T)
    prec = tp / len(P) if P else 0.0
    rec = tp / len(T) if T else 0.0
    if prec + rec == 0:
        return 0.0
    return 100.0 * 2 * prec * rec / (prec + rec)


def jaccard(pred: Iterable, truth: Iterable) -> float:
    P, T = {str(x) for x in (pred or [])}, {str(x) for x in (truth or [])}
    if not P and not T:
        return 100.0
    union = P | T
    return 100.0 * len(P & T) / len(union) if union else 0.0


def exact_match(pred: Any, truth: Any) -> float:
    return 100.0 if pred == truth else 0.0


# ----------------------------- scoreline -----------------------------

def scoreline_similarity(pred_score: str, truth_score: str) -> float:
    """Compare '3-1' vs '3-1'. Reward exact + partial credit for closeness."""
    def parse(s):
        parts = str(s or "").split("-")
        try:
            return int(parts[0]), int(parts[1])
        except (ValueError, IndexError):
            return None
    p, t = parse(pred_score), parse(truth_score)
    if p is None or t is None:
        return 0.0
    if p == t:
        return 100.0
    # partial: winner side right + total games right each worth ~half
    pw, tw = (p[0] > p[1]), (t[0] > t[1])
    side_ok = 30.0 if pw == tw else 0.0
    len_ok = 30.0 if (p[0] + p[1]) == (t[0] + t[1]) else 0.0
    return side_ok + len_ok


# ----------------------------- structural (soft) -----------------------------

def structural_completeness(obj: Any, *, min_items: int = 1, min_str_len: int = 3) -> float:
    """Binary-ish reward: is the field present and non-trivial? 0 or 100."""
    if obj is None:
        return 0.0
    if isinstance(obj, (list, tuple, set)):
        real = [x for x in obj if (len(str(x)) >= min_str_len if isinstance(x, str) else True)]
        return 100.0 if len(real) >= min_items else 0.0
    if isinstance(obj, str):
        return 100.0 if len(obj.strip()) >= min_str_len else 0.0
    if isinstance(obj, dict):
        return 100.0 if len(obj) >= min_items else 0.0
    return 100.0


def reasoning_completeness(reasoning: dict | None,
                           required_keys: list[str],
                           min_chars: dict[str, int] | None = None) -> float:
    """Average fill across required reasoning sub-fields. 0-100."""
    reasoning = reasoning or {}
    min_chars = min_chars or {}
    scores = []
    for k in required_keys:
        val = reasoning.get(k)
        need = min_chars.get(k, 0)
        if isinstance(val, str) and len(val) >= need:
            scores.append(100.0)
        elif isinstance(val, str):
            scores.append(100.0 * len(val) / need) if need else scores.append(100.0)
        else:
            scores.append(0.0)
    return float(np.mean(scores)) if scores else 0.0


def key_players_recall(pred_players: list[dict], truth_players: list[dict]) -> float:
    """What fraction of the *actual* standout players did the model flag?

    Without paid stats we approximate 'standout' as the 10 starting players
    from the roster. A model that names real starters scores; invented names don't.
    So this is really 'did the model name real, relevant players'.
    """
    pred_names = {_norm(p.get("player")) for p in (pred_players or []) if p.get("player")}
    truth_names = {_norm(p.get("name") or p.get("player")) for p in (truth_players or [])}
    truth_names.discard("")
    if not truth_names:
        return 100.0 if pred_names else 0.0
    return 100.0 * len(pred_names & truth_names) / len(truth_names)


def _norm(name: str) -> str:
    return " ".join(str(name or "").casefold().replace(".", " ").split())

"""Build data.json for the single-page leaderboard site.

Aggregates all predictions/results under data/ into one payload:
  {
    "models": [{id, display_name}],
    "leaderboard":  [{model_id, composite, n_matches, layers}],
    "game_leaderboard": [{model_id, composite, n_games}],
    "incoming":    [{slug, league, blue, red, begin_at, kickoff_utc, status}],
    "predicted_upcoming": [{... incoming match with local predictions ...}],
    "history":     [{slug, league, blue, red, truth, model_results: {model: composite}}],
    "game_history":[{match_slug, position, blue, red, truth, model_results}]
  }

Writes to docs/site/data.json (the site fetches it at runtime).
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any

from .. import config as cfg


def build() -> dict[str, Any]:
    models = _models_meta()
    history = _history()
    game_history = _game_history()
    payload = {
        "models": models,
        "leaderboard": _series_leaderboard(),
        "game_leaderboard": _game_leaderboard(),
        "incoming": _incoming(history),
        "predicted_upcoming": _predicted_upcoming(history),
        "history": history,
        "game_history": game_history,
    }
    out = cfg.SITE_DIR / "data.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[build_site] wrote {out} "
          f"(series:{len(payload['history'])} games:{len(payload['game_history'])})")
    return payload


def _models_meta() -> list[dict[str, str]]:
    return [{"id": m["id"], "display_name": m.get("display_name", m["id"])}
            for m in cfg.models_cfg()]


def _model_name_map() -> dict[str, str]:
    return {m["id"]: m.get("display_name", m["id"]) for m in cfg.models_cfg()}


# ----------------------------- series -----------------------------

def _series_leaderboard() -> list[dict]:
    totals: dict[str, dict] = defaultdict(lambda: {"composite": 0.0, "n": 0,
                                                    "layers": defaultdict(float)})
    for mdir in _match_dirs():
        for rf in (mdir / "results").glob("*.json"):
            res = _read(rf)
            mid = rf.stem
            comp = res.get("composite", 0.0)
            totals[mid]["composite"] += comp
            totals[mid]["n"] += 1
            for L, v in (res.get("layers") or {}).items():
                totals[mid]["layers"][L] += v
    rows = []
    for mid, t in totals.items():
        n = t["n"] or 1
        rows.append({
            "model_id": mid,
            "display_name": _model_name_map().get(mid, mid),
            "composite": round(t["composite"] / n, 2),
            "n_matches": t["n"],
            "layers": {L: round(v / n, 2) for L, v in t["layers"].items()},
        })
    rows.sort(key=lambda r: -r["composite"])
    return rows


def _history() -> list[dict]:
    out = []
    for mdir in _match_dirs():
        fixture = _read(mdir / "fixture.json")
        if not fixture:
            continue
        pack = _read(mdir / "context_pack.json") or {}
        header = pack.get("fixture_header", {})
        header_blue = header.get("blue") or {}
        header_red = header.get("red") or {}
        opps = fixture.get("opponents") or []
        blue_opp = opps[0]["opponent"] if opps else {}
        red_opp = opps[1]["opponent"] if len(opps) > 1 else {}
        blue = blue_opp.get("name") or header_blue.get("name") or "?"
        red = red_opp.get("name") or header_red.get("name") or "?"
        blue_image_url = header_blue.get("image_url") or blue_opp.get("image_url")
        red_image_url = header_red.get("image_url") or red_opp.get("image_url")
        results = {r.get("team_id"): r.get("score", 0) for r in (fixture.get("results") or [])}
        blue_id = blue_opp.get("id")
        red_id = red_opp.get("id")
        truth = {
            "status": fixture.get("status"),
            "series_score": f"{results.get(blue_id,0)}-{results.get(red_id,0)}",
        }
        model_results: dict[str, float] = {}
        for rf in (mdir / "results").glob("*.json"):
            model_results[rf.stem] = _read(rf).get("composite", 0.0)
        preds: dict[str, Any] = {}
        for pf in (mdir / "predictions").glob("*.json"):
            rec = _prediction_record(pf)
            if rec:
                preds[pf.stem] = rec
        out.append({
            "slug": mdir.name,
            "league": header.get("league") or (fixture.get("league") or {}).get("name"),
            "blue": blue, "red": red,
            "blue_image_url": blue_image_url, "red_image_url": red_image_url,
            "begin_at": fixture.get("begin_at"),
            "status": fixture.get("status"),
            "truth": truth,
            "predictions": preds,
            "results": model_results,
        })
    out.sort(key=lambda h: h.get("begin_at") or "", reverse=True)
    return out


def _incoming(history: list[dict] | None = None) -> list[dict]:
    rows = []
    for h in history if history is not None else _history():
        if h.get("status") in ("not_started", None, "") and not h.get("predictions"):
            rows.append(h)
    rows.sort(key=lambda h: h.get("begin_at") or "")
    return rows[:30]


def _predicted_upcoming(history: list[dict] | None = None) -> list[dict]:
    rows = []
    for h in history if history is not None else _history():
        if h.get("status") in ("not_started", None, "") and h.get("predictions"):
            rows.append(h)
    rows.sort(key=lambda h: h.get("begin_at") or "")
    return rows[:30]


# ----------------------------- games -----------------------------

def _game_leaderboard() -> list[dict]:
    totals: dict[str, dict] = defaultdict(lambda: {"composite": 0.0, "n": 0})
    for g in _game_history():
        for mid, comp in g.get("results", {}).items():
            totals[mid]["composite"] += comp
            totals[mid]["n"] += 1
    rows = []
    for mid, t in totals.items():
        n = t["n"] or 1
        rows.append({
            "model_id": mid,
            "display_name": _model_name_map().get(mid, mid),
            "composite": round(t["composite"] / n, 2),
            "n_games": t["n"],
        })
    rows.sort(key=lambda r: -r["composite"])
    return rows


def _game_history() -> list[dict]:
    out = []
    if not cfg.GAMES_DIR.exists():
        return out
    for match_dir in sorted(cfg.GAMES_DIR.glob("*")):
        for gdir in sorted(match_dir.glob("g*")):
            bp = _read(gdir / "bp.json") or {}
            preds: dict[str, Any] = {}
            for pf in (gdir / "predictions").glob("*.json"):
                rec = _prediction_record(pf)
                if rec:
                    preds[pf.stem] = rec
            truth = {
                "winner_side": _winner_side(bp),
                "length_min": round((bp.get("length_sec") or 0) / 60.0, 1),
                "status": bp.get("status"),
            }
            out.append({
                "match_slug": match_dir.name,
                "position": bp.get("position") or int(gdir.name[1:]),
                "blue": (bp.get("picks", {}).get("blue")),
                "red": (bp.get("picks", {}).get("red")),
                "bp_complete": bp.get("bp_complete"),
                "truth": truth,
                "predictions": preds,
                "results": {},   # filled by grader when results are written here
            })
    return out


def _winner_side(bp: dict) -> str | None:
    wid = bp.get("winner_id")
    if not wid:
        return None
    # crude: we don't always store blue/red team ids in bp; leave None if unknown
    return None


# ----------------------------- helpers -----------------------------

def _match_dirs() -> list[Path]:
    if not cfg.MATCHES_DIR.exists():
        return []
    return sorted(d for d in cfg.MATCHES_DIR.glob("*") if d.is_dir())


def _read(path: Path) -> dict | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def _prediction_record(path: Path) -> dict[str, Any] | None:
    rec = _read(path)
    if not rec:
        return None
    prediction = rec.get("prediction") or {}
    summary = _prediction_summary(prediction)
    detail = {
        "model_id": rec.get("model_id") or path.stem,
        "scope": rec.get("scope"),
        "target_id": rec.get("target_id"),
        "submitted_at": rec.get("submitted_at"),
        "prediction": prediction,
        "sources": rec.get("sources") or prediction.get("sources") or [],
        "searches": _prediction_searches(path),
        "input_tokens": rec.get("input_tokens"),
        "output_tokens": rec.get("output_tokens"),
        "cost_usd": rec.get("cost_usd"),
        "wall_seconds": rec.get("wall_seconds"),
        "error": rec.get("error"),
    }
    return {"summary": summary, "detail": detail, **summary}


def _prediction_summary(prediction: dict[str, Any]) -> dict[str, Any]:
    return {
        "series_score": prediction.get("series_score"),
        "series_length": prediction.get("series_length"),
        "win_probs": prediction.get("win_probs"),
        "predicted_winner": prediction.get("predicted_winner"),
        "favored_side": prediction.get("favored_side"),
        "winner": prediction.get("predicted_winner"),
        "win_prob": prediction.get("win_prob"),
        "duration": prediction.get("expected_duration_min"),
        "kills": prediction.get("kills"),
        "total_kills": prediction.get("total_kills"),
    }


def _prediction_searches(path: Path) -> dict[str, Any] | None:
    search_path = path.parent / "searches" / path.name
    return _read(search_path)


if __name__ == "__main__":
    build()

"""Build data.json for the single-page leaderboard site.

Aggregates all predictions/results under data/ into one payload:
  {
    "models": [{id, display_name}],
    "leaderboard":  [{model_id, composite, n_matches, layers}],
    "game_leaderboard": [{model_id, composite, n_games}],
    "incoming":    [{slug, league, blue, red, begin_at, kickoff_utc, status}],
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
    payload = {
        "models": models,
        "leaderboard": _series_leaderboard(),
        "game_leaderboard": _game_leaderboard(),
        "incoming": _incoming(),
        "history": _history(),
        "game_history": _game_history(),
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
        opps = fixture.get("opponents") or []
        blue = (opps[0]["opponent"] if opps else {}).get("name", "?")
        red = (opps[1]["opponent"] if len(opps) > 1 else {}).get("name", "?")
        results = {r.get("team_id"): r.get("score", 0) for r in (fixture.get("results") or [])}
        blue_id = (opps[0]["opponent"] if opps else {}).get("id")
        red_id = (opps[1]["opponent"] if len(opps) > 1 else {}).get("id")
        truth = {
            "status": fixture.get("status"),
            "series_score": f"{results.get(blue_id,0)}-{results.get(red_id,0)}",
        }
        model_results: dict[str, float] = {}
        for rf in (mdir / "results").glob("*.json"):
            model_results[rf.stem] = _read(rf).get("composite", 0.0)
        preds: dict[str, Any] = {}
        for pf in (mdir / "predictions").glob("*.json"):
            rec = _read(pf)
            p = rec.get("prediction", {})
            preds[pf.stem] = {
                "series_score": p.get("series_score"),
                "win_probs": p.get("win_probs"),
                "predicted_winner": p.get("predicted_winner"),
            }
        out.append({
            "slug": mdir.name,
            "league": header.get("league") or (fixture.get("league") or {}).get("name"),
            "blue": blue, "red": red,
            "begin_at": fixture.get("begin_at"),
            "status": fixture.get("status"),
            "truth": truth,
            "predictions": preds,
            "results": model_results,
        })
    out.sort(key=lambda h: h.get("begin_at") or "", reverse=True)
    return out


def _incoming() -> list[dict]:
    rows = []
    for h in _history():
        if h.get("status") in ("not_started", None, ""):
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
                rec = _read(pf)
                p = rec.get("prediction", {})
                preds[pf.stem] = {
                    "winner": p.get("predicted_winner"),
                    "win_prob": p.get("win_prob"),
                    "duration": p.get("expected_duration_min"),
                    "kills": p.get("kills"),
                    "total_kills": p.get("total_kills"),
                }
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


if __name__ == "__main__":
    build()

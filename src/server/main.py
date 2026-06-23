"""FastAPI app: serves the static leaderboard + exposes the BP refresh trigger.

Routes:
  GET  /                 -> docs/site/index.html
  GET  /data.json        -> docs/site/data.json
  GET  /api/matches      -> list tracked matches (from data/)
  POST /api/refresh-bp   -> fetch BP for one game; if complete, auto-predict
  POST /api/predict      -> manually trigger series prediction for a match
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel

from .. import config as cfg

app = FastAPI(title="LoLArena", version="0.1.0")
SITE = cfg.SITE_DIR


@app.get("/")
def index():
    idx = SITE / "index.html"
    if not idx.exists():
        raise HTTPException(404, "Site not built. Run: python -m src build-site")
    return FileResponse(idx)


@app.get("/data.json")
def data_json():
    f = SITE / "data.json"
    if not f.exists():
        return JSONResponse({"models": [], "leaderboard": [], "game_leaderboard": [],
                             "incoming": [], "history": [], "game_history": []})
    return FileResponse(f, media_type="application/json")


@app.get("/api/matches")
def api_matches():
    """List all match dirs with a brief status."""
    out = []
    if cfg.MATCHES_DIR.exists():
        for d in sorted(cfg.MATCHES_DIR.glob("*")):
            if not d.is_dir():
                continue
            fix_path = d / "fixture.json"
            fixture = {}
            if fix_path.exists():
                fixture = json.loads(fix_path.read_text(encoding="utf-8"))
            opps = fixture.get("opponents") or []
            out.append({
                "slug": d.name,
                "match_id": fixture.get("id"),
                "league": (fixture.get("league") or {}).get("name"),
                "blue": (opps[0]["opponent"] if opps else {}).get("name"),
                "red": (opps[1]["opponent"] if len(opps) > 1 else {}).get("name"),
                "begin_at": fixture.get("begin_at"),
                "status": fixture.get("status"),
                "number_of_games": fixture.get("number_of_games"),
                "games": [{"position": g.get("position"), "status": g.get("status")}
                          for g in (fixture.get("games") or [])],
            })
    return out


class RefreshBPRequest(BaseModel):
    match_id: int
    game_pos: int
    predict: bool = True   # auto-run all models once BP is complete


@app.post("/api/refresh-bp")
def refresh_bp(req: RefreshBPRequest):
    """Fetch BP for a game. If complete and predict=True, run single-game prediction."""
    from ..pipeline import collect as collect_mod
    from ..adapters.pandascore import PandaScoreClient
    try:
        client = PandaScoreClient()
        match = collect_mod.fetch_fixture(req.match_id, client, refresh=True)
        bp = collect_mod.fetch_game_bp(match, req.game_pos, client, refresh=True)
    except Exception as e:  # noqa: BLE001
        raise HTTPException(500, detail=f"fetch failed: {e}")
    if bp is None:
        return {"ok": False, "message": f"Game {req.game_pos} not found for match {req.match_id}."}
    if not bp.get("bp_complete"):
        return {
            "ok": True, "bp_complete": False,
            "message": "BP 尚未公开，请稍后再次刷新。",
            "blue_picks": len(bp["picks"]["blue"]), "red_picks": len(bp["picks"]["red"]),
        }
    triggered = 0
    if req.predict:
        from ..pipeline import orchestrator as orch
        recs = orch.cmd_predict_game(req.match_id, req.game_pos)
        triggered = sum(1 for r in recs if r.get("prediction") and not r.get("error"))
        failed = [r.get("model_id") for r in recs if r.get("error")]
    else:
        failed = []
    return {
        "ok": True, "bp_complete": True,
        "blue_picks": bp["picks"]["blue"], "red_picks": bp["picks"]["red"],
        "predictions_triggered": triggered,
        "site_rebuilt": bool(req.predict),
        "failed_models": failed,
    }


class PredictRequest(BaseModel):
    match_id: int
    model_ids: list[str] | None = None


@app.post("/api/predict")
def api_predict(req: PredictRequest):
    """Manually trigger series-level prediction for a match (all models)."""
    from ..pipeline import orchestrator as orch
    recs = orch.cmd_predict(req.match_id, model_ids=req.model_ids)
    ok = sum(1 for r in recs if r.get("prediction") and not r.get("error"))
    failed = [r.get("model_id") for r in recs if r.get("error")]
    return {"ok": True, "predicted": ok, "total": len(recs),
            "site_rebuilt": True, "failed_models": failed, "results": recs}


@app.post("/api/rebuild")
def rebuild_site():
    """Regenerate data.json (called by the web UI after predictions land)."""
    from ..leaderboard import build_site
    payload = build_site.build()
    return {"ok": True, "matches": len(payload["history"]), "games": len(payload["game_history"])}

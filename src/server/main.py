"""FastAPI app: serves the static leaderboard + exposes the BP refresh trigger.

Routes:
  GET  /                 -> docs/site/index.html
  GET  /data.json        -> docs/site/data.json
  GET  /api/matches      -> list tracked matches (from data/)
  POST /api/refresh-bp   -> fetch BP for one game; if complete, auto-predict
  POST /api/predict      -> manually trigger series prediction for a match
  POST /api/predict-game -> manually trigger single-game analysis (post-BP, step 2)
  POST /api/grade        -> settle a finished series (score vs truth)
  POST /api/grade-game   -> settle one finished game (score vs truth)
  POST /api/rebuild      -> regenerate data.json
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse
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
    from ..adapters.cito import get_client
    try:
        client = get_client()
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


class PredictGameRequest(BaseModel):
    match_id: int
    game_pos: int


@app.post("/api/predict-game")
def api_predict_game(req: PredictGameRequest):
    """Manually trigger single-game analysis for one game (post-BP, step 2 of 2).

    This is the decoupled half of refresh-bp: the UI calls refresh-bp first
    (predict=false) to fetch BP, then this endpoint to run the models.
    """
    from ..pipeline import orchestrator as orch
    # Pre-check BP completeness so we can return a clear 400 instead of a silent
    # empty list (cmd_predict_game only prints a warning when BP is incomplete).
    from ..adapters.cito import get_client
    from ..pipeline import collect as collect_mod
    try:
        client = get_client()
        match = collect_mod.fetch_fixture(req.match_id, client, refresh=False)
        bp = collect_mod.fetch_game_bp(match, req.game_pos, client, refresh=False)
    except Exception as e:  # noqa: BLE001
        raise HTTPException(500, detail=f"fetch failed: {e}")
    if bp is None:
        raise HTTPException(400, detail=f"Game {req.game_pos} not found for match {req.match_id}.")
    if not bp.get("bp_complete"):
        raise HTTPException(400, detail="BP 尚未完成，请先点击「刷新BP」。")
    recs = orch.cmd_predict_game(req.match_id, req.game_pos)
    ok = sum(1 for r in recs if r.get("prediction") and not r.get("error"))
    failed = [r.get("model_id") for r in recs if r.get("error")]
    return {"ok": True, "predicted": ok, "total": len(recs),
            "site_rebuilt": True, "failed_models": failed, "results": recs}


class GradeRequest(BaseModel):
    match_id: int


@app.post("/api/grade")
def api_grade(req: GradeRequest):
    """Settle a finished series: score every model's prediction vs truth."""
    from ..pipeline import orchestrator as orch
    out = orch.cmd_grade(req.match_id)
    return {"ok": True, "site_rebuilt": True,
            "truth": out.get("truth"), "results": out.get("results", {}),
            "error": out.get("error")}


class GradeGameRequest(BaseModel):
    match_id: int
    game_pos: int


@app.post("/api/grade-game")
def api_grade_game(req: GradeGameRequest):
    """Settle one finished game: score every model's game prediction vs truth."""
    from ..pipeline import orchestrator as orch
    out = orch.cmd_grade_game(req.match_id, req.game_pos)
    return {"ok": True, "site_rebuilt": True,
            "position": out.get("position"),
            "truth": out.get("truth"), "results": out.get("results", {}),
            "error": out.get("error")}


@app.post("/api/rebuild")
def rebuild_site():
    """Regenerate data.json (called by the web UI after predictions land)."""
    from ..leaderboard import build_site
    payload = build_site.build()
    return {"ok": True, "matches": len(payload["history"]), "games": len(payload["game_history"])}


# ============================== betting advice ==============================

class BettingOdds(BaseModel):
    moneyline: dict[str, float] = {}        # {"blue": 1.5, "red": 2.4}
    correct_score: dict[str, float] = {}    # {"3-0": 2.1, "0-3": 8.0, ...}
    handicap: dict[str, float] = {}         # {"-1.5": 1.9, "+1.5": 1.9}
    total_games: dict[str, float] = {}      # {"over_3.5": 1.8, "under_3.5": 1.95}


class BettingAdviceRequest(BaseModel):
    slug: str
    model_id: str
    odds: BettingOdds


@app.get("/api/betting-advice/list")
def betting_advice_list(slug: str):
    """All betting-advice runs for a match (newest first) — for the comparison view."""
    from ..pipeline import betting
    if not (cfg.MATCHES_DIR / slug).exists():
        raise HTTPException(404, detail=f"match slug '{slug}' not found")
    return betting.list_advice(slug)


@app.post("/api/betting-advice")
def betting_advice(req: BettingAdviceRequest):
    """Stream one model's betting analysis to the browser via SSE.

    Prereq: the match must already have predictions (we reason over them).
    Returns text/event-stream:
        event: start    data:{model_id, slug}
        event: delta    data:{text}
        event: thinking data:{text}
        event: ping     data:{elapsed}        # keep-alive during long waits
        event: done     data:{...raw_text, thinking_text, picks, saved, tokens, cost, error}
    """
    from ..pipeline import betting

    mdir = cfg.MATCHES_DIR / req.slug
    if not mdir.exists():
        raise HTTPException(404, detail=f"match slug '{req.slug}' not found")
    if not betting.has_predictions(req.slug):
        raise HTTPException(400, detail="该比赛尚未预测，无法生成下注建议（需先完成系列赛预测）。")
    odds = req.odds.model_dump()
    if not any(odds.values()):
        raise HTTPException(400, detail="未填入任何赔率，无法生成下注建议。")

    # Run the (blocking, network-bound) generator on a worker thread and feed
    # its events into a queue. The main thread drains the queue and interleaves
    # a heartbeat every few seconds so the connection never looks idle — this
    # is what keeps proxies/browsers from killing the stream during a long
    # thinking phase, and lets the UI show "still working" feedback.
    import queue
    import threading
    import time

    out_q: "queue.Queue[tuple[str, dict | None]]" = queue.Queue()
    HEARTBEAT = 5.0  # seconds between keep-alive pings

    def worker():
        try:
            for ev in betting.stream_betting_advice(req.slug, req.model_id, odds):
                etype = ev.pop("type", "message")
                out_q.put((etype, ev))
        except Exception as e:  # noqa: BLE001
            out_q.put(("done", {"error": f"{type(e).__name__}: {e}"}))
        finally:
            out_q.put((None, None))  # sentinel: stream finished

    threading.Thread(target=worker, daemon=True).start()

    def gen():
        t0 = time.time()
        while True:
            try:
                etype, ev = out_q.get(timeout=HEARTBEAT)
            except queue.Empty:
                # No real event for a while → emit a heartbeat so the browser
                # (and any reverse proxy) knows we're alive.
                yield f"event: ping\ndata: {json.dumps({'elapsed': round(time.time() - t0, 1)}, ensure_ascii=False)}\n\n"
                continue
            if etype is None:  # sentinel
                break
            yield f"event: {etype}\ndata: {json.dumps(ev, ensure_ascii=False)}\n\n"

    return StreamingResponse(gen(), media_type="text/event-stream",
                             headers={"Cache-Control": "no-cache",
                                      "X-Accel-Buffering": "no"})

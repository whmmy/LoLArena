"""FastAPI app: serves the static leaderboard + exposes the BP refresh trigger.

Routes:
  GET  /                 -> docs/site/index.html
  GET  /data.json        -> docs/site/data.json
  GET  /api/matches      -> list tracked matches (from data/)
  POST /api/refresh-bp   -> fetch BP for one game; if complete, auto-predict
  POST /api/refresh-bp-all -> fetch BP for EVERY game in a series at once
  POST /api/predict      -> manually trigger series prediction for a match
  POST /api/predict-game -> manually trigger single-game analysis (post-BP, step 2)
  POST /api/grade        -> settle a finished series (score vs truth)
  POST /api/grade-game   -> settle one finished game (score vs truth)
  POST /api/rebuild      -> regenerate data.json
  GET  /api/champions    -> full champion roster (name+icon+aliases) for the manual BP editor
  GET  /api/match-roster -> blue/red 5-man rosters (role+name) for a match slug
  POST /api/save-bp      -> manually save picks into bp.json (manual BP editor)
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


class RefreshBpAllRequest(BaseModel):
    match_id: int


@app.post("/api/refresh-bp-all")
def refresh_bp_all(req: RefreshBpAllRequest):
    """Fetch BP for EVERY game in a series at once.

    This is the series-level entry point — BP collection belongs on the series
    card, not the per-game card. Creates the g1/g2/g3 dirs so game cards appear,
    then a rebuild surfaces them. Returns per-game BP completeness.
    """
    from ..pipeline import collect as collect_mod
    from ..adapters.cito import get_client
    try:
        client = get_client()
        match = collect_mod.fetch_fixture(req.match_id, client, refresh=True)
        recs = collect_mod.fetch_all_game_bps(match, client, refresh=True)
    except Exception as e:  # noqa: BLE001
        raise HTTPException(500, detail=f"fetch failed: {e}")
    games = [{"position": r.get("position"),
              "bp_complete": bool((r.get("bp") or {}).get("bp_complete"))}
             for r in recs]
    complete = sum(1 for g in games if g["bp_complete"])
    # Rebuild so the freshly-created game cards show up immediately.
    from ..pipeline import orchestrator as orch
    orch._maybe_rebuild_site()
    return {"ok": True, "total": len(games), "bp_complete": complete,
            "site_rebuilt": True, "games": games}


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


# ================================ manual BP editor ================================

@app.get("/api/champions")
def api_champions():
    """Full champion roster for the manual BP editor.

    Each entry: {name, slug, image_url, big_image_url, aliases:[...]}. Aliases
    are Chinese nicknames joined from repo-root champion_aliases.py. Disk-cached
    in PandaScore's _pandascore_cache (24h TTL) + 5 min in-memory cache here.
    Returns [] if PandaScore is unreachable (editor still opens, just iconless).
    """
    from . import champions as champ_mod
    return champ_mod.get_champions_data()


@app.get("/api/match-roster")
def api_match_roster(slug: str):
    """Blue/red 5-man rosters for a match, read from the on-disk context_pack.

    Independent of the (unstable) game-stats BP API. Used by the manual BP
    editor to know which player fills each role slot. Returns players in
    canonical role order (top/jun/mid/adc/sup).
    """
    pack_path = cfg.MATCHES_DIR / slug / "context_pack.json"
    if not pack_path.exists():
        raise HTTPException(404, detail=f"context_pack not found for slug '{slug}'")
    pack = json.loads(pack_path.read_text(encoding="utf-8"))
    rosters = pack.get("rosters") or {}

    def _side(side: str) -> dict:
        block = rosters.get(side) or {}
        team = block.get("team") or {}
        players = block.get("players") or []
        # Ensure canonical role order; the context_pack already stores
        # canonical role keys, but re-sort defensively.
        order = {"top": 0, "jun": 1, "mid": 2, "adc": 3, "sup": 4}
        players = sorted(players, key=lambda p: order.get(p.get("role"), 99))
        return {
            "team": {
                "name": team.get("name"),
                "acronym": team.get("acronym"),
                "image_url": team.get("image_url"),
            },
            "players": [{"role": p.get("role"), "name": p.get("name"),
                         "id": p.get("id")} for p in players],
            "available": bool(block.get("available", True)),
        }

    return {"blue": _side("blue"), "red": _side("red")}


class SaveBPPick(BaseModel):
    role: str
    player: str | None = None
    champion: str
    spells: list[str] = []


class SaveBPRequest(BaseModel):
    # Cito/Riot ids are 18-digit — JS loses precision, so the UI sends a string.
    # Accept either; FastAPI coerces numeric strings to int via the match lookup.
    match_id: int
    game_pos: int
    blue: list[SaveBPPick]
    red: list[SaveBPPick]


@app.post("/api/save-bp")
def save_bp(req: SaveBPRequest):
    """Persist manually-picked champions into bp.json.

    Writes to data/games/<slug>/g<pos>/bp.json — the SAME file the auto-BP
    fetcher writes — preserving its existing non-pick fields (status/length/
    winner/game_id). Sets bp_complete when both sides reach 5 picks, then
    rebuilds data.json so the UI updates immediately. Does NOT auto-predict
    (the user runs single-game analysis separately after saving).
    """
    from ..pipeline import collect as collect_mod
    from ..adapters.cito import get_client
    from ..pipeline import orchestrator as orch

    try:
        client = get_client()
        match = collect_mod.fetch_fixture(req.match_id, client, refresh=False)
    except Exception as e:  # noqa: BLE001
        raise HTTPException(500, detail=f"无法加载比赛数据: {e}")

    # Resolve the EXISTING match dir by fixture id — never re-derive the slug
    # from the match object, because the league/team names in the freshly-fetched
    # detail can differ from how the dir was originally created at scan time
    # (e.g. "ReLove Deep Cross Gaming" vs "Deep Cross Gaming"), which would
    # silently write to a brand-new, orphaned dir. _find_existing_match_dir is
    # the same lookup fetch_fixture uses for exactly this reason.
    existing_dir = collect_mod._find_existing_match_dir(req.match_id)
    if existing_dir is None:
        raise HTTPException(404, detail=f"找不到 match_id={req.match_id} 对应的比赛目录，请先扫描/预测该比赛。")
    slug = existing_dir.name
    gdir = cfg.game_dir(slug, req.game_pos)
    bp_path = gdir / "bp.json"

    # Find the game stub for game_id / status / length / winner preservation.
    games = match.get("games") or []
    game_stub = next((g for g in games if g.get("position") == req.game_pos), {})

    # Keep whatever bp.json already holds (e.g. fetched_at, cached truth) and
    # only overwrite picks + bp_complete + identifying fields.
    existing: dict[str, Any] = {}
    if bp_path.exists():
        try:
            existing = json.loads(bp_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            existing = {}

    def _dump(picks: list[SaveBPPick]) -> list[dict]:
        return [{"role": p.role, "player": p.player, "champion": p.champion,
                 "spells": p.spells} for p in picks]

    blue_list = _dump(req.blue)
    red_list = _dump(req.red)
    complete = len(blue_list) >= 5 and len(red_list) >= 5

    bp = {
        "match_id": match.get("id"),
        "game_id": existing.get("game_id") or game_stub.get("id"),
        "position": req.game_pos,
        "status": existing.get("status") or game_stub.get("status"),
        "length_sec": existing.get("length_sec", game_stub.get("length")),
        "winner_id": existing.get("winner_id", (game_stub.get("winner") or {}).get("id")),
        "bp_complete": complete,
        "picks": {"blue": blue_list, "red": red_list},
        "fetched_at": existing.get("fetched_at"),
        "manual": True,   # mark this BP as hand-entered (auto-fetch overwrites it)
    }
    # Preserve any truth fields the grader may have mirrored in earlier.
    for k in ("winner_side", "kills", "total_kills", "length_min"):
        if k in existing:
            bp[k] = existing[k]

    bp_path.write_text(json.dumps(bp, ensure_ascii=False, indent=2), encoding="utf-8")
    orch._maybe_rebuild_site()
    return {
        "ok": True, "bp_complete": complete, "site_rebuilt": True,
        "blue_picks": blue_list, "red_picks": red_list,
    }


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

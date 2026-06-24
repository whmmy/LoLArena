"""Orchestrator: the commands that drive the whole flow.

  cmd_scan        -> find upcoming tracked matches, persist fixtures
  cmd_collect     -> build context_pack for a match
  cmd_predict     -> run every model on a match (series prediction)
  cmd_predict_game-> run every model on a single game (post-BP)
  cmd_grade       -> score series predictions against post-match truth
  cmd_grade_game  -> score a single game's predictions

All commands are idempotent: re-running skips already-written files unless
refresh=True.
"""

from __future__ import annotations

import json
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from .. import config as cfg
from ..adapters.pandascore import PandaScoreClient
from ..adapters.websearch import WebSearchTool
from ..runners import build_runner
from . import collect as collect_mod
from . import prompt_build, validate


# ============================== scan / collect ==============================

def cmd_scan(*, horizon_days: int | None = None, refresh: bool = False) -> list[dict]:
    """Find upcoming tracked-league matches and persist their fixtures."""
    client = PandaScoreClient()
    horizon = horizon_days or cfg.leagues_cfg().get("scan_horizon_days", 14)
    league_ids = list(client.tracked_league_ids().values())
    if not league_ids:
        print("[scan] No tracked leagues resolved from PandaScore. Check leagues.yaml slugs.")
        return []
    matches = client.upcoming_matches(league_ids, horizon_days=horizon)
    out: list[dict] = []
    print(f"[scan] {len(matches)} upcoming match(es) found in tracked leagues:\n")
    for m in matches:
        try:
            fixture = collect_mod.fetch_fixture(m["id"], client, refresh=refresh, match_obj=m)
            out.append(fixture)
        except (ValueError, FileNotFoundError) as e:
            print(f"  - [skip] match {m.get('id')}: {e}")
            continue
        opps = m.get("opponents") or []
        blue = (opps[0]["opponent"] if opps else {}).get("name", "?")
        red = (opps[1]["opponent"] if len(opps) > 1 else {}).get("name", "?")
        league = (m.get("league") or {}).get("name", "?")
        begin = (m.get("begin_at") or "")[:16].replace("T", " ")
        bo = m.get("number_of_games")
        print(f"  match_id={m['id']:>8}   {league}   Bo{bo}   "
              f"{blue} vs {red}   @ {begin} UTC")
    print(f"\n[scan] {len(out)} fixtures ready. "
          f"Pick one and run:  python -m src predict <match_id>")
    return out


def cmd_collect(match_id: int, *, refresh: bool = False) -> dict:
    """Build the shared context_pack.json for one match."""
    client = PandaScoreClient()
    match = collect_mod.fetch_fixture(match_id, client, refresh=refresh)
    pack = collect_mod.collect_context_pack(match, client)
    print(f"[collect] context_pack written for match {match_id} "
          f"({pack['fixture_header']['blue']['name']} vs "
          f"{pack['fixture_header']['red']['name']}).")
    return pack


def _match_slug_of(match: dict) -> str:
    opps = match.get("opponents") or []
    league = (match.get("league") or {}).get("name", "LoL")
    return cfg.match_slug(league, opps[0]["opponent"]["name"],
                          opps[1]["opponent"]["name"], match.get("begin_at") or "")


def _load_or_fetch_fixture(match_id: int, client, *, refresh: bool = False) -> dict:
    """Reuse an already-saved fixture.json if present (avoids re-hitting the
    network). Only fetches from PandaScore when no local fixture exists yet."""
    for mdir in sorted(cfg.MATCHES_DIR.glob("*")) if cfg.MATCHES_DIR.exists() else []:
        fp = mdir / "fixture.json"
        if not fp.exists():
            continue
        try:
            m = json.loads(fp.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        if m.get("id") == match_id:
            m["_match_dir"] = str(mdir)
            return m
    # not cached locally -> fetch (needs network)
    return collect_mod.fetch_fixture(match_id, client, refresh=refresh)


# ============================== predict (series) ==============================

def cmd_predict(match_id: int, *, model_ids: list[str] | None = None,
                max_workers: int = 4, refresh: bool = False,
                auto_rebuild_site: bool = True) -> list[dict]:
    """Run series-level prediction for every model on a match."""
    client = PandaScoreClient()
    match = _load_or_fetch_fixture(match_id, client, refresh=refresh)
    if not Path(match["_match_dir"], "context_pack.json").exists():
        collect_mod.collect_context_pack(match, client)

    pack = json.loads((Path(match["_match_dir"]) / "context_pack.json")
                      .read_text(encoding="utf-8"))
    system, user = prompt_build.build_match_prompt(pack)
    slug = _match_slug_of(match)
    target_id = slug

    models = _select_models(model_ids)
    print(f"[predict] match {match_id} ({slug}) -> {len(models)} models")
    records = _run_all(models, system, user, scope="match", target_id=target_id,
                       out_dir=Path(match["_match_dir"]) / "predictions",
                       validate_fn=validate.validate_match, max_workers=max_workers)
    if auto_rebuild_site:
        _maybe_rebuild_site()
    return records


# ============================== predict (single game) ==============================

def cmd_predict_game(match_id: int, position: int, *, model_ids: list[str] | None = None,
                     max_workers: int = 4, refresh_bp: bool = False,
                     auto_rebuild_site: bool = True) -> list[dict]:
    """Run single-game prediction for every model (after BP is fetched)."""
    client = PandaScoreClient()
    match = collect_mod.fetch_fixture(match_id, client, refresh=refresh_bp)
    bp = collect_mod.fetch_game_bp(match, position, client, refresh=refresh_bp)
    if bp is None:
        print(f"[predict-game] game {position} of match {match_id} not found.")
        return []
    if not bp.get("bp_complete"):
        print(f"[predict-game] BP for match {match_id} game {position} is NOT complete "
              f"(blue picks={len(bp['picks']['blue'])}, red picks={len(bp['picks']['red'])}). "
              f"Re-run after BP finishes.")
        return []

    # series state so far (who's ahead in games)
    results = {r.get("team_id"): r.get("score", 0) for r in (match.get("results") or [])}
    opps = match.get("opponents") or []
    blue_id = opps[0]["opponent"]["id"] if opps else None
    red_id = opps[1]["opponent"]["id"] if len(opps) > 1 else None
    series_state = {
        "series_score_blue": results.get(blue_id, 0),
        "series_score_red": results.get(red_id, 0),
        "last_game_summary": _last_game_summary(match, position),
    }

    system, user = prompt_build.build_game_prompt(bp, match, series_state)
    slug = _match_slug_of(match)
    target_id = f"{slug}/g{position}"
    gdir = cfg.game_dir(slug, position)

    models = _select_models(model_ids)
    print(f"[predict-game] match {match_id} game {position} -> {len(models)} models")
    records = _run_all(models, system, user, scope="game", target_id=target_id,
                       out_dir=gdir / "predictions",
                       validate_fn=validate.validate_game, max_workers=max_workers)
    if auto_rebuild_site:
        _maybe_rebuild_site()
    return records


def _last_game_summary(match: dict, position: int) -> dict | None:
    games = match.get("games") or []
    prev = next((g for g in games if g.get("position") == position - 1), None)
    if not prev:
        return None
    opps = match.get("opponents") or []
    winner_id = (prev.get("winner") or {}).get("id")
    winner = next((o["opponent"]["name"] for o in opps
                   if o["opponent"]["id"] == winner_id), None)
    return {
        "position": position - 1,
        "winner": winner,
        "length_min": round((prev.get("length") or 0) / 60.0, 1),
    }


# ============================== shared runner loop ==============================

def _select_models(model_ids: list[str] | None) -> list[dict]:
    all_models = cfg.models_cfg()
    if not model_ids:
        return all_models
    wanted = set(model_ids)
    chosen = [m for m in all_models if m["id"] in wanted]
    missing = wanted - {m["id"] for m in chosen}
    if missing:
        print(f"[predict] WARNING: unknown models ignored: {sorted(missing)}")
    return chosen


def _make_search_tool() -> WebSearchTool:
    """One fresh search tool per prediction (resets call count + query log)."""
    return WebSearchTool()


def _run_all(models: list[dict], system: str, user: str, *, scope: str,
             target_id: str, out_dir: Path, validate_fn, max_workers: int) -> list[dict]:
    out_dir.mkdir(parents=True, exist_ok=True)
    results: list[dict] = []
    progress_events: list[dict[str, Any]] = []
    print_lock = threading.Lock()
    started_at = datetime.now(timezone.utc)

    print(f"[predict] running with max_workers={max_workers}; logs -> {out_dir}")

    def _progress(event: dict[str, Any]) -> None:
        event = {"at": datetime.now(timezone.utc).isoformat(), **event}
        with print_lock:
            progress_events.append(event)
            line = _format_progress_event(event)
            if line:
                print(line, flush=True)

    def _job(m):
        try:
            runner = build_runner(m, _make_search_tool())
            res = runner.run(system, user, scope=scope, target_id=target_id,
                             validate_fn=validate_fn, progress=_progress)
        except Exception as e:  # noqa: BLE001
            record = {
                "model_id": m["id"], "scope": scope, "target_id": target_id,
                "submitted_at": datetime.now(timezone.utc).isoformat(),
                "prediction": {}, "sources": [], "input_tokens": 0,
                "output_tokens": 0, "tool_calls": 0, "cost_usd": 0.0,
                "wall_seconds": 0.0, "error": f"{type(e).__name__}: {e}",
            }
            (out_dir / f"{m['id']}.json").write_text(
                json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8"
            )
            return record
        record = {
            "model_id": res.model_id, "scope": res.scope, "target_id": res.target_id,
            "submitted_at": res.submitted_at, "prediction": res.prediction,
            "raw_text": res.raw_text, "thinking_text": res.thinking_text,
            "sources": res.sources, "input_tokens": res.input_tokens,
            "output_tokens": res.output_tokens, "tool_calls": res.tool_calls,
            "cost_usd": round(res.cost_usd, 6), "wall_seconds": round(res.wall_seconds, 2),
            "error": res.error,
        }
        (out_dir / f"{res.model_id}.json").write_text(
            json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        # persist the full web_search provenance log for audit / traceability
        if getattr(res, "search_log", None):
            sdir = out_dir / "searches"
            sdir.mkdir(exist_ok=True)
            (sdir / f"{res.model_id}.json").write_text(
                json.dumps({
                    "model_id": res.model_id, "scope": res.scope,
                    "target_id": res.target_id, "submitted_at": res.submitted_at,
                    "total_calls": len(res.search_log),
                    "searches": res.search_log,
                }, ensure_ascii=False, indent=2), encoding="utf-8"
            )
        # persist the full per-turn transcript (text + thinking + tool calls/
        # results for every _chat() call) for audit / traceability
        if getattr(res, "rounds", None):
            rdir = out_dir / "rounds"
            rdir.mkdir(exist_ok=True)
            (rdir / f"{res.model_id}.json").write_text(
                json.dumps({
                    "model_id": res.model_id, "scope": res.scope,
                    "target_id": res.target_id, "submitted_at": res.submitted_at,
                    "total_turns": len(res.rounds),
                    "rounds": res.rounds,
                }, ensure_ascii=False, indent=2), encoding="utf-8"
            )
        return record

    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {pool.submit(_job, m): m["id"] for m in models}
        for fut in as_completed(futures):
            rec = fut.result()
            results.append(rec)
            ok = "OK" if rec["prediction"] and not rec.get("error") else "FAIL"
            with print_lock:
                print(_format_model_result(ok, rec), flush=True)

    _write_run_summary(out_dir, scope, target_id, started_at, results, progress_events)
    _print_run_summary(results, started_at)

    return results


def _maybe_rebuild_site() -> None:
    try:
        from ..leaderboard import build_site
        build_site.build()
    except Exception as e:  # noqa: BLE001
        print(f"[predict] site rebuild skipped: {e}")


def _format_progress_event(event: dict[str, Any]) -> str:
    model_id = event.get("model_id", "?")
    kind = event.get("event")
    prefix = f"  [{model_id}]"
    if kind == "start":
        return f"{prefix} start {event.get('scope')} {event.get('target_id')}"
    if kind == "chat_start":
        suffix = " final" if event.get("final_after_budget") else ""
        return f"{prefix} round {event.get('round')} -> model call{suffix}"
    if kind == "chat_end":
        thinking = event.get("provider_thinking_chars") or 0
        thinking_note = f", provider_thinking_chars={thinking}" if thinking else ""
        return (f"{prefix} round {event.get('round')} <- "
                f"in={event.get('input_tokens')} out={event.get('output_tokens')} "
                f"text_chars={event.get('text_chars')} tool_calls={event.get('tool_calls')}"
                f"{thinking_note}")
    if kind == "tool_start":
        return f"{prefix} search #{event.get('call_no')}: {event.get('query')}"
    if kind == "tool_end":
        return (f"{prefix} search #{event.get('call_no')} done: "
                f"{event.get('result_count')} result(s)")
    if kind == "budget_hit":
        return f"{prefix} search budget hit ({event.get('max_tool_calls')}); asking for final JSON"
    if kind == "parse":
        return (f"{prefix} parsing final JSON attempt {event.get('attempt')} "
                f"({event.get('raw_chars')} chars)")
    if kind == "repair":
        errs = event.get("errors") or []
        return f"{prefix} validation repair attempt {event.get('attempt')}: {len(errs)} issue(s)"
    if kind == "validated":
        return f"{prefix} JSON validated on attempt {event.get('attempt')}"
    if kind == "error":
        return f"{prefix} ERROR {event.get('error')}"
    return ""


def _format_model_result(ok: str, rec: dict[str, Any]) -> str:
    bits = [f"  [{ok}] {rec['model_id']}"]
    if rec.get("prediction"):
        pred = rec["prediction"]
        winner = pred.get("predicted_winner") or pred.get("winner")
        confidence = pred.get("confidence")
        if winner:
            bits.append(f"winner={winner}")
        if confidence is not None:
            bits.append(f"confidence={confidence}")
        reasoning = pred.get("reasoning")
        if isinstance(reasoning, dict):
            summary = _short_reasoning(reasoning)
            if summary:
                bits.append(f"reasoning={summary}")
    bits.append(f"searches={rec.get('tool_calls', 0)}")
    bits.append(f"tokens={rec.get('input_tokens', 0)}/{rec.get('output_tokens', 0)}")
    bits.append(f"{rec.get('wall_seconds', 0)}s")
    if rec.get("error"):
        bits.append(f"err={rec['error']}")
    return "  ".join(bits)


def _short_reasoning(reasoning: dict[str, Any], limit: int = 220) -> str:
    text_parts = []
    for value in reasoning.values():
        if isinstance(value, str) and value.strip():
            text_parts.append(value.strip())
    text = " | ".join(text_parts)
    if len(text) <= limit:
        return text
    return text[:limit - 3].rstrip() + "..."


def _write_run_summary(out_dir: Path, scope: str, target_id: str,
                       started_at: datetime, results: list[dict[str, Any]],
                       progress_events: list[dict[str, Any]]) -> None:
    finished_at = datetime.now(timezone.utc)
    ok_count = sum(1 for r in results if r.get("prediction") and not r.get("error"))
    fail_count = len(results) - ok_count
    summary = {
        "scope": scope,
        "target_id": target_id,
        "started_at": started_at.isoformat(),
        "finished_at": finished_at.isoformat(),
        "wall_seconds": round((finished_at - started_at).total_seconds(), 2),
        "total_models": len(results),
        "ok": ok_count,
        "fail": fail_count,
        "total_tool_calls": sum(int(r.get("tool_calls") or 0) for r in results),
        "total_input_tokens": sum(int(r.get("input_tokens") or 0) for r in results),
        "total_output_tokens": sum(int(r.get("output_tokens") or 0) for r in results),
        "total_cost_usd": round(sum(float(r.get("cost_usd") or 0) for r in results), 6),
        "models": [_model_summary(r) for r in sorted(results, key=lambda x: x.get("model_id", ""))],
        "events": progress_events,
    }
    logs_dir = out_dir / "run_logs"
    logs_dir.mkdir(exist_ok=True)
    stamp = finished_at.strftime("%Y%m%dT%H%M%SZ")
    (logs_dir / f"{stamp}.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def _model_summary(rec: dict[str, Any]) -> dict[str, Any]:
    pred = rec.get("prediction") or {}
    return {
        "model_id": rec.get("model_id"),
        "ok": bool(pred and not rec.get("error")),
        "error": rec.get("error"),
        "predicted_winner": pred.get("predicted_winner") or pred.get("winner"),
        "confidence": pred.get("confidence"),
        "reasoning_summary": _short_reasoning(pred.get("reasoning") or {})
        if isinstance(pred.get("reasoning"), dict) else "",
        "tool_calls": rec.get("tool_calls", 0),
        "input_tokens": rec.get("input_tokens", 0),
        "output_tokens": rec.get("output_tokens", 0),
        "cost_usd": rec.get("cost_usd", 0),
        "wall_seconds": rec.get("wall_seconds", 0),
    }


def _print_run_summary(results: list[dict[str, Any]], started_at: datetime) -> None:
    finished_at = datetime.now(timezone.utc)
    ok_count = sum(1 for r in results if r.get("prediction") and not r.get("error"))
    fail_count = len(results) - ok_count
    print("[predict] summary: "
          f"ok={ok_count} fail={fail_count} models={len(results)} "
          f"searches={sum(int(r.get('tool_calls') or 0) for r in results)} "
          f"tokens={sum(int(r.get('input_tokens') or 0) for r in results)}/"
          f"{sum(int(r.get('output_tokens') or 0) for r in results)} "
          f"cost=${sum(float(r.get('cost_usd') or 0) for r in results):.6f} "
          f"wall={round((finished_at - started_at).total_seconds(), 2)}s")


# ============================== grade ==============================

def cmd_grade(match_id: int) -> dict:
    """Score every model's series prediction against the post-match truth."""
    from ..graders.grade_match import grade_match
    client = PandaScoreClient()
    match = client.match(match_id, refresh=True) or {}
    if match.get("status") != "finished":
        print(f"[grade] match {match_id} status={match.get('status')} (not finished).")
    truth = _truth_for_match(match)
    slug = _match_slug_of(match) if match.get("opponents") else f"match_{match_id}"
    pdir = cfg.match_dir(slug) / "predictions"
    out: dict[str, Any] = {"match_id": match_id, "truth": truth, "results": {}}
    for pf in sorted(pdir.glob("*.json")):
        model_id = pf.stem
        rec = json.loads(pf.read_text(encoding="utf-8"))
        scores = grade_match(rec.get("prediction", {}), truth)
        (cfg.match_dir(slug) / "results" / f"{model_id}.json").write_text(
            json.dumps(scores, ensure_ascii=False, indent=2), encoding="utf-8")
        out["results"][model_id] = scores
        print(f"  {model_id}: composite={scores.get('composite', 0):.1f}")
    return out


def cmd_grade_game(match_id: int, position: int) -> dict:
    from ..graders.grade_game import grade_game
    client = PandaScoreClient()
    match = client.match(match_id, refresh=True) or {}
    games = match.get("games") or []
    g = next((x for x in games if x.get("position") == position), None)
    if not g:
        print(f"[grade-game] game {position} of match {match_id} not found.")
        return {}
    detail = client.game_detail(g["id"], refresh=True) or {}
    truth = _truth_for_game(match, detail, g)
    slug = _match_slug_of(match) if match.get("opponents") else f"match_{match_id}"
    pdir = cfg.game_dir(slug, position) / "predictions"
    out: dict[str, Any] = {"match_id": match_id, "position": position,
                           "truth": truth, "results": {}}
    for pf in sorted(pdir.glob("*.json")):
        model_id = pf.stem
        rec = json.loads(pf.read_text(encoding="utf-8"))
        scores = grade_game(rec.get("prediction", {}), truth)
        out["results"][model_id] = scores
        print(f"  {model_id}: composite={scores.get('composite', 0):.1f}")
    return out


def _truth_for_match(match: dict) -> dict:
    opps = match.get("opponents") or []
    blue_id = opps[0]["opponent"]["id"] if opps else None
    red_id = opps[1]["opponent"]["id"] if len(opps) > 1 else None
    results = {r.get("team_id"): r.get("score", 0) for r in (match.get("results") or [])}
    blue_score = results.get(blue_id, 0)
    red_score = results.get(red_id, 0)
    return {
        "status": match.get("status"),
        "winner_side": "blue" if blue_score > red_score else "red",
        "blue_score": blue_score,
        "red_score": red_score,
        "series_length": blue_score + red_score,
        "series_score": f"{blue_score}-{red_score}",
    }


def _truth_for_game(match: dict, detail: dict, game_stub: dict) -> dict:
    opps = match.get("opponents") or []
    blue_id = opps[0]["opponent"]["id"] if opps else None
    red_id = opps[1]["opponent"]["id"] if len(opps) > 1 else None
    winner_id = (game_stub.get("winner") or {}).get("id")
    side = "blue" if winner_id == blue_id else "red"
    # total kills from per-player stats
    kills = {"blue": 0, "red": 0}
    for p in detail.get("players", []) or []:
        tid = (p.get("team") or {}).get("id")
        k = int(p.get("kills") or 0)
        if tid == blue_id:
            kills["blue"] += k
        elif tid == red_id:
            kills["red"] += k
    length_min = round((game_stub.get("length") or detail.get("length") or 0) / 60.0, 1)
    return {
        "winner_side": side,
        "length_min": length_min,
        "kills": kills,
        "total_kills": kills["blue"] + kills["red"],
        "status": game_stub.get("status"),
    }

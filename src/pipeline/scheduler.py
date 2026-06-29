"""APScheduler driver.

Event-driven job set (schedules are stable for days, so we do NOT poll them
on a short interval — that caused recurring Cito 429s):

  - scan_tick   (cron, default 0:00 + 12:00 UTC): pull ALL upcoming tracked-
    league matches and persist their fixtures. Heavy work batched twice a day.
    Does NOT build context_pack (that's ~30 req/match and would blow the
    free-tier quota if done for the whole season at once).
  - predict_tick (interval, default 15 min, LOCAL ONLY): scan on-disk
    fixtures; for any whose begin_at is within LOLA_PREDICT_LEAD_H and not yet
    predicted, run cmd_predict (which builds context_pack on demand). No API
    calls until a match enters its window.
  - grade_tick  (interval, default 15 min, TIME-GATED): for each match with
    predictions but no results, refresh its live status only once its
    estimated end time has passed (begin_at + games × LOLA_GAME_EST_MINUTES);
    if still unfinished, retry every LOLA_GRADE_RETRY_MINUTES.

All ticks back off silently for LOLA_CITO_BACKOFF_SECONDS after a rate-limit,
and share one CitoClient (and thus one key-pool cooldown) with the rest of the
process via cito.get_client().

Run standalone (`python -m src.pipeline.scheduler`) or embedded in the server
(see server/main.py) so the web app and scheduling share one process.
"""

from __future__ import annotations

import json
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

from apscheduler.schedulers.background import BackgroundScheduler

from .. import config as cfg
from ..adapters.cito import CitoError, get_client, is_rate_limited_error
from . import orchestrator as orch

# Module-level backoff: once any tick hits a rate-limit, every subsequent tick
# stays quiet until this time. Avoids the recurring `429 rate-limited` spam.
_backoff_until: float = 0.0


def _lead_hours() -> float:
    return float(cfg.env_int("LOLA_PREDICT_LEAD_H", 3))


def _game_est_minutes() -> int:
    return cfg.env_int("LOLA_GAME_EST_MINUTES", 45)


def _grade_retry_minutes() -> int:
    return cfg.env_int("LOLA_GRADE_RETRY_MINUTES", 30)


def _backoff_seconds() -> int:
    return cfg.env_int("LOLA_CITO_BACKOFF_SECONDS", 60)


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _parse_dt(s: str | None) -> datetime | None:
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None


def _match_slug_of(match: dict) -> str:
    opps = match.get("opponents") or []
    league = (match.get("league") or {}).get("name", "LoL")
    return cfg.match_slug(league, opps[0]["opponent"]["name"],
                          opps[1]["opponent"]["name"], match.get("begin_at") or "")


def _already_predicted(match: dict) -> bool:
    slug = _match_slug_of(match)
    pdir = cfg.MATCHES_DIR / slug / "predictions"
    return pdir.exists() and any(pdir.glob("*.json"))


def _throttled() -> bool:
    """True if we're in a global backoff or every Cito key is cooling down."""
    client = get_client()
    return time.time() < max(_backoff_until, client.throttled_until())


def _record_backoff(exc: BaseException) -> None:
    """On a rate-limit, set a quiet backoff window so ticks don't re-fire."""
    global _backoff_until
    if is_rate_limited_error(exc):
        _backoff_until = time.time() + _backoff_seconds()
        print(f"[scheduler] rate-limited; backing off for {_backoff_seconds()}s")


# ============================== scan (cron) ==============================

def scan_tick() -> None:
    """Pull ALL upcoming tracked-league matches and persist their fixtures.

    Runs on a daily cron (default 0:00 + 12:00 UTC). TBD-opponent matches are
    skipped inside upstream_matches(). Only fixture.json is written here;
    context_pack is built lazily by predict_tick once a match nears kickoff.
    """
    if _throttled():
        return
    try:
        horizon = cfg.env_int("LOLA_SCAN_HORIZON_DAYS", 365)
        orch.cmd_scan(horizon_days=horizon)
    except CitoError as e:
        _record_backoff(e)
        print(f"[scheduler] scan_tick error: {e}")
    except Exception as e:  # noqa: BLE001
        print(f"[scheduler] scan_tick error: {e}")


# ============================== predict (local scan) ==============================

def predict_tick() -> None:
    """Predict matches whose begin_at is within the lead window (LOCAL only).

    Reads on-disk fixtures written by scan_tick; makes NO schedule API calls.
    For each un-predicted match starting soon, runs cmd_predict (which builds
    the context_pack on demand).
    """
    if _throttled():
        return
    try:
        if not cfg.MATCHES_DIR.exists():
            return
        now = _now()
        lead = timedelta(hours=_lead_hours())
        for mdir in sorted(cfg.MATCHES_DIR.glob("*")):
            fixture_path = mdir / "fixture.json"
            if not fixture_path.exists():
                continue
            try:
                fixture = json.loads(fixture_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                continue
            begin = _parse_dt(fixture.get("begin_at"))
            if not begin:
                continue
            # only matches starting within the lead window (and already begun)
            if not (now - timedelta(minutes=30) <= begin <= now + lead):
                continue
            if _already_predicted(fixture):
                continue
            mid = fixture.get("id")
            print(f"[scheduler] predicting match {mid} ({mdir.name}) "
                  f"starting at {fixture.get('begin_at')}")
            try:
                orch.cmd_predict(mid)
            except CitoError as e:
                _record_backoff(e)
                print(f"[scheduler] predict failed for {mid}: {e}")
    except Exception as e:  # noqa: BLE001
        print(f"[scheduler] predict_tick error: {e}")


# ============================== grade (time-gated) ==============================

def grade_tick() -> None:
    """Grade finished matches that have predictions but no results yet.

    Only asks the API for live status once a match's estimated end time has
    passed (begin_at + number_of_games × LOLA_GAME_EST_MINUTES). If still not
    finished then, retry at LOLA_GRADE_RETRY_MINUTES cadence via a marker file
    so we don't refresh every tick.
    """
    if _throttled():
        return
    try:
        if not cfg.MATCHES_DIR.exists():
            return
        client = None  # lazy-init only when we actually need a live status call
        now = _now()
        for mdir in sorted(cfg.MATCHES_DIR.glob("*")):
            fixture_path = mdir / "fixture.json"
            if not fixture_path.exists():
                continue
            fixture = json.loads(fixture_path.read_text(encoding="utf-8"))
            preds = list((mdir / "predictions").glob("*.json")) \
                if (mdir / "predictions").exists() else []
            if not preds:
                continue
            rdir = mdir / "results"
            results = [r for r in rdir.glob("*.json")
                       if not r.stem.startswith("_")] if rdir.exists() else []
            if len(results) >= len(preds):
                continue  # already graded

            mid = fixture.get("id")

            # If the local snapshot already says finished, grade right away.
            if fixture.get("status") != "finished":
                # --- time gate: don't refresh matches that haven't ended yet ---
                begin = _parse_dt(fixture.get("begin_at"))
                n_games = fixture.get("number_of_games") or 3
                est_end = (begin + timedelta(minutes=n_games * _game_est_minutes())
                           ) if begin else None
                if est_end is None or now < est_end:
                    continue  # match not estimated to be over yet
                # past the estimate: throttle re-checks to the retry cadence
                marker = rdir / "_grade_last_check.json"
                if marker.exists():
                    last_check = _parse_dt(
                        json.loads(marker.read_text(encoding="utf-8")).get("checked_at"))
                    if last_check and now < last_check + timedelta(
                            minutes=_grade_retry_minutes()):
                        continue  # checked recently; wait before re-checking

                if client is None:
                    client = get_client()
                live = None
                try:
                    live = client.match(mid, refresh=True) or {}
                except CitoError as e:
                    _record_backoff(e)
                    print(f"[scheduler] live status check failed for {mid}: {e}")
                    live = {}
                # record when we last checked, regardless of outcome
                rdir.mkdir(exist_ok=True)
                marker.write_text(
                    json.dumps({"checked_at": now.isoformat()}, indent=2),
                    encoding="utf-8")
                if live.get("status") != "finished":
                    continue  # still in progress; will retry at the cadence
                # refresh the stale local fixture so it reflects reality
                fixture_path.write_text(
                    json.dumps(live, ensure_ascii=False, indent=2), encoding="utf-8")
                fixture = live

            print(f"[scheduler] grading match {fixture.get('id')} ({mdir.name})")
            result = orch.cmd_grade(fixture["id"])
            # if grading failed (e.g. match id not in Cito / network), drop a
            # marker so we don't retry every tick and spam logs.
            if result.get("error"):
                (mdir / "results" / "_grade_error.json").write_text(
                    json.dumps({"match_id": fixture.get("id"),
                                "error": result["error"]}, indent=2),
                    encoding="utf-8")
            try:
                from ..leaderboard import build_site
                build_site.build()
            except Exception as e:  # noqa: BLE001
                print(f"[scheduler] site rebuild skipped: {e}")
    except Exception as e:  # noqa: BLE001
        print(f"[scheduler] grade_tick error: {e}")


def _scan_cron_expr() -> str:
    """Return the cron `hour` expression (e.g. "0,12") from env, validated.

    APScheduler's cron trigger takes a string expression, not a list. We parse
    into ints to validate, then re-join so e.g. "0,12, 8" -> "0,12,8".
    """
    raw = cfg.env("LOLA_SCAN_CRON_HOURS", "0,12")
    out: list[int] = []
    for part in raw.split(","):
        part = part.strip()
        if part == "":
            continue
        try:
            out.append(int(part))
        except ValueError:
            print(f"[scheduler] ignoring bad LOLA_SCAN_CRON_HOURS entry: {part!r}")
    if not out:
        return "0,12"
    return ",".join(str(h) for h in out)


def _scan_cron_hours() -> list[int]:
    """Human-readable list of scan hours (for the startup log line)."""
    return [int(p) for p in _scan_cron_expr().split(",")]


def build_scheduler() -> BackgroundScheduler:
    sched = BackgroundScheduler(timezone="UTC", daemon=True)
    sched.add_job(scan_tick, "cron", hour=_scan_cron_expr(), id="scan_tick",
                  max_instances=1, coalesce=True)
    sched.add_job(predict_tick, "interval",
                  minutes=cfg.env_int("LOLA_PREDICT_TICK_MINUTES", 15),
                  id="predict_tick", max_instances=1, coalesce=True)
    sched.add_job(grade_tick, "interval",
                  minutes=cfg.env_int("LOLA_GRADE_TICK_MINUTES", 15),
                  id="grade_tick", max_instances=1, coalesce=True)
    return sched


def run_forever() -> None:
    sched = build_scheduler()
    sched.start()
    print(f"[scheduler] started (scan @ {_scan_cron_hours()}:00 UTC, "
          f"predict every {cfg.env_int('LOLA_PREDICT_TICK_MINUTES', 15)}m, "
          f"grade every {cfg.env_int('LOLA_GRADE_TICK_MINUTES', 15)}m, "
          f"lead={_lead_hours()}h). Ctrl-C to stop.")
    try:
        while True:
            time.sleep(60)
    except (KeyboardInterrupt, SystemExit):
        sched.shutdown(wait=False)


if __name__ == "__main__":
    run_forever()

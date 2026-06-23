"""APScheduler driver.

Two repeating jobs:
  - tick (every 5 min): scan upcoming matches; for any starting within
    LOLA_PREDICT_LEAD_H hours and not yet predicted, run cmd_predict.
  - grade_tick (every 15 min): for finished matches whose predictions exist
    but no results yet, run cmd_grade.

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
from ..adapters.pandascore import PandaScoreClient
from . import orchestrator as orch
from . import collect as collect_mod


def _lead_hours() -> float:
    return float(cfg.env_int("LOLA_PREDICT_LEAD_H", 3))


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


def predict_tick() -> None:
    """Find matches within the lead window that aren't predicted yet, and predict them."""
    try:
        client = PandaScoreClient()
        league_ids = list(client.tracked_league_ids().values())
        if not league_ids:
            return
        horizon = max(_lead_hours() / 24.0 + 0.5, 1.0)
        matches = client.upcoming_matches(league_ids, horizon_days=int(horizon) + 1)
        now = _now()
        lead = timedelta(hours=_lead_hours())
        for m in matches:
            begin = _parse_dt(m.get("begin_at"))
            if not begin:
                continue
            if not (now <= begin <= now + lead + timedelta(minutes=30)):
                continue
            if _already_predicted(m):
                continue
            print(f"[scheduler] predicting match {m['id']} "
                  f"({m.get('name')}) starting at {m.get('begin_at')}")
            orch.cmd_predict(m["id"])
    except Exception as e:  # noqa: BLE001
        print(f"[scheduler] predict_tick error: {e}")


def grade_tick() -> None:
    """Grade finished matches that have predictions but no results yet."""
    try:
        for mdir in sorted(cfg.MATCHES_DIR.glob("*")) if cfg.MATCHES_DIR.exists() else []:
            fixture_path = mdir / "fixture.json"
            if not fixture_path.exists():
                continue
            fixture = json.loads(fixture_path.read_text(encoding="utf-8"))
            if fixture.get("status") != "finished":
                continue
            preds = list((mdir / "predictions").glob("*.json")) if (mdir / "predictions").exists() else []
            if not preds:
                continue
            results = list((mdir / "results").glob("*.json")) if (mdir / "results").exists() else []
            if len(results) >= len(preds):
                continue  # already graded
            print(f"[scheduler] grading match {fixture.get('id')} ({mdir.name})")
            orch.cmd_grade(fixture["id"])
            try:
                from ..leaderboard import build_site
                build_site.build()
            except Exception as e:  # noqa: BLE001
                print(f"[scheduler] site rebuild skipped: {e}")
    except Exception as e:  # noqa: BLE001
        print(f"[scheduler] grade_tick error: {e}")


def build_scheduler() -> BackgroundScheduler:
    sched = BackgroundScheduler(timezone="UTC", daemon=True)
    sched.add_job(predict_tick, "interval", minutes=5, id="predict_tick",
                  max_instances=1, coalesce=True)
    sched.add_job(grade_tick, "interval", minutes=15, id="grade_tick",
                  max_instances=1, coalesce=True)
    return sched


def run_forever() -> None:
    sched = build_scheduler()
    sched.start()
    print(f"[scheduler] started (lead={_lead_hours()}h). Ctrl-C to stop.")
    try:
        while True:
            time.sleep(60)
    except (KeyboardInterrupt, SystemExit):
        sched.shutdown(wait=False)


if __name__ == "__main__":
    run_forever()

"""CLI entry point: `python -m src <command> [args]`.

Commands:
  scan                       find upcoming tracked matches (prints a match_id list)
  collect <match_id>         build context_pack for a match
  predict <match_id>         run all models (series prediction)
  predict-game <match_id> <pos>   run all models for one game (post-BP)
  refresh-bp <match_id> <pos>     fetch BP for a game (no prediction)
  grade <match_id>           score series predictions vs truth
  grade-game <match_id> <pos>     score one game's predictions
  serve                      start FastAPI + scheduler
  build-site                 regenerate data.json for the leaderboard

Typical manual run for a future match:
python -m src scan                  # see the match_id list
python -m src predict 1397580       # run all models and refresh the leaderboard data
# open the site:  python -m src serve   ->  http://127.0.0.1:8000
"""

from __future__ import annotations

import sys

from . import config as cfg


def main(argv: list[str] | None = None) -> int:
    argv = list(argv if argv is not None else sys.argv[1:])
    if not argv or argv[0] in ("-h", "--help", "help"):
        _print_help()
        return 0

    cmd, rest = argv[0], argv[1:]
    cfg.load_env()

    if cmd == "scan":
        from .pipeline import orchestrator as orch
        orch.cmd_scan()
        return 0
    if cmd == "collect":
        _need(rest, 1, "collect <match_id>")
        from .pipeline import orchestrator as orch
        orch.cmd_collect(int(rest[0]))
        return 0
    if cmd == "predict":
        _need(rest, 1, "predict <match_id> [--models a,b]")
        models = _flag(rest, "--models")
        from .pipeline import orchestrator as orch
        orch.cmd_predict(int(rest[0]), model_ids=models)
        return 0
    if cmd == "predict-game":
        _need(rest, 2, "predict-game <match_id> <game_pos>")
        from .pipeline import orchestrator as orch
        orch.cmd_predict_game(int(rest[0]), int(rest[1]))
        return 0
    if cmd == "refresh-bp":
        _need(rest, 2, "refresh-bp <match_id> <game_pos>")
        from .pipeline import collect as collect_mod
        from .adapters.cito import CitoClient
        client = CitoClient()
        match = collect_mod.fetch_fixture(int(rest[0]), client, refresh=True)
        bp = collect_mod.fetch_game_bp(match, int(rest[1]), client, refresh=True)
        if bp is None:
            print("BP not available for that game.")
        else:
            print(f"BP complete={bp.get('bp_complete')} "
                  f"blue={len(bp['picks']['blue'])} red={len(bp['picks']['red'])}")
        return 0
    if cmd == "grade":
        _need(rest, 1, "grade <match_id>")
        from .pipeline import orchestrator as orch
        orch.cmd_grade(int(rest[0]))
        return 0
    if cmd == "grade-game":
        _need(rest, 2, "grade-game <match_id> <game_pos>")
        from .pipeline import orchestrator as orch
        orch.cmd_grade_game(int(rest[0]), int(rest[1]))
        return 0
    if cmd == "serve":
        import uvicorn
        from .pipeline.scheduler import build_scheduler
        sched = build_scheduler()
        sched.start()
        uvicorn.run("src.server.main:app", host=cfg.env("LOLA_HOST", "127.0.0.1"),
                    port=cfg.env_int("LOLA_PORT", 8000), reload=False)
        sched.shutdown(wait=False)
        return 0
    if cmd == "build-site":
        from .leaderboard import build_site
        build_site.build()
        return 0
    if cmd == "scheduler":
        from .pipeline.scheduler import run_forever
        run_forever()
        return 0

    print(f"Unknown command: {cmd}\n")
    _print_help()
    return 2


def _need(rest: list[str], n: int, usage: str) -> None:
    if len(rest) < n:
        print(f"Usage: lola {usage}")
        sys.exit(2)


def _flag(rest: list[str], name: str) -> list[str] | None:
    for i, a in enumerate(rest):
        if a == name and i + 1 < len(rest):
            return [x.strip() for x in rest[i + 1].split(",") if x.strip()]
    return None


def _print_help() -> None:
    print(__doc__)

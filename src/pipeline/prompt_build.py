"""Build the final user prompt from a context_pack (match) or BP (game).

The system prompt is the same for every model (prompts/system.md). Only the
user prompt carries the match/game specifics. Both are read fresh each run so
prompt edits take effect without a restart.
"""

from __future__ import annotations

import json
from pathlib import Path

from .. import config as cfg

PROMPTS = cfg.PROMPTS


# ----------------------------- match (series) -----------------------------

def build_match_prompt(context_pack: dict) -> tuple[str, str]:
    """Return (system_prompt, user_prompt) for a series prediction."""
    system = (PROMPTS / "system.md").read_text(encoding="utf-8")
    tpl = (PROMPTS / "task_match.md").read_text(encoding="utf-8")

    header = context_pack.get("fixture_header", {})
    user = (
        tpl.replace("{{context_pack}}", _format_json(context_pack))
           .replace("{{patch_version}}", str(header.get("patch_version") or "current"))
           .replace("{{league}}", str(header.get("league") or ""))
           .replace("{{serie}}", str(header.get("serie") or ""))
           .replace("{{blue_name}}", str((header.get("blue") or {}).get("name") or "Blue"))
           .replace("{{red_name}}", str((header.get("red") or {}).get("name") or "Red"))
    )
    return system, user


# ----------------------------- game (single, post-BP) -----------------------------

def build_game_prompt(bp: dict, match_fixture: dict, series_state: dict | None = None,
                      *, game_context: dict | None = None) -> tuple[str, str]:
    """Return (system_prompt, user_prompt) for a single-game prediction.

    bp             : the BP block from collect.fetch_game_bp
    match_fixture  : the raw match object (for names / version / games list)
    series_state   : optional {series_score_blue, series_score_red, last_game_summary}
    game_context   : optional series-level baseline subset (rosters / player_form /
                     champion pools / team_objectives) reused so models don't
                     re-search what the system already collected
    """
    system = (PROMPTS / "system.md").read_text(encoding="utf-8")
    tpl = (PROMPTS / "task_game.md").read_text(encoding="utf-8")

    opps = match_fixture.get("opponents") or []
    blue = (opps[0]["opponent"] if opps else {}).get("name", "Blue")
    red = (opps[1]["opponent"] if len(opps) > 1 else {}).get("name", "Red")
    version = (match_fixture.get("videogame_version") or {}).get("name", "current")
    total_games = match_fixture.get("number_of_games") or bp.get("total_games") or "?"

    series_context = {
        "league": (match_fixture.get("league") or {}).get("name"),
        "serie": (match_fixture.get("serie") or {}).get("full_name"),
        "blue": blue, "red": red,
        "series_score": series_state or {},
        "match_name": match_fixture.get("name"),
    }

    # picks summary with champion names for template-level search hints
    champs = []
    for side in ("blue", "red"):
        for p in (bp.get("picks") or {}).get(side, []):
            if p.get("champion"):
                champs.append(p["champion"])
    champ_hint = (champs[0] if champs else "champion")

    # Baseline already on hand: surface it to the model. An empty payload means
    # the pack was unavailable, so tell the model to fetch the basics itself.
    if game_context:
        game_context_block = _format_json(game_context)
    else:
        game_context_block = _format_json(
            {"note": "无大局基线数据，队伍/选手状态请自行用 web_search 补足"}
        )

    user = (
        tpl.replace("{{series_context}}", _format_json(series_context))
           .replace("{{game_context}}", game_context_block)
           .replace("{{bp_block}}", _format_json(bp))
           .replace("{{game_position}}", str(bp.get("position", "?")))
           .replace("{{total_games}}", str(total_games))
           .replace("{{patch_version}}", str(version))
           .replace("{{champion1}}", champ_hint)
           .replace("{{champion2}}", champs[1] if len(champs) > 1 else "opponent")
    )
    return system, user


# ----------------------------- shared -----------------------------

def _format_json(obj) -> str:
    """Pretty JSON for injection. Truncated very large blobs to protect context."""
    text = json.dumps(obj, ensure_ascii=False, indent=2)
    # Hard cap: if a context_pack is huge (many recent games), trim it.
    if len(text) > 60000:
        text = text[:60000] + "\n...[truncated]"
    return text

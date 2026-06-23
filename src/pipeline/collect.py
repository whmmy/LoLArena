"""Collect the shared context_pack for a match (and for a single game after BP).

The context_pack is the SAME for every model — fairness baseline. Models then
use the unified web_search tool themselves to go deeper.

FREE-TIER NOTE: PandaScore's free plan only allows the LIST endpoints
(/lol/matches, /upcoming, /running, /past) plus static data. Detail endpoints
(/lol/matches/{id}, /lol/teams/{id}, /lol/teams/{id}/games, /lol/games/{id})
return 403. So:
  - rosters / hero_pools: NOT available on free tier -> marked unavailable,
    models fetch via web_search.
  - recent_form: rebuilt from the FREE /lol/matches/past?filter[opponent_id]=.
  - h2h: derived from that same past-matches list.
Every block degrades gracefully (never crashes the run).

Writes:
  data/matches/<slug>/fixture.json
  data/matches/<slug>/context_pack.json
  data/games/<slug>/g<pos>/bp.json   (game BP, post-refresh)
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .. import config as cfg
from ..adapters import pandascore as ps
from ..adapters.pandascore import (
    PandaScoreClient, PandaScoreError, roster_by_role, series_score_for,
    team_side, ROLE_ORDER,
)


# ----------------------------- match (series) -----------------------------

def fetch_fixture(match_id: int, client: PandaScoreClient, *, refresh: bool = False,
                  match_obj: dict | None = None) -> dict:
    """Persist the raw match object as fixture.json and return it.

    `match_obj`: if you already have the full match (e.g. from a list call),
    pass it in to skip re-fetching. Otherwise we try the FREE list endpoints
    first (upcoming/running/past — full object included) and fall back to the
    paid /lol/matches/{id} detail endpoint only if those miss.
    """
    match = match_obj
    if match is None:
        match = client.match_from_list(match_id, refresh=refresh)
    if match is None:
        match = client.match(match_id, refresh=refresh)  # paid endpoint; may 403
    if not match:
        raise FileNotFoundError(f"PandaScore returned no match for id={match_id}")
    opps = match.get("opponents") or []
    if len(opps) < 2:
        raise ValueError(f"Match {match_id} has <2 opponents; cannot predict.")
    blue = opps[0]["opponent"]
    red = opps[1]["opponent"]
    league = (match.get("league") or {}).get("name", "LoL")
    mdir = cfg.match_dir(cfg.match_slug(league, blue["name"], red["name"], match.get("begin_at") or ""))
    (mdir / "fixture.json").write_text(
        json.dumps(match, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    match["_match_dir"] = str(mdir)  # runtime-only convenience
    return match


def collect_context_pack(match: dict, client: PandaScoreClient) -> dict:
    """Build the shared context_pack and persist it next to fixture.json.

    All sub-blocks are fault-tolerant: a 403 (free-tier limit) or any fetch
    error marks that block unavailable rather than aborting the whole pack.
    """
    policy = cfg.policy().get("context_pack", {})
    window = int(policy.get("recent_form_window", 10))
    mdir = Path(match.get("_match_dir") or _dir_for_match(match))

    opps = match.get("opponents") or []
    blue = opps[0]["opponent"]
    red = opps[1]["opponent"]
    league = match.get("league") or {}
    serie = match.get("serie") or {}
    tournament = match.get("tournament") or {}
    version = (match.get("videogame_version") or {}).get("name")

    pack: dict[str, Any] = {
        "collected_at": _now(),
        "fixture_header": _fixture_header(match, league, serie, tournament, version),
    }

    # rosters (free tier has no roster data -> marked unavailable)
    if policy.get("rosters", True):
        pack["rosters"] = {
            "blue": _roster_block(client, blue),
            "red": _roster_block(client, red),
        }

    # recent form via FREE /lol/matches/past?filter[opponent_id]=
    blue_form = red_form = None
    if policy.get("recent_form", True):
        blue_form = _recent_form(client, blue["id"], window)
        red_form = _recent_form(client, red["id"], window)
        pack["recent_form"] = {"blue": blue_form, "red": red_form}

    # h2h derived from blue's past matches that involve red
    if policy.get("h2h", True):
        pack["h2h"] = _h2h(client, blue["id"], red["id"], limit=20)

    # hero pools need paid game detail -> unavailable on free tier
    if policy.get("hero_pools", True):
        pack["hero_pools"] = {"blue": _unavailable("paid /lol/games/{id} detail"),
                              "red": _unavailable("paid /lol/games/{id} detail")}

    # meta reference (free static data)
    if policy.get("meta_reference", True):
        pack["meta_reference"] = _meta_reference(client, version)

    (mdir / "context_pack.json").write_text(
        json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return pack


def _fixture_header(match: dict, league: dict, serie: dict, tournament: dict, version) -> dict:
    opps = match.get("opponents") or []
    return {
        "match_id": match.get("id"),
        "name": match.get("name"),
        "league": league.get("name"),
        "serie": serie.get("full_name"),
        "tournament": tournament.get("name"),
        "tier": tournament.get("tier"),
        "region": tournament.get("region"),
        "stage_hint": match.get("name"),
        "match_type": match.get("match_type"),
        "number_of_games": match.get("number_of_games"),
        "begin_at_utc": match.get("begin_at") or match.get("scheduled_at"),
        "patch_version": version,
        "status": match.get("status"),
        "blue": _team_stub(opps[0]["opponent"]),
        "red": _team_stub(opps[1]["opponent"]),
    }


def _team_stub(t: dict) -> dict:
    return {
        "id": t.get("id"), "name": t.get("name"), "acronym": t.get("acronym"),
        "slug": t.get("slug"), "image_url": t.get("image_url"),
        "location": t.get("location"),
    }


def _unavailable(reason: str) -> dict:
    return {"available": False, "reason": reason,
            "hint": "Use the web_search tool to fetch this yourself."}


def _roster_block(client: PandaScoreClient, team_stub: dict) -> dict:
    """Roster needs /lol/teams/{id} (paid). Gracefully degrade."""
    try:
        team_obj = client.team(team_stub["id"]) or {}
        if not team_obj.get("players"):
            return {**_team_stub(team_stub), "players": [],
                    "available": False, "reason": "no roster in response"}
        by_role = roster_by_role(team_obj)
        players = [{"role": role, "name": by_role[role].get("name"),
                    "id": by_role[role].get("id"),
                    "nationality": by_role[role].get("nationality")}
                   for role in ROLE_ORDER if by_role.get(role)]
        return {"team": _team_stub(team_stub), "players": players, "available": bool(players)}
    except Exception as e:
        return {**_team_stub(team_stub), **_unavailable(f"{type(e).__name__}: {str(e)[:120]}")}


def _recent_form(client: PandaScoreClient, team_id: int, window: int) -> dict:
    """Last `window` finished matches for a team, via the FREE list endpoint.

    Each past-match list item already carries results[], winner, opponents, and
    a games[] stub — enough to compute W/L without any paid detail call.
    Fault-tolerant: any network error degrades to 'unavailable' so the run
    can still proceed (models fetch form via web_search).
    """
    try:
        past = client.get_all(
            "/lol/matches/past",
            {"filter[opponent_id]": team_id, "sort": "-begin_at",
             "filter[finished]": "true"},
            ttl_seconds=600, max_pages=2,
        )
    except (PandaScoreError, Exception) as e:
        return _unavailable(f"{type(e).__name__}: {str(e)[:120]}")

    items: list[dict] = []
    wins = 0
    for m in past[:window]:
        results = {r.get("team_id"): r.get("score", 0) for r in (m.get("results") or [])}
        opps = m.get("opponents") or []
        opp_name = next((o.get("opponent", {}).get("name") for o in opps
                         if o.get("opponent", {}).get("id") != team_id), "?")
        # winner from match.winner (fallback: higher score in results)
        winner_id = (m.get("winner") or {}).get("id")
        if winner_id is None and results:
            winner_id = max(results, key=results.get)
        won = winner_id == team_id
        if won:
            wins += 1
        team_score = results.get(team_id)
        opp_score = next((s for tid, s in results.items() if tid != team_id), None)
        items.append({
            "date": (m.get("begin_at") or "")[:10],
            "league": (m.get("league") or {}).get("name"),
            "opponent": opp_name,
            "score": (f"{team_score}-{opp_score}"
                      if team_score is not None and opp_score is not None else None),
            "won": won,
        })
    played = max(1, len(items))
    return {
        "available": True,
        "games_played": len(items),
        "wins": wins,
        "win_rate": round(wins / played, 3),
        "matches": items,
    }


def _h2h(client: PandaScoreClient, team_a: int, team_b: int, limit: int) -> dict:
    """Matches where team_a recently faced team_b (from team_a's past matches)."""
    try:
        past = client.get_all(
            "/lol/matches/past",
            {"filter[opponent_id]": team_a, "sort": "-begin_at"},
            ttl_seconds=600, max_pages=2,
        )
    except (PandaScoreError, Exception) as e:
        return _unavailable(f"{type(e).__name__}: {str(e)[:120]}")
    head: list[dict] = []
    for m in past[:limit]:
        opps = m.get("opponents") or []
        opp_id = next((o.get("opponent", {}).get("id") for o in opps
                       if o.get("opponent", {}).get("id") != team_a), None)
        if opp_id != team_b:
            continue
        winner_id = (m.get("winner") or {}).get("id")
        results = {r.get("team_id"): r.get("score", 0) for r in (m.get("results") or [])}
        if winner_id is None and results:
            winner_id = max(results, key=results.get)
        head.append({
            "date": (m.get("begin_at") or "")[:10],
            "league": (m.get("league") or {}).get("name"),
            "team_a_won": winner_id == team_a,
        })
    a_wins = sum(1 for h in head if h["team_a_won"])
    return {
        "available": True,
        "team_a_id": team_a, "team_b_id": team_b,
        "meetings": len(head),
        "team_a_wins": a_wins,
        "team_b_wins": len(head) - a_wins,
        "recent": head,
    }


def _meta_reference(client: PandaScoreClient, version) -> dict:
    """Current-patch champion/item counts (free static data)."""
    try:
        champs = client.meta_champions()
        items = client.meta_items()
        return {"available": True, "patch_version": version,
                "champion_count": len(champs), "item_count": len(items)}
    except (PandaScoreError, Exception) as e:
        return _unavailable(f"{type(e).__name__}: {str(e)[:120]}")


# ----------------------------- single game (BP) -----------------------------

def fetch_game_bp(match: dict, position: int, client: PandaScoreClient,
                  *, refresh: bool = False) -> dict | None:
    """Fetch one game's BP. Returns None if unavailable.

    NOTE: picks require the paid /lol/games/{id} detail endpoint, so on the free
    tier this returns bp_complete=False with a clear reason. The web UI will
    surface "BP 尚未公开" until either (a) you have a paid key, or (b) you supply
    the BP via another source.
    """
    games = match.get("games") or []
    game_stub = next((g for g in games if g.get("position") == position), None)
    if not game_stub:
        return None

    opps = match.get("opponents") or []
    blue_id = opps[0]["opponent"]["id"] if len(opps) > 0 else None
    red_id = opps[1]["opponent"]["id"] if len(opps) > 1 else None

    picks: dict[str, list[dict]] = {"blue": [], "red": []}
    try:
        detail = client.game_detail(game_stub["id"], refresh=refresh)
        for p in (detail or {}).get("players", []) or []:
            team_id = (p.get("team") or {}).get("id")
            side = "blue" if team_id == blue_id else ("red" if team_id == red_id else None)
            if not side:
                continue
            champ = (p.get("champion") or {}).get("name")
            if not champ:
                continue
            picks[side].append({
                "role": p.get("role"),
                "player": (p.get("player") or {}).get("name"),
                "champion": champ,
                "spells": [s.get("name") for s in (p.get("spells") or []) if s.get("name")],
            })
    except PandaScoreError as e:
        # free tier: detail endpoint 403 -> BP not available this way
        pass

    complete = len(picks["blue"]) >= 5 and len(picks["red"]) >= 5

    bp = {
        "match_id": match.get("id"),
        "game_id": game_stub["id"],
        "position": position,
        "status": game_stub.get("status"),
        "length_sec": game_stub.get("length"),
        "winner_id": (game_stub.get("winner") or {}).get("id"),
        "bp_complete": complete,
        "picks": picks,
        "fetched_at": _now(),
    }
    if not complete:
        bp["note"] = ("BP detail requires the paid /lol/games/{id} endpoint. "
                      "If you have a paid key it'll populate; otherwise supply BP manually.")

    gdir = cfg.game_dir(cfg.match_slug(
        (match.get("league") or {}).get("name", "LoL"),
        opps[0]["opponent"]["name"], opps[1]["opponent"]["name"],
        match.get("begin_at") or "",
    ), position)
    (gdir / "bp.json").write_text(
        json.dumps(bp, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return bp


# ----------------------------- helpers -----------------------------

def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _dir_for_match(match: dict) -> Path:
    opps = match.get("opponents") or []
    league = (match.get("league") or {}).get("name", "LoL")
    return cfg.match_dir(cfg.match_slug(
        league, opps[0]["opponent"]["name"], opps[1]["opponent"]["name"],
        match.get("begin_at") or "",
    ))

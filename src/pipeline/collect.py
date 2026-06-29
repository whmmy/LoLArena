"""Collect the shared context_pack for a match (and for a single game after BP).

The context_pack is the SAME for every model — fairness baseline. Models then
use the unified web_search tool themselves to go deeper.

DATA SOURCE: Cito API (see doc/citoapi-lol/). Unlike the PandaScore free tier,
Cito exposes (free-ish) the rich data PandaScore gates behind paid plans:
  - rosters (/teams/{slug}/roster/history)
  - per-game objective control (/teams/{slug}/objectives) -> recent_form + aggregates
  - league standings (/leagues/{id}/standings)
  - player form & champion pools (/players/{id}/form, /champion-pool)
  - single-game player stats incl. champion/side/kills (/games/{id}/stats) -> BP + grade
Every block degrades gracefully (never crashes the run); a fault marks that
block unavailable so models can fetch it themselves via web_search.

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
from ..adapters import cito
from ..adapters.cito import (
    CitoClient, CitoError, ROLE_ORDER,
)


# ----------------------------- match (series) -----------------------------

def fetch_fixture(match_id: int, client: CitoClient, *, refresh: bool = False,
                  match_obj: dict | None = None) -> dict:
    """Persist the raw (normalised) match object as fixture.json and return it.

    `match_obj`: if you already have the full match (e.g. from a scan list call),
    pass it in to skip re-fetching. Otherwise we try the cached upcoming list
    first (cheap) and fall back to the /matches/{id} detail endpoint.
    """
    match = match_obj
    if match is None:
        match = client.match_from_list(match_id, refresh=refresh)
    if match is None:
        match = client.match(match_id, refresh=refresh)
    if not match:
        raise FileNotFoundError(f"Cito returned no match for id={match_id}")
    opps = match.get("opponents") or []
    if len(opps) < 2:
        raise ValueError(f"Match {match_id} has <2 opponents; cannot predict.")
    blue = opps[0]["opponent"]
    red = opps[1]["opponent"]
    # Reuse an existing match dir if one was already created (e.g. by scan),
    # so fixture.json and context_pack.json always land in the SAME dir even
    # when the freshly-fetched detail object lacks league info and would derive
    # a different slug. Match by fixture.id (works across data sources).
    mdir = _find_existing_match_dir(match_id)
    if mdir is None:
        league = (match.get("league") or {}).get("name", "LoL")
        mdir = cfg.match_dir(cfg.match_slug(league, blue["name"], red["name"], match.get("begin_at") or ""))
    (mdir / "fixture.json").write_text(
        json.dumps(match, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    match["_match_dir"] = str(mdir)  # runtime-only convenience
    return match


def _find_existing_match_dir(match_id: int) -> Path | None:
    """Locate an existing match dir whose fixture.json id == match_id."""
    if not cfg.MATCHES_DIR.exists():
        return None
    for d in sorted(cfg.MATCHES_DIR.glob("*")):
        fp = d / "fixture.json"
        if not fp.exists():
            continue
        try:
            fx = json.loads(fp.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        if fx.get("id") == match_id:
            return d
    return None


def collect_context_pack(match: dict, client: CitoClient) -> dict:
    """Build the shared context_pack and persist it next to fixture.json.

    All sub-blocks are fault-tolerant: any fetch error marks that block
    unavailable rather than aborting the whole pack.
    """
    policy = cfg.policy().get("context_pack", {})
    window = int(policy.get("recent_form_window", 10))
    mdir = Path(match.get("_match_dir") or _dir_for_match(match))

    opps = match.get("opponents") or []
    blue = opps[0]["opponent"]
    red = opps[1]["opponent"]
    blue_slug = blue.get("id") or blue.get("slug")
    red_slug = red.get("id") or red.get("slug")
    league = match.get("league") or {}
    serie = match.get("serie") or {}
    tournament = match.get("tournament") or {}
    version = (match.get("videogame_version") or {}).get("name")
    league_id = league.get("id")  # cito leagueId, e.g. lol-lck

    pack: dict[str, Any] = {
        "collected_at": _now(),
        "fixture_header": _fixture_header(match, league, serie, tournament, version),
    }

    # rosters (now available via Cito)
    rosters = {"blue": None, "red": None}
    if policy.get("rosters", True):
        rosters["blue"] = _roster_block(client, blue_slug, blue)
        rosters["red"] = _roster_block(client, red_slug, red)
        pack["rosters"] = rosters

    # team objectives: one request per team gives BOTH recent_form (game list)
    # and the aggregated objective-control / first-objective rates.
    blue_obj = red_obj = None
    if policy.get("recent_form", True) or policy.get("team_objectives", True):
        blue_obj = _safe_objectives(client, blue_slug, window)
        red_obj = _safe_objectives(client, red_slug, window)

    if policy.get("recent_form", True):
        pack["recent_form"] = {
            "blue": _recent_form(blue_obj, blue_slug, window),
            "red": _recent_form(red_obj, red_slug, window),
        }

    # h2h derived from blue's recent games that involve red
    if policy.get("h2h", True):
        pack["h2h"] = _h2h(blue_obj, blue_slug, red_slug, limit=20)

    # aggregated objective control (new block)
    if policy.get("team_objectives", True):
        pack["team_objectives"] = {
            "blue": _team_objectives_block(blue_obj),
            "red": _team_objectives_block(red_obj),
        }

    # league standings for both teams (new block)
    if policy.get("standings", True) and league_id:
        pack["team_standings"] = _standings_block(client, league_id, blue_slug, red_slug)

    # player-level blocks (heavier on quota; policy-gated)
    player_blocks = _player_blocks(client, rosters, league_slug=league.get("slug"),
                                   policy=policy)
    if policy.get("player_form", True):
        pack["player_form"] = player_blocks["form"]
    if policy.get("player_champion_pool", True):
        pack["player_champion_pool"] = player_blocks["champion_pool"]
        # hero_pools: aggregate champion pools per side as a convenience
        pack["hero_pools"] = {
            "blue": _hero_pool_from_players(player_blocks["champion_pool"].get("blue")),
            "red": _hero_pool_from_players(player_blocks["champion_pool"].get("red")),
        }
    elif policy.get("hero_pools", True):
        # player data disabled -> hero pools unavailable
        pack["hero_pools"] = {"blue": _unavailable("player_champion_pool disabled"),
                              "red": _unavailable("player_champion_pool disabled")}

    # meta reference (patch version from the match)
    if policy.get("meta_reference", True):
        pack["meta_reference"] = _meta_reference(version)

    (mdir / "context_pack.json").write_text(
        json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return pack


def _fixture_header(match: dict, league: dict, serie: dict, tournament: dict, version) -> dict:
    opps = match.get("opponents") or []
    header = {
        "match_id": match.get("id"),
        "name": match.get("name"),
        "league": league.get("name"),
        "league_id": league.get("id"),
        "serie": serie.get("full_name") or serie.get("name"),
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
    # Cito extras (block/round/vod) if present
    if match.get("block_name"):
        header["block_name"] = match["block_name"]
    if match.get("round") is not None:
        header["round"] = match["round"]
    if match.get("vod_url"):
        header["vod_url"] = match["vod_url"]
    return header


def _team_stub(t: dict) -> dict:
    return {
        "id": t.get("id"), "name": t.get("name"), "acronym": t.get("acronym"),
        "slug": t.get("slug") or t.get("id"), "image_url": t.get("image_url"),
        "location": t.get("location"),
    }


def _unavailable(reason: str) -> dict:
    return {"available": False, "reason": reason,
            "hint": "Use the web_search tool to fetch this yourself."}


# ----------------------------- roster -----------------------------

def _roster_block(client: CitoClient, slug: str | None, team_stub: dict) -> dict:
    """Active roster for a team via /teams/{slug}/roster/history. Gracefully degrade.

    Cito's roster/history mixes main roster, academy, and loaned players, and
    its `isStarter` flag is unreliable (T1's Faker/Oner/etc. are flagged
    isStarter=False). So instead of trusting that flag, we pick ONE player per
    canonical role (top/jun/mid/adc/sup), preferring starters when a role has
    one, else the first active player in that role. This yields a clean 5-man
    lineup even when the data is messy.
    """
    if not slug:
        return {**_team_stub(team_stub), **_unavailable("no team slug")}
    try:
        players_raw = client.team_roster(slug) or []
    except (CitoError, Exception) as e:
        return {**_team_stub(team_stub), **_unavailable(f"{type(e).__name__}: {str(e)[:120]}")}
    if not players_raw:
        return {**_team_stub(team_stub), "players": [],
                "available": False, "reason": "no roster in response"}
    # group by canonical role
    by_role: dict[str, list[dict]] = {r: [] for r in ROLE_ORDER}
    for p in players_raw:
        role = p.get("role")
        if role in by_role:
            by_role[role].append(p)
    players: list[dict] = []
    for role in ROLE_ORDER:
        candidates = by_role.get(role) or []
        if not candidates:
            continue
        # prefer a starter in this role; else first candidate
        pick = next((c for c in candidates if c.get("is_starter")), candidates[0])
        players.append({"role": role, "name": pick.get("name"),
                        "id": pick.get("id"), "nationality": pick.get("nationality")})
    return {"team": _team_stub(team_stub), "players": players,
            "available": bool(players)}


# ----------------------------- team objectives / recent form -----------------------------

def _safe_objectives(client: CitoClient, slug: str | None, window: int) -> dict | None:
    if not slug:
        return None
    try:
        return client.team_objectives(slug, last=max(window, 20))
    except (CitoError, Exception) as e:
        return None


def _recent_form(obj_data: dict | None, team_slug: str | None, window: int) -> dict:
    """Last `window` games from a team's objectives payload.

    Each game row carries result/opponent/date + objective detail (kills/gold/
    dragons/barons/towers), which is richer than the old series-level form.
    """
    if not obj_data:
        return _unavailable("team_objectives unavailable")
    games = obj_data.get("games") or []
    items: list[dict] = []
    wins = 0
    for g in games[:window]:
        won = bool(g.get("won"))
        if won:
            wins += 1
        items.append({
            "date": g.get("date"),
            "league": g.get("league"),
            "opponent": g.get("opponent_slug"),
            "side": g.get("side"),
            "result": g.get("result"),
            "won": won,
            "kills": g.get("kills"),
            "opponent_kills": g.get("opponent_kills"),
            "gold": g.get("gold"),
            "dragons": g.get("dragons"),
            "barons": g.get("barons"),
            "towers": g.get("towers"),
        })
    played = max(1, len(items))
    return {
        "available": True,
        "games_played": len(items),
        "wins": wins,
        "win_rate": round(wins / played, 3) if items else None,
        "matches": items,
    }


def _team_objectives_block(obj_data: dict | None) -> dict:
    """Aggregated objective control + first-objective rates for a team."""
    if not obj_data:
        return _unavailable("team_objectives unavailable")
    oc = obj_data.get("objective_control") or {}
    fo = obj_data.get("first_objectives") or {}
    gr = obj_data.get("game_record") or {}
    # compress to a compact, model-friendly shape
    control = {}
    for k in ("dragons", "barons", "towers", "kills", "gold"):
        v = oc.get(k) or {}
        control[k] = {
            "avg_per_game": v.get("avgPerGame"),
            "opponent_avg_per_game": v.get("opponentAvgPerGame"),
            "control_rate": v.get("controlRate"),
        }
    first_obj = {}
    for k in ("blood", "tower", "dragon", "baron"):
        v = fo.get(k) or {}
        first_obj[f"first_{k}_rate"] = v.get("rate")
    return {
        "available": True,
        "games_analyzed": obj_data.get("games_analyzed"),
        "game_record": {
            "wins": gr.get("wins"), "losses": gr.get("losses"),
            "win_rate": gr.get("winRate"),
        },
        "objective_control": control,
        "first_objectives": first_obj,
    }


def _h2h(obj_data: dict | None, team_a: str | None, team_b: str | None,
         limit: int) -> dict:
    """Games where team_a recently faced team_b (from team_a's objectives)."""
    if not obj_data or not team_a or not team_b:
        return _unavailable("insufficient data for h2h")
    head: list[dict] = []
    for g in (obj_data.get("games") or [])[:limit]:
        if (g.get("opponent_slug") or "").lower() != (team_b or "").lower():
            continue
        head.append({
            "date": g.get("date"),
            "league": g.get("league"),
            "team_a_side": g.get("side"),
            "team_a_won": bool(g.get("won")),
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


# ----------------------------- standings -----------------------------

def _standings_block(client: CitoClient, league_id: str,
                     blue_slug: str | None, red_slug: str | None) -> dict:
    """Both teams' league standings (rank / W-L / win rate)."""
    try:
        rankings = client.league_standings(league_id) or []
    except (CitoError, Exception) as e:
        return _unavailable(f"{type(e).__name__}: {str(e)[:120]}")
    if not rankings:
        return _unavailable("no standings rows (new season?)")

    def _pick(slug: str | None) -> dict | None:
        if not slug:
            return None
        for r in rankings:
            if (r.get("team_slug") or "").lower() == slug.lower():
                return r
        return None

    blue = _pick(blue_slug)
    red = _pick(red_slug)
    return {
        "available": True,
        "league_id": league_id,
        "total_teams": len(rankings),
        "blue": blue,
        "red": red,
    }


# ----------------------------- player-level blocks -----------------------------

def _player_blocks(client: CitoClient, rosters: dict, *,
                   league_slug: str | None, policy: dict) -> dict:
    """Build player_form and player_champion_pool blocks for both sides.

    Expensive (one request per player x 2 endpoints x 10 players = 20 req).
    Policy-gated; any per-player error degrades to unavailable for that player.
    """
    out = {"form": {"blue": [], "red": []},
           "champion_pool": {"blue": [], "red": []}}
    if not (policy.get("player_form", True) or policy.get("player_champion_pool", True)):
        return out

    # short league slug for filtering (e.g. "lck");cito accepts league= on these
    league_short = (league_slug or "").lower()

    for side, key in (("blue", "blue"), ("red", "red")):
        side_roster = (rosters or {}).get(key) or {}
        players = side_roster.get("players") or []
        if not side_roster.get("available") or not players:
            out["form"][key] = [_unavailable("roster unavailable")]
            out["champion_pool"][key] = [_unavailable("roster unavailable")]
            continue
        for p in players:
            pid = p.get("id")
            pname = p.get("name")
            role = p.get("role")
            if policy.get("player_form", True):
                out["form"][key].append(_player_form_one(client, pid, pname, role, league_short))
            if policy.get("player_champion_pool", True):
                out["champion_pool"][key].append(
                    _player_champion_pool_one(client, pid, pname, role, league_short))
    return out


def _player_form_one(client: CitoClient, pid: str | None, pname: str | None,
                     role: str | None, league: str | None) -> dict:
    if not pid:
        return {"player": pname, "role": role, **_unavailable("no player id")}
    try:
        form = client.player_form(pid, windows="20", league=league) or {}
    except (CitoError, Exception) as e:
        return {"player": pname, "role": role,
                **_unavailable(f"{type(e).__name__}: {str(e)[:120]}")}
    windows = form.get("windows") or []
    w20 = next((w for w in windows if w.get("window") == 20), windows[0] if windows else {})
    return {
        "available": True,
        "player": pname, "role": role,
        "window": w20.get("window"),
        "games_analyzed": w20.get("gamesAnalyzed"),
        "win_rate": w20.get("winRate"),
        "avg_kda": w20.get("avgKda"),
        "avg_kills": w20.get("avgKills"),
        "avg_deaths": w20.get("avgDeaths"),
        "avg_assists": w20.get("avgAssists"),
        "avg_cs_per_min": w20.get("avgCsPerMin"),
        "avg_gold_per_min": w20.get("avgGoldPerMin"),
        "avg_damage_per_min": w20.get("avgDamagePerMin"),
        "kill_participation": w20.get("killParticipation"),
        "consistency_score": w20.get("consistencyScore"),
        "kda_variance": w20.get("kdaVariance"),
    }


def _player_champion_pool_one(client: CitoClient, pid: str | None, pname: str | None,
                              role: str | None, league: str | None) -> dict:
    if not pid:
        return {"player": pname, "role": role, **_unavailable("no player id")}
    try:
        cp = client.player_champion_pool(pid, last=14, league=league) or {}
    except (CitoError, Exception) as e:
        return {"player": pname, "role": role,
                **_unavailable(f"{type(e).__name__}: {str(e)[:120]}")}
    pool = []
    for ch in (cp.get("championPool") or [])[:6]:     # top 6 by picks
        pool.append({
            "champion": ch.get("championName"),
            "picks": ch.get("picks"),
            "wins": ch.get("wins"),
            "losses": ch.get("losses"),
            "win_rate": ch.get("winRate"),
            "pick_rate": ch.get("pickRate"),
        })
    return {
        "available": bool(pool),
        "player": pname, "role": role,
        "games_analyzed": cp.get("gamesAnalyzed"),
        "champion_pool": pool,
    }


def _hero_pool_from_players(side_champion_pools: list) -> dict:
    """Aggregate a side's player champion pools into one hero_pools block."""
    if not side_champion_pools:
        return _unavailable("no player champion pools")
    champs: dict[str, dict] = {}
    for entry in side_champion_pools:
        if not entry.get("available"):
            continue
        player = entry.get("player")
        role = entry.get("role")
        for ch in entry.get("champion_pool") or []:
            name = ch.get("champion")
            if not name:
                continue
            slot = champs.setdefault(name, {"champion": name, "picks": 0,
                                            "used_by": []})
            slot["picks"] += int(ch.get("picks") or 0)
            slot["used_by"].append({"player": player, "role": role,
                                    "win_rate": ch.get("win_rate")})
    if not champs:
        return _unavailable("empty champion pools")
    ranked = sorted(champs.values(), key=lambda c: -c["picks"])
    return {"available": True, "champions": ranked[:20]}


def _meta_reference(version) -> dict:
    """Patch version reference (Cito static champion/item counts live on hidden
    endpoints we don't call to save quota; patch version comes from the match)."""
    if not version:
        return _unavailable("no patch version in match data")
    return {"available": True, "patch_version": version}


# ----------------------------- single game (BP) -----------------------------

def fetch_game_bp(match: dict, position: int, client: CitoClient,
                  *, refresh: bool = False) -> dict | None:
    """Fetch one game's BP (and per-player kills for later grading).

    Cito's /games/{id}/stats gives champion/role/side per player on the free
    tier, so BP is now genuinely available (unlike the PandaScore paid tier).
    Returns None if the game can't be found; returns bp_complete=False if the
    detail hasn't populated yet (e.g. game not played / data pending).
    """
    games = match.get("games") or []
    # Cito games carry position == gameNumber; if absent (schedule-only match),
    # re-fetch the match detail to populate games[].
    if not games:
        match = client.match(match.get("id"), refresh=refresh) or match
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
            side = p.get("side")  # Cito gives explicit blue/red
            if not side:
                # fall back to team id matching
                tid = (p.get("team") or {}).get("id")
                side = "blue" if tid == blue_id else ("red" if tid == red_id else None)
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
    except CitoError as e:
        # data genuinely unavailable for this game
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
        bp["note"] = ("Game stats not yet available. Re-run after the game is "
                      "played or once Cito populates the /games/{id}/stats data.")

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

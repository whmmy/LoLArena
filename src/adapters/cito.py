"""Cito API LoL client.

Primary LoL data source for the system. Cito covers everything the (paid)
PandaScore tier offered — rosters, single-game BP/player stats, team objective
control, league standings, player form & champion pools — on a free-ish plan.

Design highlights (see doc/citoapi-lol/):
  - Auth: `x-api-key` request header (NOT a query token like PandaScore).
  - Multi-key pool: round-robin; 429 reads `Retry-After` and cools that key;
    403 marks it exhausted for 1h. Switches keys so a free-tier's 500/month
    quota effectively multiplies by the number of keys.
  - Response envelopes vary per endpoint (7 shapes) — `_unwrap()` normalises.
  - Responses are normalised into PandaScore-shaped match objects so the rest
    of the pipeline (collect/orchestrator/grade/leaderboard) barely changes.

ID convention (critical):
  - match_id  = Riot `officialEventId` (bare numeric string), stored as int.
    CLI/scheduler/fixtures use int match_id, so this stays compatible.
  - team_id   = Cito team slug (e.g. "t1"/"gen"/"dcg"). opponents[].opponent.id,
    results[].team_id and winner.id all use the slug so the existing `==`
    comparisons (blue/red side, score mapping, winner detection) work as-is.

Auth keys come from CITO_API_KEYS (comma-separated) or CITO_API_KEY (single).
Base URL from CITO_BASE_URL (default https://api.citoapi.com), all LoL endpoints
live under /api/v1.
"""

from __future__ import annotations

import functools
import hashlib
import json
import threading
import time
from pathlib import Path
from typing import Any

import httpx

from .. import config as cfg

# Roles in canonical order (top/jungle/mid/adc/support) — kept identical to the
# pandascore module so collect.py's ROLE_ORDER usage is unchanged.
ROLE_ORDER = ["top", "jun", "mid", "adc", "sup"]

# Map Cito role spellings -> our canonical short role keys.
# Cito uses TOP/JUG/MID/BOT/SUP (roster) and Top/Jungle/Mid/ADC/Support (stats).
_ROLE_MAP = {
    "top": "top", "TOP": "top", "Top": "top",
    "jungle": "jun", "Jungle": "jun", "JUNGLE": "jun", "jung": "jun", "JUNG": "jun",
    "jug": "jun", "JUG": "jun",
    "mid": "mid", "MID": "mid", "Mid": "mid", "Middle": "mid", "middle": "mid",
    "adc": "adc", "ADC": "adc", "Adc": "adc",
    "bot": "adc", "BOT": "adc", "Bot": "adc",
    "bottom": "adc", "Bottom": "adc", "BOTTOM": "adc",
    "support": "sup", "SUP": "sup", "Support": "sup", "SUPPORT": "sup",
    "sup": "sup", "Sup": "sup",
}


class CitoError(RuntimeError):
    pass


# ============================== key pool ==============================

class CitoKeyPool:
    """Round-robin pool of API keys with per-key cooldown for rate-limit/quota.

    - 429: key is "rate limited" for `retry_after` seconds (fallback 60s).
    - 403: key is "exhausted" (quota hit) for 1 hour.
    On `next_key()` we skip keys still in cooldown; if ALL are cooling down we
    return the one with the soonest unlock (so the caller can wait or fail).
    """

    EXHAUSTED_COOLDOWN = 3600.0       # 403 / quota: cool 1h
    DEFAULT_RETRY_AFTER = 60.0        # 429 without Retry-After header

    def __init__(self, keys: list[str]):
        # de-dup while keeping order, drop empties
        seen: set[str] = set()
        self.keys = [k for k in keys if k and not (k in seen or seen.add(k))]
        if not self.keys:
            raise CitoError(
                "No Cito API keys configured. Set CITO_API_KEYS (comma-separated) "
                "or CITO_API_KEY in .env."
            )
        self._rate_until: dict[str, float] = {k: 0.0 for k in self.keys}
        self._idx = 0
        self._lock = threading.Lock()

    def __len__(self) -> int:
        return len(self.keys)

    def next_key(self) -> str:
        """Return an available key (round-robin), or the soonest-unlocking one."""
        with self._lock:
            now = time.time()
            # first pass: find an unlocked key, rotating from current idx
            n = len(self.keys)
            for offset in range(n):
                k = self.keys[(self._idx + offset) % n]
                if now >= self._rate_until[k]:
                    self._idx = (self._idx + offset + 1) % n
                    return k
            # all cooling: return the one that unlocks soonest (caller decides)
            return min(self.keys, key=lambda k: self._rate_until[k])

    def mark_rate_limited(self, key: str, retry_after: float | None) -> None:
        with self._lock:
            self._rate_until[key] = time.time() + (
                retry_after if retry_after and retry_after > 0 else self.DEFAULT_RETRY_AFTER)

    def mark_exhausted(self, key: str) -> None:
        with self._lock:
            self._rate_until[key] = time.time() + self.EXHAUSTED_COOLDOWN

    def throttled_until(self) -> float:
        """When the soonest-unlocking key becomes available again.

        Returns 0.0 if at least one key is free right now, else the earliest
        unlock time (epoch seconds). Lets callers back off without re-firing.
        """
        with self._lock:
            now = time.time()
            soonest = min(self._rate_until[k] for k in self.keys)
            return 0.0 if soonest <= now else soonest


def _load_keys() -> list[str]:
    """Read keys from CITO_API_KEYS (comma-separated) or CITO_API_KEY."""
    cfg.load_env()
    multi = cfg.env("CITO_API_KEYS")
    if multi:
        return [k.strip() for k in multi.split(",") if k.strip()]
    single = cfg.env("CITO_API_KEY")
    return [single] if single else []


@functools.lru_cache(maxsize=1)
def get_client() -> CitoClient:
    """Process-wide shared CitoClient (and thus shared key-pool cooldown state).

    `_raw_get` builds a fresh `httpx.Client` per request, so this is safe to
    share across threads/scheduler ticks; the only shared mutable state is the
    locked `key_pool`. Sharing it means a 429 cooldown set by one caller (e.g.
    a bursty `cmd_predict`) is honoured by every other caller (scheduler ticks,
    server refresh) instead of being forgotten because each built its own pool.
    """
    return CitoClient()


def is_rate_limited_error(exc: BaseException) -> bool:
    """True if a CitoError was raised due to rate-limiting (429)."""
    return isinstance(exc, CitoError) and "429" in str(exc)


# ============================== client ==============================

class CitoClient:
    def __init__(self, api_keys: list[str] | None = None, base_url: str | None = None,
                 cache_dir: Path | None = None, timeout: float = 30.0,
                 proxy: str | None = None):
        cfg.load_env()
        keys = api_keys or _load_keys()
        self.key_pool = CitoKeyPool(keys)
        base = (base_url or cfg.env("CITO_BASE_URL")
                or "https://api.citoapi.com").rstrip("/")
        # Cito LoL endpoints all live under /api/v1
        if not base.endswith("/api/v1"):
            base = base.rstrip("/") + "/api/v1"
        self.base_url = base
        self.cache_dir = cache_dir or (cfg.DATA / "_cito_cache")
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.timeout = timeout
        # proxy: explicit arg wins, else read proxies.yaml / env
        self.proxy = proxy if proxy is not None else cfg.proxy_for("cito")

    def throttled_until(self) -> float:
        """Pass-through to the key pool: when the soonest key unlocks (0.0 = free)."""
        return self.key_pool.throttled_until()

    # ---------- core request w/ disk cache + key rotation ----------
    def _cache_path(self, path: str, params: dict[str, Any]) -> Path:
        # NB: deliberately exclude the api key from the cache key (unlike
        # PandaScore) so swapping/rotating keys doesn't invalidate the cache.
        key = hashlib.sha1(
            f"{path}|{json.dumps(params, sort_keys=True)}".encode()
        ).hexdigest()[:16]
        slug = path.strip("/").replace("/", "__")
        return self.cache_dir / f"{slug}__{key}.json"

    def get(self, path: str, params: dict[str, Any] | None = None,
            *, ttl_seconds: float | None = None, refresh: bool = False) -> Any:
        """GET a Cito endpoint, returning the UNWRAPPED payload.

        Handles disk cache + key rotation across rate-limit/quota errors.
        Returns None on 404. Raises CitoError on other failures once all keys
        are exhausted.
        """
        params = dict(params or {})
        cpath = self._cache_path(path, params)

        if not refresh and cpath.exists():
            if ttl_seconds is None or (time.time() - cpath.stat().st_mtime) < ttl_seconds:
                return json.loads(cpath.read_text(encoding="utf-8"))

        tried: set[str] = set()
        last_err: str | None = None
        for _ in range(len(self.key_pool)):
            key = self.key_pool.next_key()
            if key in tried:
                # all keys already attempted in this loop — wait/short-circuit
                break
            tried.add(key)
            status, body_text, retry_after = self._raw_get(path, params, key)
            if status == 429:
                self.key_pool.mark_rate_limited(key, retry_after)
                last_err = f"429 rate-limited key {key[:12]}…"
                continue
            if status == 403:
                self.key_pool.mark_exhausted(key)
                last_err = f"403 quota/forbidden key {key[:12]}…"
                continue
            if status == 404:
                return None
            if status >= 400:
                raise CitoError(f"Cito {status} for {path}: {body_text[:300]}")
            # success
            data = json.loads(body_text)
            unwrapped = self._unwrap(path, data)
            cpath.write_text(json.dumps(unwrapped, ensure_ascii=False, indent=2),
                             encoding="utf-8")
            return unwrapped
        raise CitoError(f"Cito request failed for {path} after trying "
                        f"{len(tried)} key(s). Last: {last_err}")

    def _raw_get(self, path: str, params: dict[str, Any], key: str
                 ) -> tuple[int, str, float | None]:
        """Single HTTP GET with one key. Returns (status, text, retry_after_seconds)."""
        url = f"{self.base_url}{path}"
        client_kwargs = {"timeout": self.timeout}
        if self.proxy:
            client_kwargs["proxy"] = self.proxy
        with httpx.Client(**client_kwargs) as client:
            resp = client.get(url, params=params, headers={"x-api-key": key})
        retry_after: float | None = None
        ra = resp.headers.get("Retry-After") or resp.headers.get("retry-after")
        if ra:
            try:
                retry_after = float(ra)
            except ValueError:
                retry_after = None
        return resp.status_code, resp.text, retry_after

    # ---------- response envelope unwrapping ----------
    def _unwrap(self, path: str, data: Any) -> Any:
        """Strip the 7 Cito response shapes and return the payload.

        The cache stores the UNWRAPPED payload so callers see a consistent
        shape (list or object) regardless of envelope. Heuristics:
          - list -> list
          - {value:[...]} (wrapper F, note capital Count) -> value
          - {data:[...]} / {data:{...}} (wrappers C/D/E) -> data
          - {player, windows/championPool} (form/champion-pool composite) -> as-is
          - {gameId, section, data} (wrapper G) -> data
          - bare object -> as-is
        """
        if isinstance(data, list):
            return data
        if not isinstance(data, dict):
            return data
        # wrapper F: matches/{id}/games, transfers — {"value":[...], "Count":N}
        if "value" in data and ("Count" in data or "meta" in data):
            return data["value"]
        # wrapper G: games/{id}/plates|distributions|vision|jungle-share
        if {"gameId", "section", "data"} <= set(data):
            return data.get("data")
        # composite wrappers (kept whole — callers consume their inner structure):
        #   players/{id}/form, players/{id}/champion-pool
        if "player" in data and ("windows" in data or "championPool" in data):
            return data
        #   teams/{slug}/objectives  {team, gameRecord, objectiveControl, games:[...]}
        if "team" in data and "games" in data:
            return data
        #   leagues/{id}/schedule  {leagueId, events:[...], pages}
        if "events" in data and "leagueId" in data:
            return data["events"]
        #   teams/{slug}/roster/history  {roster:[...]}
        if "roster" in data:
            return data["roster"]
        # wrappers C/D/E: {success, [status,] [count,] data, ...}
        if "data" in data:
            return data["data"]
        # bare object (wrapper B: matches/{id}, players/{id}/stats, games/{id})
        return data

    # ---------- paginated list helper ----------
    def get_list(self, path: str, params: dict[str, Any] | None = None,
                 *, max_pages: int = 5, per_page: int = 100,
                 ttl_seconds: float | None = None) -> list[dict[str, Any]]:
        """Auto-paginate a list endpoint (capped at max_pages)."""
        params = dict(params or {})
        out: list[dict[str, Any]] = []
        for page in range(1, max_pages + 1):
            batch = self.get(path, {**params, "page": page, "limit": per_page},
                             ttl_seconds=ttl_seconds) or []
            if not isinstance(batch, list):
                break
            out.extend(batch)
            if len(batch) < per_page:
                break
        return out

    # ============================== high-level LoL helpers ==============================
    # Method names mirror PandaScoreClient where possible to minimise churn in
    # the pipeline modules.

    def tracked_league_ids(self) -> dict[str, str]:
        """Map our leagues.yaml names -> Cito leagueId (e.g. "LCK" -> "lol-lck").

        If a league entry has an explicit `cito_league_id`, trust it directly.
        Otherwise fall back to matching `slug` against /lol/leagues.
        """
        leagues_cfg = cfg.leagues_cfg()
        entries = leagues_cfg.get("leagues", []) or []
        mapping: dict[str, str] = {}

        need_slug_lookup: list[dict] = []
        for l in entries:
            cid = l.get("cito_league_id")
            if cid:
                mapping[l["name"]] = cid
            else:
                need_slug_lookup.append(l)

        if need_slug_lookup:
            # Cito short slugs (lck/lpl) for the few aliases that exist; full
            # lol-<slug> otherwise. Match against either.
            wanted: dict[str, str] = {}
            for l in need_slug_lookup:
                slug = (l.get("cito_slug") or l.get("slug") or "").lower()
                # strip a possible "league-of-legends-" panda prefix just in case
                slug = slug.replace("league-of-legends-", "")
                if slug:
                    wanted[slug] = l["name"]
            all_leagues = self.get("/lol/leagues", ttl_seconds=86400) or []
            for lg in all_leagues:
                cid = lg.get("leagueId") or ""
                short = (lg.get("slug") or "").lower()
                # match by either the full lol-<slug> or the short slug
                if cid in wanted:
                    mapping[wanted[cid]] = cid
                elif short and short in wanted:
                    mapping[wanted[short]] = cid
            missing = [n for n in wanted.values() if n not in mapping]
            if missing:
                print(f"[cito] WARNING: no cito_league_id for {missing}. "
                      f"Add cito_league_id to configs/leagues.yaml.")
        return mapping

    def upcoming_matches(self, league_ids: list[str], *, horizon_days: int = 14) -> list[dict]:
        """Upcoming matches for tracked leagues within horizon_days, normalised.

        Uses the per-league schedule endpoint (/lol/leagues/{id}/schedule) which
        is the reliable source — the global /lol/schedule/upcoming endpoint has
        been observed returning empty even when per-league schedules have
        upcoming matches. One cached request per league.
        """
        from datetime import datetime, timedelta, timezone

        now = datetime.now(timezone.utc)
        end = now + timedelta(days=horizon_days)
        uniq: list[dict] = []
        seen: set[int] = set()
        for lid in league_ids:
            raw = self.get(f"/lol/leagues/{lid}/schedule",
                           ttl_seconds=cfg.env_int("LOLA_CITO_SCHEDULE_TTL", 3600))
            # the cached payload may be the inner {leagueId, events:[...]} object
            # (unwrap strips the outer {success, data}) OR a bare events list.
            events = raw.get("events") if isinstance(raw, dict) else raw
            if not isinstance(events, list):
                continue
            for item in events:
                # only future / in-progress matches
                if item.get("state") not in ("unstarted", "inProgress"):
                    continue
                # skip bracket slots whose opponents aren't decided yet (TBD)
                teams = item.get("teams") or []
                names = [(t or {}).get("name", "") for t in teams] or [
                    (item.get("team1") or {}).get("name", ""),
                    (item.get("team2") or {}).get("name", "")]
                if any(not n or str(n).strip().upper() == "TBD" for n in names):
                    continue
                start = item.get("startTime")
                state = item.get("state")
                if start:
                    try:
                        dt = datetime.fromisoformat(start.replace("Z", "+00:00"))
                    except ValueError:
                        dt = None
                    if dt:
                        # upcoming matches must start within the horizon window.
                        # In-progress matches started in the past but are still
                        # live — keep them so they can be predicted/graded.
                        if state == "unstarted" and not (now <= dt <= end):
                            continue
                        if state == "inProgress" and dt > end:
                            continue
                m = _norm_match_from_schedule(item)
                mid = m.get("id")
                if mid is None or mid in seen:
                    continue
                seen.add(mid)
                uniq.append(m)
        uniq.sort(key=lambda m: m.get("begin_at") or "")
        return uniq

    def match(self, match_id: int, *, refresh: bool = False) -> dict | None:
        """Single-match detail, normalised to PandaScore shape (with games[]).

        Combines /lol/matches/{id} (metadata + scores) with /lol/matches/{id}/games
        (per-game stubs incl. winner/duration). ID accepts bare numeric or
        lol-match-<num>; we pass through whatever the caller gave us.
        """
        mid = str(match_id)
        meta = self.get(f"/lol/matches/{mid}", refresh=refresh, ttl_seconds=300)
        if not meta or not isinstance(meta, dict):
            return None
        games_raw = self.get(f"/lol/matches/{mid}/games", refresh=refresh, ttl_seconds=300)
        games = [_norm_game(g) for g in (games_raw or []) if isinstance(g, dict)]
        return _norm_match_from_detail(meta, games)

    def match_games(self, match_id: int, *, refresh: bool = False) -> list[dict]:
        """Per-game stubs for a match (normalised)."""
        mid = str(match_id)
        raw = self.get(f"/lol/matches/{mid}/games", refresh=refresh, ttl_seconds=300) or []
        return [_norm_game(g) for g in raw if isinstance(g, dict)]

    def match_from_list(self, match_id: int, *, refresh: bool = False) -> dict | None:
        """Fetch a match by id. Cito's /lol/matches/{id} detail endpoint accepts
        any match id directly (bare numeric or lol-match-<num>), so we just use
        it — no need for the PandaScore list-endpoint trick."""
        return self.match(match_id, refresh=refresh)

    # ---------- teams ----------
    def team_roster(self, slug: str, *, refresh: bool = False) -> list[dict]:
        """Current active roster for a team, normalised.

        Endpoint /lol/teams/{slug}/roster/history returns {roster:[...]} (every
        tenure, current + historical). We keep players currently on the team
        (leaveDate is null, isActive true) and prefer starters. Cito role names
        seen in the wild: TOP/JUG/MID/BOT/SUP and Support/Jungle/... full names.
        """
        raw = self.get(f"/lol/teams/{slug}/roster/history",
                       refresh=refresh, ttl_seconds=3600)
        rows = raw if isinstance(raw, list) else []
        active: list[dict] = []
        seen: set[str] = set()
        for r in rows:
            if r.get("leaveDate"):
                continue
            pid = r.get("lolPlayerId") or r.get("playerName")
            if pid in seen:
                continue
            seen.add(pid)
            p = r.get("player") or {}
            active.append({
                "id": r.get("lolPlayerId") or p.get("lolPlayerId"),
                "name": r.get("playerName") or p.get("currentIgn"),
                "real_name": r.get("realName") or p.get("realName"),
                "nationality": p.get("nationality"),
                "role": _ROLE_MAP.get(r.get("role", ""), (r.get("role") or "").lower()),
                "role_raw": r.get("role"),
                "is_starter": r.get("isStarter"),
                "image_url": r.get("logoUrl") or r.get("imageUrl") or p.get("imageUrl"),
            })
        return active

    def team_objectives(self, slug: str, *, last: int = 20, league: str | None = None,
                        refresh: bool = False) -> dict:
        """Recent objective control for a team.

        Returns a composite dict with BOTH the aggregated control rates AND the
        per-game list, so callers can build recent_form AND team_objectives
        blocks from one request:
            {
              "team": {...},
              "game_record": {"wins","losses","win_rate"},          # overall W/L
              "objective_control": {                                 # per-game avg
                  "dragons": {"avg_per_game","control_rate",...}, ...
              },
              "first_objectives": {"blood":{"rate"}, "tower":..., ...},
              "games": [ {date, opponent, side, result, kills, gold, dragons, ...}, ... ]
            }
        """
        params: dict[str, Any] = {"last": last}
        if league:
            params["league"] = league
        raw = self.get(f"/lol/teams/{slug}/objectives", params,
                       refresh=refresh, ttl_seconds=1800)
        if not isinstance(raw, dict):
            return {"team": {"slug": slug}, "game_record": {}, "games": []}
        games_in = raw.get("games") or []
        games: list[dict] = []
        for r in games_in:
            obj = r.get("objectives") or {}
            games.append({
                "match_id": _match_id_value(r),
                "game_id": _game_id_value(r),
                "game_number": r.get("gameNumber"),
                "date": (r.get("startTime") or "")[:10],
                "start_time": r.get("startTime"),
                "league": r.get("league"),
                "tournament": r.get("tournamentName"),
                "opponent_slug": r.get("opponentSlug"),
                "side": r.get("side"),                  # blue/red (this team's side)
                "result": r.get("result"),              # win/loss
                "won": str(r.get("result")).lower() == "win",
                "kills": obj.get("kills"),
                "opponent_kills": obj.get("opponentKills"),
                "gold": obj.get("gold"),
                "towers": obj.get("towers"),
                "dragons": obj.get("dragons"),
                "barons": obj.get("barons"),
                "first_blood": obj.get("firstBlood"),
                "first_tower": obj.get("firstTower"),
                "first_dragon": obj.get("firstDragon"),
                "first_baron": obj.get("firstBaron"),
            })
        return {
            "team": raw.get("team") or {"slug": slug},
            "games_analyzed": raw.get("gamesAnalyzed"),
            "matches_analyzed": raw.get("matchesAnalyzed"),
            "game_record": raw.get("gameRecord") or {},
            "objective_control": raw.get("objectiveControl") or {},
            "first_objectives": raw.get("firstObjectives") or {},
            "games": games,
        }

    def team_h2h(self, slug: str, opponent_slug: str, *, refresh: bool = False) -> dict | None:
        """Head-to-head between two teams. Hidden endpoint — structure may vary;
        returns the unwrapped payload as-is (caller adapts)."""
        return self.get(f"/lol/teams/{slug}/h2h/{opponent_slug}",
                        refresh=refresh, ttl_seconds=1800)

    def team_series_history(self, slug: str, *, last: int = 25,
                            league: str | None = None,
                            refresh: bool = False) -> dict:
        """Recent SERIES history for a team — the only place we can get per-game
        `duration` (seconds) and the actual series scoreline.

        `/teams/{slug}/objectives` has kills/gold/objectives but NO duration, so
        duration prediction had no anchor. This endpoint returns completed series
        with games[] carrying `duration` (seconds, may be null for very recent
        matches not yet back-filled) plus team1.score/team2.score (the series
        scoreline) — giving us BOTH the duration anchor and the sweep/series-length
        anchor for match-level scoring.

        Normalised shape (fault-tolerant; never raises):
            {
              "available": bool,
              "recent_series": [ {
                  "date, opponent_slug, side, result(won/lost),
                  team_score, opponent_score, series_length,
                  games: [ {game_number, duration_min, won} ]   # duration_min nullable
              }, ... ],
              # aggregated anchors the prompt can cite directly:
              "avg_game_duration_min": float | None,
              "avg_series_length": float | None,
              "sweep_rate": float | None,        # fraction of series won 2-0 / 3-0
              "swept_rate": float | None,        # fraction this team was swept (lost 0-2/0-3)
            }
        """
        params: dict[str, Any] = {"last": last}
        if league:
            params["league"] = league
        try:
            raw = self.get(f"/lol/teams/{slug}/matches", params,
                           refresh=refresh, ttl_seconds=3600)
        except Exception:
            return {"available": False, "recent_series": []}
        if not isinstance(raw, dict):
            return {"available": False, "recent_series": []}

        is_requested = lambda team_obj: bool(team_obj.get("isRequested"))
        series: list[dict] = []
        durations: list[float] = []
        series_lens: list[int] = []
        sweeps = 0           # this team won 2-0 / 3-0 / etc.
        swept = 0            # this team lost 0-2 / 0-3 / etc.
        decided = 0
        for m in raw.get("matches") or []:
            if m.get("state") != "completed":
                continue
            t1, t2 = m.get("team1") or {}, m.get("team2") or {}
            # identify which side is `slug` (this team). Cito marks the requested
            # team with isRequested=true; else match by slug.
            if is_requested(t1) or t1.get("slug") == slug:
                us, them = t1, t2
                side = "blue"
            elif is_requested(t2) or t2.get("slug") == slug:
                us, them = t2, t1
                side = "red"
            else:
                continue
            our_score = int(us.get("score") or 0)
            opp_score = int(them.get("score") or 0)
            won = our_score > opp_score
            slen = our_score + opp_score
            games: list[dict] = []
            for g in m.get("games") or []:
                dur = g.get("duration")
                dur_min = round(dur / 60.0, 1) if isinstance(dur, (int, float)) and dur > 0 else None
                if dur_min:
                    durations.append(dur_min)
                g_winner = g.get("winnerSlug")
                games.append({
                    "game_number": g.get("gameNumber"),
                    "duration_min": dur_min,
                    "won": (g_winner == slug) if g_winner else None,
                })
            series.append({
                "date": (m.get("startTime") or "")[:10],
                "league": m.get("tournamentName") or m.get("tournamentId"),
                "opponent_slug": them.get("slug"),
                "side": side,
                "result": "win" if won else "loss",
                "team_score": our_score,
                "opponent_score": opp_score,
                "series_length": slen,
                "games": games,
            })
            if slen:
                series_lens.append(slen)
                decided += 1
                # sweep: winner took it without dropping a game
                if our_score > 0 and opp_score == 0:
                    sweeps += 1
                elif opp_score > 0 and our_score == 0:
                    swept += 1

        avg_dur = round(sum(durations) / len(durations), 1) if durations else None
        avg_len = round(sum(series_lens) / len(series_lens), 1) if series_lens else None
        return {
            "available": bool(series),
            "series_count": len(series),
            "games_with_duration": len(durations),
            "avg_game_duration_min": avg_dur,
            "avg_series_length": avg_len,
            "sweep_rate": round(sweeps / decided, 3) if decided else None,
            "swept_rate": round(swept / decided, 3) if decided else None,
            "recent_series": series,
        }

    # ---------- standings ----------
    def league_standings(self, league_id: str, *, refresh: bool = False) -> list[dict]:
        """League standings (rankings[]), normalised. Returns [] if unavailable."""
        payload = self.get(f"/lol/leagues/{league_id}/standings",
                           refresh=refresh, ttl_seconds=3600)
        # _unwrap already drilled into data for wrapper D, so payload is the
        # inner object {leagueId, rankings:[...]} (or already the list).
        if isinstance(payload, list):
            rankings = payload
        elif isinstance(payload, dict):
            rankings = payload.get("rankings") or []
        else:
            rankings = []
        out: list[dict] = []
        for r in rankings:
            out.append({
                "rank": r.get("rank"),
                "team_slug": r.get("orgSlug"),
                "team_name": r.get("teamName"),
                "wins": r.get("wins"),
                "losses": r.get("losses"),
                "win_rate": r.get("winRate"),
                "game_wins": r.get("gameWins"),
                "game_losses": r.get("gameLosses"),
                "game_win_rate": r.get("gameWinRate"),
            })
        return out

    # ---------- players ----------
    def player_form(self, player_id: str, *, windows: str = "10,20",
                    league: str | None = None, refresh: bool = False) -> dict | None:
        """Player sliding-window form. Returns {player, windows:[...]} as-is."""
        params: dict[str, Any] = {"windows": windows}
        if league:
            params["league"] = league
        return self.get(f"/lol/players/{player_id}/form", params,
                        refresh=refresh, ttl_seconds=3600)

    def player_champion_pool(self, player_id: str, *, last: int = 14,
                             league: str | None = None, refresh: bool = False) -> dict | None:
        """Player champion pool + picks detail. Returns {player, championPool, picks}."""
        params: dict[str, Any] = {"last": last}
        if league:
            params["league"] = league
        return self.get(f"/lol/players/{player_id}/champion-pool", params,
                        refresh=refresh, ttl_seconds=3600)

    # ---------- single game ----------
    def game_detail(self, game_id: str | int, *, refresh: bool = False) -> dict | None:
        """Per-game player stats, normalised to PandaScore game_detail shape.

        Combines what BP and grade both need: champion/role/side/spells (BP)
        and kills (grade truth). Source endpoint /lol/games/{id}/stats returns
        {value:[...per-player rows...], meta}.
        """
        gid = str(game_id)
        rows = self.get(f"/lol/games/{gid}/stats", refresh=refresh, ttl_seconds=None) or []
        if not isinstance(rows, list) or not rows:
            # fall back to the games list endpoint (less detail but has winner)
            game_meta = self.get(f"/lol/games/{gid}", refresh=refresh, ttl_seconds=600)
            if isinstance(game_meta, dict):
                return _norm_game(game_meta)
            return None
        players: list[dict] = []
        for p in rows:
            side = str(p.get("side") or "").lower()           # blue/red
            champ = p.get("championName") or p.get("champion")
            team_slug = (p.get("team") or {}).get("slug") or p.get("teamSlug")
            role = _ROLE_MAP.get(p.get("role") or p.get("position") or "", "")
            spells = []
            s1, s2 = p.get("summonerSpell1"), p.get("summonerSpell2")
            if s1:
                spells.append(s1)
            if s2:
                spells.append(s2)
            players.append({
                "team": {"id": team_slug, "name": p.get("teamName"),
                         "slug": team_slug},
                "side": side,
                "role": role,
                "player": {"name": p.get("playerName") or (p.get("player") or {}).get("currentIgn"),
                           "id": (p.get("player") or {}).get("lolPlayerId")},
                "champion": {"name": champ},
                "spells": [{"name": s} for s in spells],
                "kills": int(p.get("kills") or 0),
                "deaths": int(p.get("deaths") or 0),
                "assists": int(p.get("assists") or 0),
                "stats_status": p.get("statsStatus"),
            })
        return {"players": players, "_source": "games/stats"}


# ============================== normalisation helpers ==============================
# These translate Cito field names into the PandaScore-shaped match object the
# rest of the pipeline already understands (opponents[0]=blue/[1]=red,
# results[].team_id, winner.id, games[].position/length/winner).

_STATE_MAP = {
    "unstarted": "not_started",
    "inprogress": "running",
    "completed": "finished",
}


def _state_map(state: str | None) -> str | None:
    if not state:
        return None
    return _STATE_MAP.get(state.lower(), state.lower())


def _match_id_value(obj: dict) -> int | None:
    """Pull a bare numeric match id from any of Cito's id fields."""
    for k in ("officialEventId", "esportsApiId", "matchId"):
        v = obj.get(k)
        if v is None:
            continue
        s = str(v)
        # strip a possible lol-match- prefix
        if s.startswith("lol-match-"):
            s = s[len("lol-match-"):]
        try:
            return int(s)
        except ValueError:
            continue
    return None


def _game_id_value(obj: dict) -> str | None:
    """Pull a game id (string, may keep lol-game- prefix — /games/{id} accepts both)."""
    gid = obj.get("gameId") or obj.get("esportsApiId")
    if gid is None:
        return None
    return str(gid)


def _team_stub(team_obj: dict, *, score_key: str = "score") -> dict:
    """Normalise a Cito team object (team1/team2/teams[]) into our team stub."""
    if not isinstance(team_obj, dict):
        return {}
    return {
        "id": team_obj.get("slug"),                       # slug = our team_id
        "name": team_obj.get("name"),
        "acronym": team_obj.get("code") or team_obj.get("shortName"),
        "slug": team_obj.get("slug"),
        "image_url": team_obj.get("logoUrl") or team_obj.get("imageUrl"),
    }


def _norm_match_from_schedule(item: dict) -> dict:
    """Normalise a schedule entry to PandaScore match shape.

    Handles BOTH team shapes Cito uses across schedule endpoints:
      - /lol/schedule/upcoming      -> team1/team2 (two objects), strategy "Bo5"
      - /lol/schedule/today         -> teams:[t1,t2] array, strategy {type,count}
      - /lol/leagues/{id}/schedule  -> teams:[t1,t2] array, strategy {type,count}
    """
    mid = _match_id_value(item)
    # resolve the two team objects regardless of shape
    if item.get("team1") or item.get("team2"):
        t1, t2 = item.get("team1") or {}, item.get("team2") or {}
    else:
        teams = item.get("teams") or []
        t1, t2 = (teams[0] if len(teams) > 0 else {}), (teams[1] if len(teams) > 1 else {})
    blue = _team_stub(t1)
    red = _team_stub(t2)
    bo = _parse_bo(item.get("strategy"))
    league_obj = {
        "id": item.get("leagueId"),
        "name": item.get("leagueName"),
        "slug": item.get("leagueSlug"),
    }
    tournament_obj = {
        "id": item.get("tournamentId"),
        "name": item.get("tournamentName"),
    }
    winner_slug = item.get("winnerSlug")
    results = [
        {"team_id": blue.get("id"), "score": t1.get("score", 0)},
        {"team_id": red.get("id"), "score": t2.get("score", 0)},
    ]
    return {
        "id": mid,
        "name": f"{blue.get('name','?')} vs {red.get('name','?')}",
        "match_type": None,
        "status": _state_map(item.get("state")),
        "number_of_games": bo,
        "begin_at": item.get("startTime"),
        "scheduled_at": item.get("startTime"),
        "end_at": item.get("endTime"),
        "winner_id": winner_slug,
        "winner": {"id": winner_slug, "type": "Team"} if winner_slug else None,
        "draw": False,
        "forfeit": False,
        "opponents": [{"opponent": blue}, {"opponent": red}],
        "results": results,
        "league": league_obj,
        "serie": {},
        "tournament": tournament_obj,
        "games": [],
        "videogame_version": {},
        # Cito-specific extras (useful for fixture_header enrichment)
        "block_name": item.get("blockName"),
        "round": item.get("round"),
        "vod_url": None,
    }


def _norm_match_from_detail(meta: dict, games: list[dict]) -> dict:
    """Normalise a /lol/matches/{id} detail response (bare object)."""
    mid = _match_id_value(meta) or _match_id_value({"matchId": meta.get("matchId"),
                                                    "esportsApiId": meta.get("esportsApiId")})
    t1, t2 = meta.get("team1") or {}, meta.get("team2") or {}
    blue = _team_stub(t1)
    red = _team_stub(t2)
    bo = _parse_bo(meta.get("strategy")) or meta.get("gameCount")
    winner_slug = meta.get("winnerSlug")
    results = [
        {"team_id": blue.get("id"), "score": t1.get("score", 0)},
        {"team_id": red.get("id"), "score": t2.get("score", 0)},
    ]
    # The detail endpoint omits league info; infer a display name from the
    # semantic tournamentId (e.g. "lol-lck_summer_2024" -> "LCK") so the
    # fixture header / slug carry a sensible league label.
    league_obj = _league_from_tournament(meta.get("tournamentId"))
    return {
        "id": mid,
        "name": f"{blue.get('name','?')} vs {red.get('name','?')}",
        "match_type": None,
        "status": _state_map(meta.get("state")),
        "number_of_games": bo,
        "begin_at": meta.get("startTime"),
        "scheduled_at": meta.get("startTime"),
        "end_at": meta.get("endTime"),
        "winner_id": winner_slug,
        "winner": {"id": winner_slug, "type": "Team"} if winner_slug else None,
        "draw": False,
        "forfeit": False,
        "opponents": [{"opponent": blue}, {"opponent": red}],
        "results": results,
        "league": league_obj,
        "serie": {},
        "tournament": {"id": meta.get("tournamentId")},
        "games": games,
        "videogame_version": {},
        "block_name": meta.get("blockName"),
        "round": meta.get("round"),
        "vod_url": meta.get("vodUrl"),
    }


# Known leagueId -> display name (keeps the slug prefix readable). Add as needed.
_LEAGUE_NAMES = {
    "lol-lck": "LCK", "lol-lpl": "LPL", "lol-msi": "MSI",
    "lol-worlds": "Worlds", "lol-lta-north": "LTA North",
    "lol-lta-south": "LTA South", "lol-lec": "LEC", "lol-lcs": "LCS",
}


def _league_from_tournament(tournament_id: str | None) -> dict:
    """Infer a league object {id, name} from a semantic tournamentId.

    tournamentId looks like "lol-lck_summer_2024", "lol-msi_2026", or
    "lol-tournament-<num>" (opaque). We take the part before the first "_" and
    map it to a display name; opaque ids yield an empty league.
    """
    if not tournament_id:
        return {}
    tid = str(tournament_id)
    # opaque numeric-prefixed id -> can't infer
    if tid.startswith("lol-tournament-"):
        return {}
    league_id = tid.split("_")[0]  # "lol-lck_summer_2024" -> "lol-lck"
    name = _LEAGUE_NAMES.get(league_id)
    return {"id": league_id, "name": name, "slug": league_id.replace("lol-", "")}


def _norm_game(g: dict) -> dict:
    """Normalise a /matches/{id}/games entry to PandaScore game stub shape."""
    gid = _game_id_value(g)
    blue = _team_stub(g.get("blueTeam") or {})
    red = _team_stub(g.get("redTeam") or {})
    winning_side = str(g.get("winningSide") or "").lower()    # blue/red
    winner_slug = g.get("winnerSlug")
    return {
        "id": gid,
        "position": g.get("gameNumber"),
        "status": _state_map(g.get("state")) or "finished",
        "length": g.get("duration"),
        "winner": {"id": winner_slug},
        "winning_side": winning_side,
        "match_id": _match_id_value(g),
        "blue_team": blue,
        "red_team": red,
        "patch": g.get("patch"),
        "first_objectives": g.get("firstObjectives"),
    }


def _parse_bo(strategy: Any) -> int | None:
    """Parse a Cito strategy value ("Bo5" string OR {type,count} object) -> int."""
    if strategy is None:
        return None
    if isinstance(strategy, str):
        s = strategy.lower().replace("bo", "").strip()
        try:
            return int(s)
        except ValueError:
            return None
    if isinstance(strategy, dict):
        try:
            return int(strategy.get("count") or 0) or None
        except (TypeError, ValueError):
            return None
    return None


# ============================== field extraction helpers ==============================
# Mirror the pandascore module's helpers (defensive against missing data) so
# collect.py can import them from either adapter with identical behaviour.

def team_side(match: dict, team_id: Any) -> str:
    """Guess blue/red side from opponents list order ([0]=blue, [1]=red)."""
    opps = match.get("opponents") or []
    for i, o in enumerate(opps):
        if (o.get("opponent") or {}).get("id") == team_id:
            return "blue" if i == 0 else "red"
    # fallback: match game winning_side / blue_team / red_team if available
    return "blue"


def roster_by_role(players: list[dict]) -> dict[str, dict]:
    """Map canonical role -> player dict."""
    out: dict[str, dict] = {}
    for p in players or []:
        role = p.get("role")
        if role in ROLE_ORDER:
            out[role] = p
    return out


def series_score_for(match: dict) -> dict[Any, int]:
    """Map team_id -> games won (from match.results)."""
    return {r.get("team_id"): r.get("score", 0) for r in (match.get("results") or [])}

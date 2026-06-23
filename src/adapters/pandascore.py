"""PandaScore LoL API client.

Free-tier endpoints only (no Historical plan). Used by the system to build the
shared `context_pack` before prediction. All raw responses are cached to disk
so re-runs and debugging don't re-hit the API.

Spec: see doc/pandaScoreApi/. Auth: Bearer token in header OR ?token=.
"""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any

import httpx

from .. import config as cfg

# Roles in canonical order (top/jungle/mid/adc/support)
ROLE_ORDER = ["top", "jun", "mid", "adc", "sup"]


class PandaScoreError(RuntimeError):
    pass


class PandaScoreClient:
    def __init__(self, api_key: str | None = None, base_url: str | None = None,
                 cache_dir: Path | None = None, timeout: float = 30.0,
                 proxy: str | None = None):
        cfg.load_env()
        self.api_key = api_key or cfg.env("PANDASCORE_API_KEY")
        self.base_url = (base_url or cfg.env("PANDASCORE_BASE_URL")
                         or "https://api.pandascore.co").rstrip("/")
        self.cache_dir = cache_dir or (cfg.DATA / "_pandascore_cache")
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.timeout = timeout
        # proxy: explicit arg wins, else read proxies.yaml / env
        self.proxy = proxy if proxy is not None else cfg.proxy_for("pandascore")
        if not self.api_key:
            raise PandaScoreError(
                "PANDASCORE_API_KEY not set. Copy .env.example to .env and fill it in."
            )

    # ---------- core request w/ disk cache ----------
    def _cache_path(self, path: str, params: dict[str, Any]) -> Path:
        import hashlib
        key = hashlib.sha1(
            f"{path}|{json.dumps(params, sort_keys=True)}".encode()
        ).hexdigest()[:16]
        slug = path.strip("/").replace("/", "__")
        return self.cache_dir / f"{slug}__{key}.json"

    def get(self, path: str, params: dict[str, Any] | None = None,
            *, ttl_seconds: float | None = None, refresh: bool = False) -> Any:
        params = dict(params or {})
        params.setdefault("token", self.api_key)
        cpath = self._cache_path(path, params)

        if not refresh and cpath.exists():
            if ttl_seconds is None or (time.time() - cpath.stat().st_mtime) < ttl_seconds:
                return json.loads(cpath.read_text(encoding="utf-8"))

        url = f"{self.base_url}{path}"
        client_kwargs = {"timeout": self.timeout}
        if self.proxy:
            client_kwargs["proxy"] = self.proxy
        with httpx.Client(**client_kwargs) as client:
            resp = client.get(url, params=params)
        if resp.status_code == 404:
            return None
        if resp.status_code >= 400:
            raise PandaScoreError(f"PandaScore {resp.status_code} for {path}: {resp.text[:300]}")
        data = resp.json()
        cpath.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        return data

    # ---------- paginated list helper ----------
    def get_all(self, path: str, params: dict[str, Any] | None = None,
                *, max_pages: int = 10, per_page: int = 100,
                ttl_seconds: float | None = None) -> list[dict[str, Any]]:
        """Auto-paginate a list endpoint (capped at max_pages)."""
        params = dict(params or {})
        out: list[dict[str, Any]] = []
        for page in range(1, max_pages + 1):
            batch = self.get(path, {**params, "page[size]": per_page, "page[number]": page},
                             ttl_seconds=ttl_seconds) or []
            if not isinstance(batch, list):
                break
            out.extend(batch)
            if len(batch) < per_page:
                break
        return out

    # ---------- high-level LoL helpers ----------

    def tracked_league_ids(self) -> dict[str, int]:
        """Map our leagues.yaml names -> PandaScore league.id.

        If a league entry has an explicit `id`, trust it directly (no API call
        needed). Otherwise fall back to matching `slug` against /lol/leagues.
        """
        leagues_cfg = cfg.leagues_cfg()
        entries = leagues_cfg.get("leagues", []) or []
        mapping: dict[str, int] = {}

        # 1) explicit ids win
        need_slug_lookup = []
        for l in entries:
            if l.get("id"):
                mapping[l["name"]] = int(l["id"])
            else:
                need_slug_lookup.append(l)

        # 2) resolve the rest by slug against the league list
        if need_slug_lookup:
            tracked_slugs = {l["slug"]: l["name"] for l in need_slug_lookup if l.get("slug")}
            all_leagues = self.get("/lol/leagues", {"page[size]": 100}, ttl_seconds=86400) or []
            for lg in all_leagues:
                slug = lg.get("slug", "")
                if slug in tracked_slugs:
                    mapping[tracked_slugs[slug]] = lg["id"]
            missing = [n for n in tracked_slugs.values() if n not in mapping]
            if missing:
                print(f"[pandascore] WARNING: slug match failed for {missing}. "
                      f"Run the verify snippet in configs/leagues.yaml to get correct slugs.")
        return mapping

    def upcoming_matches(self, league_ids: list[int], *, horizon_days: int = 14) -> list[dict]:
        """Upcoming matches for tracked leagues within horizon_days.

        PandaScore filter[future]=true already restricts to upcoming; we further
        narrow by league and a begin_at range so we don't pull the whole planet.
        """
        from datetime import datetime, timedelta, timezone

        now = datetime.now(timezone.utc)
        end = now + timedelta(days=horizon_days)
        matches: list[dict] = []
        for lid in league_ids:
            batch = self.get_all(
                "/lol/matches/upcoming",
                {"filter[league_id]": lid, "sort": "begin_at",
                 "range[begin_at]": f"{now.date().isoformat()},{end.date().isoformat()}"},
                ttl_seconds=300,
            )
            matches.extend(batch)
        # de-dup by id
        seen: set[int] = set()
        uniq: list[dict] = []
        for m in matches:
            mid = m.get("id")
            if mid in seen:
                continue
            seen.add(mid)
            uniq.append(m)
        uniq.sort(key=lambda m: m.get("begin_at") or "")
        return uniq

    def match(self, match_id: int, *, refresh: bool = False) -> dict | None:
        """Single-match detail. NOTE: /lol/matches/{id} requires a paid plan
        (returns 403 on the free tier). Prefer `match_from_list()` which uses
        the free /lol/matches/upcoming|past list endpoints that already carry
        the full match object (opponents/games/results/version)."""
        return self.get(f"/lol/matches/{match_id}", refresh=refresh, ttl_seconds=300)

    def match_from_list(self, match_id: int, *, refresh: bool = False) -> dict | None:
        """Fetch a match via the FREE list endpoints (upcoming + past). The list
        response already contains the complete match object, so this avoids the
        paid detail endpoint entirely."""
        for endpoint in ("/lol/matches/upcoming", "/lol/matches/running", "/lol/matches/past"):
            batch = self.get_all(endpoint, {"filter[id]": match_id, "page[size]": 5},
                                 ttl_seconds=120, max_pages=1) or []
            for m in batch:
                if m.get("id") == match_id:
                    return m
        return None

    def team(self, team_id: int, *, refresh: bool = False) -> dict | None:
        return self.get(f"/lol/teams/{team_id}", refresh=refresh, ttl_seconds=3600)

    def team_recent_games(self, team_id: int, *, limit: int = 20) -> list[dict]:
        """Recent finished games for a team. Returns game stubs (with winner)."""
        games = self.get_all(
            f"/lol/teams/{team_id}/games",
            {"filter[finished]": "true", "sort": "-begin_at"},
            ttl_seconds=600, max_pages=2,
        )
        return games[:limit]

    def game_detail(self, game_id: int, *, refresh: bool = False) -> dict | None:
        """Full single-game detail incl players[].champion/items/runes/spells."""
        return self.get(f"/lol/games/{game_id}", refresh=refresh, ttl_seconds=600)

    def meta_champions(self) -> list[dict]:
        return self.get("/lol/versions/all/champions", {"page[size]": 100},
                        ttl_seconds=86400) or []

    def meta_items(self) -> list[dict]:
        return self.get("/lol/items", {"page[size]": 100}, ttl_seconds=86400) or []


# ---------- field extraction helpers (defensive against missing data) ----------

def team_side(match: dict, team_id: int) -> str:
    """Guess blue/red side from opponents list order (PandaScore: [0]=blue)."""
    opps = match.get("opponents") or []
    for i, o in enumerate(opps):
        if (o.get("opponent") or {}).get("id") == team_id:
            return "blue" if i == 0 else "red"
    return "blue"


def roster_by_role(team_obj: dict) -> dict[str, dict]:
    """Map role -> player dict for a team's active roster."""
    out: dict[str, dict] = {}
    for p in team_obj.get("players", []) or []:
        role = p.get("role")
        if role in ROLE_ORDER:
            out[role] = p
    return out


def series_score_for(match: dict) -> dict[int, int]:
    """Map team_id -> games won (from match.results)."""
    return {r.get("team_id"): r.get("score", 0) for r in (match.get("results") or [])}

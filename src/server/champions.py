"""Champion pool data for the manual BP editor.

Aggregates the full champion roster (name + icon) from PandaScore and joins
each champion with the Chinese-nickname aliases from the repo-root
`champion_aliases.py`. Exposed to the UI via GET /api/champions.

PandaScore's `GET /lol/champions` (or the deprecated `/lol/versions/all/champions`
that `PandaScoreClient.meta_champions()` already calls) returns each champion
with an `image_url` — the only data source in this project that carries icons.
Responses are disk-cached by the adapter (TTL 24h) and re-cached in-memory here
for 5 min so opening the editor is instant after the first load.
"""

from __future__ import annotations

import importlib.util
import time
from pathlib import Path
from typing import Any

from .. import config as cfg

# In-memory cache (timestamp, payload). Avoids re-reading disk on every
# editor open. Champions change rarely; a 5 min TTL is plenty.
_CACHE_TTL = 300.0
_cache: tuple[float, list[dict[str, Any]]] = (0.0, [])

# Loaded lazily so the server still imports if the file is missing.
_ALIASES: dict[str, list[str]] | None = None


def _load_aliases() -> dict[str, list[str]]:
    """Import the repo-root champion_aliases.py (which is not on sys.path)."""
    global _ALIASES
    if _ALIASES is not None:
        return _ALIASES
    path = cfg.ROOT / "champion_aliases.py"
    spec = importlib.util.spec_from_file_location("champion_aliases", path)
    mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    _ALIASES = getattr(mod, "CHAMPION_ALIASES", {}) or {}
    return _ALIASES


# PandaScore display-name spellings that do not normalize to their alias key
# by the generic strip rule. The alias file uses Riot's compact internal ids
# (e.g. `monkeyking`, `jarvaniv`), while PandaScore uses display names
# (`Wukong`, `Jarvan IV`). Map the normalized display name -> alias key for
# the handful that diverge after stripping spaces/punctuation/lowercasing.
_NAME_TO_ALIAS_KEY_OVERRIDES: dict[str, str] = {
    "wukong": "monkeyking",
    "jarvaniv": "jarvaniv",      # "Jarvan IV" -> "jarvaniv" (strip space)
    "leesin": "leesin",
    "drmundo": "drmundo",
    "chogath": "chogath",
    "velkoz": "velkoz",
    "aurelionsol": "aurelionsol",
    "tahmkench": "tahmkench",
    "masteryi": "masteryi",
    "xinzhao": "xinzhao",
    "twistedfate": "twistedfate",
    "missfortune": "missfortune",
    "drmundo": "drmundo",
    "renataglasc": "renataglasc",
    "belveth": "belveth",         # "Bel'Veth" -> strip apostrophe
    "kogmaw": "kogmaw",
    "kaisa": "kaisa",
    "renataglasc": "renata",      # alias file uses the short "renata"
}


def _normalize_name(name: str) -> str:
    """Normalize a PandaScore display name toward an alias-file key.

    Strips spaces, apostrophes, periods; lowercases. e.g.
      "Jarvan IV" -> "jarvaniv", "Wukong" -> "wukong",
      "Lee Sin" -> "leesin", "Bel'Veth" -> "belveth".
    """
    out = []
    for ch in (name or ""):
        if ch.isalnum():
            out.append(ch.lower())
    return "".join(out)


def _aliases_for(name: str, aliases_map: dict[str, list[str]]) -> list[str]:
    """Look up the nickname list for a champion display name."""
    norm = _normalize_name(name)
    key = _NAME_TO_ALIAS_KEY_OVERRIDES.get(norm, norm)
    found = aliases_map.get(key)
    if found:
        return list(found)
    # Some alias keys are written without stripping (rare); fall back to a
    # direct lookup by the normalized name in case the file uses the same form.
    return list(aliases_map.get(norm, []))


def _fetch_from_pandascore() -> list[dict[str, Any]]:
    """Call PandaScore (disk-cached) for the full champion list.

    `filter[videogame_version]=latest` returns exactly one row per champion
    (~170), each with image_url + big_image_url. Using `=all` would explode
    to one-row-per-patch and break PandaScore's pagination, so `latest` is
    both faster and cleaner.
    """
    from ..adapters.pandascore import PandaScoreClient, PandaScoreError
    try:
        client = PandaScoreClient()
    except PandaScoreError:
        return []
    raw = client.get_all("/lol/champions",
                         {"filter[videogame_version]": "latest", "sort": "name"},
                         ttl_seconds=86400, max_pages=5, per_page=100) or []
    out: list[dict[str, Any]] = []
    seen: set[str] = set()
    for c in raw:
        name = c.get("name")
        if not name or name in seen:
            continue
        seen.add(name)
        out.append({
            "name": name,
            "slug": c.get("slug") or name,
            "image_url": c.get("image_url") or "",
            "big_image_url": c.get("big_image_url") or "",
        })
    out.sort(key=lambda x: x["name"].lower())
    return out


def get_champions_data(*, refresh: bool = False) -> list[dict[str, Any]]:
    """Return the champion roster joined with Chinese aliases.

    Each entry: {name, slug, image_url, big_image_url, aliases:[...]}.
    Serves GET /api/champions. Safe (returns []) if PandaScore is unavailable.
    """
    global _cache
    ts, cached = _cache
    if not refresh and cached and (time.time() - ts) < _CACHE_TTL:
        return cached

    champs = _fetch_from_pandascore()
    aliases_map = _load_aliases()
    for c in champs:
        c["aliases"] = _aliases_for(c["name"], aliases_map)

    # In-memory cache even if empty, so a missing PandaScore key doesn't make
    # every editor open re-attempt the (failing) client init instantly.
    _cache = (time.time(), champs)
    return champs

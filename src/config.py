"""Project paths + config loading. Single source of truth for the layout."""

from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path

import yaml
from dotenv import load_dotenv

# src/ -> project root (parents[1] because this file lives in src/)
ROOT = Path(__file__).resolve().parents[1]

CONFIGS = ROOT / "configs"
PROMPTS = ROOT / "prompts"
SCHEMAS = ROOT / "schemas"
DATA = ROOT / "data"
MATCHES_DIR = DATA / "matches"
GAMES_DIR = DATA / "games"
SITE_DIR = ROOT / "docs" / "site"
DOC_DIR = ROOT / "doc"


def env(key: str, default: str = "") -> str:
    """Read an env var (after loading .env). Returns '' if unset/empty."""
    return os.getenv(key, default) or default


def env_int(key: str, default: int) -> int:
    try:
        return int(os.getenv(key, "") or default)
    except (TypeError, ValueError):
        return default


@lru_cache(maxsize=1)
def load_env() -> None:
    """Load .env once. Safe to call from any module."""
    load_dotenv(ROOT / ".env", override=False)


@lru_cache(maxsize=1)
def policy() -> dict:
    load_env()
    return yaml.safe_load((CONFIGS / "policy.yaml").read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def models_cfg() -> dict:
    load_env()
    data = yaml.safe_load((CONFIGS / "models.yaml").read_text(encoding="utf-8"))
    return data.get("models", [])


@lru_cache(maxsize=1)
def leagues_cfg() -> dict:
    load_env()
    return yaml.safe_load((CONFIGS / "leagues.yaml").read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def tasks_cfg() -> dict:
    load_env()
    return yaml.safe_load((CONFIGS / "tasks.yaml").read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def proxies_cfg() -> dict:
    load_env()
    path = CONFIGS / "proxies.yaml"
    if not path.exists():
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


@lru_cache(maxsize=1)
def match_id_map() -> dict[int, str]:
    """Legacy PandaScore match_id -> Cito matchId mapping (see
    configs/match_id_map.yaml). Empty dict if the file is absent.

    Used by grade as a fallback when a match_id (from an old PandaScore fixture)
    can't be looked up in Cito directly.
    """
    load_env()
    path = CONFIGS / "match_id_map.yaml"
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    mappings = data.get("mappings") or {}
    # normalise keys to int, values to str
    return {int(k): str(v) for k, v in mappings.items() if v}


def proxy_for(service: str) -> str | None:
    """Return the proxy URL for a service (e.g. 'pandascore'), or None.

    Env var LOLA_<SERVICE>_PROXY_URL overrides the file;
    LOLA_<SERVICE>_PROXY_ENABLED overrides the on/off switch.
    """
    import os
    svc = service.lower()
    block = (proxies_cfg().get(service) or {})
    enabled_env = f"LOLA_{svc.upper()}_PROXY_ENABLED"
    url_env = f"LOLA_{svc.upper()}_PROXY_URL"
    if os.getenv(url_env, "").strip():
        return os.getenv(url_env).strip()
    enabled = block.get("enabled", False)
    env_flag = os.getenv(enabled_env)
    if env_flag is not None:
        enabled = env_flag.strip().lower() in ("1", "true", "yes", "on")
    if enabled and block.get("url"):
        return block["url"]
    return None


# ---- slug helpers (filenames are derived from these) ----

_SLUG_SAFE = "_-"  # keep these, strip everything else non-alnum


def slugify(text: str) -> str:
    """Make a filesystem/token-safe slug. ASCII alnum + _ -, lowercased."""
    out = []
    for ch in str(text or "").strip():
        if ch.isalnum() or ch in _SLUG_SAFE:
            out.append(ch)
        elif ch in " /":
            out.append("_")
    s = "".join(out).strip("._-")
    return (s or "unknown").lower()


def match_slug(league: str, blue: str, red: str, begin_at: str) -> str:
    """Convention: <League>_<Blue>_vs_<Red>_<YYYY-MM-DD>"""
    date = (begin_at or "")[:10] or "nodate"
    return slugify(f"{league}_{blue}_vs_{red}_{date}")


def match_dir(slug: str) -> Path:
    d = MATCHES_DIR / slug
    d.mkdir(parents=True, exist_ok=True)
    (d / "predictions").mkdir(exist_ok=True)
    (d / "results").mkdir(exist_ok=True)
    return d


def game_dir(match_slug_: str, position: int) -> Path:
    d = GAMES_DIR / match_slug_ / f"g{position}"
    d.mkdir(parents=True, exist_ok=True)
    (d / "predictions").mkdir(exist_ok=True)
    return d

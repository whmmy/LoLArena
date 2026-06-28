"""Betting-advice pipeline (盘口下注建议).

For a match that has ALREADY been predicted, let a chosen model produce a
betting-advice (value-betting) analysis: feed it the open odds + every model's
prediction for that match, stream the model's reasoning to the browser, then
persist the structured recommendation table.

This path does NOT use web_search — it reasons purely over the already-collected
analyses — so it is a single-turn, tool-free, streamed chat.

Key functions:
  build_betting_prompt(slug, odds) -> (system, user)
  load_reference_analyses(slug) -> list[dict]
  stream_betting_advice(slug, model_id, odds) -> Iterator[dict]   (SSE events)
  save_advice(slug, model_id, odds, raw_text, picks, usage) -> Path
  list_advice(slug) -> list[dict]
"""

from __future__ import annotations

import datetime as dt
import json
import logging
import time
from pathlib import Path
from typing import Any, Iterator

from .. import config as cfg
from ..runners import build_runner
from ..runners.base import parse_markdown_picks

PROMPTS = cfg.PROMPTS

log = logging.getLogger("lolarena.betting")


# ============================== prompt building ==============================

def build_betting_prompt(slug: str, odds: dict[str, Any]) -> tuple[str, str]:
    """Render (system, user) for the betting task.

    `odds` shape (any field 0/missing => that market is dropped):
        {
          "moneyline":     {"blue": 1.5, "red": 2.4},
          "correct_score": {"3-0": 2.1, "3-1": 3.0, "1-3": 8.0, ...},
          "handicap":      {"-1.5": 1.9, "+1.5": 1.9},   # keys are line strings
          "total_games":   {"over_3.5": 1.8, "under_3.5": 1.95},
        }
    """
    system = (PROMPTS / "betting_system.md").read_text(encoding="utf-8")
    tpl = (PROMPTS / "task_betting.md").read_text(encoding="utf-8")

    match_ctx = _match_context(slug)
    odds_block = _format_odds(odds, match_ctx)
    references = _format_references(_reference_json(slug))

    user = (
        tpl.replace("{{match_context}}", _format_json(match_ctx))
           .replace("{{odds_block}}", odds_block)
           .replace("{{reference_analyses}}", references)
    )
    return system, user


def _match_context(slug: str) -> dict[str, Any]:
    """Compact match header (league / teams / BoX) from fixture + context_pack."""
    mdir = cfg.MATCHES_DIR / slug
    fixture = _read(mdir / "fixture.json") or {}
    pack = _read(mdir / "context_pack.json") or {}
    header = pack.get("fixture_header", {}) or {}
    opps = fixture.get("opponents") or []
    blue = (opps[0]["opponent"] if opps else {}).get("name") \
        or (header.get("blue") or {}).get("name") or "Blue"
    red = (opps[1]["opponent"] if len(opps) > 1 else {}).get("name") \
        or (header.get("red") or {}).get("name") or "Red"
    return {
        "slug": slug,
        "league": header.get("league") or (fixture.get("league") or {}).get("name"),
        "serie": header.get("serie") or (fixture.get("serie") or {}).get("full_name"),
        "blue": blue,
        "red": red,
        "number_of_games": fixture.get("number_of_games"),
        "begin_at": fixture.get("begin_at"),
        "patch_version": header.get("patch_version"),
    }


def _format_odds(odds: dict[str, Any], match_ctx: dict[str, Any]) -> str:
    """Render only open markets (odds != 0) as a readable text block."""
    blue = match_ctx.get("blue") or "蓝方"
    red = match_ctx.get("red") or "红方"
    lines: list[str] = []

    ml = odds.get("moneyline") or {}
    ml_open = {k: v for k, v in ml.items() if _open(v)}
    if ml_open:
        b = ml_open.get("blue")
        r = ml_open.get("red")
        lines.append("【胜负盘 Moneyline】")
        lines.append(f"  {blue}(蓝) 胜: {b}" if b is not None else f"  {blue}(蓝) 胜: 未开盘")
        lines.append(f"  {red}(红) 胜: {r}" if r is not None else f"  {red}(红) 胜: 未开盘")

    cs = odds.get("correct_score") or {}
    cs_open = {k: v for k, v in cs.items() if _open(v)}
    if cs_open:
        lines.append("【正确比分 Correct Score】")
        for score, o in sorted(cs_open.items()):
            blue_w, red_w = score.split("-")
            tag = f"{blue}" if int(blue_w) > int(red_w) else f"{red}"
            lines.append(f"  比分 {score}（{tag} 赢）: {o}")

    hcp = odds.get("handicap") or {}
    hcp_open = {k: v for k, v in hcp.items() if _open(v)}
    if hcp_open:
        lines.append("【让分盘 Handicap】")
        for line, o in sorted(hcp_open.items(), key=lambda kv: float(kv[0])):
            # negative line => 蓝方让分 (蓝方强，需净胜≥|line|局), positive => 红方让分
            val = float(line)
            who = f"{blue}({line})" if val < 0 else f"{red}({line})"
            lines.append(f"  {who}: {o}")

    tg = odds.get("total_games") or {}
    tg_open = {k: v for k, v in tg.items() if _open(v)}
    if tg_open:
        lines.append("【总局数大小 Total Games】")
        for key, o in sorted(tg_open.items()):
            if key.startswith("over"):
                thr = key.split("_", 1)[1] if "_" in key else key[5:]
                lines.append(f"  大 {thr}: {o}")
            elif key.startswith("under"):
                thr = key.split("_", 1)[1] if "_" in key else key[6:]
                lines.append(f"  小 {thr}: {o}")

    if not any([ml_open, cs_open, hcp_open, tg_open]):
        lines.append("（没有开盘的盘口，无法给出下注建议。）")
    return "\n".join(lines)


def _open(v: Any) -> bool:
    """A market is 'open' only if its odds is a positive number."""
    try:
        return float(v) > 0
    except (TypeError, ValueError):
        return False


def _format_references(refs: list[dict[str, Any]]) -> str:
    """Render every model's prediction as a compact reference block."""
    if not refs:
        return "（本场尚无模型预测记录。）"
    parts = []
    for i, r in enumerate(refs, 1):
        probs = r.get("win_probs") or {}
        parts.append(
            f"### 模型 {i}：{r.get('model', '?')}\n"
            f"- 预测胜方: {r.get('predicted_winner', '?')} | "
            f"胜率: 蓝 {probs.get('blue', '?')} / 红 {probs.get('red', '?')}\n"
            f"- 预测比分: {r.get('series_score', '?')} | 总局数: {r.get('series_length', '?')}"
        )
        kp = r.get("key_players") or []
        if kp:
            names = ", ".join(f"{p.get('player', '?')}({p.get('role', '?')},"
                              f"{p.get('team', '?')})" for p in kp[:5])
            parts.append(f"- 关键选手: {names}")
        sw = r.get("swing_factors") or []
        if sw:
            parts.append("- 胜负手:\n" + "\n".join(f"  · {s}" for s in sw))
        reasoning = r.get("reasoning") or {}
        overall = reasoning.get("overall")
        if overall:
            parts.append(f"- 总体判断: {overall}")
        parts.append("")  # blank line between models
    return "\n".join(parts)


def _reference_json(slug: str) -> list[dict[str, Any]]:
    """One compact dict per prediction record for the reference block."""
    return [
        {
            "model": r.get("model_id"),
            "predicted_winner": r.get("predicted_winner"),
            "win_probs": r.get("win_probs"),
            "series_score": r.get("series_score"),
            "series_length": r.get("series_length"),
            "key_players": r.get("key_players"),
            "swing_factors": r.get("swing_factors"),
            "reasoning": r.get("reasoning"),
        }
        for r in load_reference_analyses(slug)
    ]


# ============================== reference loading ==============================

def load_reference_analyses(slug: str) -> list[dict[str, Any]]:
    """Load every model's prediction for this match.

    Returns the prediction dicts (flattened out of the saved record). Used both
    to build the prompt and to gate the feature (no predictions => no betting).
    """
    pdir = cfg.MATCHES_DIR / slug / "predictions"
    out: list[dict[str, Any]] = []
    if not pdir.exists():
        return out
    for pf in sorted(pdir.glob("*.json")):
        rec = _read(pf)
        if not rec:
            continue
        pred = rec.get("prediction") or {}
        if not isinstance(pred, dict) or not pred:
            continue
        out.append({
            "model_id": rec.get("model_id") or pf.stem,
            "predicted_winner": pred.get("predicted_winner"),
            "win_probs": pred.get("win_probs"),
            "series_score": pred.get("series_score"),
            "series_length": pred.get("series_length"),
            "key_players": pred.get("key_players"),
            "swing_factors": pred.get("swing_factors"),
            "reasoning": pred.get("reasoning"),
            "error": rec.get("error"),
        })
    return out


def has_predictions(slug: str) -> bool:
    return any(p.get("win_probs") or p.get("series_score")
               for p in load_reference_analyses(slug))


# ============================== streaming ==============================

def stream_betting_advice(slug: str, model_id: str,
                          odds: dict[str, Any]) -> Iterator[dict[str, Any]]:
    """Run one model's betting analysis, streaming events for SSE.

    Yields:
        {"type":"start",    "model_id", "slug"}
        {"type":"delta",    "text"}                 # incremental answer text
        {"type":"thinking", "text"}                 # incremental reasoning text
        {"type":"ping"}                             # keep-alive during long waits
        {"type":"done",     "model_id","slug","raw_text","picks",
                            "saved","input_tokens","output_tokens","cost_usd","error"}
    """
    t0 = time.time()
    log.info("betting start | slug=%s model=%s", slug, model_id)
    yield {"type": "start", "model_id": model_id, "slug": slug}

    model_cfg = _model_cfg(model_id)
    if model_cfg is None:
        log.warning("betting unknown model | slug=%s model=%s", slug, model_id)
        yield {"type": "done", "model_id": model_id, "slug": slug, "raw_text": "",
               "picks": [], "saved": None, "input_tokens": 0, "output_tokens": 0,
               "cost_usd": 0.0, "error": f"unknown model_id '{model_id}'"}
        return

    system, user = build_betting_prompt(slug, odds)
    messages = [{"role": "system", "content": system},
                {"role": "user", "content": user}]

    # Betting is tool-free; pass a dummy search tool placeholder (never invoked).
    runner = build_runner(model_cfg, search_tool=None)
    full_parts: list[str] = []
    thinking_parts: list[str] = []
    done: dict[str, Any] = {}
    try:
        for ev in runner.stream_chat(messages, allow_tools=False):
            if ev["type"] == "delta":
                full_parts.append(ev["text"])
                yield {"type": "delta", "text": ev["text"]}
            elif ev["type"] == "thinking":
                thinking_parts.append(ev["text"])
                yield {"type": "thinking", "text": ev["text"]}
            elif ev["type"] == "done":
                done = ev
    except Exception as e:  # noqa: BLE001
        done = {"type": "done", "error": f"{type(e).__name__}: {e}",
                "text": "", "thinking": None, "input_tokens": 0, "output_tokens": 0}

    raw_text = "".join(full_parts) or done.get("text", "")
    thinking_text = "".join(thinking_parts) or done.get("thinking")
    picks: list[dict[str, Any]] = []
    saved: str | None = None
    err = done.get("error")
    in_tok = done.get("input_tokens", 0)
    out_tok = done.get("output_tokens", 0)

    if not err and raw_text:
        picks = parse_markdown_picks(raw_text)
        # save only successful runs (error runs are surfaced to the UI but not persisted)
        usage = {"input_tokens": in_tok, "output_tokens": out_tok}
        saved = str(save_advice(slug, model_id, odds, raw_text, picks, usage))

    elapsed = time.time() - t0
    if err:
        log.warning("betting error | slug=%s model=%s elapsed=%.1fs err=%s",
                    slug, model_id, elapsed, err)
    else:
        log.info("betting done | slug=%s model=%s elapsed=%.1fs picks=%d "
                 "tok=%d/%d thinking=%dchars saved=%s",
                 slug, model_id, elapsed, len(picks), in_tok, out_tok,
                 len(thinking_text or ""), bool(saved))

    yield {
        "type": "done", "model_id": model_id, "slug": slug,
        "raw_text": raw_text, "thinking_text": thinking_text,
        "picks": picks, "saved": saved,
        "input_tokens": in_tok, "output_tokens": out_tok,
        "cost_usd": _price(model_cfg, in_tok, out_tok), "error": err,
    }


def _model_cfg(model_id: str) -> dict[str, Any] | None:
    for m in cfg.models_cfg():
        if m.get("id") == model_id:
            return m
    return None


def _price(model_cfg: dict[str, Any], in_tok: int, out_tok: int) -> float:
    p = model_cfg.get("price_per_mtok") or {}
    return round((in_tok * p.get("input", 0) + out_tok * p.get("output", 0)) / 1_000_000, 6)


# ============================== persistence ==============================

def save_advice(slug: str, model_id: str, odds: dict[str, Any],
                raw_text: str, picks: list[dict[str, Any]],
                usage: dict[str, int]) -> Path:
    """Persist one betting-advice run. Filename: <model>_<UTCtimestamp>.json"""
    d = cfg.MATCHES_DIR / slug / "betting_advice"
    d.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = d / f"{model_id}_{stamp}.json"
    rec = {
        "model_id": model_id,
        "slug": slug,
        "odds": odds,
        "submitted_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "raw_text": raw_text,
        "picks": picks,
        "input_tokens": int(usage.get("input_tokens", 0)),
        "output_tokens": int(usage.get("output_tokens", 0)),
    }
    path.write_text(json.dumps(rec, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def list_advice(slug: str) -> list[dict[str, Any]]:
    """All betting-advice runs for a match, newest first (for the comparison view)."""
    d = cfg.MATCHES_DIR / slug / "betting_advice"
    out: list[dict[str, Any]] = []
    if not d.exists():
        return out
    for pf in d.glob("*.json"):
        rec = _read(pf)
        if rec:
            rec.setdefault("filename", pf.name)
            out.append(rec)
    out.sort(key=lambda r: r.get("submitted_at", ""), reverse=True)
    return out


# ============================== helpers ==============================

def _read(path: Path) -> dict | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def _format_json(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=2)

# DeepSeek Search API — the default `web_search` backend

> Official docs: <https://api-docs.deepseek.com/guides/search/> ·
> API reference: <https://api-docs.deepseek.com/api/search/>
>
> This file is a distilled note for LoLArena. The official docs are authoritative.

LoLArena mounts **one** `web_search` tool on every model. Since 2026-10 its
default backend is DeepSeek's in-house Search API (the legacy Zhipu backend is
still available via `LOLA_WEBSEARCH_PROVIDER=zhipu`). Keeping one shared backend
is what makes the model comparison fair — the engine is a **global** choice.

## Endpoint

```
POST https://api.deepseek.com/v1/tools/search
Authorization: Bearer <DEEPSEEK_API_KEY>
Content-Type: application/json
```

Request body (LoLArena sends `query` + `count` + `need_content: false`):

| Field | Type | Required | Meaning |
| --- | --- | --- | --- |
| `query` | string | yes | 1–128 chars. Supports the operators below. |
| `count` | int | no | 1–50, default 10. Result count does not change billing. |
| `need_content` | bool | no | When true, also returns the full page as Markdown in `content`. |
| `ori_question` | string | no | The user's original question (≤128 chars), improves intent understanding. |
| `localization` | string | no | IP address used to localize results. |

Response: `{"results": [...]}`, each item with `title`, `url`, `snippet`
(100–200 chars, UI display), `summary` (600–800 chars, **written for models**),
`content` (empty unless `need_content`), `site_name`, `site_icon`, `date`
(RFC 3339 or null), `rerank_score` (0–3; ≥1.5 is high quality), `authority`
(0–4; ≥3 is authoritative, -1 unknown). No match → `results: []`.

## Query operators (supported by the engine, passed through verbatim)

| Operator | Example | Meaning |
| --- | --- | --- |
| `site:` | `T1 site:liquipedia.net` | restrict to a site (combine with `OR`) |
| `-site:` | `T1 -site:reddit.com` | exclude a site |
| `"..."` | `"T1 vs Gen.G"` | exact phrase |
| `-` | `T1 -rumor` | exclude a term |
| `lang:` | `T1 lang:zh,en` | restrict language codes |
| `after:` / `before:` | `T1 after:2026-09-01` | publication-date window (year or full date) |

## How LoLArena maps its tool schema

The tool schema is shared by every model and every engine, so the adapter
translates where the engines differ:

- `count` → `count` (clamped 1–50).
- `recency` → the engine's query language. DeepSeek has **no** `recency`
  parameter, so a non-`noLimit` window becomes `after:YYYY-MM-DD` appended to
  the query (never duplicated if the model already wrote `after:`/`before:`).
  The default is `noLimit`: `after:` drops every page with an unknown publish
  date (forums, wikis, Liquipedia), which measurably lowers result quality.
- Results are normalised to `{title, content, link, media, publish_date}` —
  `summary` → `content` (capped at 600 chars to keep the prompt budget stable),
  `url` → `link`, `site_name` → `media`, `date` → `publish_date` (date part).
  DeepSeek's `rerank_score` / `authority` are kept as extra provenance fields
  in the search log (`data/.../predictions/searches/<model>.json`) for auditing
  search quality, but are not shown to the models.
- `need_content` is always `false` on purpose: `summary` is the model-facing
  digest, while full page Markdown would bloat the conversation for no signal.

## Failure handling

The adapter soft-fails: a search error is returned to the model as a readable
`[web_search error …]` result instead of failing the prediction. Transient
failures (timeouts, HTTP 408/429/5xx) get one retry (honouring `Retry-After`).
HTTP 402 means the account balance is empty — top up; 403 on Fetch is a policy
rejection; 404 on Fetch means no usable page content.

## Billing & rate limits

- Search: **$0.75 / 1,000 successful requests** (a request is billable only on
  HTTP 200 with a non-empty `results` array). `count` does not affect price.
  Per-request billing starts at 00:00 Beijing time on 2026-11-01.
- QPS: Search **100**, Fetch **25** per account (all keys share the limit).
  LoLArena runs ≤ a few concurrent models, so 100 QPS is far above what the
  benchmark needs.
- Search and Fetch are read-only; the adapter treats search as safe to retry.

## Switching engines (global, never per model)

```dotenv
# default: DeepSeek
LOLA_WEBSEARCH_PROVIDER=deepseek
DEEPSEEK_WEBSEARCH_API_KEY=        # optional; falls back to DEEPSEEK_API_KEY

# A/B comparison: legacy Zhipu search_pro
# LOLA_WEBSEARCH_PROVIDER=zhipu
# ZHIPU_WEBSEARCH_API_KEY=...
```

`configs/policy.yaml > web_search.provider` sets the default; the env var wins.
`configs/proxies.yaml > websearch` (env: `LOLA_WEBSEARCH_PROXY_URL`) routes
searches through an explicit proxy; ambient `HTTP(S)_PROXY` is ignored.

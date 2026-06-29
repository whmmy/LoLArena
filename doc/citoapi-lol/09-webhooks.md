# 09 — Webhooks

Cito 的 LoL 实时事件推送。**官方 markdown 列了 9 个事件,实测 `/lol/webhooks/events` 实际有 11 个**——多了 `lol.standings.updated` 和 `lol.transfer.new`。

> Webhook 是 **One Game Starter** 及以上套餐的功能(详见 [01-overview.md](./01-overview.md))。推送内容用 **HMAC-SHA256** 签名,客户端必须验签。

---

## `GET /lol/webhooks/events`

列出全部可用事件 + 完整签名方案 + 示例 payload。**实测响应**(全量):

```json
{
  "success": true,
  "available_on_plans": ["BASIC", "PRO", "BUSINESS"],
  "management_endpoint": "/api/v1/webhooks",
  "events": [
    { "event": "lol.match.started",
      "description": "Fires when a scheduled LoL match changes to in progress." },
    { "event": "lol.match.completed",
      "description": "Fires when a LoL match is marked completed with final score and winner." },
    { "event": "lol.score.updated",
      "description": "Fires when the game score changes inside a LoL series." },
    { "event": "lol.standings.updated",
      "description": "Fires when stored LoL standings are updated." },
    { "event": "lol.transfer.new",
      "description": "Fires when a new LoL roster transfer is synced." },
    { "event": "lol.live.game_started",
      "description": "Fires when a live LoL game starts." },
    { "event": "lol.live.state",
      "description": "Fires periodically during live gameplay with current kills, gold, towers, dragons, Barons, and game clock." },
    { "event": "lol.live.objective",
      "description": "Fires when a live game frame indicates a Dragon, Baron, inhibitor, or other tracked objective changed." },
    { "event": "lol.live.gold_swing",
      "description": "Fires when the live gold lead changes materially during a game." },
    { "event": "lol.live.kill_update",
      "description": "Fires when team kill totals change in the live game feed." },
    { "event": "lol.live.tower_destroyed",
      "description": "Fires when team tower totals change in the live game feed." }
  ],
  "example_payload": {
    "event": "lol.score.updated",
    "id": "7f4c2d0d8f2f4b2ca6c6f35c4d53c2aa",
    "timestamp": "2026-06-29T02:01:49.422Z",
    "data": {
      "matchId": "lol-match-116249880466944893",
      "teams": ["team-a", "team-b"],
      "score": "1-0",
      "league": "LEC"
    }
  },
  "signature_headers": [
    "X-Cito-Signature",
    "X-Cito-Event",
    "X-Cito-Event-Id",
    "X-Cito-Timestamp",
    "X-Cito-Delivery-Attempt"
  ],
  "signing": {
    "algorithm": "HMAC-SHA256",
    "signedContent": "UTF-8 bytes of the exact JSON request body sent by Cito",
    "bodySerialization": "JSON.stringify(payload)",
    "signatureHeader": "X-Cito-Signature",
    "signatureEncoding": "hex",
    "signaturePrefix": "none",
    "secretFormat": "Use the exact webhook secret value shown when the webhook is created or regenerated. No whsec_ prefix is used.",
    "verificationRule": "Verify against the raw request body bytes before reparsing or reserializing JSON.",
    "sampleSecret": "cito_test_secret_123",
    "samplePayload": {
      "event": "lol.live.state",
      "id": "sample-event-id-123",
      "timestamp": "2026-06-07T16:00:00.000Z",
      "data": {
        "gameId": "lol-game-123",
        "matchId": "lol-match-123",
        "league": "LEC",
        "gameTime": 1337,
        "blueTeam": {
          "tag": "G2", "kills": 7, "gold": 24800,
          "towers": 3, "dragons": 2, "barons": 0
        },
        "redTeam": {
          "tag": "FNC", "kills": 5, "gold": 23700,
          "towers": 2, "dragons": 1, "barons": 0
        }
      }
    },
    "samplePayloadString": "{\"event\":\"lol.live.state\",\"id\":\"sample-event-id-123\",\"timestamp\":\"2026-06-07T16:00:00.000Z\",\"data\":{\"gameId\":\"lol-game-123\",\"matchId\":\"lol-match-123\",\"league\":\"LEC\",\"gameTime\":1337,\"blueTeam\":{\"tag\":\"G2\",\"kills\":7,\"gold\":24800,\"towers\":3,\"dragons\":2,\"barons\":0},\"redTeam\":{\"tag\":\"FNC\",\"kills\":5,\"gold\":23700,\"towers\":2,\"dragons\":1,\"barons\":0}}}",
    "sampleSignature": "97db77f5cd96e09a70dcf6cc75fc5d92d780c41ce82c853b51e4070954c54171",
    "sampleHeaders": {
      "Content-Type": "application/json",
      "X-Cito-Signature": "97db77f5cd96e09a70dcf6cc75fc5d92d780c41ce82c853b51e4070954c54171",
      "X-Cito-Event": "lol.live.state",
      "X-Cito-Event-Id": "sample-event-id-123",
      "X-Cito-Timestamp": "2026-06-07T16:00:00.000Z",
      "X-Cito-Delivery-Attempt": "1"
    }
  },
  "delivery": {
    "timeout_ms": 10000,
    "attempts": 3,
    "note": "Use the payload id / X-Cito-Event-Id as your idempotency key."
  },
  "filters": {
    "supported_fields": ["league", "matchId", "gameId", "side"],
    "example": {
      "league": "LEC",
      "matchId": "lol-match-116249880466944893"
    }
  },
  "docs": "https://citoapi.com/docs/api/league-of-legends"
}
```

---

## 11 个事件一览

| 事件名 | 触发时机 | 适合 |
|---|---|---|
| `lol.match.started` | 比赛开始 | 通知 / 开始抓数据 |
| `lol.match.completed` | 比赛结束(比分 + 胜者已定) | 结算 / 排行更新 |
| `lol.score.updated` | 系列赛比分变化 | 实时计分板 |
| `lol.standings.updated` | 联赛积分有更新 | 排名刷新 |
| `lol.transfer.new` | 新转会同步进库 | 转会监控 |
| `lol.live.game_started` | 单个 game 开始 | 推流读取触发 |
| `lol.live.state` | 周期性(默认 ~数秒) | 实时数值大屏 |
| `lol.live.objective` | 小龙 / 大龙 / 水晶变化 | 客观元素追踪 |
| `lol.live.gold_swing` | 经济领先方显著变化 | 翻盘提醒 |
| `lol.live.kill_update` | 团队击杀总数变化 | 击杀面板 |
| `lol.live.tower_destroyed` | 团队推塔数变化 | 推塔面板 |

### 官方 markdown 没列、但实测有的

- `lol.standings.updated`
- `lol.transfer.new`

---

## Payload 通用结构

```json
{
  "event": "lol.live.state",
  "id": "uuid-xxx",
  "timestamp": "2026-06-29T02:01:49.422Z",
  "data": { /* 事件特定数据 */ }
}
```

| 顶层字段 | 说明 |
|---|---|
| `event` | 事件名(同 events 表的 `event` 字段) |
| `id` | 唯一事件 id,**用作幂等键** |
| `timestamp` | 服务端发出时间 |
| `data` | 事件特定 payload(见下) |

---

## 各事件 `data` 字段(实测样本)

### `lol.score.updated`

```json
{
  "matchId": "lol-match-116249880466944893",
  "teams": ["team-a", "team-b"],
  "score": "1-0",
  "league": "LEC"
}
```

### `lol.live.state`

```json
{
  "gameId": "lol-game-123",
  "matchId": "lol-match-123",
  "league": "LEC",
  "gameTime": 1337,
  "blueTeam": { "tag": "G2", "kills": 7, "gold": 24800, "towers": 3, "dragons": 2, "barons": 0 },
  "redTeam":  { "tag": "FNC", "kills": 5, "gold": 23700, "towers": 2, "dragons": 1, "barons": 0 }
}
```

### `lol.live.gold_swing`(官方 webhook 文档示例)

```json
{
  "matchId": "lol-match-115564793879469312",
  "gameId": "115564793879469313",
  "league": "LCS",
  "gameTime": 1716,
  "source": "vision",
  "previousGoldDiff": -1900,
  "goldDiff": -3300,
  "swing": -1400,
  "leadingSide": "red"
}
```

### `lol.live.objective`

推断字段:`gameId`, `matchId`, `league`, `gameTime`, `objectiveType`(`"dragon"` / `"baron"` / `"inhibitor"`), `team`(`"blue"` / `"red"`), `count`。

### `lol.live.kill_update`

推断字段:`gameId`, `matchId`, `league`, `blueKills`, `redKills`, `gameTime`。

### `lol.live.tower_destroyed`

推断字段:`gameId`, `matchId`, `league`, `blueTowers`, `redTowers`, `gameTime`。

### `lol.match.started` / `lol.match.completed` / `lol.standings.updated` / `lol.transfer.new` / `lol.live.game_started`

推断字段结构与 REST 对应端点的基础字段一致(如 `transfer.new` 的 data 形如单条 `/lol/transfers` 元素)。

> ⚠️ 未实测的字段名仅作推断,实际可能略有出入。

---

## 签名 / 验签

### 算法

```
HMAC-SHA256(
  key = webhook_secret,
  message = 原始请求 body 的 UTF-8 字节流
)
```

### 关键约束(官方原话)

| 约束 | 说明 |
|---|---|
| `signatureHeader` | `"X-Cito-Signature"` |
| `signatureEncoding` | `"hex"`(小写 hex 字符串) |
| `signaturePrefix` | `"none"`(签名前面**不带任何前缀**,直接 hex) |
| `secretFormat` | 直接用 webhook 创建/重置时给的明文 secret,**没有 `whsec_` 前缀** |
| `verificationRule` | **必须用原始 body 字节验签,不要先 parse 再 reserialize**——重新序列化会改变字节,导致签名失败 |

### 签名请求头

| Header | 说明 |
|---|---|
| `X-Cito-Signature` | hex 签名 |
| `X-Cito-Event` | 事件名(冗余,客户端可省一次 parse body) |
| `X-Cito-Event-Id` | 事件唯一 id,**用作客户端幂等键** |
| `X-Cito-Timestamp` | 服务端发出时间 |
| `X-Cito-Delivery-Attempt` | 第几次重试(1 / 2 / 3) |

### 客户端验签示例(Node.js)

```js
import crypto from 'node:crypto';

app.post('/webhook', express.raw({ type: 'application/json' }), (req, res) => {
  const sig = req.headers['x-cito-signature'];
  const eventId = req.headers['x-cito-event-id'];
  const event = req.headers['x-cito-event'];

  // 1. 验签(用原始 body 字节,不要 JSON.parse 后再 stringify)
  const expected = crypto
    .createHmac('sha256', process.env.CITO_WEBHOOK_SECRET)
    .update(req.body) // Buffer
    .digest('hex');

  if (sig !== expected) {
    return res.status(401).send('Invalid signature');
  }

  // 2. 此时再 parse body
  const payload = JSON.parse(req.body.toString('utf8'));

  // 3. 幂等:用 eventId 去重
  if (await isProcessed(eventId)) {
    return res.status(200).send('duplicate');
  }

  // 4. 处理
  await handleEvent(event, payload.data);

  res.sendStatus(200);
});
```

### 客户端验签示例(Python)

```python
import hmac, hashlib, json
from flask import Flask, request, abort

app = Flask(__name__)
SECRET = b"your_webhook_secret"

@app.post("/webhook")
def webhook():
    sig = request.headers.get("X-Cito-Signature", "")
    body = request.get_data()  # bytes, 不要 request.json 再 dumps

    expected = hmac.new(SECRET, body, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(sig, expected):
        abort(401)

    payload = json.loads(body)
    event_id = request.headers.get("X-Cito-Event-Id")

    # 幂等 + 业务处理
    if is_duplicate(event_id):
        return "ok"
    handle(payload)
    return "ok"
```

---

## 投递策略

| 字段 | 值 |
|---|---|
| 超时 | 10s(`timeout_ms: 10000`) |
| 重试 | 最多 3 次 |
| 重试头 | `X-Cito-Delivery-Attempt`(1 / 2 / 3) |
| 幂等键 | `payload.id` 或 header `X-Cito-Event-Id` |

如果你的 handler 返回非 2xx 或超过 10s,Cito 会重试。

---

## 过滤(filters)

订阅时可指定过滤,避免无意义事件:

```json
{
  "events": ["lol.live.gold_swing", "lol.live.objective"],
  "filters": {
    "league": "LCS",
    "matchId": "lol-match-115564793879469312",
    "gameId": "115564793879469313",
    "side": "red"
  }
}
```

支持字段:`league` / `matchId` / `gameId` / `side`(blue / red)。

---

## Webhook 管理

| 项 | 值 |
|---|---|
| 创建 / 修改 | 在 dashboard `https://citoapi.com/dashboard/webhooks` 操作 |
| 管理端点 | `/api/v1/webhooks`(GET / POST / DELETE) |
| 列出 webhook | `GET /api/v1/webhooks` |
| 注册 webhook | `POST /api/v1/webhooks` |
| 删除 webhook | `DELETE /api/v1/webhooks/{id}` |
| 套餐 | One Game Starter / Pro / Business(免费套餐不可用) |

### 管理 webhook POST 示例

```bash
curl -X POST "https://api.citoapi.com/api/v1/webhooks" \
  -H "x-api-key: YOUR_CITO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://yourapp.com/webhook",
    "events": ["lol.live.gold_swing", "lol.live.objective", "lol.score.updated"],
    "filters": { "league": "LCK" }
  }'
```

响应示例(官方 webhooks 文档):

```json
{
  "id": "wh_abc123",
  "url": "https://yourapp.com/webhook",
  "events": ["lol.live.gold_swing", "lol.live.objective", "lol.score.updated"],
  "secret": "whsec_xyz789...",
  "isActive": true,
  "createdAt": "2026-01-15T10:00:00Z"
}
```

> ⚠️ **官方 markdown** 显示 secret 带 `whsec_` 前缀,但 `/lol/webhooks/events` 实测明确说 **"No whsec_ prefix is used"**——文档示例与官方签名说明自相矛盾,**以签名说明为准**。

---

## Quick reference

| 用途 | 推荐做法 |
|---|---|
| 拿事件清单 + 签名样例 | `GET /lol/webhooks/events` |
| 验签 | HMAC-SHA256(原始 body 字节, hex, 无前缀) |
| 幂等键 | `payload.id` 或 `X-Cito-Event-Id` |
| 重试识别 | `X-Cito-Delivery-Attempt`(1/2/3) |
| 减少噪音 | 订阅时用 `filters.league/matchId/gameId/side` |
| 配置 / 启停 | Dashboard `https://citoapi.com/dashboard/webhooks` |
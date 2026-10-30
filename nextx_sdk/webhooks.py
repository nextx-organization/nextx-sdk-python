"""Verify NextX webhooks (Standard Webhooks: https://www.standardwebhooks.com).

    from nextx_sdk.webhooks import verify_webhook, WebhookVerificationError

    @app.post("/nextx/webhook")
    async def nextx_webhook(request: Request):
        try:
            event = verify_webhook(await request.body(), request.headers, os.environ["NEXTX_WEBHOOK_SECRET"])
        except WebhookVerificationError:
            return Response(status_code=400)
        if event["type"] == "call.completed":
            save_call(event["data"]["object"])
        return Response(status_code=204)

Pass the RAW body (bytes exactly as received) — re-serialized JSON will not match the signature.
Use `webhook-id` (also `event["id"]`) to drop duplicate deliveries: NextX retries until you answer 2xx.
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import time
from collections.abc import Mapping
from typing import Any

DEFAULT_TOLERANCE_SEC = 300


class WebhookVerificationError(Exception):
    """Missing headers, bad signature, or timestamp outside the tolerance."""


def _key(secret: str) -> bytes:
    if not secret or not secret.startswith("whsec_"):
        raise WebhookVerificationError("secret must look like whsec_...")
    try:
        key = base64.b64decode(secret[len("whsec_"):], validate=True)
    except ValueError as e:
        raise WebhookVerificationError("invalid secret") from e
    if not 24 <= len(key) <= 64:
        raise WebhookVerificationError("invalid secret")
    return key


def _header(headers: Mapping[str, Any], name: str) -> str | None:
    for k, v in headers.items():
        if k.lower() == name:
            return v[0] if isinstance(v, (list, tuple)) else v
    return None


def sign_webhook(secret: str, msg_id: str, timestamp: int, body: bytes | str) -> str:
    """Sign a body the way NextX does — handy for testing your webhook receiver."""
    raw = body.encode() if isinstance(body, str) else body
    mac = hmac.new(_key(secret), f"{msg_id}.{timestamp}.".encode() + raw, hashlib.sha256).digest()
    return "v1," + base64.b64encode(mac).decode()


def verify_webhook(
    body: bytes | str,
    headers: Mapping[str, Any],
    secret: str,
    *,
    tolerance_sec: int = DEFAULT_TOLERANCE_SEC,
    now: float | None = None,
) -> dict[str, Any]:
    """Check webhook-id / webhook-timestamp / webhook-signature and return the parsed event.

    The event is ``{"id", "type", "api_version", "created_at", "workspace_id", "livemode", "data": {"object": ...}}``.
    For ``call.*`` events ``data.object`` has the same shape as ``GET /api/v1/call/partner/calls/{id}``.
    """
    msg_id = _header(headers, "webhook-id")
    ts = _header(headers, "webhook-timestamp")
    sig = _header(headers, "webhook-signature")
    if not msg_id or not ts or not sig:
        raise WebhookVerificationError("missing webhook-id / webhook-timestamp / webhook-signature")
    try:
        timestamp = int(ts)
    except ValueError as e:
        raise WebhookVerificationError("invalid webhook-timestamp") from e
    if abs((now if now is not None else time.time()) - timestamp) > tolerance_sec:
        raise WebhookVerificationError("webhook-timestamp outside tolerance")

    raw = body.encode() if isinstance(body, str) else bytes(body)
    expected = sign_webhook(secret, msg_id, timestamp, raw).encode()
    if not any(hmac.compare_digest(expected, s.encode()) for s in sig.split(" ") if s):
        raise WebhookVerificationError("signature mismatch")
    return json.loads(raw)

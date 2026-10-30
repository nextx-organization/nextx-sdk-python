"""Offline tests: package import, headers and URL building."""
import httpx
import pytest

import nextx_sdk
from nextx_sdk import SANDBOX_URL, VERSION, create_client
from nextx_sdk.api.crm import contacts_list


def test_exports():
    assert nextx_sdk.PROD_URL == "https://api.nextx.vn"
    assert VERSION and VERSION != "0.0.0"


@pytest.mark.parametrize("kw", [{}, {"api_key": "nxk_a", "access_token": "t"}])
def test_requires_exactly_one_credential(kw):
    with pytest.raises(ValueError):
        create_client(**kw)


def _call(nx, handler, **kw):
    nx.set_httpx_client(httpx.Client(base_url=SANDBOX_URL, transport=httpx.MockTransport(handler),
                                     headers=nx._headers | {nx.auth_header_name: (f"{nx.prefix} " if nx.prefix else "") + nx.token}))
    return contacts_list.sync_detailed(client=nx, **kw)


def test_api_key_sent_as_x_api_key():
    seen = {}

    def handler(req: httpx.Request) -> httpx.Response:
        seen["req"] = req
        return httpx.Response(200, json={"items": [], "totalCount": 0, "pageNumber": 2, "pageSize": 20})

    r = _call(create_client(api_key="nxk_test", base_url=SANDBOX_URL + "/", language="en"), handler, page_number=2)
    assert r.status_code == 200
    req = seen["req"]
    assert str(req.url).startswith(f"{SANDBOX_URL}/api/v1/crm/contacts?")
    assert "pageNumber=2" in str(req.url)
    assert req.headers["x-api-key"] == "nxk_test"
    assert "authorization" not in req.headers
    assert req.headers["accept-language"] == "en"
    assert req.headers["user-agent"].startswith("nextx-sdk-python/")


def test_access_token_sent_as_bearer():
    seen = {}

    def handler(req: httpx.Request) -> httpx.Response:
        seen["req"] = req
        return httpx.Response(200, json={"items": [], "totalCount": 0})

    _call(create_client(access_token="tok", base_url=SANDBOX_URL), handler)
    assert seen["req"].headers["authorization"] == "Bearer tok"
    assert "x-api-key" not in seen["req"].headers


# Official Standard Webhooks test vector — independent of NextX's signer.
SW = dict(secret="whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw", id="msg_p5jXN8AQM9LWM0D4loKWxJek",
          ts=1614265330, body=b'{"test": 2432232314}', sig="v1,g0hM9SsE+OTPJTGt/tmIKtSyZlE3uFJELVlNIOLJ1OE=")


def test_webhook_standard_vector():
    from nextx_sdk.webhooks import sign_webhook, verify_webhook

    assert sign_webhook(SW["secret"], SW["id"], SW["ts"], SW["body"]) == SW["sig"]
    headers = {"Webhook-Id": SW["id"], "webhook-timestamp": str(SW["ts"]), "webhook-signature": f"v1,old {SW['sig']}"}
    assert verify_webhook(SW["body"], headers, SW["secret"], now=SW["ts"]) == {"test": 2432232314}


@pytest.mark.parametrize("change", ["body", "sig", "late", "missing", "secret"])
def test_webhook_rejects(change):
    from nextx_sdk.webhooks import WebhookVerificationError, verify_webhook

    body, secret, now = SW["body"], SW["secret"], SW["ts"]
    headers = {"webhook-id": SW["id"], "webhook-timestamp": str(SW["ts"]), "webhook-signature": SW["sig"]}
    if change == "body":
        body = b'{"test": 1}'
    elif change == "sig":
        headers["webhook-signature"] = "v1,AAAA"
    elif change == "late":
        now = SW["ts"] + 301
    elif change == "missing":
        del headers["webhook-signature"]
    else:
        secret = "not-a-secret"
    with pytest.raises(WebhookVerificationError):
        verify_webhook(body, headers, secret, now=now)

"""Kiểm không mạng: gói nạp được, client gắn đúng header, gọi đúng đường dẫn."""
import httpx
import pytest

import nextx_sdk
from nextx_sdk import SANDBOX_URL, VERSION, create_client
from nextx_sdk.api.crm import contacts_list


def test_xuat_api():
    assert nextx_sdk.PROD_URL == "https://api.nextx.vn"
    assert VERSION and VERSION != "0.0.0"


@pytest.mark.parametrize("kw", [{}, {"api_key": "nxk_a", "access_token": "t"}])
def test_can_dung_mot_cach_xac_thuc(kw):
    with pytest.raises(ValueError):
        create_client(**kw)


def _goi(nx, handler, **kw):
    nx.set_httpx_client(httpx.Client(base_url=SANDBOX_URL, transport=httpx.MockTransport(handler),
                                     headers=nx._headers | {nx.auth_header_name: (f"{nx.prefix} " if nx.prefix else "") + nx.token}))
    return contacts_list.sync_detailed(client=nx, **kw)


def test_khoa_api_gui_x_api_key():
    seen = {}

    def handler(req: httpx.Request) -> httpx.Response:
        seen["req"] = req
        return httpx.Response(200, json={"items": [], "totalCount": 0, "pageNumber": 2, "pageSize": 20})

    r = _goi(create_client(api_key="nxk_test", base_url=SANDBOX_URL + "/", language="en"), handler, page_number=2)
    assert r.status_code == 200
    req = seen["req"]
    assert str(req.url).startswith(f"{SANDBOX_URL}/api/v1/crm/contacts?")
    assert "pageNumber=2" in str(req.url)
    assert req.headers["x-api-key"] == "nxk_test"
    assert "authorization" not in req.headers
    assert req.headers["accept-language"] == "en"
    assert req.headers["user-agent"].startswith("nextx-sdk-python/")


def test_access_token_gui_bearer():
    seen = {}

    def handler(req: httpx.Request) -> httpx.Response:
        seen["req"] = req
        return httpx.Response(200, json={"items": [], "totalCount": 0})

    _goi(create_client(access_token="tok", base_url=SANDBOX_URL), handler)
    assert seen["req"].headers["authorization"] == "Bearer tok"
    assert "x-api-key" not in seen["req"].headers

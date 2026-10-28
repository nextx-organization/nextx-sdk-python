"""Lối vào gọn cho NextX API.

    from nextx_sdk import create_client, SANDBOX_URL
    from nextx_sdk.api.crm import contacts_list

    nx = create_client(api_key=os.environ["NEXTX_API_KEY"], base_url=SANDBOX_URL)
    page = contacts_list.sync(client=nx, page_size=20)
"""

from __future__ import annotations

from typing import Literal

from .client import AuthenticatedClient
from ._version import VERSION

PROD_URL = "https://api.nextx.vn"
SANDBOX_URL = "https://api-dev.nextx.vn"


def create_client(
    api_key: str | None = None,
    *,
    access_token: str | None = None,
    base_url: str = PROD_URL,
    language: Literal["vi", "en"] = "vi",
    timeout: float = 30.0,
    raise_on_unexpected_status: bool = True,
) -> AuthenticatedClient:
    """Tạo client: khoá API của workspace (`nxk_…`, header `X-Api-Key`) HOẶC access token OAuth (`Authorization: Bearer`)."""
    if bool(api_key) == bool(access_token):
        raise ValueError("NextX SDK: cần đúng một trong api_key hoặc access_token")
    import httpx

    return AuthenticatedClient(
        base_url=base_url.rstrip("/"),
        token=api_key or access_token or "",
        prefix="" if api_key else "Bearer",
        auth_header_name="X-Api-Key" if api_key else "Authorization",
        headers={"Accept-Language": language, "User-Agent": f"nextx-sdk-python/{VERSION}"},
        timeout=httpx.Timeout(timeout),
        raise_on_unexpected_status=raise_on_unexpected_status,
    )

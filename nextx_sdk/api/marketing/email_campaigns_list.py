from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paged_result_of_email_campaign_dto import PagedResultOfEmailCampaignDto
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    status: str | Unset = UNSET,
    q: str | Unset = UNSET,
    page: int | Unset = 1,
    size: int | Unset = 20,
    days: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["status"] = status

    params["q"] = q

    params["page"] = page

    params["size"] = size

    params["days"] = days


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/marketing/email-campaigns",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PagedResultOfEmailCampaignDto | None:
    if response.status_code == 200:
        response_200 = PagedResultOfEmailCampaignDto.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PagedResultOfEmailCampaignDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    q: str | Unset = UNSET,
    page: int | Unset = 1,
    size: int | Unset = 20,
    days: int | Unset = UNSET,

) -> Response[PagedResultOfEmailCampaignDto]:
    """ Lấy danh sách email campaigns

     Trả về danh sách phân trang các email campaign trong workspace. Có thể lọc theo status
    (Draft/Scheduled/Sending/Sent/…), từ khóa và `days` (chỉ lấy chiến dịch có ngày gửi/hẹn/tạo trong N
    ngày qua).

    Args:
        status (str | Unset):
        q (str | Unset):
        page (int | Unset):  Default: 1.
        size (int | Unset):  Default: 20.
        days (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedResultOfEmailCampaignDto]
     """


    kwargs = _get_kwargs(
        status=status,
q=q,
page=page,
size=size,
days=days,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    q: str | Unset = UNSET,
    page: int | Unset = 1,
    size: int | Unset = 20,
    days: int | Unset = UNSET,

) -> PagedResultOfEmailCampaignDto | None:
    """ Lấy danh sách email campaigns

     Trả về danh sách phân trang các email campaign trong workspace. Có thể lọc theo status
    (Draft/Scheduled/Sending/Sent/…), từ khóa và `days` (chỉ lấy chiến dịch có ngày gửi/hẹn/tạo trong N
    ngày qua).

    Args:
        status (str | Unset):
        q (str | Unset):
        page (int | Unset):  Default: 1.
        size (int | Unset):  Default: 20.
        days (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedResultOfEmailCampaignDto
     """


    return sync_detailed(
        client=client,
status=status,
q=q,
page=page,
size=size,
days=days,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    q: str | Unset = UNSET,
    page: int | Unset = 1,
    size: int | Unset = 20,
    days: int | Unset = UNSET,

) -> Response[PagedResultOfEmailCampaignDto]:
    """ Lấy danh sách email campaigns

     Trả về danh sách phân trang các email campaign trong workspace. Có thể lọc theo status
    (Draft/Scheduled/Sending/Sent/…), từ khóa và `days` (chỉ lấy chiến dịch có ngày gửi/hẹn/tạo trong N
    ngày qua).

    Args:
        status (str | Unset):
        q (str | Unset):
        page (int | Unset):  Default: 1.
        size (int | Unset):  Default: 20.
        days (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedResultOfEmailCampaignDto]
     """


    kwargs = _get_kwargs(
        status=status,
q=q,
page=page,
size=size,
days=days,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    q: str | Unset = UNSET,
    page: int | Unset = 1,
    size: int | Unset = 20,
    days: int | Unset = UNSET,

) -> PagedResultOfEmailCampaignDto | None:
    """ Lấy danh sách email campaigns

     Trả về danh sách phân trang các email campaign trong workspace. Có thể lọc theo status
    (Draft/Scheduled/Sending/Sent/…), từ khóa và `days` (chỉ lấy chiến dịch có ngày gửi/hẹn/tạo trong N
    ngày qua).

    Args:
        status (str | Unset):
        q (str | Unset):
        page (int | Unset):  Default: 1.
        size (int | Unset):  Default: 20.
        days (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedResultOfEmailCampaignDto
     """


    return (await asyncio_detailed(
        client=client,
status=status,
q=q,
page=page,
size=size,
days=days,

    )).parsed

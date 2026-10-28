from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paged_result_of_email_template_list_dto import PagedResultOfEmailTemplateListDto
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    category: str | Unset = UNSET,
    q: str | Unset = UNSET,
    page: int | Unset = 1,
    size: int | Unset = 20,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["category"] = category

    params["q"] = q

    params["page"] = page

    params["size"] = size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/marketing/email-templates",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PagedResultOfEmailTemplateListDto | None:
    if response.status_code == 200:
        response_200 = PagedResultOfEmailTemplateListDto.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PagedResultOfEmailTemplateListDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    category: str | Unset = UNSET,
    q: str | Unset = UNSET,
    page: int | Unset = 1,
    size: int | Unset = 20,

) -> Response[PagedResultOfEmailTemplateListDto]:
    """ Lấy danh sách email templates

     Trả về danh sách phân trang các email template trong workspace. Có thể lọc theo category và từ khóa.

    Args:
        category (str | Unset):
        q (str | Unset):
        page (int | Unset):  Default: 1.
        size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedResultOfEmailTemplateListDto]
     """


    kwargs = _get_kwargs(
        category=category,
q=q,
page=page,
size=size,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    category: str | Unset = UNSET,
    q: str | Unset = UNSET,
    page: int | Unset = 1,
    size: int | Unset = 20,

) -> PagedResultOfEmailTemplateListDto | None:
    """ Lấy danh sách email templates

     Trả về danh sách phân trang các email template trong workspace. Có thể lọc theo category và từ khóa.

    Args:
        category (str | Unset):
        q (str | Unset):
        page (int | Unset):  Default: 1.
        size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedResultOfEmailTemplateListDto
     """


    return sync_detailed(
        client=client,
category=category,
q=q,
page=page,
size=size,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    category: str | Unset = UNSET,
    q: str | Unset = UNSET,
    page: int | Unset = 1,
    size: int | Unset = 20,

) -> Response[PagedResultOfEmailTemplateListDto]:
    """ Lấy danh sách email templates

     Trả về danh sách phân trang các email template trong workspace. Có thể lọc theo category và từ khóa.

    Args:
        category (str | Unset):
        q (str | Unset):
        page (int | Unset):  Default: 1.
        size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedResultOfEmailTemplateListDto]
     """


    kwargs = _get_kwargs(
        category=category,
q=q,
page=page,
size=size,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    category: str | Unset = UNSET,
    q: str | Unset = UNSET,
    page: int | Unset = 1,
    size: int | Unset = 20,

) -> PagedResultOfEmailTemplateListDto | None:
    """ Lấy danh sách email templates

     Trả về danh sách phân trang các email template trong workspace. Có thể lọc theo category và từ khóa.

    Args:
        category (str | Unset):
        q (str | Unset):
        page (int | Unset):  Default: 1.
        size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedResultOfEmailTemplateListDto
     """


    return (await asyncio_detailed(
        client=client,
category=category,
q=q,
page=page,
size=size,

    )).parsed

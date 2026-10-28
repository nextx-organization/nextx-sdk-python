from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paged_result_of_lot_expiry_report_dto import PagedResultOfLotExpiryReportDto
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    days_threshold: int | Unset = 30,
    branch_id: UUID | Unset = UNSET,
    include_expired: bool | Unset = True,
    page_number: int | Unset = 1,
    page_size: int | Unset = 50,
    category_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["daysThreshold"] = days_threshold

    json_branch_id: str | Unset = UNSET
    if not isinstance(branch_id, Unset):
        json_branch_id = str(branch_id)
    params["branchId"] = json_branch_id

    params["includeExpired"] = include_expired

    params["pageNumber"] = page_number

    params["pageSize"] = page_size

    json_category_id: str | Unset = UNSET
    if not isinstance(category_id, Unset):
        json_category_id = str(category_id)
    params["categoryId"] = json_category_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sales/products/expiry-report",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PagedResultOfLotExpiryReportDto | None:
    if response.status_code == 200:
        response_200 = PagedResultOfLotExpiryReportDto.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PagedResultOfLotExpiryReportDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    days_threshold: int | Unset = 30,
    branch_id: UUID | Unset = UNSET,
    include_expired: bool | Unset = True,
    page_number: int | Unset = 1,
    page_size: int | Unset = 50,
    category_id: UUID | Unset = UNSET,

) -> Response[PagedResultOfLotExpiryReportDto]:
    """ Báo cáo lô hàng theo hạn sử dụng

     Trả về danh sách lô sắp hết hạn hoặc đã hết hạn trong khoảng N ngày. categoryId: lọc theo nhóm hàng
    hoá (gồm cả nhóm con).

    Args:
        days_threshold (int | Unset):  Default: 30.
        branch_id (UUID | Unset):
        include_expired (bool | Unset):  Default: True.
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        category_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedResultOfLotExpiryReportDto]
     """


    kwargs = _get_kwargs(
        days_threshold=days_threshold,
branch_id=branch_id,
include_expired=include_expired,
page_number=page_number,
page_size=page_size,
category_id=category_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    days_threshold: int | Unset = 30,
    branch_id: UUID | Unset = UNSET,
    include_expired: bool | Unset = True,
    page_number: int | Unset = 1,
    page_size: int | Unset = 50,
    category_id: UUID | Unset = UNSET,

) -> PagedResultOfLotExpiryReportDto | None:
    """ Báo cáo lô hàng theo hạn sử dụng

     Trả về danh sách lô sắp hết hạn hoặc đã hết hạn trong khoảng N ngày. categoryId: lọc theo nhóm hàng
    hoá (gồm cả nhóm con).

    Args:
        days_threshold (int | Unset):  Default: 30.
        branch_id (UUID | Unset):
        include_expired (bool | Unset):  Default: True.
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        category_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedResultOfLotExpiryReportDto
     """


    return sync_detailed(
        client=client,
days_threshold=days_threshold,
branch_id=branch_id,
include_expired=include_expired,
page_number=page_number,
page_size=page_size,
category_id=category_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    days_threshold: int | Unset = 30,
    branch_id: UUID | Unset = UNSET,
    include_expired: bool | Unset = True,
    page_number: int | Unset = 1,
    page_size: int | Unset = 50,
    category_id: UUID | Unset = UNSET,

) -> Response[PagedResultOfLotExpiryReportDto]:
    """ Báo cáo lô hàng theo hạn sử dụng

     Trả về danh sách lô sắp hết hạn hoặc đã hết hạn trong khoảng N ngày. categoryId: lọc theo nhóm hàng
    hoá (gồm cả nhóm con).

    Args:
        days_threshold (int | Unset):  Default: 30.
        branch_id (UUID | Unset):
        include_expired (bool | Unset):  Default: True.
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        category_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedResultOfLotExpiryReportDto]
     """


    kwargs = _get_kwargs(
        days_threshold=days_threshold,
branch_id=branch_id,
include_expired=include_expired,
page_number=page_number,
page_size=page_size,
category_id=category_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    days_threshold: int | Unset = 30,
    branch_id: UUID | Unset = UNSET,
    include_expired: bool | Unset = True,
    page_number: int | Unset = 1,
    page_size: int | Unset = 50,
    category_id: UUID | Unset = UNSET,

) -> PagedResultOfLotExpiryReportDto | None:
    """ Báo cáo lô hàng theo hạn sử dụng

     Trả về danh sách lô sắp hết hạn hoặc đã hết hạn trong khoảng N ngày. categoryId: lọc theo nhóm hàng
    hoá (gồm cả nhóm con).

    Args:
        days_threshold (int | Unset):  Default: 30.
        branch_id (UUID | Unset):
        include_expired (bool | Unset):  Default: True.
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        category_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedResultOfLotExpiryReportDto
     """


    return (await asyncio_detailed(
        client=client,
days_threshold=days_threshold,
branch_id=branch_id,
include_expired=include_expired,
page_number=page_number,
page_size=page_size,
category_id=category_id,

    )).parsed

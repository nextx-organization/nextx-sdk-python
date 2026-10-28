from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paged_result_of_unknown_lot_report_dto import PagedResultOfUnknownLotReportDto
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    *,
    branch_id: UUID | Unset = UNSET,
    sold_from: datetime.datetime | Unset = UNSET,
    sold_to: datetime.datetime | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 50,
    category_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_branch_id: str | Unset = UNSET
    if not isinstance(branch_id, Unset):
        json_branch_id = str(branch_id)
    params["branchId"] = json_branch_id

    json_sold_from: str | Unset = UNSET
    if not isinstance(sold_from, Unset):
        json_sold_from = sold_from.isoformat()
    params["soldFrom"] = json_sold_from

    json_sold_to: str | Unset = UNSET
    if not isinstance(sold_to, Unset):
        json_sold_to = sold_to.isoformat()
    params["soldTo"] = json_sold_to

    params["pageNumber"] = page_number

    params["pageSize"] = page_size

    json_category_id: str | Unset = UNSET
    if not isinstance(category_id, Unset):
        json_category_id = str(category_id)
    params["categoryId"] = json_category_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sales/products/unknown-lot-report",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PagedResultOfUnknownLotReportDto | None:
    if response.status_code == 200:
        response_200 = PagedResultOfUnknownLotReportDto.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PagedResultOfUnknownLotReportDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    branch_id: UUID | Unset = UNSET,
    sold_from: datetime.datetime | Unset = UNSET,
    sold_to: datetime.datetime | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 50,
    category_id: UUID | Unset = UNSET,

) -> Response[PagedResultOfUnknownLotReportDto]:
    """ Báo cáo hàng chưa xác định lô

     Mỗi (sản phẩm × chi nhánh) một dòng: còn treo bao nhiêu ở lô giữ chỗ "CHƯA-XÁC-ĐỊNH", và đã bán ra
    bao nhiêu mà không truy được về lô nhà sản xuất. Cột còn-treo phải TEO dần theo thời gian.
    categoryId: lọc theo nhóm hàng hoá (gồm cả nhóm con).

    Args:
        branch_id (UUID | Unset):
        sold_from (datetime.datetime | Unset):
        sold_to (datetime.datetime | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        category_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedResultOfUnknownLotReportDto]
     """


    kwargs = _get_kwargs(
        branch_id=branch_id,
sold_from=sold_from,
sold_to=sold_to,
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
    branch_id: UUID | Unset = UNSET,
    sold_from: datetime.datetime | Unset = UNSET,
    sold_to: datetime.datetime | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 50,
    category_id: UUID | Unset = UNSET,

) -> PagedResultOfUnknownLotReportDto | None:
    """ Báo cáo hàng chưa xác định lô

     Mỗi (sản phẩm × chi nhánh) một dòng: còn treo bao nhiêu ở lô giữ chỗ "CHƯA-XÁC-ĐỊNH", và đã bán ra
    bao nhiêu mà không truy được về lô nhà sản xuất. Cột còn-treo phải TEO dần theo thời gian.
    categoryId: lọc theo nhóm hàng hoá (gồm cả nhóm con).

    Args:
        branch_id (UUID | Unset):
        sold_from (datetime.datetime | Unset):
        sold_to (datetime.datetime | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        category_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedResultOfUnknownLotReportDto
     """


    return sync_detailed(
        client=client,
branch_id=branch_id,
sold_from=sold_from,
sold_to=sold_to,
page_number=page_number,
page_size=page_size,
category_id=category_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    branch_id: UUID | Unset = UNSET,
    sold_from: datetime.datetime | Unset = UNSET,
    sold_to: datetime.datetime | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 50,
    category_id: UUID | Unset = UNSET,

) -> Response[PagedResultOfUnknownLotReportDto]:
    """ Báo cáo hàng chưa xác định lô

     Mỗi (sản phẩm × chi nhánh) một dòng: còn treo bao nhiêu ở lô giữ chỗ "CHƯA-XÁC-ĐỊNH", và đã bán ra
    bao nhiêu mà không truy được về lô nhà sản xuất. Cột còn-treo phải TEO dần theo thời gian.
    categoryId: lọc theo nhóm hàng hoá (gồm cả nhóm con).

    Args:
        branch_id (UUID | Unset):
        sold_from (datetime.datetime | Unset):
        sold_to (datetime.datetime | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        category_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedResultOfUnknownLotReportDto]
     """


    kwargs = _get_kwargs(
        branch_id=branch_id,
sold_from=sold_from,
sold_to=sold_to,
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
    branch_id: UUID | Unset = UNSET,
    sold_from: datetime.datetime | Unset = UNSET,
    sold_to: datetime.datetime | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 50,
    category_id: UUID | Unset = UNSET,

) -> PagedResultOfUnknownLotReportDto | None:
    """ Báo cáo hàng chưa xác định lô

     Mỗi (sản phẩm × chi nhánh) một dòng: còn treo bao nhiêu ở lô giữ chỗ "CHƯA-XÁC-ĐỊNH", và đã bán ra
    bao nhiêu mà không truy được về lô nhà sản xuất. Cột còn-treo phải TEO dần theo thời gian.
    categoryId: lọc theo nhóm hàng hoá (gồm cả nhóm con).

    Args:
        branch_id (UUID | Unset):
        sold_from (datetime.datetime | Unset):
        sold_to (datetime.datetime | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        category_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedResultOfUnknownLotReportDto
     """


    return (await asyncio_detailed(
        client=client,
branch_id=branch_id,
sold_from=sold_from,
sold_to=sold_to,
page_number=page_number,
page_size=page_size,
category_id=category_id,

    )).parsed

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.stock_movement_list_result import StockMovementListResult
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    *,
    branch_id: UUID | Unset = UNSET,
    group: str | Unset = UNSET,
    product_id: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    date_from: datetime.datetime | Unset = UNSET,
    date_to: datetime.datetime | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    sort_by: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,
    category_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_branch_id: str | Unset = UNSET
    if not isinstance(branch_id, Unset):
        json_branch_id = str(branch_id)
    params["branchId"] = json_branch_id

    params["group"] = group

    json_product_id: str | Unset = UNSET
    if not isinstance(product_id, Unset):
        json_product_id = str(product_id)
    params["productId"] = json_product_id

    params["search"] = search

    json_date_from: str | Unset = UNSET
    if not isinstance(date_from, Unset):
        json_date_from = date_from.isoformat()
    params["dateFrom"] = json_date_from

    json_date_to: str | Unset = UNSET
    if not isinstance(date_to, Unset):
        json_date_to = date_to.isoformat()
    params["dateTo"] = json_date_to

    params["pageNumber"] = page_number

    params["pageSize"] = page_size

    params["sortBy"] = sort_by

    params["sortDir"] = sort_dir

    json_category_id: str | Unset = UNSET
    if not isinstance(category_id, Unset):
        json_category_id = str(category_id)
    params["categoryId"] = json_category_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sales/inventory/movements",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> StockMovementListResult | None:
    if response.status_code == 200:
        response_200 = StockMovementListResult.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[StockMovementListResult]:
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
    group: str | Unset = UNSET,
    product_id: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    date_from: datetime.datetime | Unset = UNSET,
    date_to: datetime.datetime | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    sort_by: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,
    category_id: UUID | Unset = UNSET,

) -> Response[StockMovementListResult]:
    """ Sổ cái biến động tồn kho toàn cục

     Hợp nhất nhập–xuất vật lý (stock_movements) + đặt giữ (stock_reservations) của mọi sản phẩm. Filter:
    branchId, group (RECEIPT/ISSUE/RETURN/ADJUST/TRANSFER/DISPOSAL/RESERVE), productId, search,
    dateFrom, dateTo. Mặc định FE lọc theo chi nhánh đang chọn. Server resolve sẵn tên SP / kho / người
    tạo / mã chứng từ. sortBy: quantity/type/before/balance/document (mặc định thời gian desc); sortDir:
    asc/desc. Tên SP / SKU / kho / người tạo / khách / nhóm hàng KHÔNG sort được: chúng được gắn SAU khi
    phân trang. categoryId: lọc theo nhóm hàng hoá (gồm cả nhóm con); mỗi dòng trả kèm
    categoryId/categoryName.

    Args:
        branch_id (UUID | Unset):
        group (str | Unset):
        product_id (UUID | Unset):
        search (str | Unset):
        date_from (datetime.datetime | Unset):
        date_to (datetime.datetime | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        sort_by (str | Unset):
        sort_dir (str | Unset):
        category_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StockMovementListResult]
     """


    kwargs = _get_kwargs(
        branch_id=branch_id,
group=group,
product_id=product_id,
search=search,
date_from=date_from,
date_to=date_to,
page_number=page_number,
page_size=page_size,
sort_by=sort_by,
sort_dir=sort_dir,
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
    group: str | Unset = UNSET,
    product_id: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    date_from: datetime.datetime | Unset = UNSET,
    date_to: datetime.datetime | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    sort_by: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,
    category_id: UUID | Unset = UNSET,

) -> StockMovementListResult | None:
    """ Sổ cái biến động tồn kho toàn cục

     Hợp nhất nhập–xuất vật lý (stock_movements) + đặt giữ (stock_reservations) của mọi sản phẩm. Filter:
    branchId, group (RECEIPT/ISSUE/RETURN/ADJUST/TRANSFER/DISPOSAL/RESERVE), productId, search,
    dateFrom, dateTo. Mặc định FE lọc theo chi nhánh đang chọn. Server resolve sẵn tên SP / kho / người
    tạo / mã chứng từ. sortBy: quantity/type/before/balance/document (mặc định thời gian desc); sortDir:
    asc/desc. Tên SP / SKU / kho / người tạo / khách / nhóm hàng KHÔNG sort được: chúng được gắn SAU khi
    phân trang. categoryId: lọc theo nhóm hàng hoá (gồm cả nhóm con); mỗi dòng trả kèm
    categoryId/categoryName.

    Args:
        branch_id (UUID | Unset):
        group (str | Unset):
        product_id (UUID | Unset):
        search (str | Unset):
        date_from (datetime.datetime | Unset):
        date_to (datetime.datetime | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        sort_by (str | Unset):
        sort_dir (str | Unset):
        category_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StockMovementListResult
     """


    return sync_detailed(
        client=client,
branch_id=branch_id,
group=group,
product_id=product_id,
search=search,
date_from=date_from,
date_to=date_to,
page_number=page_number,
page_size=page_size,
sort_by=sort_by,
sort_dir=sort_dir,
category_id=category_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    branch_id: UUID | Unset = UNSET,
    group: str | Unset = UNSET,
    product_id: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    date_from: datetime.datetime | Unset = UNSET,
    date_to: datetime.datetime | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    sort_by: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,
    category_id: UUID | Unset = UNSET,

) -> Response[StockMovementListResult]:
    """ Sổ cái biến động tồn kho toàn cục

     Hợp nhất nhập–xuất vật lý (stock_movements) + đặt giữ (stock_reservations) của mọi sản phẩm. Filter:
    branchId, group (RECEIPT/ISSUE/RETURN/ADJUST/TRANSFER/DISPOSAL/RESERVE), productId, search,
    dateFrom, dateTo. Mặc định FE lọc theo chi nhánh đang chọn. Server resolve sẵn tên SP / kho / người
    tạo / mã chứng từ. sortBy: quantity/type/before/balance/document (mặc định thời gian desc); sortDir:
    asc/desc. Tên SP / SKU / kho / người tạo / khách / nhóm hàng KHÔNG sort được: chúng được gắn SAU khi
    phân trang. categoryId: lọc theo nhóm hàng hoá (gồm cả nhóm con); mỗi dòng trả kèm
    categoryId/categoryName.

    Args:
        branch_id (UUID | Unset):
        group (str | Unset):
        product_id (UUID | Unset):
        search (str | Unset):
        date_from (datetime.datetime | Unset):
        date_to (datetime.datetime | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        sort_by (str | Unset):
        sort_dir (str | Unset):
        category_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StockMovementListResult]
     """


    kwargs = _get_kwargs(
        branch_id=branch_id,
group=group,
product_id=product_id,
search=search,
date_from=date_from,
date_to=date_to,
page_number=page_number,
page_size=page_size,
sort_by=sort_by,
sort_dir=sort_dir,
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
    group: str | Unset = UNSET,
    product_id: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    date_from: datetime.datetime | Unset = UNSET,
    date_to: datetime.datetime | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    sort_by: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,
    category_id: UUID | Unset = UNSET,

) -> StockMovementListResult | None:
    """ Sổ cái biến động tồn kho toàn cục

     Hợp nhất nhập–xuất vật lý (stock_movements) + đặt giữ (stock_reservations) của mọi sản phẩm. Filter:
    branchId, group (RECEIPT/ISSUE/RETURN/ADJUST/TRANSFER/DISPOSAL/RESERVE), productId, search,
    dateFrom, dateTo. Mặc định FE lọc theo chi nhánh đang chọn. Server resolve sẵn tên SP / kho / người
    tạo / mã chứng từ. sortBy: quantity/type/before/balance/document (mặc định thời gian desc); sortDir:
    asc/desc. Tên SP / SKU / kho / người tạo / khách / nhóm hàng KHÔNG sort được: chúng được gắn SAU khi
    phân trang. categoryId: lọc theo nhóm hàng hoá (gồm cả nhóm con); mỗi dòng trả kèm
    categoryId/categoryName.

    Args:
        branch_id (UUID | Unset):
        group (str | Unset):
        product_id (UUID | Unset):
        search (str | Unset):
        date_from (datetime.datetime | Unset):
        date_to (datetime.datetime | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        sort_by (str | Unset):
        sort_dir (str | Unset):
        category_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StockMovementListResult
     """


    return (await asyncio_detailed(
        client=client,
branch_id=branch_id,
group=group,
product_id=product_id,
search=search,
date_from=date_from,
date_to=date_to,
page_number=page_number,
page_size=page_size,
sort_by=sort_by,
sort_dir=sort_dir,
category_id=category_id,

    )).parsed

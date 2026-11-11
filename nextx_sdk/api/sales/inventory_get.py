from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paged_result_of_inventory_item_dto import PagedResultOfInventoryItemDto
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    branch_id: UUID | Unset = UNSET,
    product_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 50,
    search: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_branch_id: str | Unset = UNSET
    if not isinstance(branch_id, Unset):
        json_branch_id = str(branch_id)
    params["branchId"] = json_branch_id

    json_product_id: str | Unset = UNSET
    if not isinstance(product_id, Unset):
        json_product_id = str(product_id)
    params["productId"] = json_product_id

    params["status"] = status

    params["pageNumber"] = page_number

    params["pageSize"] = page_size

    params["search"] = search

    params["sortBy"] = sort_by

    params["sortDir"] = sort_dir


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sales/inventory",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PagedResultOfInventoryItemDto | None:
    if response.status_code == 200:
        response_200 = PagedResultOfInventoryItemDto.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PagedResultOfInventoryItemDto]:
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
    product_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 50,
    search: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,

) -> Response[PagedResultOfInventoryItemDto]:
    """ Tồn kho hiện tại theo chi nhánh

     Tổng hợp tồn kho theo chi nhánh (nguồn stock_by_branch). Filter: branchId, productId, status
    (out_of_stock|low_stock|in_stock), search (mã hoặc tên SP). sortBy:
    sku|name|onhand|reserved|available|avgcost|status (mặc định tên SP tăng dần), sortDir: asc|desc.
    Lọc/sắp xếp/phân trang chạy dưới SQL. pageSize = 0 → lấy TẤT CẢ.

    Args:
        branch_id (UUID | Unset):
        product_id (UUID | Unset):
        status (str | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        search (str | Unset):
        sort_by (str | Unset):
        sort_dir (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedResultOfInventoryItemDto]
     """


    kwargs = _get_kwargs(
        branch_id=branch_id,
product_id=product_id,
status=status,
page_number=page_number,
page_size=page_size,
search=search,
sort_by=sort_by,
sort_dir=sort_dir,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    branch_id: UUID | Unset = UNSET,
    product_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 50,
    search: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,

) -> PagedResultOfInventoryItemDto | None:
    """ Tồn kho hiện tại theo chi nhánh

     Tổng hợp tồn kho theo chi nhánh (nguồn stock_by_branch). Filter: branchId, productId, status
    (out_of_stock|low_stock|in_stock), search (mã hoặc tên SP). sortBy:
    sku|name|onhand|reserved|available|avgcost|status (mặc định tên SP tăng dần), sortDir: asc|desc.
    Lọc/sắp xếp/phân trang chạy dưới SQL. pageSize = 0 → lấy TẤT CẢ.

    Args:
        branch_id (UUID | Unset):
        product_id (UUID | Unset):
        status (str | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        search (str | Unset):
        sort_by (str | Unset):
        sort_dir (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedResultOfInventoryItemDto
     """


    return sync_detailed(
        client=client,
branch_id=branch_id,
product_id=product_id,
status=status,
page_number=page_number,
page_size=page_size,
search=search,
sort_by=sort_by,
sort_dir=sort_dir,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    branch_id: UUID | Unset = UNSET,
    product_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 50,
    search: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,

) -> Response[PagedResultOfInventoryItemDto]:
    """ Tồn kho hiện tại theo chi nhánh

     Tổng hợp tồn kho theo chi nhánh (nguồn stock_by_branch). Filter: branchId, productId, status
    (out_of_stock|low_stock|in_stock), search (mã hoặc tên SP). sortBy:
    sku|name|onhand|reserved|available|avgcost|status (mặc định tên SP tăng dần), sortDir: asc|desc.
    Lọc/sắp xếp/phân trang chạy dưới SQL. pageSize = 0 → lấy TẤT CẢ.

    Args:
        branch_id (UUID | Unset):
        product_id (UUID | Unset):
        status (str | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        search (str | Unset):
        sort_by (str | Unset):
        sort_dir (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedResultOfInventoryItemDto]
     """


    kwargs = _get_kwargs(
        branch_id=branch_id,
product_id=product_id,
status=status,
page_number=page_number,
page_size=page_size,
search=search,
sort_by=sort_by,
sort_dir=sort_dir,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    branch_id: UUID | Unset = UNSET,
    product_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 50,
    search: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,

) -> PagedResultOfInventoryItemDto | None:
    """ Tồn kho hiện tại theo chi nhánh

     Tổng hợp tồn kho theo chi nhánh (nguồn stock_by_branch). Filter: branchId, productId, status
    (out_of_stock|low_stock|in_stock), search (mã hoặc tên SP). sortBy:
    sku|name|onhand|reserved|available|avgcost|status (mặc định tên SP tăng dần), sortDir: asc|desc.
    Lọc/sắp xếp/phân trang chạy dưới SQL. pageSize = 0 → lấy TẤT CẢ.

    Args:
        branch_id (UUID | Unset):
        product_id (UUID | Unset):
        status (str | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        search (str | Unset):
        sort_by (str | Unset):
        sort_dir (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedResultOfInventoryItemDto
     """


    return (await asyncio_detailed(
        client=client,
branch_id=branch_id,
product_id=product_id,
status=status,
page_number=page_number,
page_size=page_size,
search=search,
sort_by=sort_by,
sort_dir=sort_dir,

    )).parsed

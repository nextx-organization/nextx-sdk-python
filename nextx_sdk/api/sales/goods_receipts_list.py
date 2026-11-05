from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.goods_receipt_list_result import GoodsReceiptListResult
from ...models.goods_receipts_list_column_filters import GoodsReceiptsListColumnFilters
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    *,
    search: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    supplier_id: UUID | Unset = UNSET,
    purchase_order_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    source: str | Unset = UNSET,
    payment_status: str | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    sort_by: str | Unset = UNSET,
    total_from: float | Unset = UNSET,
    total_to: float | Unset = UNSET,
    column_filters: GoodsReceiptsListColumnFilters | Unset = UNSET,
    bank_account_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["search"] = search

    json_branch_id: str | Unset = UNSET
    if not isinstance(branch_id, Unset):
        json_branch_id = str(branch_id)
    params["branchId"] = json_branch_id

    json_supplier_id: str | Unset = UNSET
    if not isinstance(supplier_id, Unset):
        json_supplier_id = str(supplier_id)
    params["supplierId"] = json_supplier_id

    json_purchase_order_id: str | Unset = UNSET
    if not isinstance(purchase_order_id, Unset):
        json_purchase_order_id = str(purchase_order_id)
    params["purchaseOrderId"] = json_purchase_order_id

    params["status"] = status

    params["source"] = source

    params["paymentStatus"] = payment_status

    json_from_date: str | Unset = UNSET
    if not isinstance(from_date, Unset):
        json_from_date = from_date.isoformat()
    params["fromDate"] = json_from_date

    json_to_date: str | Unset = UNSET
    if not isinstance(to_date, Unset):
        json_to_date = to_date.isoformat()
    params["toDate"] = json_to_date

    params["pageNumber"] = page_number

    params["pageSize"] = page_size

    params["sortBy"] = sort_by

    params["totalFrom"] = total_from

    params["totalTo"] = total_to

    json_column_filters: dict[str, Any] | Unset = UNSET
    if not isinstance(column_filters, Unset):
        json_column_filters = column_filters.to_dict()
    if not isinstance(json_column_filters, Unset):
        params.update(json_column_filters)


    json_bank_account_id: str | Unset = UNSET
    if not isinstance(bank_account_id, Unset):
        json_bank_account_id = str(bank_account_id)
    params["bankAccountId"] = json_bank_account_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sales/goods-receipts",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GoodsReceiptListResult | None:
    if response.status_code == 200:
        response_200 = GoodsReceiptListResult.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GoodsReceiptListResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    search: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    supplier_id: UUID | Unset = UNSET,
    purchase_order_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    source: str | Unset = UNSET,
    payment_status: str | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    sort_by: str | Unset = UNSET,
    total_from: float | Unset = UNSET,
    total_to: float | Unset = UNSET,
    column_filters: GoodsReceiptsListColumnFilters | Unset = UNSET,
    bank_account_id: UUID | Unset = UNSET,

) -> Response[GoodsReceiptListResult]:
    """ Danh sách phiếu nhập

     Hỗ trợ search theo mã phiếu, filter branch/supplier/status, pagination.

    Args:
        search (str | Unset):
        branch_id (UUID | Unset):
        supplier_id (UUID | Unset):
        purchase_order_id (UUID | Unset):
        status (str | Unset):
        source (str | Unset):
        payment_status (str | Unset):
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        sort_by (str | Unset):
        total_from (float | Unset):
        total_to (float | Unset):
        column_filters (GoodsReceiptsListColumnFilters | Unset):
        bank_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GoodsReceiptListResult]
     """


    kwargs = _get_kwargs(
        search=search,
branch_id=branch_id,
supplier_id=supplier_id,
purchase_order_id=purchase_order_id,
status=status,
source=source,
payment_status=payment_status,
from_date=from_date,
to_date=to_date,
page_number=page_number,
page_size=page_size,
sort_by=sort_by,
total_from=total_from,
total_to=total_to,
column_filters=column_filters,
bank_account_id=bank_account_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    search: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    supplier_id: UUID | Unset = UNSET,
    purchase_order_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    source: str | Unset = UNSET,
    payment_status: str | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    sort_by: str | Unset = UNSET,
    total_from: float | Unset = UNSET,
    total_to: float | Unset = UNSET,
    column_filters: GoodsReceiptsListColumnFilters | Unset = UNSET,
    bank_account_id: UUID | Unset = UNSET,

) -> GoodsReceiptListResult | None:
    """ Danh sách phiếu nhập

     Hỗ trợ search theo mã phiếu, filter branch/supplier/status, pagination.

    Args:
        search (str | Unset):
        branch_id (UUID | Unset):
        supplier_id (UUID | Unset):
        purchase_order_id (UUID | Unset):
        status (str | Unset):
        source (str | Unset):
        payment_status (str | Unset):
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        sort_by (str | Unset):
        total_from (float | Unset):
        total_to (float | Unset):
        column_filters (GoodsReceiptsListColumnFilters | Unset):
        bank_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GoodsReceiptListResult
     """


    return sync_detailed(
        client=client,
search=search,
branch_id=branch_id,
supplier_id=supplier_id,
purchase_order_id=purchase_order_id,
status=status,
source=source,
payment_status=payment_status,
from_date=from_date,
to_date=to_date,
page_number=page_number,
page_size=page_size,
sort_by=sort_by,
total_from=total_from,
total_to=total_to,
column_filters=column_filters,
bank_account_id=bank_account_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    search: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    supplier_id: UUID | Unset = UNSET,
    purchase_order_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    source: str | Unset = UNSET,
    payment_status: str | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    sort_by: str | Unset = UNSET,
    total_from: float | Unset = UNSET,
    total_to: float | Unset = UNSET,
    column_filters: GoodsReceiptsListColumnFilters | Unset = UNSET,
    bank_account_id: UUID | Unset = UNSET,

) -> Response[GoodsReceiptListResult]:
    """ Danh sách phiếu nhập

     Hỗ trợ search theo mã phiếu, filter branch/supplier/status, pagination.

    Args:
        search (str | Unset):
        branch_id (UUID | Unset):
        supplier_id (UUID | Unset):
        purchase_order_id (UUID | Unset):
        status (str | Unset):
        source (str | Unset):
        payment_status (str | Unset):
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        sort_by (str | Unset):
        total_from (float | Unset):
        total_to (float | Unset):
        column_filters (GoodsReceiptsListColumnFilters | Unset):
        bank_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GoodsReceiptListResult]
     """


    kwargs = _get_kwargs(
        search=search,
branch_id=branch_id,
supplier_id=supplier_id,
purchase_order_id=purchase_order_id,
status=status,
source=source,
payment_status=payment_status,
from_date=from_date,
to_date=to_date,
page_number=page_number,
page_size=page_size,
sort_by=sort_by,
total_from=total_from,
total_to=total_to,
column_filters=column_filters,
bank_account_id=bank_account_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    search: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    supplier_id: UUID | Unset = UNSET,
    purchase_order_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    source: str | Unset = UNSET,
    payment_status: str | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    sort_by: str | Unset = UNSET,
    total_from: float | Unset = UNSET,
    total_to: float | Unset = UNSET,
    column_filters: GoodsReceiptsListColumnFilters | Unset = UNSET,
    bank_account_id: UUID | Unset = UNSET,

) -> GoodsReceiptListResult | None:
    """ Danh sách phiếu nhập

     Hỗ trợ search theo mã phiếu, filter branch/supplier/status, pagination.

    Args:
        search (str | Unset):
        branch_id (UUID | Unset):
        supplier_id (UUID | Unset):
        purchase_order_id (UUID | Unset):
        status (str | Unset):
        source (str | Unset):
        payment_status (str | Unset):
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        sort_by (str | Unset):
        total_from (float | Unset):
        total_to (float | Unset):
        column_filters (GoodsReceiptsListColumnFilters | Unset):
        bank_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GoodsReceiptListResult
     """


    return (await asyncio_detailed(
        client=client,
search=search,
branch_id=branch_id,
supplier_id=supplier_id,
purchase_order_id=purchase_order_id,
status=status,
source=source,
payment_status=payment_status,
from_date=from_date,
to_date=to_date,
page_number=page_number,
page_size=page_size,
sort_by=sort_by,
total_from=total_from,
total_to=total_to,
column_filters=column_filters,
bank_account_id=bank_account_id,

    )).parsed

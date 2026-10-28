from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.orders_list_column_filters import OrdersListColumnFilters
from ...models.sales_order_paged_dto import SalesOrderPagedDto
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    *,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    source: str | Unset = UNSET,
    outlet_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    date_from: datetime.date | Unset = UNSET,
    date_to: datetime.date | Unset = UNSET,
    order_type: str | Unset = UNSET,
    search: str | Unset = UNSET,
    assigned_to: UUID | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    total_min: float | Unset = UNSET,
    total_max: float | Unset = UNSET,
    column_filters: OrdersListColumnFilters | Unset = UNSET,
    sort_by: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["pageSize"] = page_size

    params["source"] = source

    json_outlet_id: str | Unset = UNSET
    if not isinstance(outlet_id, Unset):
        json_outlet_id = str(outlet_id)
    params["outletId"] = json_outlet_id

    params["status"] = status

    json_date_from: str | Unset = UNSET
    if not isinstance(date_from, Unset):
        json_date_from = date_from.isoformat()
    params["dateFrom"] = json_date_from

    json_date_to: str | Unset = UNSET
    if not isinstance(date_to, Unset):
        json_date_to = date_to.isoformat()
    params["dateTo"] = json_date_to

    params["orderType"] = order_type

    params["search"] = search

    json_assigned_to: str | Unset = UNSET
    if not isinstance(assigned_to, Unset):
        json_assigned_to = str(assigned_to)
    params["assignedTo"] = json_assigned_to

    json_branch_id: str | Unset = UNSET
    if not isinstance(branch_id, Unset):
        json_branch_id = str(branch_id)
    params["branchId"] = json_branch_id

    params["totalMin"] = total_min

    params["totalMax"] = total_max

    json_column_filters: dict[str, Any] | Unset = UNSET
    if not isinstance(column_filters, Unset):
        json_column_filters = column_filters.to_dict()
    if not isinstance(json_column_filters, Unset):
        params.update(json_column_filters)


    params["sortBy"] = sort_by


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/dms/orders",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | SalesOrderPagedDto | None:
    if response.status_code == 200:
        response_200 = SalesOrderPagedDto.from_dict(response.json())



        return response_200

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | SalesOrderPagedDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    source: str | Unset = UNSET,
    outlet_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    date_from: datetime.date | Unset = UNSET,
    date_to: datetime.date | Unset = UNSET,
    order_type: str | Unset = UNSET,
    search: str | Unset = UNSET,
    assigned_to: UUID | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    total_min: float | Unset = UNSET,
    total_max: float | Unset = UNSET,
    column_filters: OrdersListColumnFilters | Unset = UNSET,
    sort_by: str | Unset = UNSET,

) -> Response[Any | SalesOrderPagedDto]:
    """ Danh sách đơn hàng

     Proxy Sales.GetOrders. Filter theo source, outlet, NV phụ trách, chi nhánh, status, ngày, khoảng giá
    trị đơn. Rep/Driver chỉ thấy đơn của mình — assignedTo giao với phạm vi, không mở rộng.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        source (str | Unset):
        outlet_id (UUID | Unset):
        status (str | Unset):
        date_from (datetime.date | Unset):
        date_to (datetime.date | Unset):
        order_type (str | Unset):
        search (str | Unset):
        assigned_to (UUID | Unset):
        branch_id (UUID | Unset):
        total_min (float | Unset):
        total_max (float | Unset):
        column_filters (OrdersListColumnFilters | Unset):
        sort_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SalesOrderPagedDto]
     """


    kwargs = _get_kwargs(
        page=page,
page_size=page_size,
source=source,
outlet_id=outlet_id,
status=status,
date_from=date_from,
date_to=date_to,
order_type=order_type,
search=search,
assigned_to=assigned_to,
branch_id=branch_id,
total_min=total_min,
total_max=total_max,
column_filters=column_filters,
sort_by=sort_by,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    source: str | Unset = UNSET,
    outlet_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    date_from: datetime.date | Unset = UNSET,
    date_to: datetime.date | Unset = UNSET,
    order_type: str | Unset = UNSET,
    search: str | Unset = UNSET,
    assigned_to: UUID | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    total_min: float | Unset = UNSET,
    total_max: float | Unset = UNSET,
    column_filters: OrdersListColumnFilters | Unset = UNSET,
    sort_by: str | Unset = UNSET,

) -> Any | SalesOrderPagedDto | None:
    """ Danh sách đơn hàng

     Proxy Sales.GetOrders. Filter theo source, outlet, NV phụ trách, chi nhánh, status, ngày, khoảng giá
    trị đơn. Rep/Driver chỉ thấy đơn của mình — assignedTo giao với phạm vi, không mở rộng.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        source (str | Unset):
        outlet_id (UUID | Unset):
        status (str | Unset):
        date_from (datetime.date | Unset):
        date_to (datetime.date | Unset):
        order_type (str | Unset):
        search (str | Unset):
        assigned_to (UUID | Unset):
        branch_id (UUID | Unset):
        total_min (float | Unset):
        total_max (float | Unset):
        column_filters (OrdersListColumnFilters | Unset):
        sort_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SalesOrderPagedDto
     """


    return sync_detailed(
        client=client,
page=page,
page_size=page_size,
source=source,
outlet_id=outlet_id,
status=status,
date_from=date_from,
date_to=date_to,
order_type=order_type,
search=search,
assigned_to=assigned_to,
branch_id=branch_id,
total_min=total_min,
total_max=total_max,
column_filters=column_filters,
sort_by=sort_by,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    source: str | Unset = UNSET,
    outlet_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    date_from: datetime.date | Unset = UNSET,
    date_to: datetime.date | Unset = UNSET,
    order_type: str | Unset = UNSET,
    search: str | Unset = UNSET,
    assigned_to: UUID | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    total_min: float | Unset = UNSET,
    total_max: float | Unset = UNSET,
    column_filters: OrdersListColumnFilters | Unset = UNSET,
    sort_by: str | Unset = UNSET,

) -> Response[Any | SalesOrderPagedDto]:
    """ Danh sách đơn hàng

     Proxy Sales.GetOrders. Filter theo source, outlet, NV phụ trách, chi nhánh, status, ngày, khoảng giá
    trị đơn. Rep/Driver chỉ thấy đơn của mình — assignedTo giao với phạm vi, không mở rộng.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        source (str | Unset):
        outlet_id (UUID | Unset):
        status (str | Unset):
        date_from (datetime.date | Unset):
        date_to (datetime.date | Unset):
        order_type (str | Unset):
        search (str | Unset):
        assigned_to (UUID | Unset):
        branch_id (UUID | Unset):
        total_min (float | Unset):
        total_max (float | Unset):
        column_filters (OrdersListColumnFilters | Unset):
        sort_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SalesOrderPagedDto]
     """


    kwargs = _get_kwargs(
        page=page,
page_size=page_size,
source=source,
outlet_id=outlet_id,
status=status,
date_from=date_from,
date_to=date_to,
order_type=order_type,
search=search,
assigned_to=assigned_to,
branch_id=branch_id,
total_min=total_min,
total_max=total_max,
column_filters=column_filters,
sort_by=sort_by,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    source: str | Unset = UNSET,
    outlet_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    date_from: datetime.date | Unset = UNSET,
    date_to: datetime.date | Unset = UNSET,
    order_type: str | Unset = UNSET,
    search: str | Unset = UNSET,
    assigned_to: UUID | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    total_min: float | Unset = UNSET,
    total_max: float | Unset = UNSET,
    column_filters: OrdersListColumnFilters | Unset = UNSET,
    sort_by: str | Unset = UNSET,

) -> Any | SalesOrderPagedDto | None:
    """ Danh sách đơn hàng

     Proxy Sales.GetOrders. Filter theo source, outlet, NV phụ trách, chi nhánh, status, ngày, khoảng giá
    trị đơn. Rep/Driver chỉ thấy đơn của mình — assignedTo giao với phạm vi, không mở rộng.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        source (str | Unset):
        outlet_id (UUID | Unset):
        status (str | Unset):
        date_from (datetime.date | Unset):
        date_to (datetime.date | Unset):
        order_type (str | Unset):
        search (str | Unset):
        assigned_to (UUID | Unset):
        branch_id (UUID | Unset):
        total_min (float | Unset):
        total_max (float | Unset):
        column_filters (OrdersListColumnFilters | Unset):
        sort_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SalesOrderPagedDto
     """


    return (await asyncio_detailed(
        client=client,
page=page,
page_size=page_size,
source=source,
outlet_id=outlet_id,
status=status,
date_from=date_from,
date_to=date_to,
order_type=order_type,
search=search,
assigned_to=assigned_to,
branch_id=branch_id,
total_min=total_min,
total_max=total_max,
column_filters=column_filters,
sort_by=sort_by,

    )).parsed

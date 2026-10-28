from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.export_orders_result import ExportOrdersResult
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    *,
    search: str | Unset = UNSET,
    status: str | Unset = UNSET,
    order_type: str | Unset = UNSET,
    payment_method: str | Unset = UNSET,
    customer_id: UUID | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    assigned_to: UUID | Unset = UNSET,
    date_from: datetime.datetime | Unset = UNSET,
    date_to: datetime.datetime | Unset = UNSET,
    export_type: str | Unset = UNSET,
    columns: list[str] | Unset = UNSET,
    order_ids: list[UUID] | Unset = UNSET,
    outlet_id: UUID | Unset = UNSET,
    delivery_employee_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["search"] = search

    params["status"] = status

    params["orderType"] = order_type

    params["paymentMethod"] = payment_method

    json_customer_id: str | Unset = UNSET
    if not isinstance(customer_id, Unset):
        json_customer_id = str(customer_id)
    params["customerId"] = json_customer_id

    json_branch_id: str | Unset = UNSET
    if not isinstance(branch_id, Unset):
        json_branch_id = str(branch_id)
    params["branchId"] = json_branch_id

    json_assigned_to: str | Unset = UNSET
    if not isinstance(assigned_to, Unset):
        json_assigned_to = str(assigned_to)
    params["assignedTo"] = json_assigned_to

    json_date_from: str | Unset = UNSET
    if not isinstance(date_from, Unset):
        json_date_from = date_from.isoformat()
    params["dateFrom"] = json_date_from

    json_date_to: str | Unset = UNSET
    if not isinstance(date_to, Unset):
        json_date_to = date_to.isoformat()
    params["dateTo"] = json_date_to

    params["exportType"] = export_type

    json_columns: list[str] | Unset = UNSET
    if not isinstance(columns, Unset):
        json_columns = columns


    params["columns"] = json_columns

    json_order_ids: list[str] | Unset = UNSET
    if not isinstance(order_ids, Unset):
        json_order_ids = []
        for order_ids_item_data in order_ids:
            order_ids_item = str(order_ids_item_data)
            json_order_ids.append(order_ids_item)


    params["orderIds"] = json_order_ids

    json_outlet_id: str | Unset = UNSET
    if not isinstance(outlet_id, Unset):
        json_outlet_id = str(outlet_id)
    params["outletId"] = json_outlet_id

    json_delivery_employee_id: str | Unset = UNSET
    if not isinstance(delivery_employee_id, Unset):
        json_delivery_employee_id = str(delivery_employee_id)
    params["deliveryEmployeeId"] = json_delivery_employee_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sales/orders/export",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ExportOrdersResult | None:
    if response.status_code == 200:
        response_200 = ExportOrdersResult.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ExportOrdersResult]:
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
    status: str | Unset = UNSET,
    order_type: str | Unset = UNSET,
    payment_method: str | Unset = UNSET,
    customer_id: UUID | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    assigned_to: UUID | Unset = UNSET,
    date_from: datetime.datetime | Unset = UNSET,
    date_to: datetime.datetime | Unset = UNSET,
    export_type: str | Unset = UNSET,
    columns: list[str] | Unset = UNSET,
    order_ids: list[UUID] | Unset = UNSET,
    outlet_id: UUID | Unset = UNSET,
    delivery_employee_id: UUID | Unset = UNSET,

) -> Response[ExportOrdersResult]:
    """ Xuất danh sách đơn hàng ra Excel

     Tạo async export job. Trả về jobId — poll GET /reports/export/{jobId} để lấy trạng thái và
    downloadUrl.

    Args:
        search (str | Unset):
        status (str | Unset):
        order_type (str | Unset):
        payment_method (str | Unset):
        customer_id (UUID | Unset):
        branch_id (UUID | Unset):
        assigned_to (UUID | Unset):
        date_from (datetime.datetime | Unset):
        date_to (datetime.datetime | Unset):
        export_type (str | Unset):
        columns (list[str] | Unset):
        order_ids (list[UUID] | Unset):
        outlet_id (UUID | Unset):
        delivery_employee_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExportOrdersResult]
     """


    kwargs = _get_kwargs(
        search=search,
status=status,
order_type=order_type,
payment_method=payment_method,
customer_id=customer_id,
branch_id=branch_id,
assigned_to=assigned_to,
date_from=date_from,
date_to=date_to,
export_type=export_type,
columns=columns,
order_ids=order_ids,
outlet_id=outlet_id,
delivery_employee_id=delivery_employee_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    search: str | Unset = UNSET,
    status: str | Unset = UNSET,
    order_type: str | Unset = UNSET,
    payment_method: str | Unset = UNSET,
    customer_id: UUID | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    assigned_to: UUID | Unset = UNSET,
    date_from: datetime.datetime | Unset = UNSET,
    date_to: datetime.datetime | Unset = UNSET,
    export_type: str | Unset = UNSET,
    columns: list[str] | Unset = UNSET,
    order_ids: list[UUID] | Unset = UNSET,
    outlet_id: UUID | Unset = UNSET,
    delivery_employee_id: UUID | Unset = UNSET,

) -> ExportOrdersResult | None:
    """ Xuất danh sách đơn hàng ra Excel

     Tạo async export job. Trả về jobId — poll GET /reports/export/{jobId} để lấy trạng thái và
    downloadUrl.

    Args:
        search (str | Unset):
        status (str | Unset):
        order_type (str | Unset):
        payment_method (str | Unset):
        customer_id (UUID | Unset):
        branch_id (UUID | Unset):
        assigned_to (UUID | Unset):
        date_from (datetime.datetime | Unset):
        date_to (datetime.datetime | Unset):
        export_type (str | Unset):
        columns (list[str] | Unset):
        order_ids (list[UUID] | Unset):
        outlet_id (UUID | Unset):
        delivery_employee_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExportOrdersResult
     """


    return sync_detailed(
        client=client,
search=search,
status=status,
order_type=order_type,
payment_method=payment_method,
customer_id=customer_id,
branch_id=branch_id,
assigned_to=assigned_to,
date_from=date_from,
date_to=date_to,
export_type=export_type,
columns=columns,
order_ids=order_ids,
outlet_id=outlet_id,
delivery_employee_id=delivery_employee_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    search: str | Unset = UNSET,
    status: str | Unset = UNSET,
    order_type: str | Unset = UNSET,
    payment_method: str | Unset = UNSET,
    customer_id: UUID | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    assigned_to: UUID | Unset = UNSET,
    date_from: datetime.datetime | Unset = UNSET,
    date_to: datetime.datetime | Unset = UNSET,
    export_type: str | Unset = UNSET,
    columns: list[str] | Unset = UNSET,
    order_ids: list[UUID] | Unset = UNSET,
    outlet_id: UUID | Unset = UNSET,
    delivery_employee_id: UUID | Unset = UNSET,

) -> Response[ExportOrdersResult]:
    """ Xuất danh sách đơn hàng ra Excel

     Tạo async export job. Trả về jobId — poll GET /reports/export/{jobId} để lấy trạng thái và
    downloadUrl.

    Args:
        search (str | Unset):
        status (str | Unset):
        order_type (str | Unset):
        payment_method (str | Unset):
        customer_id (UUID | Unset):
        branch_id (UUID | Unset):
        assigned_to (UUID | Unset):
        date_from (datetime.datetime | Unset):
        date_to (datetime.datetime | Unset):
        export_type (str | Unset):
        columns (list[str] | Unset):
        order_ids (list[UUID] | Unset):
        outlet_id (UUID | Unset):
        delivery_employee_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExportOrdersResult]
     """


    kwargs = _get_kwargs(
        search=search,
status=status,
order_type=order_type,
payment_method=payment_method,
customer_id=customer_id,
branch_id=branch_id,
assigned_to=assigned_to,
date_from=date_from,
date_to=date_to,
export_type=export_type,
columns=columns,
order_ids=order_ids,
outlet_id=outlet_id,
delivery_employee_id=delivery_employee_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    search: str | Unset = UNSET,
    status: str | Unset = UNSET,
    order_type: str | Unset = UNSET,
    payment_method: str | Unset = UNSET,
    customer_id: UUID | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    assigned_to: UUID | Unset = UNSET,
    date_from: datetime.datetime | Unset = UNSET,
    date_to: datetime.datetime | Unset = UNSET,
    export_type: str | Unset = UNSET,
    columns: list[str] | Unset = UNSET,
    order_ids: list[UUID] | Unset = UNSET,
    outlet_id: UUID | Unset = UNSET,
    delivery_employee_id: UUID | Unset = UNSET,

) -> ExportOrdersResult | None:
    """ Xuất danh sách đơn hàng ra Excel

     Tạo async export job. Trả về jobId — poll GET /reports/export/{jobId} để lấy trạng thái và
    downloadUrl.

    Args:
        search (str | Unset):
        status (str | Unset):
        order_type (str | Unset):
        payment_method (str | Unset):
        customer_id (UUID | Unset):
        branch_id (UUID | Unset):
        assigned_to (UUID | Unset):
        date_from (datetime.datetime | Unset):
        date_to (datetime.datetime | Unset):
        export_type (str | Unset):
        columns (list[str] | Unset):
        order_ids (list[UUID] | Unset):
        outlet_id (UUID | Unset):
        delivery_employee_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExportOrdersResult
     """


    return (await asyncio_detailed(
        client=client,
search=search,
status=status,
order_type=order_type,
payment_method=payment_method,
customer_id=customer_id,
branch_id=branch_id,
assigned_to=assigned_to,
date_from=date_from,
date_to=date_to,
export_type=export_type,
columns=columns,
order_ids=order_ids,
outlet_id=outlet_id,
delivery_employee_id=delivery_employee_id,

    )).parsed

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.order_stats_dto import OrderStatsDto
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    *,
    order_type: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    assigned_to: UUID | Unset = UNSET,
    date_from: datetime.datetime | Unset = UNSET,
    date_to: datetime.datetime | Unset = UNSET,
    search: str | Unset = UNSET,
    crm_contact_id: UUID | Unset = UNSET,
    payment_method: str | Unset = UNSET,
    created_by: UUID | Unset = UNSET,
    has_debt: bool | Unset = UNSET,
    outlet_id: UUID | Unset = UNSET,
    delivery_employee_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["orderType"] = order_type

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

    params["search"] = search

    json_crm_contact_id: str | Unset = UNSET
    if not isinstance(crm_contact_id, Unset):
        json_crm_contact_id = str(crm_contact_id)
    params["crmContactId"] = json_crm_contact_id

    params["paymentMethod"] = payment_method

    json_created_by: str | Unset = UNSET
    if not isinstance(created_by, Unset):
        json_created_by = str(created_by)
    params["createdBy"] = json_created_by

    params["hasDebt"] = has_debt

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
        "url": "/api/v1/sales/orders/stats",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OrderStatsDto | None:
    if response.status_code == 200:
        response_200 = OrderStatsDto.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OrderStatsDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    order_type: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    assigned_to: UUID | Unset = UNSET,
    date_from: datetime.datetime | Unset = UNSET,
    date_to: datetime.datetime | Unset = UNSET,
    search: str | Unset = UNSET,
    crm_contact_id: UUID | Unset = UNSET,
    payment_method: str | Unset = UNSET,
    created_by: UUID | Unset = UNSET,
    has_debt: bool | Unset = UNSET,
    outlet_id: UUID | Unset = UNSET,
    delivery_employee_id: UUID | Unset = UNSET,

) -> Response[OrderStatsDto]:
    """ Thống kê đơn hàng theo trạng thái

     Trả về số lượng đơn theo 4 nhóm: pending, processing, completed, cancelled. Áp dụng cùng bộ lọc với
    danh sách đơn hàng (trừ status).

    Args:
        order_type (str | Unset):
        branch_id (UUID | Unset):
        assigned_to (UUID | Unset):
        date_from (datetime.datetime | Unset):
        date_to (datetime.datetime | Unset):
        search (str | Unset):
        crm_contact_id (UUID | Unset):
        payment_method (str | Unset):
        created_by (UUID | Unset):
        has_debt (bool | Unset):
        outlet_id (UUID | Unset):
        delivery_employee_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrderStatsDto]
     """


    kwargs = _get_kwargs(
        order_type=order_type,
branch_id=branch_id,
assigned_to=assigned_to,
date_from=date_from,
date_to=date_to,
search=search,
crm_contact_id=crm_contact_id,
payment_method=payment_method,
created_by=created_by,
has_debt=has_debt,
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
    order_type: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    assigned_to: UUID | Unset = UNSET,
    date_from: datetime.datetime | Unset = UNSET,
    date_to: datetime.datetime | Unset = UNSET,
    search: str | Unset = UNSET,
    crm_contact_id: UUID | Unset = UNSET,
    payment_method: str | Unset = UNSET,
    created_by: UUID | Unset = UNSET,
    has_debt: bool | Unset = UNSET,
    outlet_id: UUID | Unset = UNSET,
    delivery_employee_id: UUID | Unset = UNSET,

) -> OrderStatsDto | None:
    """ Thống kê đơn hàng theo trạng thái

     Trả về số lượng đơn theo 4 nhóm: pending, processing, completed, cancelled. Áp dụng cùng bộ lọc với
    danh sách đơn hàng (trừ status).

    Args:
        order_type (str | Unset):
        branch_id (UUID | Unset):
        assigned_to (UUID | Unset):
        date_from (datetime.datetime | Unset):
        date_to (datetime.datetime | Unset):
        search (str | Unset):
        crm_contact_id (UUID | Unset):
        payment_method (str | Unset):
        created_by (UUID | Unset):
        has_debt (bool | Unset):
        outlet_id (UUID | Unset):
        delivery_employee_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrderStatsDto
     """


    return sync_detailed(
        client=client,
order_type=order_type,
branch_id=branch_id,
assigned_to=assigned_to,
date_from=date_from,
date_to=date_to,
search=search,
crm_contact_id=crm_contact_id,
payment_method=payment_method,
created_by=created_by,
has_debt=has_debt,
outlet_id=outlet_id,
delivery_employee_id=delivery_employee_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    order_type: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    assigned_to: UUID | Unset = UNSET,
    date_from: datetime.datetime | Unset = UNSET,
    date_to: datetime.datetime | Unset = UNSET,
    search: str | Unset = UNSET,
    crm_contact_id: UUID | Unset = UNSET,
    payment_method: str | Unset = UNSET,
    created_by: UUID | Unset = UNSET,
    has_debt: bool | Unset = UNSET,
    outlet_id: UUID | Unset = UNSET,
    delivery_employee_id: UUID | Unset = UNSET,

) -> Response[OrderStatsDto]:
    """ Thống kê đơn hàng theo trạng thái

     Trả về số lượng đơn theo 4 nhóm: pending, processing, completed, cancelled. Áp dụng cùng bộ lọc với
    danh sách đơn hàng (trừ status).

    Args:
        order_type (str | Unset):
        branch_id (UUID | Unset):
        assigned_to (UUID | Unset):
        date_from (datetime.datetime | Unset):
        date_to (datetime.datetime | Unset):
        search (str | Unset):
        crm_contact_id (UUID | Unset):
        payment_method (str | Unset):
        created_by (UUID | Unset):
        has_debt (bool | Unset):
        outlet_id (UUID | Unset):
        delivery_employee_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrderStatsDto]
     """


    kwargs = _get_kwargs(
        order_type=order_type,
branch_id=branch_id,
assigned_to=assigned_to,
date_from=date_from,
date_to=date_to,
search=search,
crm_contact_id=crm_contact_id,
payment_method=payment_method,
created_by=created_by,
has_debt=has_debt,
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
    order_type: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    assigned_to: UUID | Unset = UNSET,
    date_from: datetime.datetime | Unset = UNSET,
    date_to: datetime.datetime | Unset = UNSET,
    search: str | Unset = UNSET,
    crm_contact_id: UUID | Unset = UNSET,
    payment_method: str | Unset = UNSET,
    created_by: UUID | Unset = UNSET,
    has_debt: bool | Unset = UNSET,
    outlet_id: UUID | Unset = UNSET,
    delivery_employee_id: UUID | Unset = UNSET,

) -> OrderStatsDto | None:
    """ Thống kê đơn hàng theo trạng thái

     Trả về số lượng đơn theo 4 nhóm: pending, processing, completed, cancelled. Áp dụng cùng bộ lọc với
    danh sách đơn hàng (trừ status).

    Args:
        order_type (str | Unset):
        branch_id (UUID | Unset):
        assigned_to (UUID | Unset):
        date_from (datetime.datetime | Unset):
        date_to (datetime.datetime | Unset):
        search (str | Unset):
        crm_contact_id (UUID | Unset):
        payment_method (str | Unset):
        created_by (UUID | Unset):
        has_debt (bool | Unset):
        outlet_id (UUID | Unset):
        delivery_employee_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrderStatsDto
     """


    return (await asyncio_detailed(
        client=client,
order_type=order_type,
branch_id=branch_id,
assigned_to=assigned_to,
date_from=date_from,
date_to=date_to,
search=search,
crm_contact_id=crm_contact_id,
payment_method=payment_method,
created_by=created_by,
has_debt=has_debt,
outlet_id=outlet_id,
delivery_employee_id=delivery_employee_id,

    )).parsed

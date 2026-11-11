from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.order_return_list_result import OrderReturnListResult
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    *,
    status: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    order_id: UUID | Unset = UNSET,
    return_type: str | Unset = UNSET,
    date_from: datetime.datetime | Unset = UNSET,
    date_to: datetime.datetime | Unset = UNSET,
    search: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    reason: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    crm_contact_id: UUID | Unset = UNSET,
    outlet_id: UUID | Unset = UNSET,
    refund_bank_account_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["status"] = status

    params["pageNumber"] = page_number

    params["pageSize"] = page_size

    json_order_id: str | Unset = UNSET
    if not isinstance(order_id, Unset):
        json_order_id = str(order_id)
    params["orderId"] = json_order_id

    params["returnType"] = return_type

    json_date_from: str | Unset = UNSET
    if not isinstance(date_from, Unset):
        json_date_from = date_from.isoformat()
    params["dateFrom"] = json_date_from

    json_date_to: str | Unset = UNSET
    if not isinstance(date_to, Unset):
        json_date_to = date_to.isoformat()
    params["dateTo"] = json_date_to

    params["search"] = search

    json_branch_id: str | Unset = UNSET
    if not isinstance(branch_id, Unset):
        json_branch_id = str(branch_id)
    params["branchId"] = json_branch_id

    params["reason"] = reason

    params["sortBy"] = sort_by

    json_crm_contact_id: str | Unset = UNSET
    if not isinstance(crm_contact_id, Unset):
        json_crm_contact_id = str(crm_contact_id)
    params["crmContactId"] = json_crm_contact_id

    json_outlet_id: str | Unset = UNSET
    if not isinstance(outlet_id, Unset):
        json_outlet_id = str(outlet_id)
    params["outletId"] = json_outlet_id

    json_refund_bank_account_id: str | Unset = UNSET
    if not isinstance(refund_bank_account_id, Unset):
        json_refund_bank_account_id = str(refund_bank_account_id)
    params["refundBankAccountId"] = json_refund_bank_account_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sales/order-returns",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OrderReturnListResult | None:
    if response.status_code == 200:
        response_200 = OrderReturnListResult.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OrderReturnListResult]:
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
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    order_id: UUID | Unset = UNSET,
    return_type: str | Unset = UNSET,
    date_from: datetime.datetime | Unset = UNSET,
    date_to: datetime.datetime | Unset = UNSET,
    search: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    reason: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    crm_contact_id: UUID | Unset = UNSET,
    outlet_id: UUID | Unset = UNSET,
    refund_bank_account_id: UUID | Unset = UNSET,

) -> Response[OrderReturnListResult]:
    """ Danh sách đơn hoàn trả

     Filter: status, orderId, returnType, branchId, date range, reason (lý do trả hàng — so khớp chính
    xác), crmContactId, outletId (match cả phiếu tự ghi lẫn phiếu suy từ đơn gốc). Tìm kiếm theo mã
    phiếu hoàn.

    Args:
        status (str | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        order_id (UUID | Unset):
        return_type (str | Unset):
        date_from (datetime.datetime | Unset):
        date_to (datetime.datetime | Unset):
        search (str | Unset):
        branch_id (UUID | Unset):
        reason (str | Unset):
        sort_by (str | Unset):
        crm_contact_id (UUID | Unset):
        outlet_id (UUID | Unset):
        refund_bank_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrderReturnListResult]
     """


    kwargs = _get_kwargs(
        status=status,
page_number=page_number,
page_size=page_size,
order_id=order_id,
return_type=return_type,
date_from=date_from,
date_to=date_to,
search=search,
branch_id=branch_id,
reason=reason,
sort_by=sort_by,
crm_contact_id=crm_contact_id,
outlet_id=outlet_id,
refund_bank_account_id=refund_bank_account_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    order_id: UUID | Unset = UNSET,
    return_type: str | Unset = UNSET,
    date_from: datetime.datetime | Unset = UNSET,
    date_to: datetime.datetime | Unset = UNSET,
    search: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    reason: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    crm_contact_id: UUID | Unset = UNSET,
    outlet_id: UUID | Unset = UNSET,
    refund_bank_account_id: UUID | Unset = UNSET,

) -> OrderReturnListResult | None:
    """ Danh sách đơn hoàn trả

     Filter: status, orderId, returnType, branchId, date range, reason (lý do trả hàng — so khớp chính
    xác), crmContactId, outletId (match cả phiếu tự ghi lẫn phiếu suy từ đơn gốc). Tìm kiếm theo mã
    phiếu hoàn.

    Args:
        status (str | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        order_id (UUID | Unset):
        return_type (str | Unset):
        date_from (datetime.datetime | Unset):
        date_to (datetime.datetime | Unset):
        search (str | Unset):
        branch_id (UUID | Unset):
        reason (str | Unset):
        sort_by (str | Unset):
        crm_contact_id (UUID | Unset):
        outlet_id (UUID | Unset):
        refund_bank_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrderReturnListResult
     """


    return sync_detailed(
        client=client,
status=status,
page_number=page_number,
page_size=page_size,
order_id=order_id,
return_type=return_type,
date_from=date_from,
date_to=date_to,
search=search,
branch_id=branch_id,
reason=reason,
sort_by=sort_by,
crm_contact_id=crm_contact_id,
outlet_id=outlet_id,
refund_bank_account_id=refund_bank_account_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    order_id: UUID | Unset = UNSET,
    return_type: str | Unset = UNSET,
    date_from: datetime.datetime | Unset = UNSET,
    date_to: datetime.datetime | Unset = UNSET,
    search: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    reason: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    crm_contact_id: UUID | Unset = UNSET,
    outlet_id: UUID | Unset = UNSET,
    refund_bank_account_id: UUID | Unset = UNSET,

) -> Response[OrderReturnListResult]:
    """ Danh sách đơn hoàn trả

     Filter: status, orderId, returnType, branchId, date range, reason (lý do trả hàng — so khớp chính
    xác), crmContactId, outletId (match cả phiếu tự ghi lẫn phiếu suy từ đơn gốc). Tìm kiếm theo mã
    phiếu hoàn.

    Args:
        status (str | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        order_id (UUID | Unset):
        return_type (str | Unset):
        date_from (datetime.datetime | Unset):
        date_to (datetime.datetime | Unset):
        search (str | Unset):
        branch_id (UUID | Unset):
        reason (str | Unset):
        sort_by (str | Unset):
        crm_contact_id (UUID | Unset):
        outlet_id (UUID | Unset):
        refund_bank_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrderReturnListResult]
     """


    kwargs = _get_kwargs(
        status=status,
page_number=page_number,
page_size=page_size,
order_id=order_id,
return_type=return_type,
date_from=date_from,
date_to=date_to,
search=search,
branch_id=branch_id,
reason=reason,
sort_by=sort_by,
crm_contact_id=crm_contact_id,
outlet_id=outlet_id,
refund_bank_account_id=refund_bank_account_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    order_id: UUID | Unset = UNSET,
    return_type: str | Unset = UNSET,
    date_from: datetime.datetime | Unset = UNSET,
    date_to: datetime.datetime | Unset = UNSET,
    search: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    reason: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    crm_contact_id: UUID | Unset = UNSET,
    outlet_id: UUID | Unset = UNSET,
    refund_bank_account_id: UUID | Unset = UNSET,

) -> OrderReturnListResult | None:
    """ Danh sách đơn hoàn trả

     Filter: status, orderId, returnType, branchId, date range, reason (lý do trả hàng — so khớp chính
    xác), crmContactId, outletId (match cả phiếu tự ghi lẫn phiếu suy từ đơn gốc). Tìm kiếm theo mã
    phiếu hoàn.

    Args:
        status (str | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        order_id (UUID | Unset):
        return_type (str | Unset):
        date_from (datetime.datetime | Unset):
        date_to (datetime.datetime | Unset):
        search (str | Unset):
        branch_id (UUID | Unset):
        reason (str | Unset):
        sort_by (str | Unset):
        crm_contact_id (UUID | Unset):
        outlet_id (UUID | Unset):
        refund_bank_account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrderReturnListResult
     """


    return (await asyncio_detailed(
        client=client,
status=status,
page_number=page_number,
page_size=page_size,
order_id=order_id,
return_type=return_type,
date_from=date_from,
date_to=date_to,
search=search,
branch_id=branch_id,
reason=reason,
sort_by=sort_by,
crm_contact_id=crm_contact_id,
outlet_id=outlet_id,
refund_bank_account_id=refund_bank_account_id,

    )).parsed

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.order_list_result import OrderListResult
from ...models.problem_details import ProblemDetails
from ...models.sales_orders_list_column_filters import SalesOrdersListColumnFilters
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    *,
    order_type: str | Unset = UNSET,
    status: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    assigned_to: UUID | Unset = UNSET,
    date_from: datetime.datetime | Unset = UNSET,
    date_to: datetime.datetime | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    crm_contact_id: UUID | Unset = UNSET,
    payment_method: str | Unset = UNSET,
    created_by: UUID | Unset = UNSET,
    total_from: float | Unset = UNSET,
    total_to: float | Unset = UNSET,
    has_debt: bool | Unset = UNSET,
    is_deleted: bool | Unset = UNSET,
    source_pre_order_id: UUID | Unset = UNSET,
    channel_code: str | Unset = UNSET,
    hour_from: int | Unset = UNSET,
    hour_to: int | Unset = UNSET,
    product_id: UUID | Unset = UNSET,
    has_vat: bool | Unset = UNSET,
    vat_export_status: str | Unset = UNSET,
    paid_not_completed: bool | Unset = UNSET,
    column_filters: SalesOrdersListColumnFilters | Unset = UNSET,
    outlet_id: UUID | Unset = UNSET,
    delivery_employee_id: UUID | Unset = UNSET,
    include_payment_methods: bool | Unset = False,
    cash_account_id: UUID | Unset = UNSET,
    bank_account_id: UUID | Unset = UNSET,
    unassigned: bool | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["orderType"] = order_type

    params["status"] = status

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

    params["sortBy"] = sort_by

    params["pageNumber"] = page_number

    params["pageSize"] = page_size

    json_crm_contact_id: str | Unset = UNSET
    if not isinstance(crm_contact_id, Unset):
        json_crm_contact_id = str(crm_contact_id)
    params["crmContactId"] = json_crm_contact_id

    params["paymentMethod"] = payment_method

    json_created_by: str | Unset = UNSET
    if not isinstance(created_by, Unset):
        json_created_by = str(created_by)
    params["createdBy"] = json_created_by

    params["totalFrom"] = total_from

    params["totalTo"] = total_to

    params["hasDebt"] = has_debt

    params["isDeleted"] = is_deleted

    json_source_pre_order_id: str | Unset = UNSET
    if not isinstance(source_pre_order_id, Unset):
        json_source_pre_order_id = str(source_pre_order_id)
    params["sourcePreOrderId"] = json_source_pre_order_id

    params["channelCode"] = channel_code

    params["hourFrom"] = hour_from

    params["hourTo"] = hour_to

    json_product_id: str | Unset = UNSET
    if not isinstance(product_id, Unset):
        json_product_id = str(product_id)
    params["productId"] = json_product_id

    params["hasVat"] = has_vat

    params["vatExportStatus"] = vat_export_status

    params["paidNotCompleted"] = paid_not_completed

    json_column_filters: dict[str, Any] | Unset = UNSET
    if not isinstance(column_filters, Unset):
        json_column_filters = column_filters.to_dict()
    if not isinstance(json_column_filters, Unset):
        params.update(json_column_filters)


    json_outlet_id: str | Unset = UNSET
    if not isinstance(outlet_id, Unset):
        json_outlet_id = str(outlet_id)
    params["outletId"] = json_outlet_id

    json_delivery_employee_id: str | Unset = UNSET
    if not isinstance(delivery_employee_id, Unset):
        json_delivery_employee_id = str(delivery_employee_id)
    params["deliveryEmployeeId"] = json_delivery_employee_id

    params["includePaymentMethods"] = include_payment_methods

    json_cash_account_id: str | Unset = UNSET
    if not isinstance(cash_account_id, Unset):
        json_cash_account_id = str(cash_account_id)
    params["cashAccountId"] = json_cash_account_id

    json_bank_account_id: str | Unset = UNSET
    if not isinstance(bank_account_id, Unset):
        json_bank_account_id = str(bank_account_id)
    params["bankAccountId"] = json_bank_account_id

    params["unassigned"] = unassigned


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sales/orders",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OrderListResult | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = OrderListResult.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ProblemDetails.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OrderListResult | ProblemDetails]:
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
    status: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    assigned_to: UUID | Unset = UNSET,
    date_from: datetime.datetime | Unset = UNSET,
    date_to: datetime.datetime | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    crm_contact_id: UUID | Unset = UNSET,
    payment_method: str | Unset = UNSET,
    created_by: UUID | Unset = UNSET,
    total_from: float | Unset = UNSET,
    total_to: float | Unset = UNSET,
    has_debt: bool | Unset = UNSET,
    is_deleted: bool | Unset = UNSET,
    source_pre_order_id: UUID | Unset = UNSET,
    channel_code: str | Unset = UNSET,
    hour_from: int | Unset = UNSET,
    hour_to: int | Unset = UNSET,
    product_id: UUID | Unset = UNSET,
    has_vat: bool | Unset = UNSET,
    vat_export_status: str | Unset = UNSET,
    paid_not_completed: bool | Unset = UNSET,
    column_filters: SalesOrdersListColumnFilters | Unset = UNSET,
    outlet_id: UUID | Unset = UNSET,
    delivery_employee_id: UUID | Unset = UNSET,
    include_payment_methods: bool | Unset = False,
    cash_account_id: UUID | Unset = UNSET,
    bank_account_id: UUID | Unset = UNSET,
    unassigned: bool | Unset = UNSET,

) -> Response[OrderListResult | ProblemDetails]:
    """ Danh sách đơn hàng

     Filter: type, status, branch, date, khách hàng, phương thức thanh toán, người tạo, khoảng tiền, có
    công nợ, khung giờ của ngày đặt đơn (order_date ?? created_at) theo giờ VN (hourFrom/hourTo, 0-23,
    hourFrom <= hourTo), sản phẩm trong đơn (productId), đơn đã thu đủ tiền nhưng chưa hoàn thành
    (paidNotCompleted), điểm bán (outletId), NV giao hàng đã gán (deliveryEmployeeId). Tìm kiếm theo mã
    đơn / ghi chú. Sort: code, total, paid, debt, created_at, confirmed_at, completed_at, order_date.
    Kèm summary (Σ tổng tiền / đã thu / còn nợ theo bộ lọc). paymentBreakdown của mỗi đơn = tiền đã thu
    theo từng PTTT, gom từ phiếu thu (fallback payment_breakdown_json → payment_method).
    includePaymentMethods=true trả thêm paymentMethodsPresent = tập mã PTTT của TOÀN BỘ tập đã lọc để
    dựng cột động — ĐẮT (2 truy vấn quét cả tập), gửi khi đổi bộ lọc chứ đừng gửi mỗi lần lật trang.

    Args:
        order_type (str | Unset):
        status (str | Unset):
        branch_id (UUID | Unset):
        assigned_to (UUID | Unset):
        date_from (datetime.datetime | Unset):
        date_to (datetime.datetime | Unset):
        search (str | Unset):
        sort_by (str | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        crm_contact_id (UUID | Unset):
        payment_method (str | Unset):
        created_by (UUID | Unset):
        total_from (float | Unset):
        total_to (float | Unset):
        has_debt (bool | Unset):
        is_deleted (bool | Unset):
        source_pre_order_id (UUID | Unset):
        channel_code (str | Unset):
        hour_from (int | Unset):
        hour_to (int | Unset):
        product_id (UUID | Unset):
        has_vat (bool | Unset):
        vat_export_status (str | Unset):
        paid_not_completed (bool | Unset):
        column_filters (SalesOrdersListColumnFilters | Unset):
        outlet_id (UUID | Unset):
        delivery_employee_id (UUID | Unset):
        include_payment_methods (bool | Unset):  Default: False.
        cash_account_id (UUID | Unset):
        bank_account_id (UUID | Unset):
        unassigned (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrderListResult | ProblemDetails]
     """


    kwargs = _get_kwargs(
        order_type=order_type,
status=status,
branch_id=branch_id,
assigned_to=assigned_to,
date_from=date_from,
date_to=date_to,
search=search,
sort_by=sort_by,
page_number=page_number,
page_size=page_size,
crm_contact_id=crm_contact_id,
payment_method=payment_method,
created_by=created_by,
total_from=total_from,
total_to=total_to,
has_debt=has_debt,
is_deleted=is_deleted,
source_pre_order_id=source_pre_order_id,
channel_code=channel_code,
hour_from=hour_from,
hour_to=hour_to,
product_id=product_id,
has_vat=has_vat,
vat_export_status=vat_export_status,
paid_not_completed=paid_not_completed,
column_filters=column_filters,
outlet_id=outlet_id,
delivery_employee_id=delivery_employee_id,
include_payment_methods=include_payment_methods,
cash_account_id=cash_account_id,
bank_account_id=bank_account_id,
unassigned=unassigned,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    order_type: str | Unset = UNSET,
    status: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    assigned_to: UUID | Unset = UNSET,
    date_from: datetime.datetime | Unset = UNSET,
    date_to: datetime.datetime | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    crm_contact_id: UUID | Unset = UNSET,
    payment_method: str | Unset = UNSET,
    created_by: UUID | Unset = UNSET,
    total_from: float | Unset = UNSET,
    total_to: float | Unset = UNSET,
    has_debt: bool | Unset = UNSET,
    is_deleted: bool | Unset = UNSET,
    source_pre_order_id: UUID | Unset = UNSET,
    channel_code: str | Unset = UNSET,
    hour_from: int | Unset = UNSET,
    hour_to: int | Unset = UNSET,
    product_id: UUID | Unset = UNSET,
    has_vat: bool | Unset = UNSET,
    vat_export_status: str | Unset = UNSET,
    paid_not_completed: bool | Unset = UNSET,
    column_filters: SalesOrdersListColumnFilters | Unset = UNSET,
    outlet_id: UUID | Unset = UNSET,
    delivery_employee_id: UUID | Unset = UNSET,
    include_payment_methods: bool | Unset = False,
    cash_account_id: UUID | Unset = UNSET,
    bank_account_id: UUID | Unset = UNSET,
    unassigned: bool | Unset = UNSET,

) -> OrderListResult | ProblemDetails | None:
    """ Danh sách đơn hàng

     Filter: type, status, branch, date, khách hàng, phương thức thanh toán, người tạo, khoảng tiền, có
    công nợ, khung giờ của ngày đặt đơn (order_date ?? created_at) theo giờ VN (hourFrom/hourTo, 0-23,
    hourFrom <= hourTo), sản phẩm trong đơn (productId), đơn đã thu đủ tiền nhưng chưa hoàn thành
    (paidNotCompleted), điểm bán (outletId), NV giao hàng đã gán (deliveryEmployeeId). Tìm kiếm theo mã
    đơn / ghi chú. Sort: code, total, paid, debt, created_at, confirmed_at, completed_at, order_date.
    Kèm summary (Σ tổng tiền / đã thu / còn nợ theo bộ lọc). paymentBreakdown của mỗi đơn = tiền đã thu
    theo từng PTTT, gom từ phiếu thu (fallback payment_breakdown_json → payment_method).
    includePaymentMethods=true trả thêm paymentMethodsPresent = tập mã PTTT của TOÀN BỘ tập đã lọc để
    dựng cột động — ĐẮT (2 truy vấn quét cả tập), gửi khi đổi bộ lọc chứ đừng gửi mỗi lần lật trang.

    Args:
        order_type (str | Unset):
        status (str | Unset):
        branch_id (UUID | Unset):
        assigned_to (UUID | Unset):
        date_from (datetime.datetime | Unset):
        date_to (datetime.datetime | Unset):
        search (str | Unset):
        sort_by (str | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        crm_contact_id (UUID | Unset):
        payment_method (str | Unset):
        created_by (UUID | Unset):
        total_from (float | Unset):
        total_to (float | Unset):
        has_debt (bool | Unset):
        is_deleted (bool | Unset):
        source_pre_order_id (UUID | Unset):
        channel_code (str | Unset):
        hour_from (int | Unset):
        hour_to (int | Unset):
        product_id (UUID | Unset):
        has_vat (bool | Unset):
        vat_export_status (str | Unset):
        paid_not_completed (bool | Unset):
        column_filters (SalesOrdersListColumnFilters | Unset):
        outlet_id (UUID | Unset):
        delivery_employee_id (UUID | Unset):
        include_payment_methods (bool | Unset):  Default: False.
        cash_account_id (UUID | Unset):
        bank_account_id (UUID | Unset):
        unassigned (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrderListResult | ProblemDetails
     """


    return sync_detailed(
        client=client,
order_type=order_type,
status=status,
branch_id=branch_id,
assigned_to=assigned_to,
date_from=date_from,
date_to=date_to,
search=search,
sort_by=sort_by,
page_number=page_number,
page_size=page_size,
crm_contact_id=crm_contact_id,
payment_method=payment_method,
created_by=created_by,
total_from=total_from,
total_to=total_to,
has_debt=has_debt,
is_deleted=is_deleted,
source_pre_order_id=source_pre_order_id,
channel_code=channel_code,
hour_from=hour_from,
hour_to=hour_to,
product_id=product_id,
has_vat=has_vat,
vat_export_status=vat_export_status,
paid_not_completed=paid_not_completed,
column_filters=column_filters,
outlet_id=outlet_id,
delivery_employee_id=delivery_employee_id,
include_payment_methods=include_payment_methods,
cash_account_id=cash_account_id,
bank_account_id=bank_account_id,
unassigned=unassigned,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    order_type: str | Unset = UNSET,
    status: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    assigned_to: UUID | Unset = UNSET,
    date_from: datetime.datetime | Unset = UNSET,
    date_to: datetime.datetime | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    crm_contact_id: UUID | Unset = UNSET,
    payment_method: str | Unset = UNSET,
    created_by: UUID | Unset = UNSET,
    total_from: float | Unset = UNSET,
    total_to: float | Unset = UNSET,
    has_debt: bool | Unset = UNSET,
    is_deleted: bool | Unset = UNSET,
    source_pre_order_id: UUID | Unset = UNSET,
    channel_code: str | Unset = UNSET,
    hour_from: int | Unset = UNSET,
    hour_to: int | Unset = UNSET,
    product_id: UUID | Unset = UNSET,
    has_vat: bool | Unset = UNSET,
    vat_export_status: str | Unset = UNSET,
    paid_not_completed: bool | Unset = UNSET,
    column_filters: SalesOrdersListColumnFilters | Unset = UNSET,
    outlet_id: UUID | Unset = UNSET,
    delivery_employee_id: UUID | Unset = UNSET,
    include_payment_methods: bool | Unset = False,
    cash_account_id: UUID | Unset = UNSET,
    bank_account_id: UUID | Unset = UNSET,
    unassigned: bool | Unset = UNSET,

) -> Response[OrderListResult | ProblemDetails]:
    """ Danh sách đơn hàng

     Filter: type, status, branch, date, khách hàng, phương thức thanh toán, người tạo, khoảng tiền, có
    công nợ, khung giờ của ngày đặt đơn (order_date ?? created_at) theo giờ VN (hourFrom/hourTo, 0-23,
    hourFrom <= hourTo), sản phẩm trong đơn (productId), đơn đã thu đủ tiền nhưng chưa hoàn thành
    (paidNotCompleted), điểm bán (outletId), NV giao hàng đã gán (deliveryEmployeeId). Tìm kiếm theo mã
    đơn / ghi chú. Sort: code, total, paid, debt, created_at, confirmed_at, completed_at, order_date.
    Kèm summary (Σ tổng tiền / đã thu / còn nợ theo bộ lọc). paymentBreakdown của mỗi đơn = tiền đã thu
    theo từng PTTT, gom từ phiếu thu (fallback payment_breakdown_json → payment_method).
    includePaymentMethods=true trả thêm paymentMethodsPresent = tập mã PTTT của TOÀN BỘ tập đã lọc để
    dựng cột động — ĐẮT (2 truy vấn quét cả tập), gửi khi đổi bộ lọc chứ đừng gửi mỗi lần lật trang.

    Args:
        order_type (str | Unset):
        status (str | Unset):
        branch_id (UUID | Unset):
        assigned_to (UUID | Unset):
        date_from (datetime.datetime | Unset):
        date_to (datetime.datetime | Unset):
        search (str | Unset):
        sort_by (str | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        crm_contact_id (UUID | Unset):
        payment_method (str | Unset):
        created_by (UUID | Unset):
        total_from (float | Unset):
        total_to (float | Unset):
        has_debt (bool | Unset):
        is_deleted (bool | Unset):
        source_pre_order_id (UUID | Unset):
        channel_code (str | Unset):
        hour_from (int | Unset):
        hour_to (int | Unset):
        product_id (UUID | Unset):
        has_vat (bool | Unset):
        vat_export_status (str | Unset):
        paid_not_completed (bool | Unset):
        column_filters (SalesOrdersListColumnFilters | Unset):
        outlet_id (UUID | Unset):
        delivery_employee_id (UUID | Unset):
        include_payment_methods (bool | Unset):  Default: False.
        cash_account_id (UUID | Unset):
        bank_account_id (UUID | Unset):
        unassigned (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrderListResult | ProblemDetails]
     """


    kwargs = _get_kwargs(
        order_type=order_type,
status=status,
branch_id=branch_id,
assigned_to=assigned_to,
date_from=date_from,
date_to=date_to,
search=search,
sort_by=sort_by,
page_number=page_number,
page_size=page_size,
crm_contact_id=crm_contact_id,
payment_method=payment_method,
created_by=created_by,
total_from=total_from,
total_to=total_to,
has_debt=has_debt,
is_deleted=is_deleted,
source_pre_order_id=source_pre_order_id,
channel_code=channel_code,
hour_from=hour_from,
hour_to=hour_to,
product_id=product_id,
has_vat=has_vat,
vat_export_status=vat_export_status,
paid_not_completed=paid_not_completed,
column_filters=column_filters,
outlet_id=outlet_id,
delivery_employee_id=delivery_employee_id,
include_payment_methods=include_payment_methods,
cash_account_id=cash_account_id,
bank_account_id=bank_account_id,
unassigned=unassigned,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    order_type: str | Unset = UNSET,
    status: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    assigned_to: UUID | Unset = UNSET,
    date_from: datetime.datetime | Unset = UNSET,
    date_to: datetime.datetime | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    crm_contact_id: UUID | Unset = UNSET,
    payment_method: str | Unset = UNSET,
    created_by: UUID | Unset = UNSET,
    total_from: float | Unset = UNSET,
    total_to: float | Unset = UNSET,
    has_debt: bool | Unset = UNSET,
    is_deleted: bool | Unset = UNSET,
    source_pre_order_id: UUID | Unset = UNSET,
    channel_code: str | Unset = UNSET,
    hour_from: int | Unset = UNSET,
    hour_to: int | Unset = UNSET,
    product_id: UUID | Unset = UNSET,
    has_vat: bool | Unset = UNSET,
    vat_export_status: str | Unset = UNSET,
    paid_not_completed: bool | Unset = UNSET,
    column_filters: SalesOrdersListColumnFilters | Unset = UNSET,
    outlet_id: UUID | Unset = UNSET,
    delivery_employee_id: UUID | Unset = UNSET,
    include_payment_methods: bool | Unset = False,
    cash_account_id: UUID | Unset = UNSET,
    bank_account_id: UUID | Unset = UNSET,
    unassigned: bool | Unset = UNSET,

) -> OrderListResult | ProblemDetails | None:
    """ Danh sách đơn hàng

     Filter: type, status, branch, date, khách hàng, phương thức thanh toán, người tạo, khoảng tiền, có
    công nợ, khung giờ của ngày đặt đơn (order_date ?? created_at) theo giờ VN (hourFrom/hourTo, 0-23,
    hourFrom <= hourTo), sản phẩm trong đơn (productId), đơn đã thu đủ tiền nhưng chưa hoàn thành
    (paidNotCompleted), điểm bán (outletId), NV giao hàng đã gán (deliveryEmployeeId). Tìm kiếm theo mã
    đơn / ghi chú. Sort: code, total, paid, debt, created_at, confirmed_at, completed_at, order_date.
    Kèm summary (Σ tổng tiền / đã thu / còn nợ theo bộ lọc). paymentBreakdown của mỗi đơn = tiền đã thu
    theo từng PTTT, gom từ phiếu thu (fallback payment_breakdown_json → payment_method).
    includePaymentMethods=true trả thêm paymentMethodsPresent = tập mã PTTT của TOÀN BỘ tập đã lọc để
    dựng cột động — ĐẮT (2 truy vấn quét cả tập), gửi khi đổi bộ lọc chứ đừng gửi mỗi lần lật trang.

    Args:
        order_type (str | Unset):
        status (str | Unset):
        branch_id (UUID | Unset):
        assigned_to (UUID | Unset):
        date_from (datetime.datetime | Unset):
        date_to (datetime.datetime | Unset):
        search (str | Unset):
        sort_by (str | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        crm_contact_id (UUID | Unset):
        payment_method (str | Unset):
        created_by (UUID | Unset):
        total_from (float | Unset):
        total_to (float | Unset):
        has_debt (bool | Unset):
        is_deleted (bool | Unset):
        source_pre_order_id (UUID | Unset):
        channel_code (str | Unset):
        hour_from (int | Unset):
        hour_to (int | Unset):
        product_id (UUID | Unset):
        has_vat (bool | Unset):
        vat_export_status (str | Unset):
        paid_not_completed (bool | Unset):
        column_filters (SalesOrdersListColumnFilters | Unset):
        outlet_id (UUID | Unset):
        delivery_employee_id (UUID | Unset):
        include_payment_methods (bool | Unset):  Default: False.
        cash_account_id (UUID | Unset):
        bank_account_id (UUID | Unset):
        unassigned (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrderListResult | ProblemDetails
     """


    return (await asyncio_detailed(
        client=client,
order_type=order_type,
status=status,
branch_id=branch_id,
assigned_to=assigned_to,
date_from=date_from,
date_to=date_to,
search=search,
sort_by=sort_by,
page_number=page_number,
page_size=page_size,
crm_contact_id=crm_contact_id,
payment_method=payment_method,
created_by=created_by,
total_from=total_from,
total_to=total_to,
has_debt=has_debt,
is_deleted=is_deleted,
source_pre_order_id=source_pre_order_id,
channel_code=channel_code,
hour_from=hour_from,
hour_to=hour_to,
product_id=product_id,
has_vat=has_vat,
vat_export_status=vat_export_status,
paid_not_completed=paid_not_completed,
column_filters=column_filters,
outlet_id=outlet_id,
delivery_employee_id=delivery_employee_id,
include_payment_methods=include_payment_methods,
cash_account_id=cash_account_id,
bank_account_id=bank_account_id,
unassigned=unassigned,

    )).parsed

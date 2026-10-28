from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.customer_list_result import CustomerListResult
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    *,
    group_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    customer_type: str | Unset = UNSET,
    search: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    smart_view: str | Unset = UNSET,
    crm_contact_id: UUID | Unset = UNSET,
    assigned_to: UUID | Unset = UNSET,
    created_from: datetime.datetime | Unset = UNSET,
    created_to: datetime.datetime | Unset = UNSET,
    gender: str | Unset = UNSET,
    birthday_month: int | Unset = UNSET,
    last_txn_from: datetime.datetime | Unset = UNSET,
    last_txn_to: datetime.datetime | Unset = UNSET,
    revenue_from: float | Unset = UNSET,
    revenue_to: float | Unset = UNSET,
    debt_from: float | Unset = UNSET,
    debt_to: float | Unset = UNSET,
    created_by: UUID | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,
    f: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_group_id: str | Unset = UNSET
    if not isinstance(group_id, Unset):
        json_group_id = str(group_id)
    params["groupId"] = json_group_id

    params["status"] = status

    params["customerType"] = customer_type

    params["search"] = search

    params["pageNumber"] = page_number

    params["pageSize"] = page_size

    params["smartView"] = smart_view

    json_crm_contact_id: str | Unset = UNSET
    if not isinstance(crm_contact_id, Unset):
        json_crm_contact_id = str(crm_contact_id)
    params["crmContactId"] = json_crm_contact_id

    json_assigned_to: str | Unset = UNSET
    if not isinstance(assigned_to, Unset):
        json_assigned_to = str(assigned_to)
    params["assignedTo"] = json_assigned_to

    json_created_from: str | Unset = UNSET
    if not isinstance(created_from, Unset):
        json_created_from = created_from.isoformat()
    params["createdFrom"] = json_created_from

    json_created_to: str | Unset = UNSET
    if not isinstance(created_to, Unset):
        json_created_to = created_to.isoformat()
    params["createdTo"] = json_created_to

    params["gender"] = gender

    params["birthdayMonth"] = birthday_month

    json_last_txn_from: str | Unset = UNSET
    if not isinstance(last_txn_from, Unset):
        json_last_txn_from = last_txn_from.isoformat()
    params["lastTxnFrom"] = json_last_txn_from

    json_last_txn_to: str | Unset = UNSET
    if not isinstance(last_txn_to, Unset):
        json_last_txn_to = last_txn_to.isoformat()
    params["lastTxnTo"] = json_last_txn_to

    params["revenueFrom"] = revenue_from

    params["revenueTo"] = revenue_to

    params["debtFrom"] = debt_from

    params["debtTo"] = debt_to

    json_created_by: str | Unset = UNSET
    if not isinstance(created_by, Unset):
        json_created_by = str(created_by)
    params["createdBy"] = json_created_by

    params["sortBy"] = sort_by

    params["sortDir"] = sort_dir

    params["f"] = f

    json_branch_id: str | Unset = UNSET
    if not isinstance(branch_id, Unset):
        json_branch_id = str(branch_id)
    params["branchId"] = json_branch_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sales/customers",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CustomerListResult | None:
    if response.status_code == 200:
        response_200 = CustomerListResult.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CustomerListResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    group_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    customer_type: str | Unset = UNSET,
    search: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    smart_view: str | Unset = UNSET,
    crm_contact_id: UUID | Unset = UNSET,
    assigned_to: UUID | Unset = UNSET,
    created_from: datetime.datetime | Unset = UNSET,
    created_to: datetime.datetime | Unset = UNSET,
    gender: str | Unset = UNSET,
    birthday_month: int | Unset = UNSET,
    last_txn_from: datetime.datetime | Unset = UNSET,
    last_txn_to: datetime.datetime | Unset = UNSET,
    revenue_from: float | Unset = UNSET,
    revenue_to: float | Unset = UNSET,
    debt_from: float | Unset = UNSET,
    debt_to: float | Unset = UNSET,
    created_by: UUID | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,
    f: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,

) -> Response[CustomerListResult]:
    """ Danh sách khách hàng

     Lấy danh sách khách hàng theo workspace, có hỗ trợ lọc và phân trang.

    Args:
        group_id (UUID | Unset):
        status (str | Unset):
        customer_type (str | Unset):
        search (str | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        smart_view (str | Unset):
        crm_contact_id (UUID | Unset):
        assigned_to (UUID | Unset):
        created_from (datetime.datetime | Unset):
        created_to (datetime.datetime | Unset):
        gender (str | Unset):
        birthday_month (int | Unset):
        last_txn_from (datetime.datetime | Unset):
        last_txn_to (datetime.datetime | Unset):
        revenue_from (float | Unset):
        revenue_to (float | Unset):
        debt_from (float | Unset):
        debt_to (float | Unset):
        created_by (UUID | Unset):
        sort_by (str | Unset):
        sort_dir (str | Unset):
        f (str | Unset):
        branch_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomerListResult]
     """


    kwargs = _get_kwargs(
        group_id=group_id,
status=status,
customer_type=customer_type,
search=search,
page_number=page_number,
page_size=page_size,
smart_view=smart_view,
crm_contact_id=crm_contact_id,
assigned_to=assigned_to,
created_from=created_from,
created_to=created_to,
gender=gender,
birthday_month=birthday_month,
last_txn_from=last_txn_from,
last_txn_to=last_txn_to,
revenue_from=revenue_from,
revenue_to=revenue_to,
debt_from=debt_from,
debt_to=debt_to,
created_by=created_by,
sort_by=sort_by,
sort_dir=sort_dir,
f=f,
branch_id=branch_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    group_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    customer_type: str | Unset = UNSET,
    search: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    smart_view: str | Unset = UNSET,
    crm_contact_id: UUID | Unset = UNSET,
    assigned_to: UUID | Unset = UNSET,
    created_from: datetime.datetime | Unset = UNSET,
    created_to: datetime.datetime | Unset = UNSET,
    gender: str | Unset = UNSET,
    birthday_month: int | Unset = UNSET,
    last_txn_from: datetime.datetime | Unset = UNSET,
    last_txn_to: datetime.datetime | Unset = UNSET,
    revenue_from: float | Unset = UNSET,
    revenue_to: float | Unset = UNSET,
    debt_from: float | Unset = UNSET,
    debt_to: float | Unset = UNSET,
    created_by: UUID | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,
    f: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,

) -> CustomerListResult | None:
    """ Danh sách khách hàng

     Lấy danh sách khách hàng theo workspace, có hỗ trợ lọc và phân trang.

    Args:
        group_id (UUID | Unset):
        status (str | Unset):
        customer_type (str | Unset):
        search (str | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        smart_view (str | Unset):
        crm_contact_id (UUID | Unset):
        assigned_to (UUID | Unset):
        created_from (datetime.datetime | Unset):
        created_to (datetime.datetime | Unset):
        gender (str | Unset):
        birthday_month (int | Unset):
        last_txn_from (datetime.datetime | Unset):
        last_txn_to (datetime.datetime | Unset):
        revenue_from (float | Unset):
        revenue_to (float | Unset):
        debt_from (float | Unset):
        debt_to (float | Unset):
        created_by (UUID | Unset):
        sort_by (str | Unset):
        sort_dir (str | Unset):
        f (str | Unset):
        branch_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomerListResult
     """


    return sync_detailed(
        client=client,
group_id=group_id,
status=status,
customer_type=customer_type,
search=search,
page_number=page_number,
page_size=page_size,
smart_view=smart_view,
crm_contact_id=crm_contact_id,
assigned_to=assigned_to,
created_from=created_from,
created_to=created_to,
gender=gender,
birthday_month=birthday_month,
last_txn_from=last_txn_from,
last_txn_to=last_txn_to,
revenue_from=revenue_from,
revenue_to=revenue_to,
debt_from=debt_from,
debt_to=debt_to,
created_by=created_by,
sort_by=sort_by,
sort_dir=sort_dir,
f=f,
branch_id=branch_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    group_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    customer_type: str | Unset = UNSET,
    search: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    smart_view: str | Unset = UNSET,
    crm_contact_id: UUID | Unset = UNSET,
    assigned_to: UUID | Unset = UNSET,
    created_from: datetime.datetime | Unset = UNSET,
    created_to: datetime.datetime | Unset = UNSET,
    gender: str | Unset = UNSET,
    birthday_month: int | Unset = UNSET,
    last_txn_from: datetime.datetime | Unset = UNSET,
    last_txn_to: datetime.datetime | Unset = UNSET,
    revenue_from: float | Unset = UNSET,
    revenue_to: float | Unset = UNSET,
    debt_from: float | Unset = UNSET,
    debt_to: float | Unset = UNSET,
    created_by: UUID | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,
    f: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,

) -> Response[CustomerListResult]:
    """ Danh sách khách hàng

     Lấy danh sách khách hàng theo workspace, có hỗ trợ lọc và phân trang.

    Args:
        group_id (UUID | Unset):
        status (str | Unset):
        customer_type (str | Unset):
        search (str | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        smart_view (str | Unset):
        crm_contact_id (UUID | Unset):
        assigned_to (UUID | Unset):
        created_from (datetime.datetime | Unset):
        created_to (datetime.datetime | Unset):
        gender (str | Unset):
        birthday_month (int | Unset):
        last_txn_from (datetime.datetime | Unset):
        last_txn_to (datetime.datetime | Unset):
        revenue_from (float | Unset):
        revenue_to (float | Unset):
        debt_from (float | Unset):
        debt_to (float | Unset):
        created_by (UUID | Unset):
        sort_by (str | Unset):
        sort_dir (str | Unset):
        f (str | Unset):
        branch_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomerListResult]
     """


    kwargs = _get_kwargs(
        group_id=group_id,
status=status,
customer_type=customer_type,
search=search,
page_number=page_number,
page_size=page_size,
smart_view=smart_view,
crm_contact_id=crm_contact_id,
assigned_to=assigned_to,
created_from=created_from,
created_to=created_to,
gender=gender,
birthday_month=birthday_month,
last_txn_from=last_txn_from,
last_txn_to=last_txn_to,
revenue_from=revenue_from,
revenue_to=revenue_to,
debt_from=debt_from,
debt_to=debt_to,
created_by=created_by,
sort_by=sort_by,
sort_dir=sort_dir,
f=f,
branch_id=branch_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    group_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    customer_type: str | Unset = UNSET,
    search: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    smart_view: str | Unset = UNSET,
    crm_contact_id: UUID | Unset = UNSET,
    assigned_to: UUID | Unset = UNSET,
    created_from: datetime.datetime | Unset = UNSET,
    created_to: datetime.datetime | Unset = UNSET,
    gender: str | Unset = UNSET,
    birthday_month: int | Unset = UNSET,
    last_txn_from: datetime.datetime | Unset = UNSET,
    last_txn_to: datetime.datetime | Unset = UNSET,
    revenue_from: float | Unset = UNSET,
    revenue_to: float | Unset = UNSET,
    debt_from: float | Unset = UNSET,
    debt_to: float | Unset = UNSET,
    created_by: UUID | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,
    f: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,

) -> CustomerListResult | None:
    """ Danh sách khách hàng

     Lấy danh sách khách hàng theo workspace, có hỗ trợ lọc và phân trang.

    Args:
        group_id (UUID | Unset):
        status (str | Unset):
        customer_type (str | Unset):
        search (str | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        smart_view (str | Unset):
        crm_contact_id (UUID | Unset):
        assigned_to (UUID | Unset):
        created_from (datetime.datetime | Unset):
        created_to (datetime.datetime | Unset):
        gender (str | Unset):
        birthday_month (int | Unset):
        last_txn_from (datetime.datetime | Unset):
        last_txn_to (datetime.datetime | Unset):
        revenue_from (float | Unset):
        revenue_to (float | Unset):
        debt_from (float | Unset):
        debt_to (float | Unset):
        created_by (UUID | Unset):
        sort_by (str | Unset):
        sort_dir (str | Unset):
        f (str | Unset):
        branch_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomerListResult
     """


    return (await asyncio_detailed(
        client=client,
group_id=group_id,
status=status,
customer_type=customer_type,
search=search,
page_number=page_number,
page_size=page_size,
smart_view=smart_view,
crm_contact_id=crm_contact_id,
assigned_to=assigned_to,
created_from=created_from,
created_to=created_to,
gender=gender,
birthday_month=birthday_month,
last_txn_from=last_txn_from,
last_txn_to=last_txn_to,
revenue_from=revenue_from,
revenue_to=revenue_to,
debt_from=debt_from,
debt_to=debt_to,
created_by=created_by,
sort_by=sort_by,
sort_dir=sort_dir,
f=f,
branch_id=branch_id,

    )).parsed

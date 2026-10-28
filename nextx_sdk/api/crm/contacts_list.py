from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.contacts_list_column_filters import ContactsListColumnFilters
from ...models.paged_result_of_contact_summary_dto import PagedResultOfContactSummaryDto
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    *,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    q: str | Unset = UNSET,
    tier: str | Unset = UNSET,
    has_customer_profile: bool | Unset = UNSET,
    tag_id: UUID | Unset = UNSET,
    from_date: datetime.datetime | Unset = UNSET,
    to_date: datetime.datetime | Unset = UNSET,
    lifecycle_stage: str | Unset = UNSET,
    assignee_id: UUID | Unset = UNSET,
    source_id: UUID | Unset = UNSET,
    industry_id: UUID | Unset = UNSET,
    contact_type: str | Unset = UNSET,
    duplicates_only: bool | Unset = UNSET,
    lifecycle_stages: list[str] | Unset = UNSET,
    customer_group_id: UUID | Unset = UNSET,
    contact_status_id: UUID | Unset = UNSET,
    customer_created_from: datetime.datetime | Unset = UNSET,
    customer_created_to: datetime.datetime | Unset = UNSET,
    inactive_days: int | Unset = UNSET,
    f: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_descending: bool | Unset = False,
    column_filters: ContactsListColumnFilters | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    all_branches: bool | Unset = False,
    sla_overdue: bool | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["pageNumber"] = page_number

    params["pageSize"] = page_size

    params["q"] = q

    params["tier"] = tier

    params["hasCustomerProfile"] = has_customer_profile

    json_tag_id: str | Unset = UNSET
    if not isinstance(tag_id, Unset):
        json_tag_id = str(tag_id)
    params["tagId"] = json_tag_id

    json_from_date: str | Unset = UNSET
    if not isinstance(from_date, Unset):
        json_from_date = from_date.isoformat()
    params["fromDate"] = json_from_date

    json_to_date: str | Unset = UNSET
    if not isinstance(to_date, Unset):
        json_to_date = to_date.isoformat()
    params["toDate"] = json_to_date

    params["lifecycleStage"] = lifecycle_stage

    json_assignee_id: str | Unset = UNSET
    if not isinstance(assignee_id, Unset):
        json_assignee_id = str(assignee_id)
    params["assigneeId"] = json_assignee_id

    json_source_id: str | Unset = UNSET
    if not isinstance(source_id, Unset):
        json_source_id = str(source_id)
    params["sourceId"] = json_source_id

    json_industry_id: str | Unset = UNSET
    if not isinstance(industry_id, Unset):
        json_industry_id = str(industry_id)
    params["industryId"] = json_industry_id

    params["contactType"] = contact_type

    params["duplicatesOnly"] = duplicates_only

    json_lifecycle_stages: list[str] | Unset = UNSET
    if not isinstance(lifecycle_stages, Unset):
        json_lifecycle_stages = lifecycle_stages


    params["lifecycleStages"] = json_lifecycle_stages

    json_customer_group_id: str | Unset = UNSET
    if not isinstance(customer_group_id, Unset):
        json_customer_group_id = str(customer_group_id)
    params["customerGroupId"] = json_customer_group_id

    json_contact_status_id: str | Unset = UNSET
    if not isinstance(contact_status_id, Unset):
        json_contact_status_id = str(contact_status_id)
    params["contactStatusId"] = json_contact_status_id

    json_customer_created_from: str | Unset = UNSET
    if not isinstance(customer_created_from, Unset):
        json_customer_created_from = customer_created_from.isoformat()
    params["customerCreatedFrom"] = json_customer_created_from

    json_customer_created_to: str | Unset = UNSET
    if not isinstance(customer_created_to, Unset):
        json_customer_created_to = customer_created_to.isoformat()
    params["customerCreatedTo"] = json_customer_created_to

    params["inactiveDays"] = inactive_days

    params["f"] = f

    params["sortBy"] = sort_by

    params["sortDescending"] = sort_descending

    json_column_filters: dict[str, Any] | Unset = UNSET
    if not isinstance(column_filters, Unset):
        json_column_filters = column_filters.to_dict()
    if not isinstance(json_column_filters, Unset):
        params.update(json_column_filters)


    json_branch_id: str | Unset = UNSET
    if not isinstance(branch_id, Unset):
        json_branch_id = str(branch_id)
    params["branchId"] = json_branch_id

    params["allBranches"] = all_branches

    params["slaOverdue"] = sla_overdue


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/crm/contacts",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PagedResultOfContactSummaryDto | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = PagedResultOfContactSummaryDto.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ProblemDetails.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PagedResultOfContactSummaryDto | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    q: str | Unset = UNSET,
    tier: str | Unset = UNSET,
    has_customer_profile: bool | Unset = UNSET,
    tag_id: UUID | Unset = UNSET,
    from_date: datetime.datetime | Unset = UNSET,
    to_date: datetime.datetime | Unset = UNSET,
    lifecycle_stage: str | Unset = UNSET,
    assignee_id: UUID | Unset = UNSET,
    source_id: UUID | Unset = UNSET,
    industry_id: UUID | Unset = UNSET,
    contact_type: str | Unset = UNSET,
    duplicates_only: bool | Unset = UNSET,
    lifecycle_stages: list[str] | Unset = UNSET,
    customer_group_id: UUID | Unset = UNSET,
    contact_status_id: UUID | Unset = UNSET,
    customer_created_from: datetime.datetime | Unset = UNSET,
    customer_created_to: datetime.datetime | Unset = UNSET,
    inactive_days: int | Unset = UNSET,
    f: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_descending: bool | Unset = False,
    column_filters: ContactsListColumnFilters | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    all_branches: bool | Unset = False,
    sla_overdue: bool | Unset = UNSET,

) -> Response[PagedResultOfContactSummaryDto | ProblemDetails]:
    """ Lấy danh sách contacts

     Hỗ trợ full-text search, filter theo tier, tag, ngày tạo, nguồn, phụ trách, ngành, loại khách hàng,
    trùng lặp. Drill-down dashboard: customerCreatedFrom/customerCreatedTo (có CustomerProfile tạo trong
    khoảng), inactiveDays=N (không có activity nào trong N ngày gần nhất). Kết quả phân trang.

    Args:
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        q (str | Unset):
        tier (str | Unset):
        has_customer_profile (bool | Unset):
        tag_id (UUID | Unset):
        from_date (datetime.datetime | Unset):
        to_date (datetime.datetime | Unset):
        lifecycle_stage (str | Unset):
        assignee_id (UUID | Unset):
        source_id (UUID | Unset):
        industry_id (UUID | Unset):
        contact_type (str | Unset):
        duplicates_only (bool | Unset):
        lifecycle_stages (list[str] | Unset):
        customer_group_id (UUID | Unset):
        contact_status_id (UUID | Unset):
        customer_created_from (datetime.datetime | Unset):
        customer_created_to (datetime.datetime | Unset):
        inactive_days (int | Unset):
        f (str | Unset):
        sort_by (str | Unset):
        sort_descending (bool | Unset):  Default: False.
        column_filters (ContactsListColumnFilters | Unset):
        branch_id (UUID | Unset):
        all_branches (bool | Unset):  Default: False.
        sla_overdue (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedResultOfContactSummaryDto | ProblemDetails]
     """


    kwargs = _get_kwargs(
        page_number=page_number,
page_size=page_size,
q=q,
tier=tier,
has_customer_profile=has_customer_profile,
tag_id=tag_id,
from_date=from_date,
to_date=to_date,
lifecycle_stage=lifecycle_stage,
assignee_id=assignee_id,
source_id=source_id,
industry_id=industry_id,
contact_type=contact_type,
duplicates_only=duplicates_only,
lifecycle_stages=lifecycle_stages,
customer_group_id=customer_group_id,
contact_status_id=contact_status_id,
customer_created_from=customer_created_from,
customer_created_to=customer_created_to,
inactive_days=inactive_days,
f=f,
sort_by=sort_by,
sort_descending=sort_descending,
column_filters=column_filters,
branch_id=branch_id,
all_branches=all_branches,
sla_overdue=sla_overdue,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    q: str | Unset = UNSET,
    tier: str | Unset = UNSET,
    has_customer_profile: bool | Unset = UNSET,
    tag_id: UUID | Unset = UNSET,
    from_date: datetime.datetime | Unset = UNSET,
    to_date: datetime.datetime | Unset = UNSET,
    lifecycle_stage: str | Unset = UNSET,
    assignee_id: UUID | Unset = UNSET,
    source_id: UUID | Unset = UNSET,
    industry_id: UUID | Unset = UNSET,
    contact_type: str | Unset = UNSET,
    duplicates_only: bool | Unset = UNSET,
    lifecycle_stages: list[str] | Unset = UNSET,
    customer_group_id: UUID | Unset = UNSET,
    contact_status_id: UUID | Unset = UNSET,
    customer_created_from: datetime.datetime | Unset = UNSET,
    customer_created_to: datetime.datetime | Unset = UNSET,
    inactive_days: int | Unset = UNSET,
    f: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_descending: bool | Unset = False,
    column_filters: ContactsListColumnFilters | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    all_branches: bool | Unset = False,
    sla_overdue: bool | Unset = UNSET,

) -> PagedResultOfContactSummaryDto | ProblemDetails | None:
    """ Lấy danh sách contacts

     Hỗ trợ full-text search, filter theo tier, tag, ngày tạo, nguồn, phụ trách, ngành, loại khách hàng,
    trùng lặp. Drill-down dashboard: customerCreatedFrom/customerCreatedTo (có CustomerProfile tạo trong
    khoảng), inactiveDays=N (không có activity nào trong N ngày gần nhất). Kết quả phân trang.

    Args:
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        q (str | Unset):
        tier (str | Unset):
        has_customer_profile (bool | Unset):
        tag_id (UUID | Unset):
        from_date (datetime.datetime | Unset):
        to_date (datetime.datetime | Unset):
        lifecycle_stage (str | Unset):
        assignee_id (UUID | Unset):
        source_id (UUID | Unset):
        industry_id (UUID | Unset):
        contact_type (str | Unset):
        duplicates_only (bool | Unset):
        lifecycle_stages (list[str] | Unset):
        customer_group_id (UUID | Unset):
        contact_status_id (UUID | Unset):
        customer_created_from (datetime.datetime | Unset):
        customer_created_to (datetime.datetime | Unset):
        inactive_days (int | Unset):
        f (str | Unset):
        sort_by (str | Unset):
        sort_descending (bool | Unset):  Default: False.
        column_filters (ContactsListColumnFilters | Unset):
        branch_id (UUID | Unset):
        all_branches (bool | Unset):  Default: False.
        sla_overdue (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedResultOfContactSummaryDto | ProblemDetails
     """


    return sync_detailed(
        client=client,
page_number=page_number,
page_size=page_size,
q=q,
tier=tier,
has_customer_profile=has_customer_profile,
tag_id=tag_id,
from_date=from_date,
to_date=to_date,
lifecycle_stage=lifecycle_stage,
assignee_id=assignee_id,
source_id=source_id,
industry_id=industry_id,
contact_type=contact_type,
duplicates_only=duplicates_only,
lifecycle_stages=lifecycle_stages,
customer_group_id=customer_group_id,
contact_status_id=contact_status_id,
customer_created_from=customer_created_from,
customer_created_to=customer_created_to,
inactive_days=inactive_days,
f=f,
sort_by=sort_by,
sort_descending=sort_descending,
column_filters=column_filters,
branch_id=branch_id,
all_branches=all_branches,
sla_overdue=sla_overdue,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    q: str | Unset = UNSET,
    tier: str | Unset = UNSET,
    has_customer_profile: bool | Unset = UNSET,
    tag_id: UUID | Unset = UNSET,
    from_date: datetime.datetime | Unset = UNSET,
    to_date: datetime.datetime | Unset = UNSET,
    lifecycle_stage: str | Unset = UNSET,
    assignee_id: UUID | Unset = UNSET,
    source_id: UUID | Unset = UNSET,
    industry_id: UUID | Unset = UNSET,
    contact_type: str | Unset = UNSET,
    duplicates_only: bool | Unset = UNSET,
    lifecycle_stages: list[str] | Unset = UNSET,
    customer_group_id: UUID | Unset = UNSET,
    contact_status_id: UUID | Unset = UNSET,
    customer_created_from: datetime.datetime | Unset = UNSET,
    customer_created_to: datetime.datetime | Unset = UNSET,
    inactive_days: int | Unset = UNSET,
    f: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_descending: bool | Unset = False,
    column_filters: ContactsListColumnFilters | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    all_branches: bool | Unset = False,
    sla_overdue: bool | Unset = UNSET,

) -> Response[PagedResultOfContactSummaryDto | ProblemDetails]:
    """ Lấy danh sách contacts

     Hỗ trợ full-text search, filter theo tier, tag, ngày tạo, nguồn, phụ trách, ngành, loại khách hàng,
    trùng lặp. Drill-down dashboard: customerCreatedFrom/customerCreatedTo (có CustomerProfile tạo trong
    khoảng), inactiveDays=N (không có activity nào trong N ngày gần nhất). Kết quả phân trang.

    Args:
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        q (str | Unset):
        tier (str | Unset):
        has_customer_profile (bool | Unset):
        tag_id (UUID | Unset):
        from_date (datetime.datetime | Unset):
        to_date (datetime.datetime | Unset):
        lifecycle_stage (str | Unset):
        assignee_id (UUID | Unset):
        source_id (UUID | Unset):
        industry_id (UUID | Unset):
        contact_type (str | Unset):
        duplicates_only (bool | Unset):
        lifecycle_stages (list[str] | Unset):
        customer_group_id (UUID | Unset):
        contact_status_id (UUID | Unset):
        customer_created_from (datetime.datetime | Unset):
        customer_created_to (datetime.datetime | Unset):
        inactive_days (int | Unset):
        f (str | Unset):
        sort_by (str | Unset):
        sort_descending (bool | Unset):  Default: False.
        column_filters (ContactsListColumnFilters | Unset):
        branch_id (UUID | Unset):
        all_branches (bool | Unset):  Default: False.
        sla_overdue (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedResultOfContactSummaryDto | ProblemDetails]
     """


    kwargs = _get_kwargs(
        page_number=page_number,
page_size=page_size,
q=q,
tier=tier,
has_customer_profile=has_customer_profile,
tag_id=tag_id,
from_date=from_date,
to_date=to_date,
lifecycle_stage=lifecycle_stage,
assignee_id=assignee_id,
source_id=source_id,
industry_id=industry_id,
contact_type=contact_type,
duplicates_only=duplicates_only,
lifecycle_stages=lifecycle_stages,
customer_group_id=customer_group_id,
contact_status_id=contact_status_id,
customer_created_from=customer_created_from,
customer_created_to=customer_created_to,
inactive_days=inactive_days,
f=f,
sort_by=sort_by,
sort_descending=sort_descending,
column_filters=column_filters,
branch_id=branch_id,
all_branches=all_branches,
sla_overdue=sla_overdue,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    q: str | Unset = UNSET,
    tier: str | Unset = UNSET,
    has_customer_profile: bool | Unset = UNSET,
    tag_id: UUID | Unset = UNSET,
    from_date: datetime.datetime | Unset = UNSET,
    to_date: datetime.datetime | Unset = UNSET,
    lifecycle_stage: str | Unset = UNSET,
    assignee_id: UUID | Unset = UNSET,
    source_id: UUID | Unset = UNSET,
    industry_id: UUID | Unset = UNSET,
    contact_type: str | Unset = UNSET,
    duplicates_only: bool | Unset = UNSET,
    lifecycle_stages: list[str] | Unset = UNSET,
    customer_group_id: UUID | Unset = UNSET,
    contact_status_id: UUID | Unset = UNSET,
    customer_created_from: datetime.datetime | Unset = UNSET,
    customer_created_to: datetime.datetime | Unset = UNSET,
    inactive_days: int | Unset = UNSET,
    f: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_descending: bool | Unset = False,
    column_filters: ContactsListColumnFilters | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    all_branches: bool | Unset = False,
    sla_overdue: bool | Unset = UNSET,

) -> PagedResultOfContactSummaryDto | ProblemDetails | None:
    """ Lấy danh sách contacts

     Hỗ trợ full-text search, filter theo tier, tag, ngày tạo, nguồn, phụ trách, ngành, loại khách hàng,
    trùng lặp. Drill-down dashboard: customerCreatedFrom/customerCreatedTo (có CustomerProfile tạo trong
    khoảng), inactiveDays=N (không có activity nào trong N ngày gần nhất). Kết quả phân trang.

    Args:
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        q (str | Unset):
        tier (str | Unset):
        has_customer_profile (bool | Unset):
        tag_id (UUID | Unset):
        from_date (datetime.datetime | Unset):
        to_date (datetime.datetime | Unset):
        lifecycle_stage (str | Unset):
        assignee_id (UUID | Unset):
        source_id (UUID | Unset):
        industry_id (UUID | Unset):
        contact_type (str | Unset):
        duplicates_only (bool | Unset):
        lifecycle_stages (list[str] | Unset):
        customer_group_id (UUID | Unset):
        contact_status_id (UUID | Unset):
        customer_created_from (datetime.datetime | Unset):
        customer_created_to (datetime.datetime | Unset):
        inactive_days (int | Unset):
        f (str | Unset):
        sort_by (str | Unset):
        sort_descending (bool | Unset):  Default: False.
        column_filters (ContactsListColumnFilters | Unset):
        branch_id (UUID | Unset):
        all_branches (bool | Unset):  Default: False.
        sla_overdue (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedResultOfContactSummaryDto | ProblemDetails
     """


    return (await asyncio_detailed(
        client=client,
page_number=page_number,
page_size=page_size,
q=q,
tier=tier,
has_customer_profile=has_customer_profile,
tag_id=tag_id,
from_date=from_date,
to_date=to_date,
lifecycle_stage=lifecycle_stage,
assignee_id=assignee_id,
source_id=source_id,
industry_id=industry_id,
contact_type=contact_type,
duplicates_only=duplicates_only,
lifecycle_stages=lifecycle_stages,
customer_group_id=customer_group_id,
contact_status_id=contact_status_id,
customer_created_from=customer_created_from,
customer_created_to=customer_created_to,
inactive_days=inactive_days,
f=f,
sort_by=sort_by,
sort_descending=sort_descending,
column_filters=column_filters,
branch_id=branch_id,
all_branches=all_branches,
sla_overdue=sla_overdue,

    )).parsed

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paged_result_of_opportunity_summary_dto import PagedResultOfOpportunitySummaryDto
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    *,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    q: str | Unset = UNSET,
    status: str | Unset = UNSET,
    stage_id: UUID | Unset = UNSET,
    assignee_id: UUID | Unset = UNSET,
    contact_id: UUID | Unset = UNSET,
    lead_id: UUID | Unset = UNSET,
    from_date: datetime.datetime | Unset = UNSET,
    to_date: datetime.datetime | Unset = UNSET,
    source_id: UUID | Unset = UNSET,
    won_from: datetime.datetime | Unset = UNSET,
    won_to: datetime.datetime | Unset = UNSET,
    overdue: bool | Unset = UNSET,
    pipeline_id: UUID | Unset = UNSET,
    value_gte: float | Unset = UNSET,
    value_lte: float | Unset = UNSET,
    f: str | Unset = UNSET,
    campaign_id: UUID | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    next_call_from: datetime.date | Unset = UNSET,
    next_call_to: datetime.date | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["pageNumber"] = page_number

    params["pageSize"] = page_size

    params["q"] = q

    params["status"] = status

    json_stage_id: str | Unset = UNSET
    if not isinstance(stage_id, Unset):
        json_stage_id = str(stage_id)
    params["stageId"] = json_stage_id

    json_assignee_id: str | Unset = UNSET
    if not isinstance(assignee_id, Unset):
        json_assignee_id = str(assignee_id)
    params["assigneeId"] = json_assignee_id

    json_contact_id: str | Unset = UNSET
    if not isinstance(contact_id, Unset):
        json_contact_id = str(contact_id)
    params["contactId"] = json_contact_id

    json_lead_id: str | Unset = UNSET
    if not isinstance(lead_id, Unset):
        json_lead_id = str(lead_id)
    params["leadId"] = json_lead_id

    json_from_date: str | Unset = UNSET
    if not isinstance(from_date, Unset):
        json_from_date = from_date.isoformat()
    params["fromDate"] = json_from_date

    json_to_date: str | Unset = UNSET
    if not isinstance(to_date, Unset):
        json_to_date = to_date.isoformat()
    params["toDate"] = json_to_date

    json_source_id: str | Unset = UNSET
    if not isinstance(source_id, Unset):
        json_source_id = str(source_id)
    params["sourceId"] = json_source_id

    json_won_from: str | Unset = UNSET
    if not isinstance(won_from, Unset):
        json_won_from = won_from.isoformat()
    params["wonFrom"] = json_won_from

    json_won_to: str | Unset = UNSET
    if not isinstance(won_to, Unset):
        json_won_to = won_to.isoformat()
    params["wonTo"] = json_won_to

    params["overdue"] = overdue

    json_pipeline_id: str | Unset = UNSET
    if not isinstance(pipeline_id, Unset):
        json_pipeline_id = str(pipeline_id)
    params["pipelineId"] = json_pipeline_id

    params["valueGte"] = value_gte

    params["valueLte"] = value_lte

    params["f"] = f

    json_campaign_id: str | Unset = UNSET
    if not isinstance(campaign_id, Unset):
        json_campaign_id = str(campaign_id)
    params["campaignId"] = json_campaign_id

    params["sortBy"] = sort_by

    json_next_call_from: str | Unset = UNSET
    if not isinstance(next_call_from, Unset):
        json_next_call_from = next_call_from.isoformat()
    params["nextCallFrom"] = json_next_call_from

    json_next_call_to: str | Unset = UNSET
    if not isinstance(next_call_to, Unset):
        json_next_call_to = next_call_to.isoformat()
    params["nextCallTo"] = json_next_call_to


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/crm/opportunities",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PagedResultOfOpportunitySummaryDto | None:
    if response.status_code == 200:
        response_200 = PagedResultOfOpportunitySummaryDto.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PagedResultOfOpportunitySummaryDto]:
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
    status: str | Unset = UNSET,
    stage_id: UUID | Unset = UNSET,
    assignee_id: UUID | Unset = UNSET,
    contact_id: UUID | Unset = UNSET,
    lead_id: UUID | Unset = UNSET,
    from_date: datetime.datetime | Unset = UNSET,
    to_date: datetime.datetime | Unset = UNSET,
    source_id: UUID | Unset = UNSET,
    won_from: datetime.datetime | Unset = UNSET,
    won_to: datetime.datetime | Unset = UNSET,
    overdue: bool | Unset = UNSET,
    pipeline_id: UUID | Unset = UNSET,
    value_gte: float | Unset = UNSET,
    value_lte: float | Unset = UNSET,
    f: str | Unset = UNSET,
    campaign_id: UUID | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    next_call_from: datetime.date | Unset = UNSET,
    next_call_to: datetime.date | Unset = UNSET,

) -> Response[PagedResultOfOpportunitySummaryDto]:
    """ Lấy danh sách opportunities

     Hỗ trợ full-text search (q: name/code) + filter theo status, stage, assignee, contact, lead. Drill-
    down dashboard: sourceId (nguồn của contact liên kết), wonFrom/wonTo (khoảng WonAt), overdue=true
    (Open + quá hạn đóng dự kiến theo ngày VN), valueGte/valueLte (khoảng giá trị dự kiến — VND),
    campaignId (chiến dịch nguồn). sortBy: nextCall (hạn task mở sớm nhất) | expectedClose | createdAt
    (mặc định). nextCallFrom/nextCallTo: lọc cơ hội có hạn task mở sớm nhất trong khoảng ngày (chip 'hôm
    nay' = From=To=today, 'quá hạn' = To=hôm qua). Hỗ trợ cả chế độ list và kanban.

    Args:
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        q (str | Unset):
        status (str | Unset):
        stage_id (UUID | Unset):
        assignee_id (UUID | Unset):
        contact_id (UUID | Unset):
        lead_id (UUID | Unset):
        from_date (datetime.datetime | Unset):
        to_date (datetime.datetime | Unset):
        source_id (UUID | Unset):
        won_from (datetime.datetime | Unset):
        won_to (datetime.datetime | Unset):
        overdue (bool | Unset):
        pipeline_id (UUID | Unset):
        value_gte (float | Unset):
        value_lte (float | Unset):
        f (str | Unset):
        campaign_id (UUID | Unset):
        sort_by (str | Unset):
        next_call_from (datetime.date | Unset):
        next_call_to (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedResultOfOpportunitySummaryDto]
     """


    kwargs = _get_kwargs(
        page_number=page_number,
page_size=page_size,
q=q,
status=status,
stage_id=stage_id,
assignee_id=assignee_id,
contact_id=contact_id,
lead_id=lead_id,
from_date=from_date,
to_date=to_date,
source_id=source_id,
won_from=won_from,
won_to=won_to,
overdue=overdue,
pipeline_id=pipeline_id,
value_gte=value_gte,
value_lte=value_lte,
f=f,
campaign_id=campaign_id,
sort_by=sort_by,
next_call_from=next_call_from,
next_call_to=next_call_to,

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
    status: str | Unset = UNSET,
    stage_id: UUID | Unset = UNSET,
    assignee_id: UUID | Unset = UNSET,
    contact_id: UUID | Unset = UNSET,
    lead_id: UUID | Unset = UNSET,
    from_date: datetime.datetime | Unset = UNSET,
    to_date: datetime.datetime | Unset = UNSET,
    source_id: UUID | Unset = UNSET,
    won_from: datetime.datetime | Unset = UNSET,
    won_to: datetime.datetime | Unset = UNSET,
    overdue: bool | Unset = UNSET,
    pipeline_id: UUID | Unset = UNSET,
    value_gte: float | Unset = UNSET,
    value_lte: float | Unset = UNSET,
    f: str | Unset = UNSET,
    campaign_id: UUID | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    next_call_from: datetime.date | Unset = UNSET,
    next_call_to: datetime.date | Unset = UNSET,

) -> PagedResultOfOpportunitySummaryDto | None:
    """ Lấy danh sách opportunities

     Hỗ trợ full-text search (q: name/code) + filter theo status, stage, assignee, contact, lead. Drill-
    down dashboard: sourceId (nguồn của contact liên kết), wonFrom/wonTo (khoảng WonAt), overdue=true
    (Open + quá hạn đóng dự kiến theo ngày VN), valueGte/valueLte (khoảng giá trị dự kiến — VND),
    campaignId (chiến dịch nguồn). sortBy: nextCall (hạn task mở sớm nhất) | expectedClose | createdAt
    (mặc định). nextCallFrom/nextCallTo: lọc cơ hội có hạn task mở sớm nhất trong khoảng ngày (chip 'hôm
    nay' = From=To=today, 'quá hạn' = To=hôm qua). Hỗ trợ cả chế độ list và kanban.

    Args:
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        q (str | Unset):
        status (str | Unset):
        stage_id (UUID | Unset):
        assignee_id (UUID | Unset):
        contact_id (UUID | Unset):
        lead_id (UUID | Unset):
        from_date (datetime.datetime | Unset):
        to_date (datetime.datetime | Unset):
        source_id (UUID | Unset):
        won_from (datetime.datetime | Unset):
        won_to (datetime.datetime | Unset):
        overdue (bool | Unset):
        pipeline_id (UUID | Unset):
        value_gte (float | Unset):
        value_lte (float | Unset):
        f (str | Unset):
        campaign_id (UUID | Unset):
        sort_by (str | Unset):
        next_call_from (datetime.date | Unset):
        next_call_to (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedResultOfOpportunitySummaryDto
     """


    return sync_detailed(
        client=client,
page_number=page_number,
page_size=page_size,
q=q,
status=status,
stage_id=stage_id,
assignee_id=assignee_id,
contact_id=contact_id,
lead_id=lead_id,
from_date=from_date,
to_date=to_date,
source_id=source_id,
won_from=won_from,
won_to=won_to,
overdue=overdue,
pipeline_id=pipeline_id,
value_gte=value_gte,
value_lte=value_lte,
f=f,
campaign_id=campaign_id,
sort_by=sort_by,
next_call_from=next_call_from,
next_call_to=next_call_to,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    q: str | Unset = UNSET,
    status: str | Unset = UNSET,
    stage_id: UUID | Unset = UNSET,
    assignee_id: UUID | Unset = UNSET,
    contact_id: UUID | Unset = UNSET,
    lead_id: UUID | Unset = UNSET,
    from_date: datetime.datetime | Unset = UNSET,
    to_date: datetime.datetime | Unset = UNSET,
    source_id: UUID | Unset = UNSET,
    won_from: datetime.datetime | Unset = UNSET,
    won_to: datetime.datetime | Unset = UNSET,
    overdue: bool | Unset = UNSET,
    pipeline_id: UUID | Unset = UNSET,
    value_gte: float | Unset = UNSET,
    value_lte: float | Unset = UNSET,
    f: str | Unset = UNSET,
    campaign_id: UUID | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    next_call_from: datetime.date | Unset = UNSET,
    next_call_to: datetime.date | Unset = UNSET,

) -> Response[PagedResultOfOpportunitySummaryDto]:
    """ Lấy danh sách opportunities

     Hỗ trợ full-text search (q: name/code) + filter theo status, stage, assignee, contact, lead. Drill-
    down dashboard: sourceId (nguồn của contact liên kết), wonFrom/wonTo (khoảng WonAt), overdue=true
    (Open + quá hạn đóng dự kiến theo ngày VN), valueGte/valueLte (khoảng giá trị dự kiến — VND),
    campaignId (chiến dịch nguồn). sortBy: nextCall (hạn task mở sớm nhất) | expectedClose | createdAt
    (mặc định). nextCallFrom/nextCallTo: lọc cơ hội có hạn task mở sớm nhất trong khoảng ngày (chip 'hôm
    nay' = From=To=today, 'quá hạn' = To=hôm qua). Hỗ trợ cả chế độ list và kanban.

    Args:
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        q (str | Unset):
        status (str | Unset):
        stage_id (UUID | Unset):
        assignee_id (UUID | Unset):
        contact_id (UUID | Unset):
        lead_id (UUID | Unset):
        from_date (datetime.datetime | Unset):
        to_date (datetime.datetime | Unset):
        source_id (UUID | Unset):
        won_from (datetime.datetime | Unset):
        won_to (datetime.datetime | Unset):
        overdue (bool | Unset):
        pipeline_id (UUID | Unset):
        value_gte (float | Unset):
        value_lte (float | Unset):
        f (str | Unset):
        campaign_id (UUID | Unset):
        sort_by (str | Unset):
        next_call_from (datetime.date | Unset):
        next_call_to (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedResultOfOpportunitySummaryDto]
     """


    kwargs = _get_kwargs(
        page_number=page_number,
page_size=page_size,
q=q,
status=status,
stage_id=stage_id,
assignee_id=assignee_id,
contact_id=contact_id,
lead_id=lead_id,
from_date=from_date,
to_date=to_date,
source_id=source_id,
won_from=won_from,
won_to=won_to,
overdue=overdue,
pipeline_id=pipeline_id,
value_gte=value_gte,
value_lte=value_lte,
f=f,
campaign_id=campaign_id,
sort_by=sort_by,
next_call_from=next_call_from,
next_call_to=next_call_to,

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
    status: str | Unset = UNSET,
    stage_id: UUID | Unset = UNSET,
    assignee_id: UUID | Unset = UNSET,
    contact_id: UUID | Unset = UNSET,
    lead_id: UUID | Unset = UNSET,
    from_date: datetime.datetime | Unset = UNSET,
    to_date: datetime.datetime | Unset = UNSET,
    source_id: UUID | Unset = UNSET,
    won_from: datetime.datetime | Unset = UNSET,
    won_to: datetime.datetime | Unset = UNSET,
    overdue: bool | Unset = UNSET,
    pipeline_id: UUID | Unset = UNSET,
    value_gte: float | Unset = UNSET,
    value_lte: float | Unset = UNSET,
    f: str | Unset = UNSET,
    campaign_id: UUID | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    next_call_from: datetime.date | Unset = UNSET,
    next_call_to: datetime.date | Unset = UNSET,

) -> PagedResultOfOpportunitySummaryDto | None:
    """ Lấy danh sách opportunities

     Hỗ trợ full-text search (q: name/code) + filter theo status, stage, assignee, contact, lead. Drill-
    down dashboard: sourceId (nguồn của contact liên kết), wonFrom/wonTo (khoảng WonAt), overdue=true
    (Open + quá hạn đóng dự kiến theo ngày VN), valueGte/valueLte (khoảng giá trị dự kiến — VND),
    campaignId (chiến dịch nguồn). sortBy: nextCall (hạn task mở sớm nhất) | expectedClose | createdAt
    (mặc định). nextCallFrom/nextCallTo: lọc cơ hội có hạn task mở sớm nhất trong khoảng ngày (chip 'hôm
    nay' = From=To=today, 'quá hạn' = To=hôm qua). Hỗ trợ cả chế độ list và kanban.

    Args:
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        q (str | Unset):
        status (str | Unset):
        stage_id (UUID | Unset):
        assignee_id (UUID | Unset):
        contact_id (UUID | Unset):
        lead_id (UUID | Unset):
        from_date (datetime.datetime | Unset):
        to_date (datetime.datetime | Unset):
        source_id (UUID | Unset):
        won_from (datetime.datetime | Unset):
        won_to (datetime.datetime | Unset):
        overdue (bool | Unset):
        pipeline_id (UUID | Unset):
        value_gte (float | Unset):
        value_lte (float | Unset):
        f (str | Unset):
        campaign_id (UUID | Unset):
        sort_by (str | Unset):
        next_call_from (datetime.date | Unset):
        next_call_to (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedResultOfOpportunitySummaryDto
     """


    return (await asyncio_detailed(
        client=client,
page_number=page_number,
page_size=page_size,
q=q,
status=status,
stage_id=stage_id,
assignee_id=assignee_id,
contact_id=contact_id,
lead_id=lead_id,
from_date=from_date,
to_date=to_date,
source_id=source_id,
won_from=won_from,
won_to=won_to,
overdue=overdue,
pipeline_id=pipeline_id,
value_gte=value_gte,
value_lte=value_lte,
f=f,
campaign_id=campaign_id,
sort_by=sort_by,
next_call_from=next_call_from,
next_call_to=next_call_to,

    )).parsed

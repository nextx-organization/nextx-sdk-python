from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.call_list_result import CallListResult
from ...models.calls_list_direction import CallsListDirection
from ...models.calls_list_direction import check_calls_list_direction
from ...models.calls_list_status import CallsListStatus
from ...models.calls_list_status import check_calls_list_status
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    *,
    direction: CallsListDirection | Unset = UNSET,
    status: CallsListStatus | Unset = UNSET,
    agent_id: UUID | Unset = UNSET,
    queue_id: UUID | Unset = UNSET,
    campaign_id: UUID | Unset = UNSET,
    date_from: datetime.datetime | Unset = UNSET,
    date_to: datetime.datetime | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: str | Unset = 'createdAt',
    sort_order: str | Unset = 'desc',
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    crm_contact_id: UUID | Unset = UNSET,
    agent_inbox_id: UUID | Unset = UNSET,
    call_type: str | Unset = UNSET,
    disposition: str | Unset = UNSET,
    hour_from: int | Unset = UNSET,
    hour_to: int | Unset = UNSET,
    result: str | Unset = UNSET,
    culprit: str | Unset = UNSET,
    has_recording: bool | Unset = UNSET,
    duration_min: int | Unset = UNSET,
    duration_max: int | Unset = UNSET,
    f: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_direction: str | Unset = UNSET
    if not isinstance(direction, Unset):
        json_direction = direction

    params["direction"] = json_direction

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    json_agent_id: str | Unset = UNSET
    if not isinstance(agent_id, Unset):
        json_agent_id = str(agent_id)
    params["agentId"] = json_agent_id

    json_queue_id: str | Unset = UNSET
    if not isinstance(queue_id, Unset):
        json_queue_id = str(queue_id)
    params["queueId"] = json_queue_id

    json_campaign_id: str | Unset = UNSET
    if not isinstance(campaign_id, Unset):
        json_campaign_id = str(campaign_id)
    params["campaignId"] = json_campaign_id

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

    params["sortOrder"] = sort_order

    params["pageNumber"] = page_number

    params["pageSize"] = page_size

    json_crm_contact_id: str | Unset = UNSET
    if not isinstance(crm_contact_id, Unset):
        json_crm_contact_id = str(crm_contact_id)
    params["crmContactId"] = json_crm_contact_id

    json_agent_inbox_id: str | Unset = UNSET
    if not isinstance(agent_inbox_id, Unset):
        json_agent_inbox_id = str(agent_inbox_id)
    params["agentInboxId"] = json_agent_inbox_id

    params["callType"] = call_type

    params["disposition"] = disposition

    params["hourFrom"] = hour_from

    params["hourTo"] = hour_to

    params["result"] = result

    params["culprit"] = culprit

    params["hasRecording"] = has_recording

    params["durationMin"] = duration_min

    params["durationMax"] = duration_max

    params["f"] = f


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/call/calls",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CallListResult | None:
    if response.status_code == 200:
        response_200 = CallListResult.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CallListResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    direction: CallsListDirection | Unset = UNSET,
    status: CallsListStatus | Unset = UNSET,
    agent_id: UUID | Unset = UNSET,
    queue_id: UUID | Unset = UNSET,
    campaign_id: UUID | Unset = UNSET,
    date_from: datetime.datetime | Unset = UNSET,
    date_to: datetime.datetime | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: str | Unset = 'createdAt',
    sort_order: str | Unset = 'desc',
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    crm_contact_id: UUID | Unset = UNSET,
    agent_inbox_id: UUID | Unset = UNSET,
    call_type: str | Unset = UNSET,
    disposition: str | Unset = UNSET,
    hour_from: int | Unset = UNSET,
    hour_to: int | Unset = UNSET,
    result: str | Unset = UNSET,
    culprit: str | Unset = UNSET,
    has_recording: bool | Unset = UNSET,
    duration_min: int | Unset = UNSET,
    duration_max: int | Unset = UNSET,
    f: str | Unset = UNSET,

) -> Response[CallListResult]:
    """ Lịch sử cuộc gọi

     PagedResult với filters. Agent role: chỉ thấy calls có agent_id = userId.

    Args:
        direction (CallsListDirection | Unset):
        status (CallsListStatus | Unset):
        agent_id (UUID | Unset):
        queue_id (UUID | Unset):
        campaign_id (UUID | Unset):
        date_from (datetime.datetime | Unset):
        date_to (datetime.datetime | Unset):
        search (str | Unset):
        sort_by (str | Unset):  Default: 'createdAt'.
        sort_order (str | Unset):  Default: 'desc'.
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        crm_contact_id (UUID | Unset):
        agent_inbox_id (UUID | Unset):
        call_type (str | Unset):
        disposition (str | Unset):
        hour_from (int | Unset):
        hour_to (int | Unset):
        result (str | Unset):
        culprit (str | Unset):
        has_recording (bool | Unset):
        duration_min (int | Unset):
        duration_max (int | Unset):
        f (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CallListResult]
     """


    kwargs = _get_kwargs(
        direction=direction,
status=status,
agent_id=agent_id,
queue_id=queue_id,
campaign_id=campaign_id,
date_from=date_from,
date_to=date_to,
search=search,
sort_by=sort_by,
sort_order=sort_order,
page_number=page_number,
page_size=page_size,
crm_contact_id=crm_contact_id,
agent_inbox_id=agent_inbox_id,
call_type=call_type,
disposition=disposition,
hour_from=hour_from,
hour_to=hour_to,
result=result,
culprit=culprit,
has_recording=has_recording,
duration_min=duration_min,
duration_max=duration_max,
f=f,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    direction: CallsListDirection | Unset = UNSET,
    status: CallsListStatus | Unset = UNSET,
    agent_id: UUID | Unset = UNSET,
    queue_id: UUID | Unset = UNSET,
    campaign_id: UUID | Unset = UNSET,
    date_from: datetime.datetime | Unset = UNSET,
    date_to: datetime.datetime | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: str | Unset = 'createdAt',
    sort_order: str | Unset = 'desc',
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    crm_contact_id: UUID | Unset = UNSET,
    agent_inbox_id: UUID | Unset = UNSET,
    call_type: str | Unset = UNSET,
    disposition: str | Unset = UNSET,
    hour_from: int | Unset = UNSET,
    hour_to: int | Unset = UNSET,
    result: str | Unset = UNSET,
    culprit: str | Unset = UNSET,
    has_recording: bool | Unset = UNSET,
    duration_min: int | Unset = UNSET,
    duration_max: int | Unset = UNSET,
    f: str | Unset = UNSET,

) -> CallListResult | None:
    """ Lịch sử cuộc gọi

     PagedResult với filters. Agent role: chỉ thấy calls có agent_id = userId.

    Args:
        direction (CallsListDirection | Unset):
        status (CallsListStatus | Unset):
        agent_id (UUID | Unset):
        queue_id (UUID | Unset):
        campaign_id (UUID | Unset):
        date_from (datetime.datetime | Unset):
        date_to (datetime.datetime | Unset):
        search (str | Unset):
        sort_by (str | Unset):  Default: 'createdAt'.
        sort_order (str | Unset):  Default: 'desc'.
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        crm_contact_id (UUID | Unset):
        agent_inbox_id (UUID | Unset):
        call_type (str | Unset):
        disposition (str | Unset):
        hour_from (int | Unset):
        hour_to (int | Unset):
        result (str | Unset):
        culprit (str | Unset):
        has_recording (bool | Unset):
        duration_min (int | Unset):
        duration_max (int | Unset):
        f (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CallListResult
     """


    return sync_detailed(
        client=client,
direction=direction,
status=status,
agent_id=agent_id,
queue_id=queue_id,
campaign_id=campaign_id,
date_from=date_from,
date_to=date_to,
search=search,
sort_by=sort_by,
sort_order=sort_order,
page_number=page_number,
page_size=page_size,
crm_contact_id=crm_contact_id,
agent_inbox_id=agent_inbox_id,
call_type=call_type,
disposition=disposition,
hour_from=hour_from,
hour_to=hour_to,
result=result,
culprit=culprit,
has_recording=has_recording,
duration_min=duration_min,
duration_max=duration_max,
f=f,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    direction: CallsListDirection | Unset = UNSET,
    status: CallsListStatus | Unset = UNSET,
    agent_id: UUID | Unset = UNSET,
    queue_id: UUID | Unset = UNSET,
    campaign_id: UUID | Unset = UNSET,
    date_from: datetime.datetime | Unset = UNSET,
    date_to: datetime.datetime | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: str | Unset = 'createdAt',
    sort_order: str | Unset = 'desc',
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    crm_contact_id: UUID | Unset = UNSET,
    agent_inbox_id: UUID | Unset = UNSET,
    call_type: str | Unset = UNSET,
    disposition: str | Unset = UNSET,
    hour_from: int | Unset = UNSET,
    hour_to: int | Unset = UNSET,
    result: str | Unset = UNSET,
    culprit: str | Unset = UNSET,
    has_recording: bool | Unset = UNSET,
    duration_min: int | Unset = UNSET,
    duration_max: int | Unset = UNSET,
    f: str | Unset = UNSET,

) -> Response[CallListResult]:
    """ Lịch sử cuộc gọi

     PagedResult với filters. Agent role: chỉ thấy calls có agent_id = userId.

    Args:
        direction (CallsListDirection | Unset):
        status (CallsListStatus | Unset):
        agent_id (UUID | Unset):
        queue_id (UUID | Unset):
        campaign_id (UUID | Unset):
        date_from (datetime.datetime | Unset):
        date_to (datetime.datetime | Unset):
        search (str | Unset):
        sort_by (str | Unset):  Default: 'createdAt'.
        sort_order (str | Unset):  Default: 'desc'.
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        crm_contact_id (UUID | Unset):
        agent_inbox_id (UUID | Unset):
        call_type (str | Unset):
        disposition (str | Unset):
        hour_from (int | Unset):
        hour_to (int | Unset):
        result (str | Unset):
        culprit (str | Unset):
        has_recording (bool | Unset):
        duration_min (int | Unset):
        duration_max (int | Unset):
        f (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CallListResult]
     """


    kwargs = _get_kwargs(
        direction=direction,
status=status,
agent_id=agent_id,
queue_id=queue_id,
campaign_id=campaign_id,
date_from=date_from,
date_to=date_to,
search=search,
sort_by=sort_by,
sort_order=sort_order,
page_number=page_number,
page_size=page_size,
crm_contact_id=crm_contact_id,
agent_inbox_id=agent_inbox_id,
call_type=call_type,
disposition=disposition,
hour_from=hour_from,
hour_to=hour_to,
result=result,
culprit=culprit,
has_recording=has_recording,
duration_min=duration_min,
duration_max=duration_max,
f=f,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    direction: CallsListDirection | Unset = UNSET,
    status: CallsListStatus | Unset = UNSET,
    agent_id: UUID | Unset = UNSET,
    queue_id: UUID | Unset = UNSET,
    campaign_id: UUID | Unset = UNSET,
    date_from: datetime.datetime | Unset = UNSET,
    date_to: datetime.datetime | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: str | Unset = 'createdAt',
    sort_order: str | Unset = 'desc',
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    crm_contact_id: UUID | Unset = UNSET,
    agent_inbox_id: UUID | Unset = UNSET,
    call_type: str | Unset = UNSET,
    disposition: str | Unset = UNSET,
    hour_from: int | Unset = UNSET,
    hour_to: int | Unset = UNSET,
    result: str | Unset = UNSET,
    culprit: str | Unset = UNSET,
    has_recording: bool | Unset = UNSET,
    duration_min: int | Unset = UNSET,
    duration_max: int | Unset = UNSET,
    f: str | Unset = UNSET,

) -> CallListResult | None:
    """ Lịch sử cuộc gọi

     PagedResult với filters. Agent role: chỉ thấy calls có agent_id = userId.

    Args:
        direction (CallsListDirection | Unset):
        status (CallsListStatus | Unset):
        agent_id (UUID | Unset):
        queue_id (UUID | Unset):
        campaign_id (UUID | Unset):
        date_from (datetime.datetime | Unset):
        date_to (datetime.datetime | Unset):
        search (str | Unset):
        sort_by (str | Unset):  Default: 'createdAt'.
        sort_order (str | Unset):  Default: 'desc'.
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        crm_contact_id (UUID | Unset):
        agent_inbox_id (UUID | Unset):
        call_type (str | Unset):
        disposition (str | Unset):
        hour_from (int | Unset):
        hour_to (int | Unset):
        result (str | Unset):
        culprit (str | Unset):
        has_recording (bool | Unset):
        duration_min (int | Unset):
        duration_max (int | Unset):
        f (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CallListResult
     """


    return (await asyncio_detailed(
        client=client,
direction=direction,
status=status,
agent_id=agent_id,
queue_id=queue_id,
campaign_id=campaign_id,
date_from=date_from,
date_to=date_to,
search=search,
sort_by=sort_by,
sort_order=sort_order,
page_number=page_number,
page_size=page_size,
crm_contact_id=crm_contact_id,
agent_inbox_id=agent_inbox_id,
call_type=call_type,
disposition=disposition,
hour_from=hour_from,
hour_to=hour_to,
result=result,
culprit=culprit,
has_recording=has_recording,
duration_min=duration_min,
duration_max=duration_max,
f=f,

    )).parsed

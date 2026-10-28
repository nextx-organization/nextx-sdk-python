from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paged_result_of_workspace_activity_dto import PagedResultOfWorkspaceActivityDto
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    *,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    activity_type: str | Unset = UNSET,
    from_date: datetime.datetime | Unset = UNSET,
    to_date: datetime.datetime | Unset = UNSET,
    contact_id: UUID | Unset = UNSET,
    day_of_week: int | Unset = UNSET,
    hour: int | Unset = UNSET,
    activity_types: list[str] | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["pageNumber"] = page_number

    params["pageSize"] = page_size

    params["activityType"] = activity_type

    json_from_date: str | Unset = UNSET
    if not isinstance(from_date, Unset):
        json_from_date = from_date.isoformat()
    params["fromDate"] = json_from_date

    json_to_date: str | Unset = UNSET
    if not isinstance(to_date, Unset):
        json_to_date = to_date.isoformat()
    params["toDate"] = json_to_date

    json_contact_id: str | Unset = UNSET
    if not isinstance(contact_id, Unset):
        json_contact_id = str(contact_id)
    params["contactId"] = json_contact_id

    params["dayOfWeek"] = day_of_week

    params["hour"] = hour

    json_activity_types: list[str] | Unset = UNSET
    if not isinstance(activity_types, Unset):
        json_activity_types = activity_types


    params["activityTypes"] = json_activity_types


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/crm/activities",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PagedResultOfWorkspaceActivityDto | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = PagedResultOfWorkspaceActivityDto.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ProblemDetails.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PagedResultOfWorkspaceActivityDto | ProblemDetails]:
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
    activity_type: str | Unset = UNSET,
    from_date: datetime.datetime | Unset = UNSET,
    to_date: datetime.datetime | Unset = UNSET,
    contact_id: UUID | Unset = UNSET,
    day_of_week: int | Unset = UNSET,
    hour: int | Unset = UNSET,
    activity_types: list[str] | Unset = UNSET,

) -> Response[PagedResultOfWorkspaceActivityDto | ProblemDetails]:
    """ Danh sách hoạt động workspace

     Variant workspace-wide của GET /contacts/{id}/activities — filter theo activityType, khoảng thời
    gian, contactId. Drill-down dashboard: dayOfWeek (0=Thứ Hai..6=Chủ Nhật) + hour (0-23) bucket theo
    giờ VN (UTC+7) — dùng cho heatmap; activityTypes (lặp lại query param) lọc nhiều loại cùng lúc, ưu
    tiên hơn activityType. Sắp theo occurredAt giảm dần. Không cache.

    Args:
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        activity_type (str | Unset):
        from_date (datetime.datetime | Unset):
        to_date (datetime.datetime | Unset):
        contact_id (UUID | Unset):
        day_of_week (int | Unset):
        hour (int | Unset):
        activity_types (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedResultOfWorkspaceActivityDto | ProblemDetails]
     """


    kwargs = _get_kwargs(
        page_number=page_number,
page_size=page_size,
activity_type=activity_type,
from_date=from_date,
to_date=to_date,
contact_id=contact_id,
day_of_week=day_of_week,
hour=hour,
activity_types=activity_types,

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
    activity_type: str | Unset = UNSET,
    from_date: datetime.datetime | Unset = UNSET,
    to_date: datetime.datetime | Unset = UNSET,
    contact_id: UUID | Unset = UNSET,
    day_of_week: int | Unset = UNSET,
    hour: int | Unset = UNSET,
    activity_types: list[str] | Unset = UNSET,

) -> PagedResultOfWorkspaceActivityDto | ProblemDetails | None:
    """ Danh sách hoạt động workspace

     Variant workspace-wide của GET /contacts/{id}/activities — filter theo activityType, khoảng thời
    gian, contactId. Drill-down dashboard: dayOfWeek (0=Thứ Hai..6=Chủ Nhật) + hour (0-23) bucket theo
    giờ VN (UTC+7) — dùng cho heatmap; activityTypes (lặp lại query param) lọc nhiều loại cùng lúc, ưu
    tiên hơn activityType. Sắp theo occurredAt giảm dần. Không cache.

    Args:
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        activity_type (str | Unset):
        from_date (datetime.datetime | Unset):
        to_date (datetime.datetime | Unset):
        contact_id (UUID | Unset):
        day_of_week (int | Unset):
        hour (int | Unset):
        activity_types (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedResultOfWorkspaceActivityDto | ProblemDetails
     """


    return sync_detailed(
        client=client,
page_number=page_number,
page_size=page_size,
activity_type=activity_type,
from_date=from_date,
to_date=to_date,
contact_id=contact_id,
day_of_week=day_of_week,
hour=hour,
activity_types=activity_types,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    activity_type: str | Unset = UNSET,
    from_date: datetime.datetime | Unset = UNSET,
    to_date: datetime.datetime | Unset = UNSET,
    contact_id: UUID | Unset = UNSET,
    day_of_week: int | Unset = UNSET,
    hour: int | Unset = UNSET,
    activity_types: list[str] | Unset = UNSET,

) -> Response[PagedResultOfWorkspaceActivityDto | ProblemDetails]:
    """ Danh sách hoạt động workspace

     Variant workspace-wide của GET /contacts/{id}/activities — filter theo activityType, khoảng thời
    gian, contactId. Drill-down dashboard: dayOfWeek (0=Thứ Hai..6=Chủ Nhật) + hour (0-23) bucket theo
    giờ VN (UTC+7) — dùng cho heatmap; activityTypes (lặp lại query param) lọc nhiều loại cùng lúc, ưu
    tiên hơn activityType. Sắp theo occurredAt giảm dần. Không cache.

    Args:
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        activity_type (str | Unset):
        from_date (datetime.datetime | Unset):
        to_date (datetime.datetime | Unset):
        contact_id (UUID | Unset):
        day_of_week (int | Unset):
        hour (int | Unset):
        activity_types (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedResultOfWorkspaceActivityDto | ProblemDetails]
     """


    kwargs = _get_kwargs(
        page_number=page_number,
page_size=page_size,
activity_type=activity_type,
from_date=from_date,
to_date=to_date,
contact_id=contact_id,
day_of_week=day_of_week,
hour=hour,
activity_types=activity_types,

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
    activity_type: str | Unset = UNSET,
    from_date: datetime.datetime | Unset = UNSET,
    to_date: datetime.datetime | Unset = UNSET,
    contact_id: UUID | Unset = UNSET,
    day_of_week: int | Unset = UNSET,
    hour: int | Unset = UNSET,
    activity_types: list[str] | Unset = UNSET,

) -> PagedResultOfWorkspaceActivityDto | ProblemDetails | None:
    """ Danh sách hoạt động workspace

     Variant workspace-wide của GET /contacts/{id}/activities — filter theo activityType, khoảng thời
    gian, contactId. Drill-down dashboard: dayOfWeek (0=Thứ Hai..6=Chủ Nhật) + hour (0-23) bucket theo
    giờ VN (UTC+7) — dùng cho heatmap; activityTypes (lặp lại query param) lọc nhiều loại cùng lúc, ưu
    tiên hơn activityType. Sắp theo occurredAt giảm dần. Không cache.

    Args:
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        activity_type (str | Unset):
        from_date (datetime.datetime | Unset):
        to_date (datetime.datetime | Unset):
        contact_id (UUID | Unset):
        day_of_week (int | Unset):
        hour (int | Unset):
        activity_types (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedResultOfWorkspaceActivityDto | ProblemDetails
     """


    return (await asyncio_detailed(
        client=client,
page_number=page_number,
page_size=page_size,
activity_type=activity_type,
from_date=from_date,
to_date=to_date,
contact_id=contact_id,
day_of_week=day_of_week,
hour=hour,
activity_types=activity_types,

    )).parsed

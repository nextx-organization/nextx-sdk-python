from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.daily_plan_dto_paged_result import DailyPlanDtoPagedResult
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    *,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    employee_id: UUID | Unset = UNSET,
    plan_date: datetime.date | Unset = UNSET,
    status: str | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["pageSize"] = page_size

    json_employee_id: str | Unset = UNSET
    if not isinstance(employee_id, Unset):
        json_employee_id = str(employee_id)
    params["employeeId"] = json_employee_id

    json_plan_date: str | Unset = UNSET
    if not isinstance(plan_date, Unset):
        json_plan_date = plan_date.isoformat()
    params["planDate"] = json_plan_date

    params["status"] = status

    json_zone_id: str | Unset = UNSET
    if not isinstance(zone_id, Unset):
        json_zone_id = str(zone_id)
    params["zoneId"] = json_zone_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/dms/daily-plans",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DailyPlanDtoPagedResult | None:
    if response.status_code == 200:
        response_200 = DailyPlanDtoPagedResult.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DailyPlanDtoPagedResult]:
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
    employee_id: UUID | Unset = UNSET,
    plan_date: datetime.date | Unset = UNSET,
    status: str | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,

) -> Response[DailyPlanDtoPagedResult]:
    """ Danh sách kế hoạch ngày

     Lấy danh sách kế hoạch ngày. Manager/Supervisor xem được tất cả, NV chỉ xem được bản thân.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        employee_id (UUID | Unset):
        plan_date (datetime.date | Unset):
        status (str | Unset):
        zone_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DailyPlanDtoPagedResult]
     """


    kwargs = _get_kwargs(
        page=page,
page_size=page_size,
employee_id=employee_id,
plan_date=plan_date,
status=status,
zone_id=zone_id,

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
    employee_id: UUID | Unset = UNSET,
    plan_date: datetime.date | Unset = UNSET,
    status: str | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,

) -> DailyPlanDtoPagedResult | None:
    """ Danh sách kế hoạch ngày

     Lấy danh sách kế hoạch ngày. Manager/Supervisor xem được tất cả, NV chỉ xem được bản thân.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        employee_id (UUID | Unset):
        plan_date (datetime.date | Unset):
        status (str | Unset):
        zone_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DailyPlanDtoPagedResult
     """


    return sync_detailed(
        client=client,
page=page,
page_size=page_size,
employee_id=employee_id,
plan_date=plan_date,
status=status,
zone_id=zone_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    employee_id: UUID | Unset = UNSET,
    plan_date: datetime.date | Unset = UNSET,
    status: str | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,

) -> Response[DailyPlanDtoPagedResult]:
    """ Danh sách kế hoạch ngày

     Lấy danh sách kế hoạch ngày. Manager/Supervisor xem được tất cả, NV chỉ xem được bản thân.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        employee_id (UUID | Unset):
        plan_date (datetime.date | Unset):
        status (str | Unset):
        zone_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DailyPlanDtoPagedResult]
     """


    kwargs = _get_kwargs(
        page=page,
page_size=page_size,
employee_id=employee_id,
plan_date=plan_date,
status=status,
zone_id=zone_id,

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
    employee_id: UUID | Unset = UNSET,
    plan_date: datetime.date | Unset = UNSET,
    status: str | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,

) -> DailyPlanDtoPagedResult | None:
    """ Danh sách kế hoạch ngày

     Lấy danh sách kế hoạch ngày. Manager/Supervisor xem được tất cả, NV chỉ xem được bản thân.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        employee_id (UUID | Unset):
        plan_date (datetime.date | Unset):
        status (str | Unset):
        zone_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DailyPlanDtoPagedResult
     """


    return (await asyncio_detailed(
        client=client,
page=page,
page_size=page_size,
employee_id=employee_id,
plan_date=plan_date,
status=status,
zone_id=zone_id,

    )).parsed

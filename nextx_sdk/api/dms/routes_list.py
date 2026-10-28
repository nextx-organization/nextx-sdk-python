from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.route_dto_paged_result import RouteDtoPagedResult
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    branch_ids: str | Unset = UNSET,
    zone_ids: str | Unset = UNSET,
    channel_codes: str | Unset = UNSET,
    days_of_week: str | Unset = UNSET,
    status: str | Unset = UNSET,
    employee_id: UUID | Unset = UNSET,
    search: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["pageSize"] = page_size

    params["branchIds"] = branch_ids

    params["zoneIds"] = zone_ids

    params["channelCodes"] = channel_codes

    params["daysOfWeek"] = days_of_week

    params["status"] = status

    json_employee_id: str | Unset = UNSET
    if not isinstance(employee_id, Unset):
        json_employee_id = str(employee_id)
    params["employeeId"] = json_employee_id

    params["search"] = search


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/dms/routes",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RouteDtoPagedResult | None:
    if response.status_code == 200:
        response_200 = RouteDtoPagedResult.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RouteDtoPagedResult]:
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
    branch_ids: str | Unset = UNSET,
    zone_ids: str | Unset = UNSET,
    channel_codes: str | Unset = UNSET,
    days_of_week: str | Unset = UNSET,
    status: str | Unset = UNSET,
    employee_id: UUID | Unset = UNSET,
    search: str | Unset = UNSET,

) -> Response[RouteDtoPagedResult]:
    """ Danh sách tuyến

     Lấy danh sách tuyến bán hàng theo workspace. Hỗ trợ filter theo branch, zone, kênh, ngày trong tuần,
    nhân viên và tìm kiếm theo mã/tên tuyến.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        branch_ids (str | Unset):
        zone_ids (str | Unset):
        channel_codes (str | Unset):
        days_of_week (str | Unset):
        status (str | Unset):
        employee_id (UUID | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RouteDtoPagedResult]
     """


    kwargs = _get_kwargs(
        page=page,
page_size=page_size,
branch_ids=branch_ids,
zone_ids=zone_ids,
channel_codes=channel_codes,
days_of_week=days_of_week,
status=status,
employee_id=employee_id,
search=search,

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
    branch_ids: str | Unset = UNSET,
    zone_ids: str | Unset = UNSET,
    channel_codes: str | Unset = UNSET,
    days_of_week: str | Unset = UNSET,
    status: str | Unset = UNSET,
    employee_id: UUID | Unset = UNSET,
    search: str | Unset = UNSET,

) -> RouteDtoPagedResult | None:
    """ Danh sách tuyến

     Lấy danh sách tuyến bán hàng theo workspace. Hỗ trợ filter theo branch, zone, kênh, ngày trong tuần,
    nhân viên và tìm kiếm theo mã/tên tuyến.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        branch_ids (str | Unset):
        zone_ids (str | Unset):
        channel_codes (str | Unset):
        days_of_week (str | Unset):
        status (str | Unset):
        employee_id (UUID | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RouteDtoPagedResult
     """


    return sync_detailed(
        client=client,
page=page,
page_size=page_size,
branch_ids=branch_ids,
zone_ids=zone_ids,
channel_codes=channel_codes,
days_of_week=days_of_week,
status=status,
employee_id=employee_id,
search=search,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    branch_ids: str | Unset = UNSET,
    zone_ids: str | Unset = UNSET,
    channel_codes: str | Unset = UNSET,
    days_of_week: str | Unset = UNSET,
    status: str | Unset = UNSET,
    employee_id: UUID | Unset = UNSET,
    search: str | Unset = UNSET,

) -> Response[RouteDtoPagedResult]:
    """ Danh sách tuyến

     Lấy danh sách tuyến bán hàng theo workspace. Hỗ trợ filter theo branch, zone, kênh, ngày trong tuần,
    nhân viên và tìm kiếm theo mã/tên tuyến.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        branch_ids (str | Unset):
        zone_ids (str | Unset):
        channel_codes (str | Unset):
        days_of_week (str | Unset):
        status (str | Unset):
        employee_id (UUID | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RouteDtoPagedResult]
     """


    kwargs = _get_kwargs(
        page=page,
page_size=page_size,
branch_ids=branch_ids,
zone_ids=zone_ids,
channel_codes=channel_codes,
days_of_week=days_of_week,
status=status,
employee_id=employee_id,
search=search,

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
    branch_ids: str | Unset = UNSET,
    zone_ids: str | Unset = UNSET,
    channel_codes: str | Unset = UNSET,
    days_of_week: str | Unset = UNSET,
    status: str | Unset = UNSET,
    employee_id: UUID | Unset = UNSET,
    search: str | Unset = UNSET,

) -> RouteDtoPagedResult | None:
    """ Danh sách tuyến

     Lấy danh sách tuyến bán hàng theo workspace. Hỗ trợ filter theo branch, zone, kênh, ngày trong tuần,
    nhân viên và tìm kiếm theo mã/tên tuyến.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        branch_ids (str | Unset):
        zone_ids (str | Unset):
        channel_codes (str | Unset):
        days_of_week (str | Unset):
        status (str | Unset):
        employee_id (UUID | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RouteDtoPagedResult
     """


    return (await asyncio_detailed(
        client=client,
page=page,
page_size=page_size,
branch_ids=branch_ids,
zone_ids=zone_ids,
channel_codes=channel_codes,
days_of_week=days_of_week,
status=status,
employee_id=employee_id,
search=search,

    )).parsed

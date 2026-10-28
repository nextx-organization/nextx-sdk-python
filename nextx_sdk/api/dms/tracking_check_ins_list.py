from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.checkin_log_dto_paged_result import CheckinLogDtoPagedResult
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    *,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    employee_id: UUID | Unset = UNSET,
    date_from: datetime.date | Unset = UNSET,
    date_to: datetime.date | Unset = UNSET,
    is_valid: bool | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["pageSize"] = page_size

    json_employee_id: str | Unset = UNSET
    if not isinstance(employee_id, Unset):
        json_employee_id = str(employee_id)
    params["employeeId"] = json_employee_id

    json_date_from: str | Unset = UNSET
    if not isinstance(date_from, Unset):
        json_date_from = date_from.isoformat()
    params["dateFrom"] = json_date_from

    json_date_to: str | Unset = UNSET
    if not isinstance(date_to, Unset):
        json_date_to = date_to.isoformat()
    params["dateTo"] = json_date_to

    params["isValid"] = is_valid


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/dms/tracking/check-ins",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CheckinLogDtoPagedResult | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = CheckinLogDtoPagedResult.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = ProblemDetails.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CheckinLogDtoPagedResult | ProblemDetails]:
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
    date_from: datetime.date | Unset = UNSET,
    date_to: datetime.date | Unset = UNSET,
    is_valid: bool | Unset = UNSET,

) -> Response[CheckinLogDtoPagedResult | ProblemDetails]:
    """ Danh sach check-in

     Lay danh sach check-in. Date range toi da 30 ngay. Loc theo isValid (true=hop le, false=bi flag geo-
    fence). Manager/Supervisor xem tat ca, NV xem ban than.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        employee_id (UUID | Unset):
        date_from (datetime.date | Unset):
        date_to (datetime.date | Unset):
        is_valid (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckinLogDtoPagedResult | ProblemDetails]
     """


    kwargs = _get_kwargs(
        page=page,
page_size=page_size,
employee_id=employee_id,
date_from=date_from,
date_to=date_to,
is_valid=is_valid,

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
    date_from: datetime.date | Unset = UNSET,
    date_to: datetime.date | Unset = UNSET,
    is_valid: bool | Unset = UNSET,

) -> CheckinLogDtoPagedResult | ProblemDetails | None:
    """ Danh sach check-in

     Lay danh sach check-in. Date range toi da 30 ngay. Loc theo isValid (true=hop le, false=bi flag geo-
    fence). Manager/Supervisor xem tat ca, NV xem ban than.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        employee_id (UUID | Unset):
        date_from (datetime.date | Unset):
        date_to (datetime.date | Unset):
        is_valid (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckinLogDtoPagedResult | ProblemDetails
     """


    return sync_detailed(
        client=client,
page=page,
page_size=page_size,
employee_id=employee_id,
date_from=date_from,
date_to=date_to,
is_valid=is_valid,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    employee_id: UUID | Unset = UNSET,
    date_from: datetime.date | Unset = UNSET,
    date_to: datetime.date | Unset = UNSET,
    is_valid: bool | Unset = UNSET,

) -> Response[CheckinLogDtoPagedResult | ProblemDetails]:
    """ Danh sach check-in

     Lay danh sach check-in. Date range toi da 30 ngay. Loc theo isValid (true=hop le, false=bi flag geo-
    fence). Manager/Supervisor xem tat ca, NV xem ban than.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        employee_id (UUID | Unset):
        date_from (datetime.date | Unset):
        date_to (datetime.date | Unset):
        is_valid (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckinLogDtoPagedResult | ProblemDetails]
     """


    kwargs = _get_kwargs(
        page=page,
page_size=page_size,
employee_id=employee_id,
date_from=date_from,
date_to=date_to,
is_valid=is_valid,

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
    date_from: datetime.date | Unset = UNSET,
    date_to: datetime.date | Unset = UNSET,
    is_valid: bool | Unset = UNSET,

) -> CheckinLogDtoPagedResult | ProblemDetails | None:
    """ Danh sach check-in

     Lay danh sach check-in. Date range toi da 30 ngay. Loc theo isValid (true=hop le, false=bi flag geo-
    fence). Manager/Supervisor xem tat ca, NV xem ban than.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        employee_id (UUID | Unset):
        date_from (datetime.date | Unset):
        date_to (datetime.date | Unset):
        is_valid (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckinLogDtoPagedResult | ProblemDetails
     """


    return (await asyncio_detailed(
        client=client,
page=page,
page_size=page_size,
employee_id=employee_id,
date_from=date_from,
date_to=date_to,
is_valid=is_valid,

    )).parsed

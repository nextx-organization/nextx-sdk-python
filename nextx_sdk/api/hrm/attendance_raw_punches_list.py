from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paged_result_of_attendance_raw_punch_dto import PagedResultOfAttendanceRawPunchDto
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    *,
    employee_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    credential_type: str | Unset = UNSET,
    device_serial: str | Unset = UNSET,
    search: str | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    include_duplicates: bool | Unset = False,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_employee_id: str | Unset = UNSET
    if not isinstance(employee_id, Unset):
        json_employee_id = str(employee_id)
    params["employeeId"] = json_employee_id

    params["status"] = status

    params["credentialType"] = credential_type

    params["deviceSerial"] = device_serial

    params["search"] = search

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params["page"] = page

    params["pageSize"] = page_size

    params["includeDuplicates"] = include_duplicates


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/hrm/attendance/raw-punches",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PagedResultOfAttendanceRawPunchDto | None:
    if response.status_code == 200:
        response_200 = PagedResultOfAttendanceRawPunchDto.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PagedResultOfAttendanceRawPunchDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    employee_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    credential_type: str | Unset = UNSET,
    device_serial: str | Unset = UNSET,
    search: str | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    include_duplicates: bool | Unset = False,

) -> Response[PagedResultOfAttendanceRawPunchDto]:
    """ Liệt kê raw punch events

     Filter theo employee/status/date range. Status: PENDING / PROCESSED / UNMATCHED / FAILED.

    Args:
        employee_id (UUID | Unset):
        status (str | Unset):
        credential_type (str | Unset):
        device_serial (str | Unset):
        search (str | Unset):
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        include_duplicates (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedResultOfAttendanceRawPunchDto]
     """


    kwargs = _get_kwargs(
        employee_id=employee_id,
status=status,
credential_type=credential_type,
device_serial=device_serial,
search=search,
from_=from_,
to=to,
page=page,
page_size=page_size,
include_duplicates=include_duplicates,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    employee_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    credential_type: str | Unset = UNSET,
    device_serial: str | Unset = UNSET,
    search: str | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    include_duplicates: bool | Unset = False,

) -> PagedResultOfAttendanceRawPunchDto | None:
    """ Liệt kê raw punch events

     Filter theo employee/status/date range. Status: PENDING / PROCESSED / UNMATCHED / FAILED.

    Args:
        employee_id (UUID | Unset):
        status (str | Unset):
        credential_type (str | Unset):
        device_serial (str | Unset):
        search (str | Unset):
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        include_duplicates (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedResultOfAttendanceRawPunchDto
     """


    return sync_detailed(
        client=client,
employee_id=employee_id,
status=status,
credential_type=credential_type,
device_serial=device_serial,
search=search,
from_=from_,
to=to,
page=page,
page_size=page_size,
include_duplicates=include_duplicates,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    employee_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    credential_type: str | Unset = UNSET,
    device_serial: str | Unset = UNSET,
    search: str | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    include_duplicates: bool | Unset = False,

) -> Response[PagedResultOfAttendanceRawPunchDto]:
    """ Liệt kê raw punch events

     Filter theo employee/status/date range. Status: PENDING / PROCESSED / UNMATCHED / FAILED.

    Args:
        employee_id (UUID | Unset):
        status (str | Unset):
        credential_type (str | Unset):
        device_serial (str | Unset):
        search (str | Unset):
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        include_duplicates (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedResultOfAttendanceRawPunchDto]
     """


    kwargs = _get_kwargs(
        employee_id=employee_id,
status=status,
credential_type=credential_type,
device_serial=device_serial,
search=search,
from_=from_,
to=to,
page=page,
page_size=page_size,
include_duplicates=include_duplicates,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    employee_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    credential_type: str | Unset = UNSET,
    device_serial: str | Unset = UNSET,
    search: str | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    include_duplicates: bool | Unset = False,

) -> PagedResultOfAttendanceRawPunchDto | None:
    """ Liệt kê raw punch events

     Filter theo employee/status/date range. Status: PENDING / PROCESSED / UNMATCHED / FAILED.

    Args:
        employee_id (UUID | Unset):
        status (str | Unset):
        credential_type (str | Unset):
        device_serial (str | Unset):
        search (str | Unset):
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        include_duplicates (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedResultOfAttendanceRawPunchDto
     """


    return (await asyncio_detailed(
        client=client,
employee_id=employee_id,
status=status,
credential_type=credential_type,
device_serial=device_serial,
search=search,
from_=from_,
to=to,
page=page,
page_size=page_size,
include_duplicates=include_duplicates,

    )).parsed

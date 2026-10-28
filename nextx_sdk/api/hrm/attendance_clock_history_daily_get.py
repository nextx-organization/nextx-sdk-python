from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paged_result_of_daily_clock_row import PagedResultOfDailyClockRow
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    *,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    employee_id: UUID | Unset = UNSET,
    org_unit_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    json_employee_id: str | Unset = UNSET
    if not isinstance(employee_id, Unset):
        json_employee_id = str(employee_id)
    params["employeeId"] = json_employee_id

    json_org_unit_id: str | Unset = UNSET
    if not isinstance(org_unit_id, Unset):
        json_org_unit_id = str(org_unit_id)
    params["orgUnitId"] = json_org_unit_id

    params["page"] = page

    params["pageSize"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/hrm/attendance/clock-history/daily",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PagedResultOfDailyClockRow | None:
    if response.status_code == 200:
        response_200 = PagedResultOfDailyClockRow.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PagedResultOfDailyClockRow]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    employee_id: UUID | Unset = UNSET,
    org_unit_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> Response[PagedResultOfDailyClockRow]:
    """ P2 — Lịch sử chấm công gom theo ngày (có phân trang)

     1 row / NV / ngày: firstIn, lastOut, scanCount, sources, manualEntryCount.

    Args:
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):
        employee_id (UUID | Unset):
        org_unit_id (UUID | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedResultOfDailyClockRow]
     """


    kwargs = _get_kwargs(
        from_=from_,
to=to,
employee_id=employee_id,
org_unit_id=org_unit_id,
page=page,
page_size=page_size,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    employee_id: UUID | Unset = UNSET,
    org_unit_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> PagedResultOfDailyClockRow | None:
    """ P2 — Lịch sử chấm công gom theo ngày (có phân trang)

     1 row / NV / ngày: firstIn, lastOut, scanCount, sources, manualEntryCount.

    Args:
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):
        employee_id (UUID | Unset):
        org_unit_id (UUID | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedResultOfDailyClockRow
     """


    return sync_detailed(
        client=client,
from_=from_,
to=to,
employee_id=employee_id,
org_unit_id=org_unit_id,
page=page,
page_size=page_size,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    employee_id: UUID | Unset = UNSET,
    org_unit_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> Response[PagedResultOfDailyClockRow]:
    """ P2 — Lịch sử chấm công gom theo ngày (có phân trang)

     1 row / NV / ngày: firstIn, lastOut, scanCount, sources, manualEntryCount.

    Args:
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):
        employee_id (UUID | Unset):
        org_unit_id (UUID | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedResultOfDailyClockRow]
     """


    kwargs = _get_kwargs(
        from_=from_,
to=to,
employee_id=employee_id,
org_unit_id=org_unit_id,
page=page,
page_size=page_size,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    employee_id: UUID | Unset = UNSET,
    org_unit_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> PagedResultOfDailyClockRow | None:
    """ P2 — Lịch sử chấm công gom theo ngày (có phân trang)

     1 row / NV / ngày: firstIn, lastOut, scanCount, sources, manualEntryCount.

    Args:
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):
        employee_id (UUID | Unset):
        org_unit_id (UUID | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedResultOfDailyClockRow
     """


    return (await asyncio_detailed(
        client=client,
from_=from_,
to=to,
employee_id=employee_id,
org_unit_id=org_unit_id,
page=page,
page_size=page_size,

    )).parsed

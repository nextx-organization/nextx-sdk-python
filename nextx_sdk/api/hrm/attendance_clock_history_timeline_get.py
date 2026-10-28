from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.timeline_event_row import TimelineEventRow
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    employee_id: UUID,
    *,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,

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


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/hrm/attendance/clock-history/timeline/{employee_id}".format(employee_id=quote(str(employee_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[TimelineEventRow] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = TimelineEventRow.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[TimelineEventRow]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    employee_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,

) -> Response[list[TimelineEventRow]]:
    """ P3 — Timeline 1 NV (union device + manual)

     Trả mọi event chấm công theo time desc, badge source DEVICE/MANUAL.

    Args:
        employee_id (UUID):
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[TimelineEventRow]]
     """


    kwargs = _get_kwargs(
        employee_id=employee_id,
from_=from_,
to=to,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    employee_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,

) -> list[TimelineEventRow] | None:
    """ P3 — Timeline 1 NV (union device + manual)

     Trả mọi event chấm công theo time desc, badge source DEVICE/MANUAL.

    Args:
        employee_id (UUID):
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[TimelineEventRow]
     """


    return sync_detailed(
        employee_id=employee_id,
client=client,
from_=from_,
to=to,

    ).parsed

async def asyncio_detailed(
    employee_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,

) -> Response[list[TimelineEventRow]]:
    """ P3 — Timeline 1 NV (union device + manual)

     Trả mọi event chấm công theo time desc, badge source DEVICE/MANUAL.

    Args:
        employee_id (UUID):
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[TimelineEventRow]]
     """


    kwargs = _get_kwargs(
        employee_id=employee_id,
from_=from_,
to=to,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    employee_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,

) -> list[TimelineEventRow] | None:
    """ P3 — Timeline 1 NV (union device + manual)

     Trả mọi event chấm công theo time desc, badge source DEVICE/MANUAL.

    Args:
        employee_id (UUID):
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[TimelineEventRow]
     """


    return (await asyncio_detailed(
        employee_id=employee_id,
client=client,
from_=from_,
to=to,

    )).parsed

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.problem_details import ProblemDetails
from ...models.record_dto import RecordDto
from typing import cast
from uuid import UUID



def _get_kwargs(
    table_id: UUID,
    record_id: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/office/tables/{table_id}/records/{record_id}".format(table_id=quote(str(table_id), safe=""),record_id=quote(str(record_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ProblemDetails | RecordDto | None:
    if response.status_code == 200:
        response_200 = RecordDto.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ProblemDetails | RecordDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    table_id: UUID,
    record_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ProblemDetails | RecordDto]:
    """ Lấy chi tiết record

    Args:
        table_id (UUID):
        record_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | RecordDto]
     """


    kwargs = _get_kwargs(
        table_id=table_id,
record_id=record_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    table_id: UUID,
    record_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> ProblemDetails | RecordDto | None:
    """ Lấy chi tiết record

    Args:
        table_id (UUID):
        record_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | RecordDto
     """


    return sync_detailed(
        table_id=table_id,
record_id=record_id,
client=client,

    ).parsed

async def asyncio_detailed(
    table_id: UUID,
    record_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ProblemDetails | RecordDto]:
    """ Lấy chi tiết record

    Args:
        table_id (UUID):
        record_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | RecordDto]
     """


    kwargs = _get_kwargs(
        table_id=table_id,
record_id=record_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    table_id: UUID,
    record_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> ProblemDetails | RecordDto | None:
    """ Lấy chi tiết record

    Args:
        table_id (UUID):
        record_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | RecordDto
     """


    return (await asyncio_detailed(
        table_id=table_id,
record_id=record_id,
client=client,

    )).parsed

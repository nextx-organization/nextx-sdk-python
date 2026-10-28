from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.completed_intent_dto import CompletedIntentDto
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    *,
    workspace_id: UUID | Unset = UNSET,
    reference_types: str | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    take: int | Unset = 200,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_workspace_id: str | Unset = UNSET
    if not isinstance(workspace_id, Unset):
        json_workspace_id = str(workspace_id)
    params["workspaceId"] = json_workspace_id

    params["referenceTypes"] = reference_types

    json_since: str | Unset = UNSET
    if not isinstance(since, Unset):
        json_since = since.isoformat()
    params["since"] = json_since

    params["take"] = take


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/payment/intents/completed",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[CompletedIntentDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = CompletedIntentDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[CompletedIntentDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    workspace_id: UUID | Unset = UNSET,
    reference_types: str | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    take: int | Unset = 200,

) -> Response[list[CompletedIntentDto]]:
    """ 
    Args:
        workspace_id (UUID | Unset):
        reference_types (str | Unset):
        since (datetime.datetime | Unset):
        take (int | Unset):  Default: 200.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[CompletedIntentDto]]
     """


    kwargs = _get_kwargs(
        workspace_id=workspace_id,
reference_types=reference_types,
since=since,
take=take,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    workspace_id: UUID | Unset = UNSET,
    reference_types: str | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    take: int | Unset = 200,

) -> list[CompletedIntentDto] | None:
    """ 
    Args:
        workspace_id (UUID | Unset):
        reference_types (str | Unset):
        since (datetime.datetime | Unset):
        take (int | Unset):  Default: 200.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[CompletedIntentDto]
     """


    return sync_detailed(
        client=client,
workspace_id=workspace_id,
reference_types=reference_types,
since=since,
take=take,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    workspace_id: UUID | Unset = UNSET,
    reference_types: str | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    take: int | Unset = 200,

) -> Response[list[CompletedIntentDto]]:
    """ 
    Args:
        workspace_id (UUID | Unset):
        reference_types (str | Unset):
        since (datetime.datetime | Unset):
        take (int | Unset):  Default: 200.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[CompletedIntentDto]]
     """


    kwargs = _get_kwargs(
        workspace_id=workspace_id,
reference_types=reference_types,
since=since,
take=take,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    workspace_id: UUID | Unset = UNSET,
    reference_types: str | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    take: int | Unset = 200,

) -> list[CompletedIntentDto] | None:
    """ 
    Args:
        workspace_id (UUID | Unset):
        reference_types (str | Unset):
        since (datetime.datetime | Unset):
        take (int | Unset):  Default: 200.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[CompletedIntentDto]
     """


    return (await asyncio_detailed(
        client=client,
workspace_id=workspace_id,
reference_types=reference_types,
since=since,
take=take,

    )).parsed

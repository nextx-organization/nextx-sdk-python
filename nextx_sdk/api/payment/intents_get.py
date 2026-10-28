from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.payment_intent_dto import PaymentIntentDto
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,
    *,
    workspace_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_workspace_id: str | Unset = UNSET
    if not isinstance(workspace_id, Unset):
        json_workspace_id = str(workspace_id)
    params["workspaceId"] = json_workspace_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/payment/intents/{id}".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PaymentIntentDto | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = PaymentIntentDto.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PaymentIntentDto | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    workspace_id: UUID | Unset = UNSET,

) -> Response[PaymentIntentDto | ProblemDetails]:
    """ 
    Args:
        id (UUID):
        workspace_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaymentIntentDto | ProblemDetails]
     """


    kwargs = _get_kwargs(
        id=id,
workspace_id=workspace_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    workspace_id: UUID | Unset = UNSET,

) -> PaymentIntentDto | ProblemDetails | None:
    """ 
    Args:
        id (UUID):
        workspace_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaymentIntentDto | ProblemDetails
     """


    return sync_detailed(
        id=id,
client=client,
workspace_id=workspace_id,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    workspace_id: UUID | Unset = UNSET,

) -> Response[PaymentIntentDto | ProblemDetails]:
    """ 
    Args:
        id (UUID):
        workspace_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaymentIntentDto | ProblemDetails]
     """


    kwargs = _get_kwargs(
        id=id,
workspace_id=workspace_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    workspace_id: UUID | Unset = UNSET,

) -> PaymentIntentDto | ProblemDetails | None:
    """ 
    Args:
        id (UUID):
        workspace_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaymentIntentDto | ProblemDetails
     """


    return (await asyncio_detailed(
        id=id,
client=client,
workspace_id=workspace_id,

    )).parsed

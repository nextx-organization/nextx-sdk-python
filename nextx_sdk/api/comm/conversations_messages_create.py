from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.message_dto import MessageDto
from ...models.problem_details import ProblemDetails
from ...models.send_message_request import SendMessageRequest
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,
    *,
    body: SendMessageRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/comm/conversations/{id}/messages".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MessageDto | ProblemDetails | None:
    if response.status_code == 201:
        response_201 = MessageDto.from_dict(response.json())



        return response_201

    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = ProblemDetails.from_dict(response.json())



        return response_409

    if response.status_code == 422:
        response_422 = ProblemDetails.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MessageDto | ProblemDetails]:
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
    body: SendMessageRequest | Unset = UNSET,

) -> Response[MessageDto | ProblemDetails]:
    """ Gửi tin nhắn

     Agent gửi tin nhắn vào hội thoại. Hỗ trợ idempotency qua clientId. Không thể gửi vào hội thoại
    Resolved hoặc BotHandling.

    Args:
        id (UUID):
        body (SendMessageRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageDto | ProblemDetails]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SendMessageRequest | Unset = UNSET,

) -> MessageDto | ProblemDetails | None:
    """ Gửi tin nhắn

     Agent gửi tin nhắn vào hội thoại. Hỗ trợ idempotency qua clientId. Không thể gửi vào hội thoại
    Resolved hoặc BotHandling.

    Args:
        id (UUID):
        body (SendMessageRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageDto | ProblemDetails
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SendMessageRequest | Unset = UNSET,

) -> Response[MessageDto | ProblemDetails]:
    """ Gửi tin nhắn

     Agent gửi tin nhắn vào hội thoại. Hỗ trợ idempotency qua clientId. Không thể gửi vào hội thoại
    Resolved hoặc BotHandling.

    Args:
        id (UUID):
        body (SendMessageRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageDto | ProblemDetails]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SendMessageRequest | Unset = UNSET,

) -> MessageDto | ProblemDetails | None:
    """ Gửi tin nhắn

     Agent gửi tin nhắn vào hội thoại. Hỗ trợ idempotency qua clientId. Không thể gửi vào hội thoại
    Resolved hoặc BotHandling.

    Args:
        id (UUID):
        body (SendMessageRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageDto | ProblemDetails
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed

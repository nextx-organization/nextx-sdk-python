from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.partner_agent_status_dto import PartnerAgentStatusDto
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    agent_id: UUID | Unset = UNSET,
    agent_email: str | Unset = UNSET,
    extension: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_agent_id: str | Unset = UNSET
    if not isinstance(agent_id, Unset):
        json_agent_id = str(agent_id)
    params["agentId"] = json_agent_id

    params["agentEmail"] = agent_email

    params["extension"] = extension


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/call/partner/agents/status",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PartnerAgentStatusDto | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = PartnerAgentStatusDto.from_dict(response.json())



        return response_200

    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PartnerAgentStatusDto | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    agent_id: UUID | Unset = UNSET,
    agent_email: str | Unset = UNSET,
    extension: str | Unset = UNSET,

) -> Response[PartnerAgentStatusDto | ProblemDetails]:
    """ Trạng thái tổng đài viên

     Tìm theo đúng một trong agentId / agentEmail / extension (query).

    Args:
        agent_id (UUID | Unset):
        agent_email (str | Unset):
        extension (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PartnerAgentStatusDto | ProblemDetails]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
agent_email=agent_email,
extension=extension,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    agent_id: UUID | Unset = UNSET,
    agent_email: str | Unset = UNSET,
    extension: str | Unset = UNSET,

) -> PartnerAgentStatusDto | ProblemDetails | None:
    """ Trạng thái tổng đài viên

     Tìm theo đúng một trong agentId / agentEmail / extension (query).

    Args:
        agent_id (UUID | Unset):
        agent_email (str | Unset):
        extension (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PartnerAgentStatusDto | ProblemDetails
     """


    return sync_detailed(
        client=client,
agent_id=agent_id,
agent_email=agent_email,
extension=extension,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    agent_id: UUID | Unset = UNSET,
    agent_email: str | Unset = UNSET,
    extension: str | Unset = UNSET,

) -> Response[PartnerAgentStatusDto | ProblemDetails]:
    """ Trạng thái tổng đài viên

     Tìm theo đúng một trong agentId / agentEmail / extension (query).

    Args:
        agent_id (UUID | Unset):
        agent_email (str | Unset):
        extension (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PartnerAgentStatusDto | ProblemDetails]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
agent_email=agent_email,
extension=extension,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    agent_id: UUID | Unset = UNSET,
    agent_email: str | Unset = UNSET,
    extension: str | Unset = UNSET,

) -> PartnerAgentStatusDto | ProblemDetails | None:
    """ Trạng thái tổng đài viên

     Tìm theo đúng một trong agentId / agentEmail / extension (query).

    Args:
        agent_id (UUID | Unset):
        agent_email (str | Unset):
        extension (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PartnerAgentStatusDto | ProblemDetails
     """


    return (await asyncio_detailed(
        client=client,
agent_id=agent_id,
agent_email=agent_email,
extension=extension,

    )).parsed

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.agent_list_result import AgentListResult
from ...models.agents_list_status import AgentsListStatus
from ...models.agents_list_status import check_agents_list_status
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    status: AgentsListStatus | Unset = UNSET,
    queue_id: UUID | Unset = UNSET,
    is_active: bool | Unset = UNSET,
    search: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["pageNumber"] = page_number

    params["pageSize"] = page_size

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    json_queue_id: str | Unset = UNSET
    if not isinstance(queue_id, Unset):
        json_queue_id = str(queue_id)
    params["queueId"] = json_queue_id

    params["isActive"] = is_active

    params["search"] = search


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/call/agents",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AgentListResult | None:
    if response.status_code == 200:
        response_200 = AgentListResult.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AgentListResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    status: AgentsListStatus | Unset = UNSET,
    queue_id: UUID | Unset = UNSET,
    is_active: bool | Unset = UNSET,
    search: str | Unset = UNSET,

) -> Response[AgentListResult]:
    """ Danh sách agents

     Danh sách có phân trang, kèm trạng thái trực tuyến hiện tại của từng agent. sip_password không trả
    về.

    Args:
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        status (AgentsListStatus | Unset):
        queue_id (UUID | Unset):
        is_active (bool | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentListResult]
     """


    kwargs = _get_kwargs(
        page_number=page_number,
page_size=page_size,
status=status,
queue_id=queue_id,
is_active=is_active,
search=search,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    status: AgentsListStatus | Unset = UNSET,
    queue_id: UUID | Unset = UNSET,
    is_active: bool | Unset = UNSET,
    search: str | Unset = UNSET,

) -> AgentListResult | None:
    """ Danh sách agents

     Danh sách có phân trang, kèm trạng thái trực tuyến hiện tại của từng agent. sip_password không trả
    về.

    Args:
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        status (AgentsListStatus | Unset):
        queue_id (UUID | Unset):
        is_active (bool | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentListResult
     """


    return sync_detailed(
        client=client,
page_number=page_number,
page_size=page_size,
status=status,
queue_id=queue_id,
is_active=is_active,
search=search,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    status: AgentsListStatus | Unset = UNSET,
    queue_id: UUID | Unset = UNSET,
    is_active: bool | Unset = UNSET,
    search: str | Unset = UNSET,

) -> Response[AgentListResult]:
    """ Danh sách agents

     Danh sách có phân trang, kèm trạng thái trực tuyến hiện tại của từng agent. sip_password không trả
    về.

    Args:
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        status (AgentsListStatus | Unset):
        queue_id (UUID | Unset):
        is_active (bool | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentListResult]
     """


    kwargs = _get_kwargs(
        page_number=page_number,
page_size=page_size,
status=status,
queue_id=queue_id,
is_active=is_active,
search=search,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    status: AgentsListStatus | Unset = UNSET,
    queue_id: UUID | Unset = UNSET,
    is_active: bool | Unset = UNSET,
    search: str | Unset = UNSET,

) -> AgentListResult | None:
    """ Danh sách agents

     Danh sách có phân trang, kèm trạng thái trực tuyến hiện tại của từng agent. sip_password không trả
    về.

    Args:
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        status (AgentsListStatus | Unset):
        queue_id (UUID | Unset):
        is_active (bool | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentListResult
     """


    return (await asyncio_detailed(
        client=client,
page_number=page_number,
page_size=page_size,
status=status,
queue_id=queue_id,
is_active=is_active,
search=search,

    )).parsed

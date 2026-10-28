from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.contact_list_stats_dto import ContactListStatsDto
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/crm/contacts/stats",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ContactListStatsDto | None:
    if response.status_code == 200:
        response_200 = ContactListStatsDto.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ContactListStatsDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[ContactListStatsDto]:
    """ Thống kê KPI contacts

     Trả về tổng số contacts, số contacts có customer profile, phân bố theo tier (Standard/Premium/Vip)
    và theo lifecycle stage. Tôn trọng data scope giống GET /contacts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactListStatsDto]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,

) -> ContactListStatsDto | None:
    """ Thống kê KPI contacts

     Trả về tổng số contacts, số contacts có customer profile, phân bố theo tier (Standard/Premium/Vip)
    và theo lifecycle stage. Tôn trọng data scope giống GET /contacts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactListStatsDto
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[ContactListStatsDto]:
    """ Thống kê KPI contacts

     Trả về tổng số contacts, số contacts có customer profile, phân bố theo tier (Standard/Premium/Vip)
    và theo lifecycle stage. Tôn trọng data scope giống GET /contacts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactListStatsDto]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,

) -> ContactListStatsDto | None:
    """ Thống kê KPI contacts

     Trả về tổng số contacts, số contacts có customer profile, phân bố theo tier (Standard/Premium/Vip)
    và theo lifecycle stage. Tôn trọng data scope giống GET /contacts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactListStatsDto
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed

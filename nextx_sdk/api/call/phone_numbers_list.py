from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.phone_number_list_result import PhoneNumberListResult
from ...models.phone_numbers_list_direction import check_phone_numbers_list_direction
from ...models.phone_numbers_list_direction import PhoneNumbersListDirection
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    sip_trunk_id: UUID | Unset = UNSET,
    trunk_id: UUID | Unset = UNSET,
    direction: PhoneNumbersListDirection | Unset = UNSET,
    is_active: bool | Unset = UNSET,
    search: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["pageNumber"] = page_number

    params["pageSize"] = page_size

    json_sip_trunk_id: str | Unset = UNSET
    if not isinstance(sip_trunk_id, Unset):
        json_sip_trunk_id = str(sip_trunk_id)
    params["sipTrunkId"] = json_sip_trunk_id

    json_trunk_id: str | Unset = UNSET
    if not isinstance(trunk_id, Unset):
        json_trunk_id = str(trunk_id)
    params["trunkId"] = json_trunk_id

    json_direction: str | Unset = UNSET
    if not isinstance(direction, Unset):
        json_direction = direction

    params["direction"] = json_direction

    params["isActive"] = is_active

    params["search"] = search


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/call/phone-numbers",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PhoneNumberListResult | None:
    if response.status_code == 200:
        response_200 = PhoneNumberListResult.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PhoneNumberListResult]:
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
    sip_trunk_id: UUID | Unset = UNSET,
    trunk_id: UUID | Unset = UNSET,
    direction: PhoneNumbersListDirection | Unset = UNSET,
    is_active: bool | Unset = UNSET,
    search: str | Unset = UNSET,

) -> Response[PhoneNumberListResult]:
    """ 
    Args:
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        sip_trunk_id (UUID | Unset):
        trunk_id (UUID | Unset):
        direction (PhoneNumbersListDirection | Unset):
        is_active (bool | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PhoneNumberListResult]
     """


    kwargs = _get_kwargs(
        page_number=page_number,
page_size=page_size,
sip_trunk_id=sip_trunk_id,
trunk_id=trunk_id,
direction=direction,
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
    sip_trunk_id: UUID | Unset = UNSET,
    trunk_id: UUID | Unset = UNSET,
    direction: PhoneNumbersListDirection | Unset = UNSET,
    is_active: bool | Unset = UNSET,
    search: str | Unset = UNSET,

) -> PhoneNumberListResult | None:
    """ 
    Args:
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        sip_trunk_id (UUID | Unset):
        trunk_id (UUID | Unset):
        direction (PhoneNumbersListDirection | Unset):
        is_active (bool | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PhoneNumberListResult
     """


    return sync_detailed(
        client=client,
page_number=page_number,
page_size=page_size,
sip_trunk_id=sip_trunk_id,
trunk_id=trunk_id,
direction=direction,
is_active=is_active,
search=search,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    sip_trunk_id: UUID | Unset = UNSET,
    trunk_id: UUID | Unset = UNSET,
    direction: PhoneNumbersListDirection | Unset = UNSET,
    is_active: bool | Unset = UNSET,
    search: str | Unset = UNSET,

) -> Response[PhoneNumberListResult]:
    """ 
    Args:
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        sip_trunk_id (UUID | Unset):
        trunk_id (UUID | Unset):
        direction (PhoneNumbersListDirection | Unset):
        is_active (bool | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PhoneNumberListResult]
     """


    kwargs = _get_kwargs(
        page_number=page_number,
page_size=page_size,
sip_trunk_id=sip_trunk_id,
trunk_id=trunk_id,
direction=direction,
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
    sip_trunk_id: UUID | Unset = UNSET,
    trunk_id: UUID | Unset = UNSET,
    direction: PhoneNumbersListDirection | Unset = UNSET,
    is_active: bool | Unset = UNSET,
    search: str | Unset = UNSET,

) -> PhoneNumberListResult | None:
    """ 
    Args:
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        sip_trunk_id (UUID | Unset):
        trunk_id (UUID | Unset):
        direction (PhoneNumbersListDirection | Unset):
        is_active (bool | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PhoneNumberListResult
     """


    return (await asyncio_detailed(
        client=client,
page_number=page_number,
page_size=page_size,
sip_trunk_id=sip_trunk_id,
trunk_id=trunk_id,
direction=direction,
is_active=is_active,
search=search,

    )).parsed

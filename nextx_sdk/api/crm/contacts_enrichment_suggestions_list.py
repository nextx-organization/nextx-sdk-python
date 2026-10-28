from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.enrichment_suggestion_dto import EnrichmentSuggestionDto
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    contact_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_contact_id: str | Unset = UNSET
    if not isinstance(contact_id, Unset):
        json_contact_id = str(contact_id)
    params["contactId"] = json_contact_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/crm/contacts/enrichment-suggestions",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[EnrichmentSuggestionDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = EnrichmentSuggestionDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[EnrichmentSuggestionDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    contact_id: UUID | Unset = UNSET,

) -> Response[list[EnrichmentSuggestionDto]]:
    """ Danh sách gợi ý làm giàu đang chờ duyệt

     Địa chỉ/ý định LLM trích từ chat của khách. Truyền contactId để lọc theo 1 khách. Đây CHỈ là gợi ý —
    chưa áp vào contact cho tới khi duyệt (Accept).

    Args:
        contact_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[EnrichmentSuggestionDto]]
     """


    kwargs = _get_kwargs(
        contact_id=contact_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    contact_id: UUID | Unset = UNSET,

) -> list[EnrichmentSuggestionDto] | None:
    """ Danh sách gợi ý làm giàu đang chờ duyệt

     Địa chỉ/ý định LLM trích từ chat của khách. Truyền contactId để lọc theo 1 khách. Đây CHỈ là gợi ý —
    chưa áp vào contact cho tới khi duyệt (Accept).

    Args:
        contact_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[EnrichmentSuggestionDto]
     """


    return sync_detailed(
        client=client,
contact_id=contact_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    contact_id: UUID | Unset = UNSET,

) -> Response[list[EnrichmentSuggestionDto]]:
    """ Danh sách gợi ý làm giàu đang chờ duyệt

     Địa chỉ/ý định LLM trích từ chat của khách. Truyền contactId để lọc theo 1 khách. Đây CHỈ là gợi ý —
    chưa áp vào contact cho tới khi duyệt (Accept).

    Args:
        contact_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[EnrichmentSuggestionDto]]
     """


    kwargs = _get_kwargs(
        contact_id=contact_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    contact_id: UUID | Unset = UNSET,

) -> list[EnrichmentSuggestionDto] | None:
    """ Danh sách gợi ý làm giàu đang chờ duyệt

     Địa chỉ/ý định LLM trích từ chat của khách. Truyền contactId để lọc theo 1 khách. Đây CHỈ là gợi ý —
    chưa áp vào contact cho tới khi duyệt (Accept).

    Args:
        contact_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[EnrichmentSuggestionDto]
     """


    return (await asyncio_detailed(
        client=client,
contact_id=contact_id,

    )).parsed

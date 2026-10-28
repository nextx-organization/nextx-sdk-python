from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.series_dto import SeriesDto
from ...models.series_list_provider_code import check_series_list_provider_code
from ...models.series_list_provider_code import SeriesListProviderCode
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    provider_code: SeriesListProviderCode | Unset = UNSET,
    provider_config_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_provider_code: str | Unset = UNSET
    if not isinstance(provider_code, Unset):
        json_provider_code = provider_code

    params["providerCode"] = json_provider_code

    json_provider_config_id: str | Unset = UNSET
    if not isinstance(provider_config_id, Unset):
        json_provider_config_id = str(provider_config_id)
    params["providerConfigId"] = json_provider_config_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/einvoice/series",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[SeriesDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = SeriesDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[SeriesDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    provider_code: SeriesListProviderCode | Unset = UNSET,
    provider_config_id: UUID | Unset = UNSET,

) -> Response[list[SeriesDto]]:
    """ Lấy danh sách ký hiệu hóa đơn

     Lọc theo tài khoản HĐĐT (providerConfigId) và/hoặc provider — cả hai tùy chọn. Trả về cả active và
    inactive.

    Args:
        provider_code (SeriesListProviderCode | Unset):
        provider_config_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[SeriesDto]]
     """


    kwargs = _get_kwargs(
        provider_code=provider_code,
provider_config_id=provider_config_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    provider_code: SeriesListProviderCode | Unset = UNSET,
    provider_config_id: UUID | Unset = UNSET,

) -> list[SeriesDto] | None:
    """ Lấy danh sách ký hiệu hóa đơn

     Lọc theo tài khoản HĐĐT (providerConfigId) và/hoặc provider — cả hai tùy chọn. Trả về cả active và
    inactive.

    Args:
        provider_code (SeriesListProviderCode | Unset):
        provider_config_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[SeriesDto]
     """


    return sync_detailed(
        client=client,
provider_code=provider_code,
provider_config_id=provider_config_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    provider_code: SeriesListProviderCode | Unset = UNSET,
    provider_config_id: UUID | Unset = UNSET,

) -> Response[list[SeriesDto]]:
    """ Lấy danh sách ký hiệu hóa đơn

     Lọc theo tài khoản HĐĐT (providerConfigId) và/hoặc provider — cả hai tùy chọn. Trả về cả active và
    inactive.

    Args:
        provider_code (SeriesListProviderCode | Unset):
        provider_config_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[SeriesDto]]
     """


    kwargs = _get_kwargs(
        provider_code=provider_code,
provider_config_id=provider_config_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    provider_code: SeriesListProviderCode | Unset = UNSET,
    provider_config_id: UUID | Unset = UNSET,

) -> list[SeriesDto] | None:
    """ Lấy danh sách ký hiệu hóa đơn

     Lọc theo tài khoản HĐĐT (providerConfigId) và/hoặc provider — cả hai tùy chọn. Trả về cả active và
    inactive.

    Args:
        provider_code (SeriesListProviderCode | Unset):
        provider_config_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[SeriesDto]
     """


    return (await asyncio_detailed(
        client=client,
provider_code=provider_code,
provider_config_id=provider_config_id,

    )).parsed

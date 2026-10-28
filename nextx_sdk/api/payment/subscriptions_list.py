from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paged_subscriptions_result import PagedSubscriptionsResult
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    status: str | Unset = UNSET,
    reference_type: str | Unset = UNSET,
    provider_code: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["status"] = status

    params["referenceType"] = reference_type

    params["providerCode"] = provider_code

    params["pageNumber"] = page_number

    params["pageSize"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/payment/subscriptions",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PagedSubscriptionsResult | None:
    if response.status_code == 200:
        response_200 = PagedSubscriptionsResult.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PagedSubscriptionsResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    reference_type: str | Unset = UNSET,
    provider_code: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,

) -> Response[PagedSubscriptionsResult]:
    """ 
    Args:
        status (str | Unset):
        reference_type (str | Unset):
        provider_code (str | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedSubscriptionsResult]
     """


    kwargs = _get_kwargs(
        status=status,
reference_type=reference_type,
provider_code=provider_code,
page_number=page_number,
page_size=page_size,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    reference_type: str | Unset = UNSET,
    provider_code: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,

) -> PagedSubscriptionsResult | None:
    """ 
    Args:
        status (str | Unset):
        reference_type (str | Unset):
        provider_code (str | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedSubscriptionsResult
     """


    return sync_detailed(
        client=client,
status=status,
reference_type=reference_type,
provider_code=provider_code,
page_number=page_number,
page_size=page_size,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    reference_type: str | Unset = UNSET,
    provider_code: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,

) -> Response[PagedSubscriptionsResult]:
    """ 
    Args:
        status (str | Unset):
        reference_type (str | Unset):
        provider_code (str | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedSubscriptionsResult]
     """


    kwargs = _get_kwargs(
        status=status,
reference_type=reference_type,
provider_code=provider_code,
page_number=page_number,
page_size=page_size,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    reference_type: str | Unset = UNSET,
    provider_code: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,

) -> PagedSubscriptionsResult | None:
    """ 
    Args:
        status (str | Unset):
        reference_type (str | Unset):
        provider_code (str | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedSubscriptionsResult
     """


    return (await asyncio_detailed(
        client=client,
status=status,
reference_type=reference_type,
provider_code=provider_code,
page_number=page_number,
page_size=page_size,

    )).parsed

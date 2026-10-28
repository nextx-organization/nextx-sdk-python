from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_payment_transactions_result import GetPaymentTransactionsResult
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    *,
    provider_code: str | Unset = UNSET,
    reference_type: str | Unset = UNSET,
    reference_id: UUID | Unset = UNSET,
    payer_id: UUID | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    search: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["providerCode"] = provider_code

    params["referenceType"] = reference_type

    json_reference_id: str | Unset = UNSET
    if not isinstance(reference_id, Unset):
        json_reference_id = str(reference_id)
    params["referenceId"] = json_reference_id

    json_payer_id: str | Unset = UNSET
    if not isinstance(payer_id, Unset):
        json_payer_id = str(payer_id)
    params["payerId"] = json_payer_id

    json_from_date: str | Unset = UNSET
    if not isinstance(from_date, Unset):
        json_from_date = from_date.isoformat()
    params["fromDate"] = json_from_date

    json_to_date: str | Unset = UNSET
    if not isinstance(to_date, Unset):
        json_to_date = to_date.isoformat()
    params["toDate"] = json_to_date

    params["search"] = search

    params["pageNumber"] = page_number

    params["pageSize"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/payment/transactions",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetPaymentTransactionsResult | None:
    if response.status_code == 200:
        response_200 = GetPaymentTransactionsResult.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetPaymentTransactionsResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    provider_code: str | Unset = UNSET,
    reference_type: str | Unset = UNSET,
    reference_id: UUID | Unset = UNSET,
    payer_id: UUID | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    search: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,

) -> Response[GetPaymentTransactionsResult]:
    """ 
    Args:
        provider_code (str | Unset):
        reference_type (str | Unset):
        reference_id (UUID | Unset):
        payer_id (UUID | Unset):
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):
        search (str | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPaymentTransactionsResult]
     """


    kwargs = _get_kwargs(
        provider_code=provider_code,
reference_type=reference_type,
reference_id=reference_id,
payer_id=payer_id,
from_date=from_date,
to_date=to_date,
search=search,
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
    provider_code: str | Unset = UNSET,
    reference_type: str | Unset = UNSET,
    reference_id: UUID | Unset = UNSET,
    payer_id: UUID | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    search: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,

) -> GetPaymentTransactionsResult | None:
    """ 
    Args:
        provider_code (str | Unset):
        reference_type (str | Unset):
        reference_id (UUID | Unset):
        payer_id (UUID | Unset):
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):
        search (str | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPaymentTransactionsResult
     """


    return sync_detailed(
        client=client,
provider_code=provider_code,
reference_type=reference_type,
reference_id=reference_id,
payer_id=payer_id,
from_date=from_date,
to_date=to_date,
search=search,
page_number=page_number,
page_size=page_size,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    provider_code: str | Unset = UNSET,
    reference_type: str | Unset = UNSET,
    reference_id: UUID | Unset = UNSET,
    payer_id: UUID | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    search: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,

) -> Response[GetPaymentTransactionsResult]:
    """ 
    Args:
        provider_code (str | Unset):
        reference_type (str | Unset):
        reference_id (UUID | Unset):
        payer_id (UUID | Unset):
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):
        search (str | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPaymentTransactionsResult]
     """


    kwargs = _get_kwargs(
        provider_code=provider_code,
reference_type=reference_type,
reference_id=reference_id,
payer_id=payer_id,
from_date=from_date,
to_date=to_date,
search=search,
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
    provider_code: str | Unset = UNSET,
    reference_type: str | Unset = UNSET,
    reference_id: UUID | Unset = UNSET,
    payer_id: UUID | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    search: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,

) -> GetPaymentTransactionsResult | None:
    """ 
    Args:
        provider_code (str | Unset):
        reference_type (str | Unset):
        reference_id (UUID | Unset):
        payer_id (UUID | Unset):
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):
        search (str | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPaymentTransactionsResult
     """


    return (await asyncio_detailed(
        client=client,
provider_code=provider_code,
reference_type=reference_type,
reference_id=reference_id,
payer_id=payer_id,
from_date=from_date,
to_date=to_date,
search=search,
page_number=page_number,
page_size=page_size,

    )).parsed

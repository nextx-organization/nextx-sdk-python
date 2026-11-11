from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.open_api_order_status_dto import OpenApiOrderStatusDto
from ...models.problem_details import ProblemDetails
from typing import cast



def _get_kwargs(
    external_order_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sales/open/orders/{external_order_id}".format(external_order_id=quote(str(external_order_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OpenApiOrderStatusDto | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = OpenApiOrderStatusDto.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OpenApiOrderStatusDto | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    external_order_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[OpenApiOrderStatusDto | ProblemDetails]:
    """ Tra trạng thái đơn theo mã đơn ngoài

     Trả trạng thái đơn, thanh toán (UNPAID/PARTIAL/PAID, đã trả, còn nợ) và vận chuyển (hãng, mã vận
    đơn, trạng thái).

    Args:
        external_order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpenApiOrderStatusDto | ProblemDetails]
     """


    kwargs = _get_kwargs(
        external_order_id=external_order_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    external_order_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> OpenApiOrderStatusDto | ProblemDetails | None:
    """ Tra trạng thái đơn theo mã đơn ngoài

     Trả trạng thái đơn, thanh toán (UNPAID/PARTIAL/PAID, đã trả, còn nợ) và vận chuyển (hãng, mã vận
    đơn, trạng thái).

    Args:
        external_order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpenApiOrderStatusDto | ProblemDetails
     """


    return sync_detailed(
        external_order_id=external_order_id,
client=client,

    ).parsed

async def asyncio_detailed(
    external_order_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[OpenApiOrderStatusDto | ProblemDetails]:
    """ Tra trạng thái đơn theo mã đơn ngoài

     Trả trạng thái đơn, thanh toán (UNPAID/PARTIAL/PAID, đã trả, còn nợ) và vận chuyển (hãng, mã vận
    đơn, trạng thái).

    Args:
        external_order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpenApiOrderStatusDto | ProblemDetails]
     """


    kwargs = _get_kwargs(
        external_order_id=external_order_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    external_order_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> OpenApiOrderStatusDto | ProblemDetails | None:
    """ Tra trạng thái đơn theo mã đơn ngoài

     Trả trạng thái đơn, thanh toán (UNPAID/PARTIAL/PAID, đã trả, còn nợ) và vận chuyển (hãng, mã vận
    đơn, trạng thái).

    Args:
        external_order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpenApiOrderStatusDto | ProblemDetails
     """


    return (await asyncio_detailed(
        external_order_id=external_order_id,
client=client,

    )).parsed

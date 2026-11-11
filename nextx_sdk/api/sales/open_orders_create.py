from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_open_api_order_request import CreateOpenApiOrderRequest
from ...models.open_api_order_status_dto import OpenApiOrderStatusDto
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: CreateOpenApiOrderRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/sales/open/orders",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OpenApiOrderStatusDto | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = OpenApiOrderStatusDto.from_dict(response.json())



        return response_200

    if response.status_code == 201:
        response_201 = OpenApiOrderStatusDto.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OpenApiOrderStatusDto | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateOpenApiOrderRequest | Unset = UNSET,

) -> Response[OpenApiOrderStatusDto | ProblemDetails]:
    """ Đẩy đơn từ hệ thống ngoài

     Idempotent theo externalOrderId: gửi lại trả đơn cũ (200, idempotentReplay=true). Khách tìm theo
    SĐT; chưa có thì tự tạo nếu nhà bật cài đặt. Sản phẩm theo productId hoặc sku.

    Args:
        body (CreateOpenApiOrderRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpenApiOrderStatusDto | ProblemDetails]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateOpenApiOrderRequest | Unset = UNSET,

) -> OpenApiOrderStatusDto | ProblemDetails | None:
    """ Đẩy đơn từ hệ thống ngoài

     Idempotent theo externalOrderId: gửi lại trả đơn cũ (200, idempotentReplay=true). Khách tìm theo
    SĐT; chưa có thì tự tạo nếu nhà bật cài đặt. Sản phẩm theo productId hoặc sku.

    Args:
        body (CreateOpenApiOrderRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpenApiOrderStatusDto | ProblemDetails
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateOpenApiOrderRequest | Unset = UNSET,

) -> Response[OpenApiOrderStatusDto | ProblemDetails]:
    """ Đẩy đơn từ hệ thống ngoài

     Idempotent theo externalOrderId: gửi lại trả đơn cũ (200, idempotentReplay=true). Khách tìm theo
    SĐT; chưa có thì tự tạo nếu nhà bật cài đặt. Sản phẩm theo productId hoặc sku.

    Args:
        body (CreateOpenApiOrderRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpenApiOrderStatusDto | ProblemDetails]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateOpenApiOrderRequest | Unset = UNSET,

) -> OpenApiOrderStatusDto | ProblemDetails | None:
    """ Đẩy đơn từ hệ thống ngoài

     Idempotent theo externalOrderId: gửi lại trả đơn cũ (200, idempotentReplay=true). Khách tìm theo
    SĐT; chưa có thì tự tạo nếu nhà bật cài đặt. Sản phẩm theo productId hoặc sku.

    Args:
        body (CreateOpenApiOrderRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpenApiOrderStatusDto | ProblemDetails
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed

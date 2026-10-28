from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.barcode_product_dto import BarcodeProductDto
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    code: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["code"] = code

    json_branch_id: str | Unset = UNSET
    if not isinstance(branch_id, Unset):
        json_branch_id = str(branch_id)
    params["branchId"] = json_branch_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sales/products/barcode-lookup",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[BarcodeProductDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = BarcodeProductDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[BarcodeProductDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    code: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,

) -> Response[list[BarcodeProductDto]]:
    """ Tra cứu sản phẩm theo mã vạch

     Tìm sản phẩm theo mã sản phẩm hoặc mã SKU. Dùng cho chức năng quét mã vạch khi tạo đơn hàng.

    Args:
        code (str | Unset):
        branch_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BarcodeProductDto]]
     """


    kwargs = _get_kwargs(
        code=code,
branch_id=branch_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    code: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,

) -> list[BarcodeProductDto] | None:
    """ Tra cứu sản phẩm theo mã vạch

     Tìm sản phẩm theo mã sản phẩm hoặc mã SKU. Dùng cho chức năng quét mã vạch khi tạo đơn hàng.

    Args:
        code (str | Unset):
        branch_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BarcodeProductDto]
     """


    return sync_detailed(
        client=client,
code=code,
branch_id=branch_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    code: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,

) -> Response[list[BarcodeProductDto]]:
    """ Tra cứu sản phẩm theo mã vạch

     Tìm sản phẩm theo mã sản phẩm hoặc mã SKU. Dùng cho chức năng quét mã vạch khi tạo đơn hàng.

    Args:
        code (str | Unset):
        branch_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BarcodeProductDto]]
     """


    kwargs = _get_kwargs(
        code=code,
branch_id=branch_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    code: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,

) -> list[BarcodeProductDto] | None:
    """ Tra cứu sản phẩm theo mã vạch

     Tìm sản phẩm theo mã sản phẩm hoặc mã SKU. Dùng cho chức năng quét mã vạch khi tạo đơn hàng.

    Args:
        code (str | Unset):
        branch_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BarcodeProductDto]
     """


    return (await asyncio_detailed(
        client=client,
code=code,
branch_id=branch_id,

    )).parsed

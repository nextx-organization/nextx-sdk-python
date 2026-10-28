from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.kit_availability_dto import KitAvailabilityDto
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    kit_sku_ids: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["kitSkuIds"] = kit_sku_ids

    json_branch_id: str | Unset = UNSET
    if not isinstance(branch_id, Unset):
        json_branch_id = str(branch_id)
    params["branchId"] = json_branch_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sales/products/kit-availability",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[KitAvailabilityDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = KitAvailabilityDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[KitAvailabilityDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    kit_sku_ids: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,

) -> Response[list[KitAvailabilityDto]]:
    """ Tồn bán được của combo (số bộ ghép được)

     kitSkuIds: danh sách product_skus.id của combo (phân tách dấu phẩy, tối đa 200). Số bộ = MIN(tồn khả
    dụng ÷ SL mỗi bộ) trên các thành phần có tồn; null = không giới hạn (toàn dịch vụ). branchId bỏ
    trống = mọi chi nhánh.

    Args:
        kit_sku_ids (str | Unset):
        branch_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[KitAvailabilityDto]]
     """


    kwargs = _get_kwargs(
        kit_sku_ids=kit_sku_ids,
branch_id=branch_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    kit_sku_ids: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,

) -> list[KitAvailabilityDto] | None:
    """ Tồn bán được của combo (số bộ ghép được)

     kitSkuIds: danh sách product_skus.id của combo (phân tách dấu phẩy, tối đa 200). Số bộ = MIN(tồn khả
    dụng ÷ SL mỗi bộ) trên các thành phần có tồn; null = không giới hạn (toàn dịch vụ). branchId bỏ
    trống = mọi chi nhánh.

    Args:
        kit_sku_ids (str | Unset):
        branch_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[KitAvailabilityDto]
     """


    return sync_detailed(
        client=client,
kit_sku_ids=kit_sku_ids,
branch_id=branch_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    kit_sku_ids: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,

) -> Response[list[KitAvailabilityDto]]:
    """ Tồn bán được của combo (số bộ ghép được)

     kitSkuIds: danh sách product_skus.id của combo (phân tách dấu phẩy, tối đa 200). Số bộ = MIN(tồn khả
    dụng ÷ SL mỗi bộ) trên các thành phần có tồn; null = không giới hạn (toàn dịch vụ). branchId bỏ
    trống = mọi chi nhánh.

    Args:
        kit_sku_ids (str | Unset):
        branch_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[KitAvailabilityDto]]
     """


    kwargs = _get_kwargs(
        kit_sku_ids=kit_sku_ids,
branch_id=branch_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    kit_sku_ids: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,

) -> list[KitAvailabilityDto] | None:
    """ Tồn bán được của combo (số bộ ghép được)

     kitSkuIds: danh sách product_skus.id của combo (phân tách dấu phẩy, tối đa 200). Số bộ = MIN(tồn khả
    dụng ÷ SL mỗi bộ) trên các thành phần có tồn; null = không giới hạn (toàn dịch vụ). branchId bỏ
    trống = mọi chi nhánh.

    Args:
        kit_sku_ids (str | Unset):
        branch_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[KitAvailabilityDto]
     """


    return (await asyncio_detailed(
        client=client,
kit_sku_ids=kit_sku_ids,
branch_id=branch_id,

    )).parsed

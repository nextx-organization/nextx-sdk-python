from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.stock_forecast_dto import StockForecastDto
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    days_threshold: int | Unset = 30,
    branch_id: UUID | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 50,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["daysThreshold"] = days_threshold

    json_branch_id: str | Unset = UNSET
    if not isinstance(branch_id, Unset):
        json_branch_id = str(branch_id)
    params["branchId"] = json_branch_id

    params["pageNumber"] = page_number

    params["pageSize"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sales/products/stock-forecast",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[StockForecastDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = StockForecastDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[StockForecastDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    days_threshold: int | Unset = 30,
    branch_id: UUID | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 50,

) -> Response[list[StockForecastDto]]:
    """ Dự báo hết hàng

     Tính tốc độ bán trung bình 30 ngày và dự báo số ngày hết hàng. Chỉ trả sản phẩm sắp hết trong
    DaysThreshold ngày.

    Args:
        days_threshold (int | Unset):  Default: 30.
        branch_id (UUID | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[StockForecastDto]]
     """


    kwargs = _get_kwargs(
        days_threshold=days_threshold,
branch_id=branch_id,
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
    days_threshold: int | Unset = 30,
    branch_id: UUID | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 50,

) -> list[StockForecastDto] | None:
    """ Dự báo hết hàng

     Tính tốc độ bán trung bình 30 ngày và dự báo số ngày hết hàng. Chỉ trả sản phẩm sắp hết trong
    DaysThreshold ngày.

    Args:
        days_threshold (int | Unset):  Default: 30.
        branch_id (UUID | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[StockForecastDto]
     """


    return sync_detailed(
        client=client,
days_threshold=days_threshold,
branch_id=branch_id,
page_number=page_number,
page_size=page_size,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    days_threshold: int | Unset = 30,
    branch_id: UUID | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 50,

) -> Response[list[StockForecastDto]]:
    """ Dự báo hết hàng

     Tính tốc độ bán trung bình 30 ngày và dự báo số ngày hết hàng. Chỉ trả sản phẩm sắp hết trong
    DaysThreshold ngày.

    Args:
        days_threshold (int | Unset):  Default: 30.
        branch_id (UUID | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[StockForecastDto]]
     """


    kwargs = _get_kwargs(
        days_threshold=days_threshold,
branch_id=branch_id,
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
    days_threshold: int | Unset = 30,
    branch_id: UUID | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 50,

) -> list[StockForecastDto] | None:
    """ Dự báo hết hàng

     Tính tốc độ bán trung bình 30 ngày và dự báo số ngày hết hàng. Chỉ trả sản phẩm sắp hết trong
    DaysThreshold ngày.

    Args:
        days_threshold (int | Unset):  Default: 30.
        branch_id (UUID | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[StockForecastDto]
     """


    return (await asyncio_detailed(
        client=client,
days_threshold=days_threshold,
branch_id=branch_id,
page_number=page_number,
page_size=page_size,

    )).parsed

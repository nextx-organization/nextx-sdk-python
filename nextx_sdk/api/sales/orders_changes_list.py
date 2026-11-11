from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.order_changes_result import OrderChangesResult
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Unset
from typing import cast
import datetime



def _get_kwargs(
    *,
    cursor: str | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 500,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    json_updated_since: str | Unset = UNSET
    if not isinstance(updated_since, Unset):
        json_updated_since = updated_since.isoformat()
    params["updatedSince"] = json_updated_since

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sales/orders/changes",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OrderChangesResult | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = OrderChangesResult.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ProblemDetails.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OrderChangesResult | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 500,

) -> Response[OrderChangesResult | ProblemDetails]:
    """ Thay đổi đơn hàng để tải tăng dần

     Phân trang bằng cursor, không đếm và không tính tổng. Có đơn đã xoá (isDeleted). Lần đầu truyền
    updatedSince, các lần sau truyền nextCursor. limit tối đa 1000.

    Args:
        cursor (str | Unset):
        updated_since (datetime.datetime | Unset):
        limit (int | Unset):  Default: 500.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrderChangesResult | ProblemDetails]
     """


    kwargs = _get_kwargs(
        cursor=cursor,
updated_since=updated_since,
limit=limit,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 500,

) -> OrderChangesResult | ProblemDetails | None:
    """ Thay đổi đơn hàng để tải tăng dần

     Phân trang bằng cursor, không đếm và không tính tổng. Có đơn đã xoá (isDeleted). Lần đầu truyền
    updatedSince, các lần sau truyền nextCursor. limit tối đa 1000.

    Args:
        cursor (str | Unset):
        updated_since (datetime.datetime | Unset):
        limit (int | Unset):  Default: 500.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrderChangesResult | ProblemDetails
     """


    return sync_detailed(
        client=client,
cursor=cursor,
updated_since=updated_since,
limit=limit,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 500,

) -> Response[OrderChangesResult | ProblemDetails]:
    """ Thay đổi đơn hàng để tải tăng dần

     Phân trang bằng cursor, không đếm và không tính tổng. Có đơn đã xoá (isDeleted). Lần đầu truyền
    updatedSince, các lần sau truyền nextCursor. limit tối đa 1000.

    Args:
        cursor (str | Unset):
        updated_since (datetime.datetime | Unset):
        limit (int | Unset):  Default: 500.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrderChangesResult | ProblemDetails]
     """


    kwargs = _get_kwargs(
        cursor=cursor,
updated_since=updated_since,
limit=limit,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 500,

) -> OrderChangesResult | ProblemDetails | None:
    """ Thay đổi đơn hàng để tải tăng dần

     Phân trang bằng cursor, không đếm và không tính tổng. Có đơn đã xoá (isDeleted). Lần đầu truyền
    updatedSince, các lần sau truyền nextCursor. limit tối đa 1000.

    Args:
        cursor (str | Unset):
        updated_since (datetime.datetime | Unset):
        limit (int | Unset):  Default: 500.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrderChangesResult | ProblemDetails
     """


    return (await asyncio_detailed(
        client=client,
cursor=cursor,
updated_since=updated_since,
limit=limit,

    )).parsed

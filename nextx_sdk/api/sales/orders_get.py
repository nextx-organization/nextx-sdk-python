from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.order_detail_dto import OrderDetailDto
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,
    *,
    exclude_return_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_exclude_return_id: str | Unset = UNSET
    if not isinstance(exclude_return_id, Unset):
        json_exclude_return_id = str(exclude_return_id)
    params["excludeReturnId"] = json_exclude_return_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sales/orders/{id}".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OrderDetailDto | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = OrderDetailDto.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OrderDetailDto | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    exclude_return_id: UUID | Unset = UNSET,

) -> Response[OrderDetailDto | ProblemDetails]:
    """ Chi tiết đơn hàng

     `excludeReturnId`: bỏ qua phiếu hoàn đó khi tính `openReturnQuantity` từng dòng. Dành cho màn SỬA
    phiếu hoàn — không truyền thì chính phiếu đang sửa tự giữ chỗ số lượng của nó, mọi dòng ra 0 còn-
    trả-được và form sửa hiện trắng.

    Args:
        id (UUID):
        exclude_return_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrderDetailDto | ProblemDetails]
     """


    kwargs = _get_kwargs(
        id=id,
exclude_return_id=exclude_return_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    exclude_return_id: UUID | Unset = UNSET,

) -> OrderDetailDto | ProblemDetails | None:
    """ Chi tiết đơn hàng

     `excludeReturnId`: bỏ qua phiếu hoàn đó khi tính `openReturnQuantity` từng dòng. Dành cho màn SỬA
    phiếu hoàn — không truyền thì chính phiếu đang sửa tự giữ chỗ số lượng của nó, mọi dòng ra 0 còn-
    trả-được và form sửa hiện trắng.

    Args:
        id (UUID):
        exclude_return_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrderDetailDto | ProblemDetails
     """


    return sync_detailed(
        id=id,
client=client,
exclude_return_id=exclude_return_id,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    exclude_return_id: UUID | Unset = UNSET,

) -> Response[OrderDetailDto | ProblemDetails]:
    """ Chi tiết đơn hàng

     `excludeReturnId`: bỏ qua phiếu hoàn đó khi tính `openReturnQuantity` từng dòng. Dành cho màn SỬA
    phiếu hoàn — không truyền thì chính phiếu đang sửa tự giữ chỗ số lượng của nó, mọi dòng ra 0 còn-
    trả-được và form sửa hiện trắng.

    Args:
        id (UUID):
        exclude_return_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrderDetailDto | ProblemDetails]
     """


    kwargs = _get_kwargs(
        id=id,
exclude_return_id=exclude_return_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    exclude_return_id: UUID | Unset = UNSET,

) -> OrderDetailDto | ProblemDetails | None:
    """ Chi tiết đơn hàng

     `excludeReturnId`: bỏ qua phiếu hoàn đó khi tính `openReturnQuantity` từng dòng. Dành cho màn SỬA
    phiếu hoàn — không truyền thì chính phiếu đang sửa tự giữ chỗ số lượng của nó, mọi dòng ra 0 còn-
    trả-được và form sửa hiện trắng.

    Args:
        id (UUID):
        exclude_return_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrderDetailDto | ProblemDetails
     """


    return (await asyncio_detailed(
        id=id,
client=client,
exclude_return_id=exclude_return_id,

    )).parsed

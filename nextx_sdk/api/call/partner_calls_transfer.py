from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.partner_call_dto import PartnerCallDto
from ...models.partner_transfer_request import PartnerTransferRequest
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,
    *,
    body: PartnerTransferRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/call/partner/calls/{id}/transfer".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PartnerCallDto | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = PartnerCallDto.from_dict(response.json())



        return response_200

    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = ProblemDetails.from_dict(response.json())



        return response_409

    if response.status_code == 422:
        response_422 = ProblemDetails.from_dict(response.json())



        return response_422

    if response.status_code == 502:
        response_502 = ProblemDetails.from_dict(response.json())



        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PartnerCallDto | ProblemDetails]:
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
    body: PartnerTransferRequest | Unset = UNSET,

) -> Response[PartnerCallDto | ProblemDetails]:
    """ Chuyển máy

     Chuyển khách sang tổng đài viên khác (toAgent), hàng chờ (toQueueId) hoặc số ngoài (toNumber — chỉ
    cuộc gọi ra). Gửi đúng một đích.

    Args:
        id (UUID):
        body (PartnerTransferRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PartnerCallDto | ProblemDetails]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PartnerTransferRequest | Unset = UNSET,

) -> PartnerCallDto | ProblemDetails | None:
    """ Chuyển máy

     Chuyển khách sang tổng đài viên khác (toAgent), hàng chờ (toQueueId) hoặc số ngoài (toNumber — chỉ
    cuộc gọi ra). Gửi đúng một đích.

    Args:
        id (UUID):
        body (PartnerTransferRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PartnerCallDto | ProblemDetails
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PartnerTransferRequest | Unset = UNSET,

) -> Response[PartnerCallDto | ProblemDetails]:
    """ Chuyển máy

     Chuyển khách sang tổng đài viên khác (toAgent), hàng chờ (toQueueId) hoặc số ngoài (toNumber — chỉ
    cuộc gọi ra). Gửi đúng một đích.

    Args:
        id (UUID):
        body (PartnerTransferRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PartnerCallDto | ProblemDetails]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PartnerTransferRequest | Unset = UNSET,

) -> PartnerCallDto | ProblemDetails | None:
    """ Chuyển máy

     Chuyển khách sang tổng đài viên khác (toAgent), hàng chờ (toQueueId) hoặc số ngoài (toNumber — chỉ
    cuộc gọi ra). Gửi đúng một đích.

    Args:
        id (UUID):
        body (PartnerTransferRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PartnerCallDto | ProblemDetails
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed

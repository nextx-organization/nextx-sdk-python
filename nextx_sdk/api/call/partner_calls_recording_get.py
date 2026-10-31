from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.partner_recording_link_dto import PartnerRecordingLinkDto
from ...models.problem_details import ProblemDetails
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/call/partner/calls/{id}/recording".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PartnerRecordingLinkDto | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = PartnerRecordingLinkDto.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PartnerRecordingLinkDto | ProblemDetails]:
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

) -> Response[PartnerRecordingLinkDto | ProblemDetails]:
    """ Link tải ghi âm (15 phút)

     Mỗi lượt lấy link đều được ghi nhật ký. Hết hạn thì gọi lại để lấy link mới.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PartnerRecordingLinkDto | ProblemDetails]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> PartnerRecordingLinkDto | ProblemDetails | None:
    """ Link tải ghi âm (15 phút)

     Mỗi lượt lấy link đều được ghi nhật ký. Hết hạn thì gọi lại để lấy link mới.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PartnerRecordingLinkDto | ProblemDetails
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[PartnerRecordingLinkDto | ProblemDetails]:
    """ Link tải ghi âm (15 phút)

     Mỗi lượt lấy link đều được ghi nhật ký. Hết hạn thì gọi lại để lấy link mới.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PartnerRecordingLinkDto | ProblemDetails]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> PartnerRecordingLinkDto | ProblemDetails | None:
    """ Link tải ghi âm (15 phút)

     Mỗi lượt lấy link đều được ghi nhật ký. Hết hạn thì gọi lại để lấy link mới.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PartnerRecordingLinkDto | ProblemDetails
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed

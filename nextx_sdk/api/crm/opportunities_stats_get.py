from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.opportunity_stats_dto import OpportunityStatsDto
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    period_days: int | Unset = 30,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["periodDays"] = period_days


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/crm/opportunities/stats",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OpportunityStatsDto | None:
    if response.status_code == 200:
        response_200 = OpportunityStatsDto.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OpportunityStatsDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    period_days: int | Unset = 30,

) -> Response[OpportunityStatsDto]:
    """ Thống kê tổng quan cơ hội kinh doanh

     Trả về tổng cơ hội (open/won/lost), doanh thu dự kiến, dự báo doanh thu, tỷ lệ thắng, mới trong N
    ngày, phân bổ theo pipeline stage.

    Args:
        period_days (int | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpportunityStatsDto]
     """


    kwargs = _get_kwargs(
        period_days=period_days,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    period_days: int | Unset = 30,

) -> OpportunityStatsDto | None:
    """ Thống kê tổng quan cơ hội kinh doanh

     Trả về tổng cơ hội (open/won/lost), doanh thu dự kiến, dự báo doanh thu, tỷ lệ thắng, mới trong N
    ngày, phân bổ theo pipeline stage.

    Args:
        period_days (int | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpportunityStatsDto
     """


    return sync_detailed(
        client=client,
period_days=period_days,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    period_days: int | Unset = 30,

) -> Response[OpportunityStatsDto]:
    """ Thống kê tổng quan cơ hội kinh doanh

     Trả về tổng cơ hội (open/won/lost), doanh thu dự kiến, dự báo doanh thu, tỷ lệ thắng, mới trong N
    ngày, phân bổ theo pipeline stage.

    Args:
        period_days (int | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpportunityStatsDto]
     """


    kwargs = _get_kwargs(
        period_days=period_days,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    period_days: int | Unset = 30,

) -> OpportunityStatsDto | None:
    """ Thống kê tổng quan cơ hội kinh doanh

     Trả về tổng cơ hội (open/won/lost), doanh thu dự kiến, dự báo doanh thu, tỷ lệ thắng, mới trong N
    ngày, phân bổ theo pipeline stage.

    Args:
        period_days (int | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpportunityStatsDto
     """


    return (await asyncio_detailed(
        client=client,
period_days=period_days,

    )).parsed

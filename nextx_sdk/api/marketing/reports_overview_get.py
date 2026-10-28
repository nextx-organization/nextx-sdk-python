from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.report_overview_dto import ReportOverviewDto
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["from"] = from_

    params["to"] = to


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/marketing/reports/overview",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ReportOverviewDto | None:
    if response.status_code == 200:
        response_200 = ReportOverviewDto.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ReportOverviewDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,

) -> Response[ReportOverviewDto]:
    """ Tổng quan báo cáo marketing

     Trả về KPIs tổng hợp, thống kê theo ngày và theo kênh trong khoảng thời gian chỉ định.

    Args:
        from_ (str | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReportOverviewDto]
     """


    kwargs = _get_kwargs(
        from_=from_,
to=to,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,

) -> ReportOverviewDto | None:
    """ Tổng quan báo cáo marketing

     Trả về KPIs tổng hợp, thống kê theo ngày và theo kênh trong khoảng thời gian chỉ định.

    Args:
        from_ (str | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReportOverviewDto
     """


    return sync_detailed(
        client=client,
from_=from_,
to=to,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,

) -> Response[ReportOverviewDto]:
    """ Tổng quan báo cáo marketing

     Trả về KPIs tổng hợp, thống kê theo ngày và theo kênh trong khoảng thời gian chỉ định.

    Args:
        from_ (str | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReportOverviewDto]
     """


    kwargs = _get_kwargs(
        from_=from_,
to=to,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,

) -> ReportOverviewDto | None:
    """ Tổng quan báo cáo marketing

     Trả về KPIs tổng hợp, thống kê theo ngày và theo kênh trong khoảng thời gian chỉ định.

    Args:
        from_ (str | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReportOverviewDto
     """


    return (await asyncio_detailed(
        client=client,
from_=from_,
to=to,

    )).parsed

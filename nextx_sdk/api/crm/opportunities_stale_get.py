from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.problem_details import ProblemDetails
from ...models.stale_opportunities_dto import StaleOpportunitiesDto
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    days_overdue: int | Unset = 90,
    page: int | Unset = 1,
    page_size: int | Unset = 20,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["daysOverdue"] = days_overdue

    params["page"] = page

    params["pageSize"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/crm/opportunities/stale",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ProblemDetails | StaleOpportunitiesDto | None:
    if response.status_code == 200:
        response_200 = StaleOpportunitiesDto.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = ProblemDetails.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ProblemDetails | StaleOpportunitiesDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    days_overdue: int | Unset = 90,
    page: int | Unset = 1,
    page_size: int | Unset = 20,

) -> Response[ProblemDetails | StaleOpportunitiesDto]:
    """ Xem trước cơ hội quá hạn lâu

     Cơ hội còn Open nhưng ngày dự kiến chốt đã qua quá số ngày chỉ định. Trả tổng số, tổng giá trị ước
    tính và một trang danh sách. Con số totalCount trả về ở đây chính là expectedCount phải gửi khi đóng
    hàng loạt.

    Args:
        days_overdue (int | Unset):  Default: 90.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | StaleOpportunitiesDto]
     """


    kwargs = _get_kwargs(
        days_overdue=days_overdue,
page=page,
page_size=page_size,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    days_overdue: int | Unset = 90,
    page: int | Unset = 1,
    page_size: int | Unset = 20,

) -> ProblemDetails | StaleOpportunitiesDto | None:
    """ Xem trước cơ hội quá hạn lâu

     Cơ hội còn Open nhưng ngày dự kiến chốt đã qua quá số ngày chỉ định. Trả tổng số, tổng giá trị ước
    tính và một trang danh sách. Con số totalCount trả về ở đây chính là expectedCount phải gửi khi đóng
    hàng loạt.

    Args:
        days_overdue (int | Unset):  Default: 90.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | StaleOpportunitiesDto
     """


    return sync_detailed(
        client=client,
days_overdue=days_overdue,
page=page,
page_size=page_size,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    days_overdue: int | Unset = 90,
    page: int | Unset = 1,
    page_size: int | Unset = 20,

) -> Response[ProblemDetails | StaleOpportunitiesDto]:
    """ Xem trước cơ hội quá hạn lâu

     Cơ hội còn Open nhưng ngày dự kiến chốt đã qua quá số ngày chỉ định. Trả tổng số, tổng giá trị ước
    tính và một trang danh sách. Con số totalCount trả về ở đây chính là expectedCount phải gửi khi đóng
    hàng loạt.

    Args:
        days_overdue (int | Unset):  Default: 90.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | StaleOpportunitiesDto]
     """


    kwargs = _get_kwargs(
        days_overdue=days_overdue,
page=page,
page_size=page_size,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    days_overdue: int | Unset = 90,
    page: int | Unset = 1,
    page_size: int | Unset = 20,

) -> ProblemDetails | StaleOpportunitiesDto | None:
    """ Xem trước cơ hội quá hạn lâu

     Cơ hội còn Open nhưng ngày dự kiến chốt đã qua quá số ngày chỉ định. Trả tổng số, tổng giá trị ước
    tính và một trang danh sách. Con số totalCount trả về ở đây chính là expectedCount phải gửi khi đóng
    hàng loạt.

    Args:
        days_overdue (int | Unset):  Default: 90.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | StaleOpportunitiesDto
     """


    return (await asyncio_detailed(
        client=client,
days_overdue=days_overdue,
page=page,
page_size=page_size,

    )).parsed

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.my_visit_dto import MyVisitDto
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Unset
from typing import cast
import datetime



def _get_kwargs(
    *,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/dms/daily-plans/my-visits",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ProblemDetails | list[MyVisitDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = MyVisitDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = ProblemDetails.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ProblemDetails | list[MyVisitDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,

) -> Response[ProblemDetails | list[MyVisitDto]]:
    """ Lịch đi tuyến của nhân viên đang đăng nhập, trải theo ngày

     Quá khứ đọc check-in thật; tương lai TÍNH ẢO từ ma trận lịch chăm sóc (visit_days AND
    week_of_month), không có bản ghi nào trong DB. Chỉ ĐỌC — hôm nay muốn check-in thì vẫn dùng GET
    /daily-plans/today vì tiến độ ghi vào DailyPlanStop thật. Khoảng ngày tối đa 92 ngày một lần gọi.

    Args:
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | list[MyVisitDto]]
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
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,

) -> ProblemDetails | list[MyVisitDto] | None:
    """ Lịch đi tuyến của nhân viên đang đăng nhập, trải theo ngày

     Quá khứ đọc check-in thật; tương lai TÍNH ẢO từ ma trận lịch chăm sóc (visit_days AND
    week_of_month), không có bản ghi nào trong DB. Chỉ ĐỌC — hôm nay muốn check-in thì vẫn dùng GET
    /daily-plans/today vì tiến độ ghi vào DailyPlanStop thật. Khoảng ngày tối đa 92 ngày một lần gọi.

    Args:
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | list[MyVisitDto]
     """


    return sync_detailed(
        client=client,
from_=from_,
to=to,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,

) -> Response[ProblemDetails | list[MyVisitDto]]:
    """ Lịch đi tuyến của nhân viên đang đăng nhập, trải theo ngày

     Quá khứ đọc check-in thật; tương lai TÍNH ẢO từ ma trận lịch chăm sóc (visit_days AND
    week_of_month), không có bản ghi nào trong DB. Chỉ ĐỌC — hôm nay muốn check-in thì vẫn dùng GET
    /daily-plans/today vì tiến độ ghi vào DailyPlanStop thật. Khoảng ngày tối đa 92 ngày một lần gọi.

    Args:
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | list[MyVisitDto]]
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
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,

) -> ProblemDetails | list[MyVisitDto] | None:
    """ Lịch đi tuyến của nhân viên đang đăng nhập, trải theo ngày

     Quá khứ đọc check-in thật; tương lai TÍNH ẢO từ ma trận lịch chăm sóc (visit_days AND
    week_of_month), không có bản ghi nào trong DB. Chỉ ĐỌC — hôm nay muốn check-in thì vẫn dùng GET
    /daily-plans/today vì tiến độ ghi vào DailyPlanStop thật. Khoảng ngày tối đa 92 ngày một lần gọi.

    Args:
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | list[MyVisitDto]
     """


    return (await asyncio_detailed(
        client=client,
from_=from_,
to=to,

    )).parsed

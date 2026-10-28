from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invoice_summary_dto import InvoiceSummaryDto
from ...types import UNSET, Unset
from typing import cast
import datetime



def _get_kwargs(
    *,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_from_date: str | Unset = UNSET
    if not isinstance(from_date, Unset):
        json_from_date = from_date.isoformat()
    params["fromDate"] = json_from_date

    json_to_date: str | Unset = UNSET
    if not isinstance(to_date, Unset):
        json_to_date = to_date.isoformat()
    params["toDate"] = json_to_date


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/einvoice/reports/summary",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InvoiceSummaryDto | None:
    if response.status_code == 200:
        response_200 = InvoiceSummaryDto.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InvoiceSummaryDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,

) -> Response[InvoiceSummaryDto]:
    """ Tổng hợp hóa đơn theo trạng thái

     Đếm số lượng theo từng trạng thái (phát hành/chờ ký/nháp/lỗi/huỷ/đã gửi), doanh thu + thuế của HĐ đã
    phát hành, và cơ cấu theo nguồn. Lọc theo khoảng ngày.

    Args:
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoiceSummaryDto]
     """


    kwargs = _get_kwargs(
        from_date=from_date,
to_date=to_date,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,

) -> InvoiceSummaryDto | None:
    """ Tổng hợp hóa đơn theo trạng thái

     Đếm số lượng theo từng trạng thái (phát hành/chờ ký/nháp/lỗi/huỷ/đã gửi), doanh thu + thuế của HĐ đã
    phát hành, và cơ cấu theo nguồn. Lọc theo khoảng ngày.

    Args:
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoiceSummaryDto
     """


    return sync_detailed(
        client=client,
from_date=from_date,
to_date=to_date,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,

) -> Response[InvoiceSummaryDto]:
    """ Tổng hợp hóa đơn theo trạng thái

     Đếm số lượng theo từng trạng thái (phát hành/chờ ký/nháp/lỗi/huỷ/đã gửi), doanh thu + thuế của HĐ đã
    phát hành, và cơ cấu theo nguồn. Lọc theo khoảng ngày.

    Args:
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoiceSummaryDto]
     """


    kwargs = _get_kwargs(
        from_date=from_date,
to_date=to_date,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,

) -> InvoiceSummaryDto | None:
    """ Tổng hợp hóa đơn theo trạng thái

     Đếm số lượng theo từng trạng thái (phát hành/chờ ký/nháp/lỗi/huỷ/đã gửi), doanh thu + thuế của HĐ đã
    phát hành, và cơ cấu theo nguồn. Lọc theo khoảng ngày.

    Args:
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoiceSummaryDto
     """


    return (await asyncio_detailed(
        client=client,
from_date=from_date,
to_date=to_date,

    )).parsed

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invoice_dto_paged_result import InvoiceDtoPagedResult
from ...models.invoices_list_status import check_invoices_list_status
from ...models.invoices_list_status import InvoicesListStatus
from ...types import UNSET, Unset
from typing import cast
import datetime



def _get_kwargs(
    *,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    status: InvoicesListStatus | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    keyword: str | Unset = UNSET,
    source: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["pageNumber"] = page_number

    params["pageSize"] = page_size

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    json_from_date: str | Unset = UNSET
    if not isinstance(from_date, Unset):
        json_from_date = from_date.isoformat()
    params["fromDate"] = json_from_date

    json_to_date: str | Unset = UNSET
    if not isinstance(to_date, Unset):
        json_to_date = to_date.isoformat()
    params["toDate"] = json_to_date

    params["keyword"] = keyword

    params["source"] = source


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/einvoice/invoices",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InvoiceDtoPagedResult | None:
    if response.status_code == 200:
        response_200 = InvoiceDtoPagedResult.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InvoiceDtoPagedResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    status: InvoicesListStatus | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    keyword: str | Unset = UNSET,
    source: str | Unset = UNSET,

) -> Response[InvoiceDtoPagedResult]:
    """ Lấy danh sách hóa đơn có phân trang

     Lọc theo trạng thái, ngày tháng, nguồn (sales_order/gym_contract/manual) và tìm kiếm theo số HĐ /
    tên người mua. Kết quả phân trang.

    Args:
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        status (InvoicesListStatus | Unset):
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):
        keyword (str | Unset):
        source (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoiceDtoPagedResult]
     """


    kwargs = _get_kwargs(
        page_number=page_number,
page_size=page_size,
status=status,
from_date=from_date,
to_date=to_date,
keyword=keyword,
source=source,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    status: InvoicesListStatus | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    keyword: str | Unset = UNSET,
    source: str | Unset = UNSET,

) -> InvoiceDtoPagedResult | None:
    """ Lấy danh sách hóa đơn có phân trang

     Lọc theo trạng thái, ngày tháng, nguồn (sales_order/gym_contract/manual) và tìm kiếm theo số HĐ /
    tên người mua. Kết quả phân trang.

    Args:
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        status (InvoicesListStatus | Unset):
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):
        keyword (str | Unset):
        source (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoiceDtoPagedResult
     """


    return sync_detailed(
        client=client,
page_number=page_number,
page_size=page_size,
status=status,
from_date=from_date,
to_date=to_date,
keyword=keyword,
source=source,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    status: InvoicesListStatus | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    keyword: str | Unset = UNSET,
    source: str | Unset = UNSET,

) -> Response[InvoiceDtoPagedResult]:
    """ Lấy danh sách hóa đơn có phân trang

     Lọc theo trạng thái, ngày tháng, nguồn (sales_order/gym_contract/manual) và tìm kiếm theo số HĐ /
    tên người mua. Kết quả phân trang.

    Args:
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        status (InvoicesListStatus | Unset):
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):
        keyword (str | Unset):
        source (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoiceDtoPagedResult]
     """


    kwargs = _get_kwargs(
        page_number=page_number,
page_size=page_size,
status=status,
from_date=from_date,
to_date=to_date,
keyword=keyword,
source=source,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,
    status: InvoicesListStatus | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    keyword: str | Unset = UNSET,
    source: str | Unset = UNSET,

) -> InvoiceDtoPagedResult | None:
    """ Lấy danh sách hóa đơn có phân trang

     Lọc theo trạng thái, ngày tháng, nguồn (sales_order/gym_contract/manual) và tìm kiếm theo số HĐ /
    tên người mua. Kết quả phân trang.

    Args:
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        status (InvoicesListStatus | Unset):
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):
        keyword (str | Unset):
        source (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoiceDtoPagedResult
     """


    return (await asyncio_detailed(
        client=client,
page_number=page_number,
page_size=page_size,
status=status,
from_date=from_date,
to_date=to_date,
keyword=keyword,
source=source,

    )).parsed

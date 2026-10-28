from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paged_result_of_approval_instance_dto import PagedResultOfApprovalInstanceDto
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    role: str | Unset = 'mine',
    page: int | Unset = 1,
    page_size: int | Unset = 20,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["role"] = role

    params["page"] = page

    params["pageSize"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/office/approvals/instances",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PagedResultOfApprovalInstanceDto | None:
    if response.status_code == 200:
        response_200 = PagedResultOfApprovalInstanceDto.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PagedResultOfApprovalInstanceDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    role: str | Unset = 'mine',
    page: int | Unset = 1,
    page_size: int | Unset = 20,

) -> Response[PagedResultOfApprovalInstanceDto]:
    """ Hộp đơn (role=mine | todo | acted)

     mine = đơn tôi nộp · todo = đơn đang chờ tôi duyệt · acted = đơn tôi ĐÃ quyết (duyệt/từ chối/chuyển
    đi), mới trước cũ sau theo thời điểm quyết. Giá trị khác ba giá trị trên trả 400 — không đoán hộ
    người gọi. Mỗi dòng kèm sẵn definitionName (tên quy trình) và myPendingTaskId (việc đang chờ của
    người gọi, rỗng nếu không có), nên giao diện không phải gọi chi tiết từng phiếu để dựng nút Duyệt/Từ
    chối.

    Args:
        role (str | Unset):  Default: 'mine'.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedResultOfApprovalInstanceDto]
     """


    kwargs = _get_kwargs(
        role=role,
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
    role: str | Unset = 'mine',
    page: int | Unset = 1,
    page_size: int | Unset = 20,

) -> PagedResultOfApprovalInstanceDto | None:
    """ Hộp đơn (role=mine | todo | acted)

     mine = đơn tôi nộp · todo = đơn đang chờ tôi duyệt · acted = đơn tôi ĐÃ quyết (duyệt/từ chối/chuyển
    đi), mới trước cũ sau theo thời điểm quyết. Giá trị khác ba giá trị trên trả 400 — không đoán hộ
    người gọi. Mỗi dòng kèm sẵn definitionName (tên quy trình) và myPendingTaskId (việc đang chờ của
    người gọi, rỗng nếu không có), nên giao diện không phải gọi chi tiết từng phiếu để dựng nút Duyệt/Từ
    chối.

    Args:
        role (str | Unset):  Default: 'mine'.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedResultOfApprovalInstanceDto
     """


    return sync_detailed(
        client=client,
role=role,
page=page,
page_size=page_size,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    role: str | Unset = 'mine',
    page: int | Unset = 1,
    page_size: int | Unset = 20,

) -> Response[PagedResultOfApprovalInstanceDto]:
    """ Hộp đơn (role=mine | todo | acted)

     mine = đơn tôi nộp · todo = đơn đang chờ tôi duyệt · acted = đơn tôi ĐÃ quyết (duyệt/từ chối/chuyển
    đi), mới trước cũ sau theo thời điểm quyết. Giá trị khác ba giá trị trên trả 400 — không đoán hộ
    người gọi. Mỗi dòng kèm sẵn definitionName (tên quy trình) và myPendingTaskId (việc đang chờ của
    người gọi, rỗng nếu không có), nên giao diện không phải gọi chi tiết từng phiếu để dựng nút Duyệt/Từ
    chối.

    Args:
        role (str | Unset):  Default: 'mine'.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedResultOfApprovalInstanceDto]
     """


    kwargs = _get_kwargs(
        role=role,
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
    role: str | Unset = 'mine',
    page: int | Unset = 1,
    page_size: int | Unset = 20,

) -> PagedResultOfApprovalInstanceDto | None:
    """ Hộp đơn (role=mine | todo | acted)

     mine = đơn tôi nộp · todo = đơn đang chờ tôi duyệt · acted = đơn tôi ĐÃ quyết (duyệt/từ chối/chuyển
    đi), mới trước cũ sau theo thời điểm quyết. Giá trị khác ba giá trị trên trả 400 — không đoán hộ
    người gọi. Mỗi dòng kèm sẵn definitionName (tên quy trình) và myPendingTaskId (việc đang chờ của
    người gọi, rỗng nếu không có), nên giao diện không phải gọi chi tiết từng phiếu để dựng nút Duyệt/Từ
    chối.

    Args:
        role (str | Unset):  Default: 'mine'.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedResultOfApprovalInstanceDto
     """


    return (await asyncio_detailed(
        client=client,
role=role,
page=page,
page_size=page_size,

    )).parsed

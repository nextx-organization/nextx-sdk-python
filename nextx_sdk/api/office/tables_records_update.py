from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.problem_details import ProblemDetails
from ...models.record_update_result import RecordUpdateResult
from ...models.update_record_request import UpdateRecordRequest
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    table_id: UUID,
    record_id: UUID,
    *,
    body: UpdateRecordRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/office/tables/{table_id}/records/{record_id}".format(table_id=quote(str(table_id), safe=""),record_id=quote(str(record_id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ProblemDetails | RecordUpdateResult | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = RecordUpdateResult.from_dict(response.json())



        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ProblemDetails | RecordUpdateResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    table_id: UUID,
    record_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateRecordRequest | Unset = UNSET,

) -> Response[Any | ProblemDetails | RecordUpdateResult]:
    """ Cập nhật record (merge mặc định; replace=true để ghi đè)

     Gửi kèm `expectedValues` — bản đồ field_id → giá trị mà giao diện ĐANG HIỆN của đúng những ô đang
    sửa — để bật khoá lạc quan. Ô nào đã bị người khác đổi thì lời gọi trả **409** kèm danh sách ô xung
    đột và giá trị hiện tại của chúng, và **không ô nào được ghi**. Bỏ trống `expectedValues` thì không
    kiểm, đúng như nếp cũ — nên client đang chạy không đổi hành vi.

    Args:
        table_id (UUID):
        record_id (UUID):
        body (UpdateRecordRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | RecordUpdateResult]
     """


    kwargs = _get_kwargs(
        table_id=table_id,
record_id=record_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    table_id: UUID,
    record_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateRecordRequest | Unset = UNSET,

) -> Any | ProblemDetails | RecordUpdateResult | None:
    """ Cập nhật record (merge mặc định; replace=true để ghi đè)

     Gửi kèm `expectedValues` — bản đồ field_id → giá trị mà giao diện ĐANG HIỆN của đúng những ô đang
    sửa — để bật khoá lạc quan. Ô nào đã bị người khác đổi thì lời gọi trả **409** kèm danh sách ô xung
    đột và giá trị hiện tại của chúng, và **không ô nào được ghi**. Bỏ trống `expectedValues` thì không
    kiểm, đúng như nếp cũ — nên client đang chạy không đổi hành vi.

    Args:
        table_id (UUID):
        record_id (UUID):
        body (UpdateRecordRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | RecordUpdateResult
     """


    return sync_detailed(
        table_id=table_id,
record_id=record_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    table_id: UUID,
    record_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateRecordRequest | Unset = UNSET,

) -> Response[Any | ProblemDetails | RecordUpdateResult]:
    """ Cập nhật record (merge mặc định; replace=true để ghi đè)

     Gửi kèm `expectedValues` — bản đồ field_id → giá trị mà giao diện ĐANG HIỆN của đúng những ô đang
    sửa — để bật khoá lạc quan. Ô nào đã bị người khác đổi thì lời gọi trả **409** kèm danh sách ô xung
    đột và giá trị hiện tại của chúng, và **không ô nào được ghi**. Bỏ trống `expectedValues` thì không
    kiểm, đúng như nếp cũ — nên client đang chạy không đổi hành vi.

    Args:
        table_id (UUID):
        record_id (UUID):
        body (UpdateRecordRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | RecordUpdateResult]
     """


    kwargs = _get_kwargs(
        table_id=table_id,
record_id=record_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    table_id: UUID,
    record_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateRecordRequest | Unset = UNSET,

) -> Any | ProblemDetails | RecordUpdateResult | None:
    """ Cập nhật record (merge mặc định; replace=true để ghi đè)

     Gửi kèm `expectedValues` — bản đồ field_id → giá trị mà giao diện ĐANG HIỆN của đúng những ô đang
    sửa — để bật khoá lạc quan. Ô nào đã bị người khác đổi thì lời gọi trả **409** kèm danh sách ô xung
    đột và giá trị hiện tại của chúng, và **không ô nào được ghi**. Bỏ trống `expectedValues` thì không
    kiểm, đúng như nếp cũ — nên client đang chạy không đổi hành vi.

    Args:
        table_id (UUID):
        record_id (UUID):
        body (UpdateRecordRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | RecordUpdateResult
     """


    return (await asyncio_detailed(
        table_id=table_id,
record_id=record_id,
client=client,
body=body,

    )).parsed

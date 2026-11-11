from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    *,
    account_id: UUID | Unset = UNSET,
    transaction_type: str | Unset = UNSET,
    date_from: datetime.date | Unset = UNSET,
    date_to: datetime.date | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 50,
    bank_account_ids: list[UUID] | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_account_id: str | Unset = UNSET
    if not isinstance(account_id, Unset):
        json_account_id = str(account_id)
    params["accountId"] = json_account_id

    params["transactionType"] = transaction_type

    json_date_from: str | Unset = UNSET
    if not isinstance(date_from, Unset):
        json_date_from = date_from.isoformat()
    params["dateFrom"] = json_date_from

    json_date_to: str | Unset = UNSET
    if not isinstance(date_to, Unset):
        json_date_to = date_to.isoformat()
    params["dateTo"] = json_date_to

    params["pageNumber"] = page_number

    params["pageSize"] = page_size

    json_bank_account_ids: list[str] | Unset = UNSET
    if not isinstance(bank_account_ids, Unset):
        json_bank_account_ids = []
        for bank_account_ids_item_data in bank_account_ids:
            bank_account_ids_item = str(bank_account_ids_item_data)
            json_bank_account_ids.append(bank_account_ids_item)


    params["bankAccountIds"] = json_bank_account_ids


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sales/cashbook/transactions",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID | Unset = UNSET,
    transaction_type: str | Unset = UNSET,
    date_from: datetime.date | Unset = UNSET,
    date_to: datetime.date | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 50,
    bank_account_ids: list[UUID] | Unset = UNSET,

) -> Response[Any]:
    """ Danh sách bút toán quỹ (append-only)

     Nguồn của báo cáo dòng tiền. Lọc theo quỹ, loại giao dịch (CREDIT/DEBIT), khoảng ngày, tài khoản
    ngân hàng.

    Args:
        account_id (UUID | Unset):
        transaction_type (str | Unset):
        date_from (datetime.date | Unset):
        date_to (datetime.date | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        bank_account_ids (list[UUID] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
transaction_type=transaction_type,
date_from=date_from,
date_to=date_to,
page_number=page_number,
page_size=page_size,
bank_account_ids=bank_account_ids,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID | Unset = UNSET,
    transaction_type: str | Unset = UNSET,
    date_from: datetime.date | Unset = UNSET,
    date_to: datetime.date | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 50,
    bank_account_ids: list[UUID] | Unset = UNSET,

) -> Response[Any]:
    """ Danh sách bút toán quỹ (append-only)

     Nguồn của báo cáo dòng tiền. Lọc theo quỹ, loại giao dịch (CREDIT/DEBIT), khoảng ngày, tài khoản
    ngân hàng.

    Args:
        account_id (UUID | Unset):
        transaction_type (str | Unset):
        date_from (datetime.date | Unset):
        date_to (datetime.date | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        bank_account_ids (list[UUID] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
transaction_type=transaction_type,
date_from=date_from,
date_to=date_to,
page_number=page_number,
page_size=page_size,
bank_account_ids=bank_account_ids,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)


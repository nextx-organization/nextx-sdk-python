from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.contact_detail_dto import ContactDetailDto
from ...models.create_contact_request import CreateContactRequest
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: CreateContactRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/crm/contacts",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ContactDetailDto | ProblemDetails | None:
    if response.status_code == 201:
        response_201 = ContactDetailDto.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = ProblemDetails.from_dict(response.json())



        return response_400

    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())



        return response_403

    if response.status_code == 409:
        response_409 = ProblemDetails.from_dict(response.json())



        return response_409

    if response.status_code == 422:
        response_422 = ProblemDetails.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ContactDetailDto | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateContactRequest | Unset = UNSET,

) -> Response[ContactDetailDto | ProblemDetails]:
    """ Tạo contact mới

     Tạo contact (ADR-CRM4 v1.3). lifecycle_stage = Lead nếu không gửi; gửi lifecycleStage = "Customer"
    để tạo thẳng khách hàng (nút Thêm khách hàng). ContactType IMMUTABLE sau khi tạo (INV-CRM4-11).
    referralCodeId (P5): chỉ quản lý (crm.settings.manage) — mã nhân viên + bỏ trống người phụ trách ⇒
    chủ mã nhận lead.

    Args:
        body (CreateContactRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactDetailDto | ProblemDetails]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateContactRequest | Unset = UNSET,

) -> ContactDetailDto | ProblemDetails | None:
    """ Tạo contact mới

     Tạo contact (ADR-CRM4 v1.3). lifecycle_stage = Lead nếu không gửi; gửi lifecycleStage = "Customer"
    để tạo thẳng khách hàng (nút Thêm khách hàng). ContactType IMMUTABLE sau khi tạo (INV-CRM4-11).
    referralCodeId (P5): chỉ quản lý (crm.settings.manage) — mã nhân viên + bỏ trống người phụ trách ⇒
    chủ mã nhận lead.

    Args:
        body (CreateContactRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactDetailDto | ProblemDetails
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateContactRequest | Unset = UNSET,

) -> Response[ContactDetailDto | ProblemDetails]:
    """ Tạo contact mới

     Tạo contact (ADR-CRM4 v1.3). lifecycle_stage = Lead nếu không gửi; gửi lifecycleStage = "Customer"
    để tạo thẳng khách hàng (nút Thêm khách hàng). ContactType IMMUTABLE sau khi tạo (INV-CRM4-11).
    referralCodeId (P5): chỉ quản lý (crm.settings.manage) — mã nhân viên + bỏ trống người phụ trách ⇒
    chủ mã nhận lead.

    Args:
        body (CreateContactRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactDetailDto | ProblemDetails]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateContactRequest | Unset = UNSET,

) -> ContactDetailDto | ProblemDetails | None:
    """ Tạo contact mới

     Tạo contact (ADR-CRM4 v1.3). lifecycle_stage = Lead nếu không gửi; gửi lifecycleStage = "Customer"
    để tạo thẳng khách hàng (nút Thêm khách hàng). ContactType IMMUTABLE sau khi tạo (INV-CRM4-11).
    referralCodeId (P5): chỉ quản lý (crm.settings.manage) — mã nhân viên + bỏ trống người phụ trách ⇒
    chủ mã nhận lead.

    Args:
        body (CreateContactRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactDetailDto | ProblemDetails
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed

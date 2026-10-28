from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.contact_branch_lookup_dto import ContactBranchLookupDto
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    q: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["q"] = q


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/crm/contacts/branch-lookup",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[ContactBranchLookupDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = ContactBranchLookupDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[ContactBranchLookupDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,

) -> Response[list[ContactBranchLookupDto]]:
    """ Tra khách theo đúng SĐT/mã (kể cả ngoài phạm vi)

     Dùng khi ô tìm không ra mà tạo mới báo trùng SĐT. Chỉ khớp CHÍNH XÁC (SĐT mọi cách viết 0/84/+84,
    hoặc mã khách), tối đa 5. Khách người gọi không được xem thì SĐT che 3 số giữa. canClaim = có quyền
    crm.contacts.claim_branch.

    Args:
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ContactBranchLookupDto]]
     """


    kwargs = _get_kwargs(
        q=q,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,

) -> list[ContactBranchLookupDto] | None:
    """ Tra khách theo đúng SĐT/mã (kể cả ngoài phạm vi)

     Dùng khi ô tìm không ra mà tạo mới báo trùng SĐT. Chỉ khớp CHÍNH XÁC (SĐT mọi cách viết 0/84/+84,
    hoặc mã khách), tối đa 5. Khách người gọi không được xem thì SĐT che 3 số giữa. canClaim = có quyền
    crm.contacts.claim_branch.

    Args:
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ContactBranchLookupDto]
     """


    return sync_detailed(
        client=client,
q=q,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,

) -> Response[list[ContactBranchLookupDto]]:
    """ Tra khách theo đúng SĐT/mã (kể cả ngoài phạm vi)

     Dùng khi ô tìm không ra mà tạo mới báo trùng SĐT. Chỉ khớp CHÍNH XÁC (SĐT mọi cách viết 0/84/+84,
    hoặc mã khách), tối đa 5. Khách người gọi không được xem thì SĐT che 3 số giữa. canClaim = có quyền
    crm.contacts.claim_branch.

    Args:
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ContactBranchLookupDto]]
     """


    kwargs = _get_kwargs(
        q=q,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,

) -> list[ContactBranchLookupDto] | None:
    """ Tra khách theo đúng SĐT/mã (kể cả ngoài phạm vi)

     Dùng khi ô tìm không ra mà tạo mới báo trùng SĐT. Chỉ khớp CHÍNH XÁC (SĐT mọi cách viết 0/84/+84,
    hoặc mã khách), tối đa 5. Khách người gọi không được xem thì SĐT che 3 số giữa. canClaim = có quyền
    crm.contacts.claim_branch.

    Args:
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ContactBranchLookupDto]
     """


    return (await asyncio_detailed(
        client=client,
q=q,

    )).parsed

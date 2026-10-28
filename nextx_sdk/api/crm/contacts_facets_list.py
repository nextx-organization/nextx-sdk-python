from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.contacts_facets_list_response_200 import ContactsFacetsListResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    fields: str | Unset = UNSET,
    f: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["fields"] = fields

    params["f"] = f


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/crm/contacts/facets",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ContactsFacetsListResponse200 | None:
    if response.status_code == 200:
        response_200 = ContactsFacetsListResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ContactsFacetsListResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    fields: str | Unset = UNSET,
    f: str | Unset = UNSET,

) -> Response[ContactsFacetsListResponse200]:
    """ Đếm sẵn theo trường lọc (facet)

     GROUP BY qua đúng query đã scope quyền + đã áp FilterRules (?f=).
    fields=lifecycle_stage,lead_tier,source… Trả code → { value → count }.

    Args:
        fields (str | Unset):
        f (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactsFacetsListResponse200]
     """


    kwargs = _get_kwargs(
        fields=fields,
f=f,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    fields: str | Unset = UNSET,
    f: str | Unset = UNSET,

) -> ContactsFacetsListResponse200 | None:
    """ Đếm sẵn theo trường lọc (facet)

     GROUP BY qua đúng query đã scope quyền + đã áp FilterRules (?f=).
    fields=lifecycle_stage,lead_tier,source… Trả code → { value → count }.

    Args:
        fields (str | Unset):
        f (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactsFacetsListResponse200
     """


    return sync_detailed(
        client=client,
fields=fields,
f=f,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    fields: str | Unset = UNSET,
    f: str | Unset = UNSET,

) -> Response[ContactsFacetsListResponse200]:
    """ Đếm sẵn theo trường lọc (facet)

     GROUP BY qua đúng query đã scope quyền + đã áp FilterRules (?f=).
    fields=lifecycle_stage,lead_tier,source… Trả code → { value → count }.

    Args:
        fields (str | Unset):
        f (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactsFacetsListResponse200]
     """


    kwargs = _get_kwargs(
        fields=fields,
f=f,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    fields: str | Unset = UNSET,
    f: str | Unset = UNSET,

) -> ContactsFacetsListResponse200 | None:
    """ Đếm sẵn theo trường lọc (facet)

     GROUP BY qua đúng query đã scope quyền + đã áp FilterRules (?f=).
    fields=lifecycle_stage,lead_tier,source… Trả code → { value → count }.

    Args:
        fields (str | Unset):
        f (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactsFacetsListResponse200
     """


    return (await asyncio_detailed(
        client=client,
fields=fields,
f=f,

    )).parsed

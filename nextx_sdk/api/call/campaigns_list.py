from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.campaign_list_result import CampaignListResult
from ...models.campaigns_list_status import CampaignsListStatus
from ...models.campaigns_list_status import check_campaigns_list_status
from ...models.campaigns_list_type import CampaignsListType
from ...models.campaigns_list_type import check_campaigns_list_type
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    status: CampaignsListStatus | Unset = UNSET,
    type_: CampaignsListType | Unset = UNSET,
    search: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_

    params["type"] = json_type_

    params["search"] = search

    params["pageNumber"] = page_number

    params["pageSize"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/call/campaigns",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CampaignListResult | None:
    if response.status_code == 200:
        response_200 = CampaignListResult.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CampaignListResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: CampaignsListStatus | Unset = UNSET,
    type_: CampaignsListType | Unset = UNSET,
    search: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,

) -> Response[CampaignListResult]:
    """ Danh sách campaigns

     PagedResult với filters: status, type, search. Bao gồm progress stats.

    Args:
        status (CampaignsListStatus | Unset):
        type_ (CampaignsListType | Unset):
        search (str | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CampaignListResult]
     """


    kwargs = _get_kwargs(
        status=status,
type_=type_,
search=search,
page_number=page_number,
page_size=page_size,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    status: CampaignsListStatus | Unset = UNSET,
    type_: CampaignsListType | Unset = UNSET,
    search: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,

) -> CampaignListResult | None:
    """ Danh sách campaigns

     PagedResult với filters: status, type, search. Bao gồm progress stats.

    Args:
        status (CampaignsListStatus | Unset):
        type_ (CampaignsListType | Unset):
        search (str | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CampaignListResult
     """


    return sync_detailed(
        client=client,
status=status,
type_=type_,
search=search,
page_number=page_number,
page_size=page_size,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: CampaignsListStatus | Unset = UNSET,
    type_: CampaignsListType | Unset = UNSET,
    search: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,

) -> Response[CampaignListResult]:
    """ Danh sách campaigns

     PagedResult với filters: status, type, search. Bao gồm progress stats.

    Args:
        status (CampaignsListStatus | Unset):
        type_ (CampaignsListType | Unset):
        search (str | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CampaignListResult]
     """


    kwargs = _get_kwargs(
        status=status,
type_=type_,
search=search,
page_number=page_number,
page_size=page_size,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    status: CampaignsListStatus | Unset = UNSET,
    type_: CampaignsListType | Unset = UNSET,
    search: str | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 20,

) -> CampaignListResult | None:
    """ Danh sách campaigns

     PagedResult với filters: status, type, search. Bao gồm progress stats.

    Args:
        status (CampaignsListStatus | Unset):
        type_ (CampaignsListType | Unset):
        search (str | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CampaignListResult
     """


    return (await asyncio_detailed(
        client=client,
status=status,
type_=type_,
search=search,
page_number=page_number,
page_size=page_size,

    )).parsed

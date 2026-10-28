from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.outlet_dto_paged_result import OutletDtoPagedResult
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    *,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    channel_codes: list[str] | Unset = UNSET,
    statuses: list[str] | Unset = UNSET,
    zone_ids: list[UUID] | Unset = UNSET,
    branch_ids: list[UUID] | Unset = UNSET,
    route_ids: list[UUID] | Unset = UNSET,
    sales_rep_ids: list[UUID] | Unset = UNSET,
    tiers: list[str] | Unset = UNSET,
    ranks: list[str] | Unset = UNSET,
    sales_rep_unassigned: bool | Unset = UNSET,
    has_coordinates: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    crm_contact_id: UUID | Unset = UNSET,
    care_status_ids: list[UUID] | Unset = UNSET,
    include_order_stats: bool | Unset = False,
    stats_from: datetime.date | Unset = UNSET,
    stats_to: datetime.date | Unset = UNSET,
    suspected_duplicates: bool | Unset = False,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["pageSize"] = page_size

    json_channel_codes: list[str] | Unset = UNSET
    if not isinstance(channel_codes, Unset):
        json_channel_codes = channel_codes


    params["channelCodes"] = json_channel_codes

    json_statuses: list[str] | Unset = UNSET
    if not isinstance(statuses, Unset):
        json_statuses = statuses


    params["statuses"] = json_statuses

    json_zone_ids: list[str] | Unset = UNSET
    if not isinstance(zone_ids, Unset):
        json_zone_ids = []
        for zone_ids_item_data in zone_ids:
            zone_ids_item = str(zone_ids_item_data)
            json_zone_ids.append(zone_ids_item)


    params["zoneIds"] = json_zone_ids

    json_branch_ids: list[str] | Unset = UNSET
    if not isinstance(branch_ids, Unset):
        json_branch_ids = []
        for branch_ids_item_data in branch_ids:
            branch_ids_item = str(branch_ids_item_data)
            json_branch_ids.append(branch_ids_item)


    params["branchIds"] = json_branch_ids

    json_route_ids: list[str] | Unset = UNSET
    if not isinstance(route_ids, Unset):
        json_route_ids = []
        for route_ids_item_data in route_ids:
            route_ids_item = str(route_ids_item_data)
            json_route_ids.append(route_ids_item)


    params["routeIds"] = json_route_ids

    json_sales_rep_ids: list[str] | Unset = UNSET
    if not isinstance(sales_rep_ids, Unset):
        json_sales_rep_ids = []
        for sales_rep_ids_item_data in sales_rep_ids:
            sales_rep_ids_item = str(sales_rep_ids_item_data)
            json_sales_rep_ids.append(sales_rep_ids_item)


    params["salesRepIds"] = json_sales_rep_ids

    json_tiers: list[str] | Unset = UNSET
    if not isinstance(tiers, Unset):
        json_tiers = tiers


    params["tiers"] = json_tiers

    json_ranks: list[str] | Unset = UNSET
    if not isinstance(ranks, Unset):
        json_ranks = ranks


    params["ranks"] = json_ranks

    params["salesRepUnassigned"] = sales_rep_unassigned

    params["hasCoordinates"] = has_coordinates

    params["q"] = q

    json_crm_contact_id: str | Unset = UNSET
    if not isinstance(crm_contact_id, Unset):
        json_crm_contact_id = str(crm_contact_id)
    params["crmContactId"] = json_crm_contact_id

    json_care_status_ids: list[str] | Unset = UNSET
    if not isinstance(care_status_ids, Unset):
        json_care_status_ids = []
        for care_status_ids_item_data in care_status_ids:
            care_status_ids_item = str(care_status_ids_item_data)
            json_care_status_ids.append(care_status_ids_item)


    params["careStatusIds"] = json_care_status_ids

    params["includeOrderStats"] = include_order_stats

    json_stats_from: str | Unset = UNSET
    if not isinstance(stats_from, Unset):
        json_stats_from = stats_from.isoformat()
    params["statsFrom"] = json_stats_from

    json_stats_to: str | Unset = UNSET
    if not isinstance(stats_to, Unset):
        json_stats_to = stats_to.isoformat()
    params["statsTo"] = json_stats_to

    params["suspectedDuplicates"] = suspected_duplicates


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/dms/outlets",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OutletDtoPagedResult | None:
    if response.status_code == 200:
        response_200 = OutletDtoPagedResult.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OutletDtoPagedResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    channel_codes: list[str] | Unset = UNSET,
    statuses: list[str] | Unset = UNSET,
    zone_ids: list[UUID] | Unset = UNSET,
    branch_ids: list[UUID] | Unset = UNSET,
    route_ids: list[UUID] | Unset = UNSET,
    sales_rep_ids: list[UUID] | Unset = UNSET,
    tiers: list[str] | Unset = UNSET,
    ranks: list[str] | Unset = UNSET,
    sales_rep_unassigned: bool | Unset = UNSET,
    has_coordinates: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    crm_contact_id: UUID | Unset = UNSET,
    care_status_ids: list[UUID] | Unset = UNSET,
    include_order_stats: bool | Unset = False,
    stats_from: datetime.date | Unset = UNSET,
    stats_to: datetime.date | Unset = UNSET,
    suspected_duplicates: bool | Unset = False,

) -> Response[OutletDtoPagedResult]:
    """ Danh sách outlets

     Query DMS DB. Multi-select filter: channelCodes, statuses, zoneIds, branchIds, routeIds,
    salesRepIds, tiers, ranks, hasCoordinates, q.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        channel_codes (list[str] | Unset):
        statuses (list[str] | Unset):
        zone_ids (list[UUID] | Unset):
        branch_ids (list[UUID] | Unset):
        route_ids (list[UUID] | Unset):
        sales_rep_ids (list[UUID] | Unset):
        tiers (list[str] | Unset):
        ranks (list[str] | Unset):
        sales_rep_unassigned (bool | Unset):
        has_coordinates (bool | Unset):
        q (str | Unset):
        crm_contact_id (UUID | Unset):
        care_status_ids (list[UUID] | Unset):
        include_order_stats (bool | Unset):  Default: False.
        stats_from (datetime.date | Unset):
        stats_to (datetime.date | Unset):
        suspected_duplicates (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutletDtoPagedResult]
     """


    kwargs = _get_kwargs(
        page=page,
page_size=page_size,
channel_codes=channel_codes,
statuses=statuses,
zone_ids=zone_ids,
branch_ids=branch_ids,
route_ids=route_ids,
sales_rep_ids=sales_rep_ids,
tiers=tiers,
ranks=ranks,
sales_rep_unassigned=sales_rep_unassigned,
has_coordinates=has_coordinates,
q=q,
crm_contact_id=crm_contact_id,
care_status_ids=care_status_ids,
include_order_stats=include_order_stats,
stats_from=stats_from,
stats_to=stats_to,
suspected_duplicates=suspected_duplicates,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    channel_codes: list[str] | Unset = UNSET,
    statuses: list[str] | Unset = UNSET,
    zone_ids: list[UUID] | Unset = UNSET,
    branch_ids: list[UUID] | Unset = UNSET,
    route_ids: list[UUID] | Unset = UNSET,
    sales_rep_ids: list[UUID] | Unset = UNSET,
    tiers: list[str] | Unset = UNSET,
    ranks: list[str] | Unset = UNSET,
    sales_rep_unassigned: bool | Unset = UNSET,
    has_coordinates: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    crm_contact_id: UUID | Unset = UNSET,
    care_status_ids: list[UUID] | Unset = UNSET,
    include_order_stats: bool | Unset = False,
    stats_from: datetime.date | Unset = UNSET,
    stats_to: datetime.date | Unset = UNSET,
    suspected_duplicates: bool | Unset = False,

) -> OutletDtoPagedResult | None:
    """ Danh sách outlets

     Query DMS DB. Multi-select filter: channelCodes, statuses, zoneIds, branchIds, routeIds,
    salesRepIds, tiers, ranks, hasCoordinates, q.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        channel_codes (list[str] | Unset):
        statuses (list[str] | Unset):
        zone_ids (list[UUID] | Unset):
        branch_ids (list[UUID] | Unset):
        route_ids (list[UUID] | Unset):
        sales_rep_ids (list[UUID] | Unset):
        tiers (list[str] | Unset):
        ranks (list[str] | Unset):
        sales_rep_unassigned (bool | Unset):
        has_coordinates (bool | Unset):
        q (str | Unset):
        crm_contact_id (UUID | Unset):
        care_status_ids (list[UUID] | Unset):
        include_order_stats (bool | Unset):  Default: False.
        stats_from (datetime.date | Unset):
        stats_to (datetime.date | Unset):
        suspected_duplicates (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutletDtoPagedResult
     """


    return sync_detailed(
        client=client,
page=page,
page_size=page_size,
channel_codes=channel_codes,
statuses=statuses,
zone_ids=zone_ids,
branch_ids=branch_ids,
route_ids=route_ids,
sales_rep_ids=sales_rep_ids,
tiers=tiers,
ranks=ranks,
sales_rep_unassigned=sales_rep_unassigned,
has_coordinates=has_coordinates,
q=q,
crm_contact_id=crm_contact_id,
care_status_ids=care_status_ids,
include_order_stats=include_order_stats,
stats_from=stats_from,
stats_to=stats_to,
suspected_duplicates=suspected_duplicates,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    channel_codes: list[str] | Unset = UNSET,
    statuses: list[str] | Unset = UNSET,
    zone_ids: list[UUID] | Unset = UNSET,
    branch_ids: list[UUID] | Unset = UNSET,
    route_ids: list[UUID] | Unset = UNSET,
    sales_rep_ids: list[UUID] | Unset = UNSET,
    tiers: list[str] | Unset = UNSET,
    ranks: list[str] | Unset = UNSET,
    sales_rep_unassigned: bool | Unset = UNSET,
    has_coordinates: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    crm_contact_id: UUID | Unset = UNSET,
    care_status_ids: list[UUID] | Unset = UNSET,
    include_order_stats: bool | Unset = False,
    stats_from: datetime.date | Unset = UNSET,
    stats_to: datetime.date | Unset = UNSET,
    suspected_duplicates: bool | Unset = False,

) -> Response[OutletDtoPagedResult]:
    """ Danh sách outlets

     Query DMS DB. Multi-select filter: channelCodes, statuses, zoneIds, branchIds, routeIds,
    salesRepIds, tiers, ranks, hasCoordinates, q.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        channel_codes (list[str] | Unset):
        statuses (list[str] | Unset):
        zone_ids (list[UUID] | Unset):
        branch_ids (list[UUID] | Unset):
        route_ids (list[UUID] | Unset):
        sales_rep_ids (list[UUID] | Unset):
        tiers (list[str] | Unset):
        ranks (list[str] | Unset):
        sales_rep_unassigned (bool | Unset):
        has_coordinates (bool | Unset):
        q (str | Unset):
        crm_contact_id (UUID | Unset):
        care_status_ids (list[UUID] | Unset):
        include_order_stats (bool | Unset):  Default: False.
        stats_from (datetime.date | Unset):
        stats_to (datetime.date | Unset):
        suspected_duplicates (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutletDtoPagedResult]
     """


    kwargs = _get_kwargs(
        page=page,
page_size=page_size,
channel_codes=channel_codes,
statuses=statuses,
zone_ids=zone_ids,
branch_ids=branch_ids,
route_ids=route_ids,
sales_rep_ids=sales_rep_ids,
tiers=tiers,
ranks=ranks,
sales_rep_unassigned=sales_rep_unassigned,
has_coordinates=has_coordinates,
q=q,
crm_contact_id=crm_contact_id,
care_status_ids=care_status_ids,
include_order_stats=include_order_stats,
stats_from=stats_from,
stats_to=stats_to,
suspected_duplicates=suspected_duplicates,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    channel_codes: list[str] | Unset = UNSET,
    statuses: list[str] | Unset = UNSET,
    zone_ids: list[UUID] | Unset = UNSET,
    branch_ids: list[UUID] | Unset = UNSET,
    route_ids: list[UUID] | Unset = UNSET,
    sales_rep_ids: list[UUID] | Unset = UNSET,
    tiers: list[str] | Unset = UNSET,
    ranks: list[str] | Unset = UNSET,
    sales_rep_unassigned: bool | Unset = UNSET,
    has_coordinates: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    crm_contact_id: UUID | Unset = UNSET,
    care_status_ids: list[UUID] | Unset = UNSET,
    include_order_stats: bool | Unset = False,
    stats_from: datetime.date | Unset = UNSET,
    stats_to: datetime.date | Unset = UNSET,
    suspected_duplicates: bool | Unset = False,

) -> OutletDtoPagedResult | None:
    """ Danh sách outlets

     Query DMS DB. Multi-select filter: channelCodes, statuses, zoneIds, branchIds, routeIds,
    salesRepIds, tiers, ranks, hasCoordinates, q.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        channel_codes (list[str] | Unset):
        statuses (list[str] | Unset):
        zone_ids (list[UUID] | Unset):
        branch_ids (list[UUID] | Unset):
        route_ids (list[UUID] | Unset):
        sales_rep_ids (list[UUID] | Unset):
        tiers (list[str] | Unset):
        ranks (list[str] | Unset):
        sales_rep_unassigned (bool | Unset):
        has_coordinates (bool | Unset):
        q (str | Unset):
        crm_contact_id (UUID | Unset):
        care_status_ids (list[UUID] | Unset):
        include_order_stats (bool | Unset):  Default: False.
        stats_from (datetime.date | Unset):
        stats_to (datetime.date | Unset):
        suspected_duplicates (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutletDtoPagedResult
     """


    return (await asyncio_detailed(
        client=client,
page=page,
page_size=page_size,
channel_codes=channel_codes,
statuses=statuses,
zone_ids=zone_ids,
branch_ids=branch_ids,
route_ids=route_ids,
sales_rep_ids=sales_rep_ids,
tiers=tiers,
ranks=ranks,
sales_rep_unassigned=sales_rep_unassigned,
has_coordinates=has_coordinates,
q=q,
crm_contact_id=crm_contact_id,
care_status_ids=care_status_ids,
include_order_stats=include_order_stats,
stats_from=stats_from,
stats_to=stats_to,
suspected_duplicates=suspected_duplicates,

    )).parsed

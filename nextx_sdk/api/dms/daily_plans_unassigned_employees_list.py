from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.unassigned_employee_dto import UnassignedEmployeeDto
from ...types import UNSET, Unset
from typing import cast
import datetime



def _get_kwargs(
    *,
    plan_date: datetime.date | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_plan_date: str | Unset = UNSET
    if not isinstance(plan_date, Unset):
        json_plan_date = plan_date.isoformat()
    params["planDate"] = json_plan_date


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/dms/daily-plans/unassigned-employees",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[UnassignedEmployeeDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = UnassignedEmployeeDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[UnassignedEmployeeDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    plan_date: datetime.date | Unset = UNSET,

) -> Response[list[UnassignedEmployeeDto]]:
    """ Nhân viên chưa có kế hoạch ngày

     Lấy danh sách nhân viên field (SalesRep, DeliveryStaff, Merchandiser) chưa có kế hoạch ngày cho ngày
    chỉ định.

    Args:
        plan_date (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[UnassignedEmployeeDto]]
     """


    kwargs = _get_kwargs(
        plan_date=plan_date,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    plan_date: datetime.date | Unset = UNSET,

) -> list[UnassignedEmployeeDto] | None:
    """ Nhân viên chưa có kế hoạch ngày

     Lấy danh sách nhân viên field (SalesRep, DeliveryStaff, Merchandiser) chưa có kế hoạch ngày cho ngày
    chỉ định.

    Args:
        plan_date (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[UnassignedEmployeeDto]
     """


    return sync_detailed(
        client=client,
plan_date=plan_date,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    plan_date: datetime.date | Unset = UNSET,

) -> Response[list[UnassignedEmployeeDto]]:
    """ Nhân viên chưa có kế hoạch ngày

     Lấy danh sách nhân viên field (SalesRep, DeliveryStaff, Merchandiser) chưa có kế hoạch ngày cho ngày
    chỉ định.

    Args:
        plan_date (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[UnassignedEmployeeDto]]
     """


    kwargs = _get_kwargs(
        plan_date=plan_date,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    plan_date: datetime.date | Unset = UNSET,

) -> list[UnassignedEmployeeDto] | None:
    """ Nhân viên chưa có kế hoạch ngày

     Lấy danh sách nhân viên field (SalesRep, DeliveryStaff, Merchandiser) chưa có kế hoạch ngày cho ngày
    chỉ định.

    Args:
        plan_date (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[UnassignedEmployeeDto]
     """


    return (await asyncio_detailed(
        client=client,
plan_date=plan_date,

    )).parsed

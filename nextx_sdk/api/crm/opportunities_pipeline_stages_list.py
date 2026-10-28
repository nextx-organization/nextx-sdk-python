from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.pipeline_stage_dto import PipelineStageDto
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    pipeline_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_pipeline_id: str | Unset = UNSET
    if not isinstance(pipeline_id, Unset):
        json_pipeline_id = str(pipeline_id)
    params["pipelineId"] = json_pipeline_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/crm/opportunities/pipeline-stages",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[PipelineStageDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = PipelineStageDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[PipelineStageDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    pipeline_id: UUID | Unset = UNSET,

) -> Response[list[PipelineStageDto]]:
    """ Danh sách giai đoạn pipeline (chỉ đọc)

     Cùng dữ liệu với GET /settings/pipeline-stages nhưng chỉ cần quyền xem cơ hội. Nhân viên bán hàng
    không có crm.settings.manage nên không gọi được endpoint kia.

    Args:
        pipeline_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[PipelineStageDto]]
     """


    kwargs = _get_kwargs(
        pipeline_id=pipeline_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    pipeline_id: UUID | Unset = UNSET,

) -> list[PipelineStageDto] | None:
    """ Danh sách giai đoạn pipeline (chỉ đọc)

     Cùng dữ liệu với GET /settings/pipeline-stages nhưng chỉ cần quyền xem cơ hội. Nhân viên bán hàng
    không có crm.settings.manage nên không gọi được endpoint kia.

    Args:
        pipeline_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[PipelineStageDto]
     """


    return sync_detailed(
        client=client,
pipeline_id=pipeline_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    pipeline_id: UUID | Unset = UNSET,

) -> Response[list[PipelineStageDto]]:
    """ Danh sách giai đoạn pipeline (chỉ đọc)

     Cùng dữ liệu với GET /settings/pipeline-stages nhưng chỉ cần quyền xem cơ hội. Nhân viên bán hàng
    không có crm.settings.manage nên không gọi được endpoint kia.

    Args:
        pipeline_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[PipelineStageDto]]
     """


    kwargs = _get_kwargs(
        pipeline_id=pipeline_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    pipeline_id: UUID | Unset = UNSET,

) -> list[PipelineStageDto] | None:
    """ Danh sách giai đoạn pipeline (chỉ đọc)

     Cùng dữ liệu với GET /settings/pipeline-stages nhưng chỉ cần quyền xem cơ hội. Nhân viên bán hàng
    không có crm.settings.manage nên không gọi được endpoint kia.

    Args:
        pipeline_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[PipelineStageDto]
     """


    return (await asyncio_detailed(
        client=client,
pipeline_id=pipeline_id,

    )).parsed

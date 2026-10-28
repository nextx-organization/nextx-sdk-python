from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.products_export_get_attr import ProductsExportGetAttr
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    format_: str | Unset = 'XLSX',
    search: str | Unset = UNSET,
    category_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    product_ids: list[UUID] | Unset = UNSET,
    brand_id: UUID | Unset = UNSET,
    supplier_id: UUID | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    product_type: str | Unset = UNSET,
    tracking_type: str | Unset = UNSET,
    stock_view: str | Unset = UNSET,
    attr: ProductsExportGetAttr | Unset = UNSET,
    report_type: str | Unset = 'PRODUCT_LIST',
    columns: list[str] | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["format"] = format_

    params["search"] = search

    json_category_id: str | Unset = UNSET
    if not isinstance(category_id, Unset):
        json_category_id = str(category_id)
    params["categoryId"] = json_category_id

    params["status"] = status

    json_product_ids: list[str] | Unset = UNSET
    if not isinstance(product_ids, Unset):
        json_product_ids = []
        for product_ids_item_data in product_ids:
            product_ids_item = str(product_ids_item_data)
            json_product_ids.append(product_ids_item)


    params["productIds"] = json_product_ids

    json_brand_id: str | Unset = UNSET
    if not isinstance(brand_id, Unset):
        json_brand_id = str(brand_id)
    params["brandId"] = json_brand_id

    json_supplier_id: str | Unset = UNSET
    if not isinstance(supplier_id, Unset):
        json_supplier_id = str(supplier_id)
    params["supplierId"] = json_supplier_id

    json_branch_id: str | Unset = UNSET
    if not isinstance(branch_id, Unset):
        json_branch_id = str(branch_id)
    params["branchId"] = json_branch_id

    params["productType"] = product_type

    params["trackingType"] = tracking_type

    params["stockView"] = stock_view

    json_attr: dict[str, Any] | Unset = UNSET
    if not isinstance(attr, Unset):
        json_attr = attr.to_dict()
    if not isinstance(json_attr, Unset):
        params.update(json_attr)


    params["reportType"] = report_type

    json_columns: list[str] | Unset = UNSET
    if not isinstance(columns, Unset):
        json_columns = columns


    params["columns"] = json_columns


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sales/products/export",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 202:
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
    format_: str | Unset = 'XLSX',
    search: str | Unset = UNSET,
    category_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    product_ids: list[UUID] | Unset = UNSET,
    brand_id: UUID | Unset = UNSET,
    supplier_id: UUID | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    product_type: str | Unset = UNSET,
    tracking_type: str | Unset = UNSET,
    stock_view: str | Unset = UNSET,
    attr: ProductsExportGetAttr | Unset = UNSET,
    report_type: str | Unset = 'PRODUCT_LIST',
    columns: list[str] | Unset = UNSET,

) -> Response[Any]:
    """ Export danh sách sản phẩm

     Async export. Trả về jobId để poll trạng thái.

    Args:
        format_ (str | Unset):  Default: 'XLSX'.
        search (str | Unset):
        category_id (UUID | Unset):
        status (str | Unset):
        product_ids (list[UUID] | Unset):
        brand_id (UUID | Unset):
        supplier_id (UUID | Unset):
        branch_id (UUID | Unset):
        product_type (str | Unset):
        tracking_type (str | Unset):
        stock_view (str | Unset):
        attr (ProductsExportGetAttr | Unset):
        report_type (str | Unset):  Default: 'PRODUCT_LIST'.
        columns (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        format_=format_,
search=search,
category_id=category_id,
status=status,
product_ids=product_ids,
brand_id=brand_id,
supplier_id=supplier_id,
branch_id=branch_id,
product_type=product_type,
tracking_type=tracking_type,
stock_view=stock_view,
attr=attr,
report_type=report_type,
columns=columns,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    format_: str | Unset = 'XLSX',
    search: str | Unset = UNSET,
    category_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    product_ids: list[UUID] | Unset = UNSET,
    brand_id: UUID | Unset = UNSET,
    supplier_id: UUID | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    product_type: str | Unset = UNSET,
    tracking_type: str | Unset = UNSET,
    stock_view: str | Unset = UNSET,
    attr: ProductsExportGetAttr | Unset = UNSET,
    report_type: str | Unset = 'PRODUCT_LIST',
    columns: list[str] | Unset = UNSET,

) -> Response[Any]:
    """ Export danh sách sản phẩm

     Async export. Trả về jobId để poll trạng thái.

    Args:
        format_ (str | Unset):  Default: 'XLSX'.
        search (str | Unset):
        category_id (UUID | Unset):
        status (str | Unset):
        product_ids (list[UUID] | Unset):
        brand_id (UUID | Unset):
        supplier_id (UUID | Unset):
        branch_id (UUID | Unset):
        product_type (str | Unset):
        tracking_type (str | Unset):
        stock_view (str | Unset):
        attr (ProductsExportGetAttr | Unset):
        report_type (str | Unset):  Default: 'PRODUCT_LIST'.
        columns (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        format_=format_,
search=search,
category_id=category_id,
status=status,
product_ids=product_ids,
brand_id=brand_id,
supplier_id=supplier_id,
branch_id=branch_id,
product_type=product_type,
tracking_type=tracking_type,
stock_view=stock_view,
attr=attr,
report_type=report_type,
columns=columns,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)


from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.product_list_result import ProductListResult
from ...models.products_list_attr import ProductsListAttr
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    status: str | Unset = UNSET,
    category_id: UUID | Unset = UNSET,
    product_type: str | Unset = UNSET,
    tracking_type: str | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 50,
    stock_view: str | Unset = UNSET,
    attr: ProductsListAttr | Unset = UNSET,
    is_sold_directly: bool | Unset = UNSET,
    supplier_id: UUID | Unset = UNSET,
    brand_id: UUID | Unset = UNSET,
    price_from: float | Unset = UNSET,
    price_to: float | Unset = UNSET,
    stock_from: float | Unset = UNSET,
    stock_to: float | Unset = UNSET,
    sort_dir: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["status"] = status

    json_category_id: str | Unset = UNSET
    if not isinstance(category_id, Unset):
        json_category_id = str(category_id)
    params["categoryId"] = json_category_id

    params["productType"] = product_type

    params["trackingType"] = tracking_type

    params["search"] = search

    params["sortBy"] = sort_by

    json_branch_id: str | Unset = UNSET
    if not isinstance(branch_id, Unset):
        json_branch_id = str(branch_id)
    params["branchId"] = json_branch_id

    params["pageNumber"] = page_number

    params["pageSize"] = page_size

    params["stockView"] = stock_view

    json_attr: dict[str, Any] | Unset = UNSET
    if not isinstance(attr, Unset):
        json_attr = attr.to_dict()
    if not isinstance(json_attr, Unset):
        params.update(json_attr)


    params["isSoldDirectly"] = is_sold_directly

    json_supplier_id: str | Unset = UNSET
    if not isinstance(supplier_id, Unset):
        json_supplier_id = str(supplier_id)
    params["supplierId"] = json_supplier_id

    json_brand_id: str | Unset = UNSET
    if not isinstance(brand_id, Unset):
        json_brand_id = str(brand_id)
    params["brandId"] = json_brand_id

    params["priceFrom"] = price_from

    params["priceTo"] = price_to

    params["stockFrom"] = stock_from

    params["stockTo"] = stock_to

    params["sortDir"] = sort_dir


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sales/products",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ProductListResult | None:
    if response.status_code == 200:
        response_200 = ProductListResult.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ProductListResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    category_id: UUID | Unset = UNSET,
    product_type: str | Unset = UNSET,
    tracking_type: str | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 50,
    stock_view: str | Unset = UNSET,
    attr: ProductsListAttr | Unset = UNSET,
    is_sold_directly: bool | Unset = UNSET,
    supplier_id: UUID | Unset = UNSET,
    brand_id: UUID | Unset = UNSET,
    price_from: float | Unset = UNSET,
    price_to: float | Unset = UNSET,
    stock_from: float | Unset = UNSET,
    stock_to: float | Unset = UNSET,
    sort_dir: str | Unset = UNSET,

) -> Response[ProductListResult]:
    """ Danh sách sản phẩm

     Hỗ trợ filter theo status, category, type. Tìm kiếm theo tên (partial) hoặc SKU (exact).

    Args:
        status (str | Unset):
        category_id (UUID | Unset):
        product_type (str | Unset):
        tracking_type (str | Unset):
        search (str | Unset):
        sort_by (str | Unset):
        branch_id (UUID | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        stock_view (str | Unset):
        attr (ProductsListAttr | Unset):
        is_sold_directly (bool | Unset):
        supplier_id (UUID | Unset):
        brand_id (UUID | Unset):
        price_from (float | Unset):
        price_to (float | Unset):
        stock_from (float | Unset):
        stock_to (float | Unset):
        sort_dir (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProductListResult]
     """


    kwargs = _get_kwargs(
        status=status,
category_id=category_id,
product_type=product_type,
tracking_type=tracking_type,
search=search,
sort_by=sort_by,
branch_id=branch_id,
page_number=page_number,
page_size=page_size,
stock_view=stock_view,
attr=attr,
is_sold_directly=is_sold_directly,
supplier_id=supplier_id,
brand_id=brand_id,
price_from=price_from,
price_to=price_to,
stock_from=stock_from,
stock_to=stock_to,
sort_dir=sort_dir,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    category_id: UUID | Unset = UNSET,
    product_type: str | Unset = UNSET,
    tracking_type: str | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 50,
    stock_view: str | Unset = UNSET,
    attr: ProductsListAttr | Unset = UNSET,
    is_sold_directly: bool | Unset = UNSET,
    supplier_id: UUID | Unset = UNSET,
    brand_id: UUID | Unset = UNSET,
    price_from: float | Unset = UNSET,
    price_to: float | Unset = UNSET,
    stock_from: float | Unset = UNSET,
    stock_to: float | Unset = UNSET,
    sort_dir: str | Unset = UNSET,

) -> ProductListResult | None:
    """ Danh sách sản phẩm

     Hỗ trợ filter theo status, category, type. Tìm kiếm theo tên (partial) hoặc SKU (exact).

    Args:
        status (str | Unset):
        category_id (UUID | Unset):
        product_type (str | Unset):
        tracking_type (str | Unset):
        search (str | Unset):
        sort_by (str | Unset):
        branch_id (UUID | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        stock_view (str | Unset):
        attr (ProductsListAttr | Unset):
        is_sold_directly (bool | Unset):
        supplier_id (UUID | Unset):
        brand_id (UUID | Unset):
        price_from (float | Unset):
        price_to (float | Unset):
        stock_from (float | Unset):
        stock_to (float | Unset):
        sort_dir (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProductListResult
     """


    return sync_detailed(
        client=client,
status=status,
category_id=category_id,
product_type=product_type,
tracking_type=tracking_type,
search=search,
sort_by=sort_by,
branch_id=branch_id,
page_number=page_number,
page_size=page_size,
stock_view=stock_view,
attr=attr,
is_sold_directly=is_sold_directly,
supplier_id=supplier_id,
brand_id=brand_id,
price_from=price_from,
price_to=price_to,
stock_from=stock_from,
stock_to=stock_to,
sort_dir=sort_dir,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    category_id: UUID | Unset = UNSET,
    product_type: str | Unset = UNSET,
    tracking_type: str | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 50,
    stock_view: str | Unset = UNSET,
    attr: ProductsListAttr | Unset = UNSET,
    is_sold_directly: bool | Unset = UNSET,
    supplier_id: UUID | Unset = UNSET,
    brand_id: UUID | Unset = UNSET,
    price_from: float | Unset = UNSET,
    price_to: float | Unset = UNSET,
    stock_from: float | Unset = UNSET,
    stock_to: float | Unset = UNSET,
    sort_dir: str | Unset = UNSET,

) -> Response[ProductListResult]:
    """ Danh sách sản phẩm

     Hỗ trợ filter theo status, category, type. Tìm kiếm theo tên (partial) hoặc SKU (exact).

    Args:
        status (str | Unset):
        category_id (UUID | Unset):
        product_type (str | Unset):
        tracking_type (str | Unset):
        search (str | Unset):
        sort_by (str | Unset):
        branch_id (UUID | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        stock_view (str | Unset):
        attr (ProductsListAttr | Unset):
        is_sold_directly (bool | Unset):
        supplier_id (UUID | Unset):
        brand_id (UUID | Unset):
        price_from (float | Unset):
        price_to (float | Unset):
        stock_from (float | Unset):
        stock_to (float | Unset):
        sort_dir (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProductListResult]
     """


    kwargs = _get_kwargs(
        status=status,
category_id=category_id,
product_type=product_type,
tracking_type=tracking_type,
search=search,
sort_by=sort_by,
branch_id=branch_id,
page_number=page_number,
page_size=page_size,
stock_view=stock_view,
attr=attr,
is_sold_directly=is_sold_directly,
supplier_id=supplier_id,
brand_id=brand_id,
price_from=price_from,
price_to=price_to,
stock_from=stock_from,
stock_to=stock_to,
sort_dir=sort_dir,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    category_id: UUID | Unset = UNSET,
    product_type: str | Unset = UNSET,
    tracking_type: str | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    page_number: int | Unset = 1,
    page_size: int | Unset = 50,
    stock_view: str | Unset = UNSET,
    attr: ProductsListAttr | Unset = UNSET,
    is_sold_directly: bool | Unset = UNSET,
    supplier_id: UUID | Unset = UNSET,
    brand_id: UUID | Unset = UNSET,
    price_from: float | Unset = UNSET,
    price_to: float | Unset = UNSET,
    stock_from: float | Unset = UNSET,
    stock_to: float | Unset = UNSET,
    sort_dir: str | Unset = UNSET,

) -> ProductListResult | None:
    """ Danh sách sản phẩm

     Hỗ trợ filter theo status, category, type. Tìm kiếm theo tên (partial) hoặc SKU (exact).

    Args:
        status (str | Unset):
        category_id (UUID | Unset):
        product_type (str | Unset):
        tracking_type (str | Unset):
        search (str | Unset):
        sort_by (str | Unset):
        branch_id (UUID | Unset):
        page_number (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        stock_view (str | Unset):
        attr (ProductsListAttr | Unset):
        is_sold_directly (bool | Unset):
        supplier_id (UUID | Unset):
        brand_id (UUID | Unset):
        price_from (float | Unset):
        price_to (float | Unset):
        stock_from (float | Unset):
        stock_to (float | Unset):
        sort_dir (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProductListResult
     """


    return (await asyncio_detailed(
        client=client,
status=status,
category_id=category_id,
product_type=product_type,
tracking_type=tracking_type,
search=search,
sort_by=sort_by,
branch_id=branch_id,
page_number=page_number,
page_size=page_size,
stock_view=stock_view,
attr=attr,
is_sold_directly=is_sold_directly,
supplier_id=supplier_id,
brand_id=brand_id,
price_from=price_from,
price_to=price_to,
stock_from=stock_from,
stock_to=stock_to,
sort_dir=sort_dir,

    )).parsed

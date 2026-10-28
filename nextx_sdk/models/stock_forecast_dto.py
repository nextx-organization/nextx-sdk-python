from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="StockForecastDto")



@_attrs_define
class StockForecastDto:
    

    product_id: UUID | Unset = UNSET
    product_code: None | str | Unset = UNSET
    product_name: None | str | Unset = UNSET
    image_url: None | str | Unset = UNSET
    current_stock: float | Unset = UNSET
    avg_daily_sales: float | Unset = UNSET
    days_until_stockout: int | None | Unset = UNSET
    stock_status: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        product_id: str | Unset = UNSET
        if not isinstance(self.product_id, Unset):
            product_id = str(self.product_id)

        product_code: None | str | Unset
        if isinstance(self.product_code, Unset):
            product_code = UNSET
        else:
            product_code = self.product_code

        product_name: None | str | Unset
        if isinstance(self.product_name, Unset):
            product_name = UNSET
        else:
            product_name = self.product_name

        image_url: None | str | Unset
        if isinstance(self.image_url, Unset):
            image_url = UNSET
        else:
            image_url = self.image_url

        current_stock = self.current_stock

        avg_daily_sales = self.avg_daily_sales

        days_until_stockout: int | None | Unset
        if isinstance(self.days_until_stockout, Unset):
            days_until_stockout = UNSET
        else:
            days_until_stockout = self.days_until_stockout

        stock_status: None | str | Unset
        if isinstance(self.stock_status, Unset):
            stock_status = UNSET
        else:
            stock_status = self.stock_status


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if product_code is not UNSET:
            field_dict["productCode"] = product_code
        if product_name is not UNSET:
            field_dict["productName"] = product_name
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if current_stock is not UNSET:
            field_dict["currentStock"] = current_stock
        if avg_daily_sales is not UNSET:
            field_dict["avgDailySales"] = avg_daily_sales
        if days_until_stockout is not UNSET:
            field_dict["daysUntilStockout"] = days_until_stockout
        if stock_status is not UNSET:
            field_dict["stockStatus"] = stock_status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _product_id = d.pop("productId", UNSET)
        product_id: UUID | Unset
        if isinstance(_product_id,  Unset):
            product_id = UNSET
        else:
            product_id = UUID(_product_id)




        def _parse_product_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_code = _parse_product_code(d.pop("productCode", UNSET))


        def _parse_product_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_name = _parse_product_name(d.pop("productName", UNSET))


        def _parse_image_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_url = _parse_image_url(d.pop("imageUrl", UNSET))


        current_stock = d.pop("currentStock", UNSET)

        avg_daily_sales = d.pop("avgDailySales", UNSET)

        def _parse_days_until_stockout(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        days_until_stockout = _parse_days_until_stockout(d.pop("daysUntilStockout", UNSET))


        def _parse_stock_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stock_status = _parse_stock_status(d.pop("stockStatus", UNSET))


        stock_forecast_dto = cls(
            product_id=product_id,
            product_code=product_code,
            product_name=product_name,
            image_url=image_url,
            current_stock=current_stock,
            avg_daily_sales=avg_daily_sales,
            days_until_stockout=days_until_stockout,
            stock_status=stock_status,
        )

        return stock_forecast_dto


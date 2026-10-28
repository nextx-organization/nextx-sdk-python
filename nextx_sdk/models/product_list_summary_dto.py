from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ProductListSummaryDto")



@_attrs_define
class ProductListSummaryDto:
    

    total_stock: float | Unset = UNSET
    total_reserved: float | Unset = UNSET
    total_stock_value_cost: float | Unset = UNSET
    total_stock_value_price: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        total_stock = self.total_stock

        total_reserved = self.total_reserved

        total_stock_value_cost = self.total_stock_value_cost

        total_stock_value_price = self.total_stock_value_price


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if total_stock is not UNSET:
            field_dict["totalStock"] = total_stock
        if total_reserved is not UNSET:
            field_dict["totalReserved"] = total_reserved
        if total_stock_value_cost is not UNSET:
            field_dict["totalStockValueCost"] = total_stock_value_cost
        if total_stock_value_price is not UNSET:
            field_dict["totalStockValuePrice"] = total_stock_value_price

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_stock = d.pop("totalStock", UNSET)

        total_reserved = d.pop("totalReserved", UNSET)

        total_stock_value_cost = d.pop("totalStockValueCost", UNSET)

        total_stock_value_price = d.pop("totalStockValuePrice", UNSET)

        product_list_summary_dto = cls(
            total_stock=total_stock,
            total_reserved=total_reserved,
            total_stock_value_cost=total_stock_value_cost,
            total_stock_value_price=total_stock_value_price,
        )

        return product_list_summary_dto


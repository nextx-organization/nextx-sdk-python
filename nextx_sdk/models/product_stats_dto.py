from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ProductStatsDto")



@_attrs_define
class ProductStatsDto:
    

    total_products: int | Unset = UNSET
    active_products: int | Unset = UNSET
    variant_products: int | Unset = UNSET
    low_stock_products: int | Unset = UNSET
    total_quantity: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        total_products = self.total_products

        active_products = self.active_products

        variant_products = self.variant_products

        low_stock_products = self.low_stock_products

        total_quantity = self.total_quantity


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if total_products is not UNSET:
            field_dict["totalProducts"] = total_products
        if active_products is not UNSET:
            field_dict["activeProducts"] = active_products
        if variant_products is not UNSET:
            field_dict["variantProducts"] = variant_products
        if low_stock_products is not UNSET:
            field_dict["lowStockProducts"] = low_stock_products
        if total_quantity is not UNSET:
            field_dict["totalQuantity"] = total_quantity

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_products = d.pop("totalProducts", UNSET)

        active_products = d.pop("activeProducts", UNSET)

        variant_products = d.pop("variantProducts", UNSET)

        low_stock_products = d.pop("lowStockProducts", UNSET)

        total_quantity = d.pop("totalQuantity", UNSET)

        product_stats_dto = cls(
            total_products=total_products,
            active_products=active_products,
            variant_products=variant_products,
            low_stock_products=low_stock_products,
            total_quantity=total_quantity,
        )

        return product_stats_dto


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="InventoryItemDto")



@_attrs_define
class InventoryItemDto:
    

    product_id: UUID | Unset = UNSET
    sku: None | str | Unset = UNSET
    product_name: None | str | Unset = UNSET
    product_type: None | str | Unset = UNSET
    qty_on_hand: float | Unset = UNSET
    qty_reserved: float | Unset = UNSET
    qty_available: float | Unset = UNSET
    avg_cost: int | Unset = UNSET
    unit_name: None | str | Unset = UNSET
    stock_status: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        product_id: str | Unset = UNSET
        if not isinstance(self.product_id, Unset):
            product_id = str(self.product_id)

        sku: None | str | Unset
        if isinstance(self.sku, Unset):
            sku = UNSET
        else:
            sku = self.sku

        product_name: None | str | Unset
        if isinstance(self.product_name, Unset):
            product_name = UNSET
        else:
            product_name = self.product_name

        product_type: None | str | Unset
        if isinstance(self.product_type, Unset):
            product_type = UNSET
        else:
            product_type = self.product_type

        qty_on_hand = self.qty_on_hand

        qty_reserved = self.qty_reserved

        qty_available = self.qty_available

        avg_cost = self.avg_cost

        unit_name: None | str | Unset
        if isinstance(self.unit_name, Unset):
            unit_name = UNSET
        else:
            unit_name = self.unit_name

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
        if sku is not UNSET:
            field_dict["sku"] = sku
        if product_name is not UNSET:
            field_dict["productName"] = product_name
        if product_type is not UNSET:
            field_dict["productType"] = product_type
        if qty_on_hand is not UNSET:
            field_dict["qtyOnHand"] = qty_on_hand
        if qty_reserved is not UNSET:
            field_dict["qtyReserved"] = qty_reserved
        if qty_available is not UNSET:
            field_dict["qtyAvailable"] = qty_available
        if avg_cost is not UNSET:
            field_dict["avgCost"] = avg_cost
        if unit_name is not UNSET:
            field_dict["unitName"] = unit_name
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




        def _parse_sku(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sku = _parse_sku(d.pop("sku", UNSET))


        def _parse_product_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_name = _parse_product_name(d.pop("productName", UNSET))


        def _parse_product_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_type = _parse_product_type(d.pop("productType", UNSET))


        qty_on_hand = d.pop("qtyOnHand", UNSET)

        qty_reserved = d.pop("qtyReserved", UNSET)

        qty_available = d.pop("qtyAvailable", UNSET)

        avg_cost = d.pop("avgCost", UNSET)

        def _parse_unit_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit_name = _parse_unit_name(d.pop("unitName", UNSET))


        def _parse_stock_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stock_status = _parse_stock_status(d.pop("stockStatus", UNSET))


        inventory_item_dto = cls(
            product_id=product_id,
            sku=sku,
            product_name=product_name,
            product_type=product_type,
            qty_on_hand=qty_on_hand,
            qty_reserved=qty_reserved,
            qty_available=qty_available,
            avg_cost=avg_cost,
            unit_name=unit_name,
            stock_status=stock_status,
        )

        return inventory_item_dto


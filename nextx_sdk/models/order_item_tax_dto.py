from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OrderItemTaxDto")



@_attrs_define
class OrderItemTaxDto:
    

    rate: float | Unset = UNSET
    amount: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        rate = self.rate

        amount = self.amount


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if rate is not UNSET:
            field_dict["rate"] = rate
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rate = d.pop("rate", UNSET)

        amount = d.pop("amount", UNSET)

        order_item_tax_dto = cls(
            rate=rate,
            amount=amount,
        )

        return order_item_tax_dto


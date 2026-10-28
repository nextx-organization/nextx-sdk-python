from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OrderItemDiscountDto")



@_attrs_define
class OrderItemDiscountDto:
    

    type_: None | str | Unset = UNSET
    rate: float | None | Unset = UNSET
    amount: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        rate: float | None | Unset
        if isinstance(self.rate, Unset):
            rate = UNSET
        else:
            rate = self.rate

        amount = self.amount


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if rate is not UNSET:
            field_dict["rate"] = rate
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))


        def _parse_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        rate = _parse_rate(d.pop("rate", UNSET))


        amount = d.pop("amount", UNSET)

        order_item_discount_dto = cls(
            type_=type_,
            rate=rate,
            amount=amount,
        )

        return order_item_discount_dto


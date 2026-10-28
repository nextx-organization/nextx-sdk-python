from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OrderVatDto")



@_attrs_define
class OrderVatDto:
    

    percent: float | None | Unset = UNSET
    included: bool | Unset = UNSET
    mode: None | str | Unset = UNSET
    amount: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        percent: float | None | Unset
        if isinstance(self.percent, Unset):
            percent = UNSET
        else:
            percent = self.percent

        included = self.included

        mode: None | str | Unset
        if isinstance(self.mode, Unset):
            mode = UNSET
        else:
            mode = self.mode

        amount = self.amount


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if percent is not UNSET:
            field_dict["percent"] = percent
        if included is not UNSET:
            field_dict["included"] = included
        if mode is not UNSET:
            field_dict["mode"] = mode
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        percent = _parse_percent(d.pop("percent", UNSET))


        included = d.pop("included", UNSET)

        def _parse_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mode = _parse_mode(d.pop("mode", UNSET))


        amount = d.pop("amount", UNSET)

        order_vat_dto = cls(
            percent=percent,
            included=included,
            mode=mode,
            amount=amount,
        )

        return order_vat_dto


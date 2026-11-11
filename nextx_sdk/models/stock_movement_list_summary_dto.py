from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="StockMovementListSummaryDto")



@_attrs_define
class StockMovementListSummaryDto:
    

    total_in: float | Unset = UNSET
    total_out: float | Unset = UNSET
    total_value: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        total_in = self.total_in

        total_out = self.total_out

        total_value = self.total_value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if total_in is not UNSET:
            field_dict["totalIn"] = total_in
        if total_out is not UNSET:
            field_dict["totalOut"] = total_out
        if total_value is not UNSET:
            field_dict["totalValue"] = total_value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_in = d.pop("totalIn", UNSET)

        total_out = d.pop("totalOut", UNSET)

        total_value = d.pop("totalValue", UNSET)

        stock_movement_list_summary_dto = cls(
            total_in=total_in,
            total_out=total_out,
            total_value=total_value,
        )

        return stock_movement_list_summary_dto


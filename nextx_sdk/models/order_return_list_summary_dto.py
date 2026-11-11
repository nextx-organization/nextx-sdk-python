from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OrderReturnListSummaryDto")



@_attrs_define
class OrderReturnListSummaryDto:
    

    total_refund: float | Unset = UNSET
    total_grand_total: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        total_refund = self.total_refund

        total_grand_total = self.total_grand_total


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if total_refund is not UNSET:
            field_dict["totalRefund"] = total_refund
        if total_grand_total is not UNSET:
            field_dict["totalGrandTotal"] = total_grand_total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_refund = d.pop("totalRefund", UNSET)

        total_grand_total = d.pop("totalGrandTotal", UNSET)

        order_return_list_summary_dto = cls(
            total_refund=total_refund,
            total_grand_total=total_grand_total,
        )

        return order_return_list_summary_dto


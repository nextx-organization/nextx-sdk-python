from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GoodsReceiptListSummaryDto")



@_attrs_define
class GoodsReceiptListSummaryDto:
    

    total_amount: float | Unset = UNSET
    total_import_cost: float | Unset = UNSET
    total_paid: float | Unset = UNSET
    total_debt: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        total_amount = self.total_amount

        total_import_cost = self.total_import_cost

        total_paid = self.total_paid

        total_debt = self.total_debt


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if total_import_cost is not UNSET:
            field_dict["totalImportCost"] = total_import_cost
        if total_paid is not UNSET:
            field_dict["totalPaid"] = total_paid
        if total_debt is not UNSET:
            field_dict["totalDebt"] = total_debt

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_amount = d.pop("totalAmount", UNSET)

        total_import_cost = d.pop("totalImportCost", UNSET)

        total_paid = d.pop("totalPaid", UNSET)

        total_debt = d.pop("totalDebt", UNSET)

        goods_receipt_list_summary_dto = cls(
            total_amount=total_amount,
            total_import_cost=total_import_cost,
            total_paid=total_paid,
            total_debt=total_debt,
        )

        return goods_receipt_list_summary_dto


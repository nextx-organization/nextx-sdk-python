from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OrderStatsDto")



@_attrs_define
class OrderStatsDto:
    

    pending: int | Unset = UNSET
    processing: int | Unset = UNSET
    completed: int | Unset = UNSET
    cancelled: int | Unset = UNSET
    total_amount: float | Unset = UNSET
    paid_amount: float | Unset = UNSET
    debt_amount: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        pending = self.pending

        processing = self.processing

        completed = self.completed

        cancelled = self.cancelled

        total_amount = self.total_amount

        paid_amount = self.paid_amount

        debt_amount = self.debt_amount


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if pending is not UNSET:
            field_dict["pending"] = pending
        if processing is not UNSET:
            field_dict["processing"] = processing
        if completed is not UNSET:
            field_dict["completed"] = completed
        if cancelled is not UNSET:
            field_dict["cancelled"] = cancelled
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if paid_amount is not UNSET:
            field_dict["paidAmount"] = paid_amount
        if debt_amount is not UNSET:
            field_dict["debtAmount"] = debt_amount

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pending = d.pop("pending", UNSET)

        processing = d.pop("processing", UNSET)

        completed = d.pop("completed", UNSET)

        cancelled = d.pop("cancelled", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        paid_amount = d.pop("paidAmount", UNSET)

        debt_amount = d.pop("debtAmount", UNSET)

        order_stats_dto = cls(
            pending=pending,
            processing=processing,
            completed=completed,
            cancelled=cancelled,
            total_amount=total_amount,
            paid_amount=paid_amount,
            debt_amount=debt_amount,
        )

        return order_stats_dto


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OrderListSummaryDto")



@_attrs_define
class OrderListSummaryDto:
    

    subtotal: float | Unset = UNSET
    discount_amount: float | Unset = UNSET
    tax_amount: float | Unset = UNSET
    total_amount: float | Unset = UNSET
    total_paid: float | Unset = UNSET
    total_debt: float | Unset = UNSET
    total_quantity: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        subtotal = self.subtotal

        discount_amount = self.discount_amount

        tax_amount = self.tax_amount

        total_amount = self.total_amount

        total_paid = self.total_paid

        total_debt = self.total_debt

        total_quantity = self.total_quantity


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if subtotal is not UNSET:
            field_dict["subtotal"] = subtotal
        if discount_amount is not UNSET:
            field_dict["discountAmount"] = discount_amount
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if total_paid is not UNSET:
            field_dict["totalPaid"] = total_paid
        if total_debt is not UNSET:
            field_dict["totalDebt"] = total_debt
        if total_quantity is not UNSET:
            field_dict["totalQuantity"] = total_quantity

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subtotal = d.pop("subtotal", UNSET)

        discount_amount = d.pop("discountAmount", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        total_paid = d.pop("totalPaid", UNSET)

        total_debt = d.pop("totalDebt", UNSET)

        total_quantity = d.pop("totalQuantity", UNSET)

        order_list_summary_dto = cls(
            subtotal=subtotal,
            discount_amount=discount_amount,
            tax_amount=tax_amount,
            total_amount=total_amount,
            total_paid=total_paid,
            total_debt=total_debt,
            total_quantity=total_quantity,
        )

        return order_list_summary_dto


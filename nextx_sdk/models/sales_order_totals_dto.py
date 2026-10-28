from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SalesOrderTotalsDto")



@_attrs_define
class SalesOrderTotalsDto:
    

    subtotal: float | Unset = UNSET
    discount_amount: float | Unset = UNSET
    tax_amount: float | Unset = UNSET
    total: float | Unset = UNSET
    paid_amount: float | Unset = UNSET
    debt_amount: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        subtotal = self.subtotal

        discount_amount = self.discount_amount

        tax_amount = self.tax_amount

        total = self.total

        paid_amount = self.paid_amount

        debt_amount = self.debt_amount


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if subtotal is not UNSET:
            field_dict["subtotal"] = subtotal
        if discount_amount is not UNSET:
            field_dict["discountAmount"] = discount_amount
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if total is not UNSET:
            field_dict["total"] = total
        if paid_amount is not UNSET:
            field_dict["paidAmount"] = paid_amount
        if debt_amount is not UNSET:
            field_dict["debtAmount"] = debt_amount

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subtotal = d.pop("subtotal", UNSET)

        discount_amount = d.pop("discountAmount", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        total = d.pop("total", UNSET)

        paid_amount = d.pop("paidAmount", UNSET)

        debt_amount = d.pop("debtAmount", UNSET)

        sales_order_totals_dto = cls(
            subtotal=subtotal,
            discount_amount=discount_amount,
            tax_amount=tax_amount,
            total=total,
            paid_amount=paid_amount,
            debt_amount=debt_amount,
        )

        return sales_order_totals_dto


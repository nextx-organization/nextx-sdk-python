from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="InvoiceItemDto")



@_attrs_define
class InvoiceItemDto:
    

    id: UUID | Unset = UNSET
    line_number: int | Unset = UNSET
    product_code: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    unit: None | str | Unset = UNSET
    quantity: float | Unset = UNSET
    unit_price: float | Unset = UNSET
    discount_pct: float | Unset = UNSET
    line_subtotal: float | Unset = UNSET
    vat_rate: float | Unset = UNSET
    vat_amount: float | Unset = UNSET
    line_total: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        line_number = self.line_number

        product_code: None | str | Unset
        if isinstance(self.product_code, Unset):
            product_code = UNSET
        else:
            product_code = self.product_code

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        unit: None | str | Unset
        if isinstance(self.unit, Unset):
            unit = UNSET
        else:
            unit = self.unit

        quantity = self.quantity

        unit_price = self.unit_price

        discount_pct = self.discount_pct

        line_subtotal = self.line_subtotal

        vat_rate = self.vat_rate

        vat_amount = self.vat_amount

        line_total = self.line_total


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if line_number is not UNSET:
            field_dict["lineNumber"] = line_number
        if product_code is not UNSET:
            field_dict["productCode"] = product_code
        if description is not UNSET:
            field_dict["description"] = description
        if unit is not UNSET:
            field_dict["unit"] = unit
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if discount_pct is not UNSET:
            field_dict["discountPct"] = discount_pct
        if line_subtotal is not UNSET:
            field_dict["lineSubtotal"] = line_subtotal
        if vat_rate is not UNSET:
            field_dict["vatRate"] = vat_rate
        if vat_amount is not UNSET:
            field_dict["vatAmount"] = vat_amount
        if line_total is not UNSET:
            field_dict["lineTotal"] = line_total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        line_number = d.pop("lineNumber", UNSET)

        def _parse_product_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_code = _parse_product_code(d.pop("productCode", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit = _parse_unit(d.pop("unit", UNSET))


        quantity = d.pop("quantity", UNSET)

        unit_price = d.pop("unitPrice", UNSET)

        discount_pct = d.pop("discountPct", UNSET)

        line_subtotal = d.pop("lineSubtotal", UNSET)

        vat_rate = d.pop("vatRate", UNSET)

        vat_amount = d.pop("vatAmount", UNSET)

        line_total = d.pop("lineTotal", UNSET)

        invoice_item_dto = cls(
            id=id,
            line_number=line_number,
            product_code=product_code,
            description=description,
            unit=unit,
            quantity=quantity,
            unit_price=unit_price,
            discount_pct=discount_pct,
            line_subtotal=line_subtotal,
            vat_rate=vat_rate,
            vat_amount=vat_amount,
            line_total=line_total,
        )

        return invoice_item_dto


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="ProductUnitConversionDto")



@_attrs_define
class ProductUnitConversionDto:
    

    id: UUID | Unset = UNSET
    unit_id: UUID | Unset = UNSET
    unit_code: None | str | Unset = UNSET
    unit_name: None | str | Unset = UNSET
    conversion_to_base: float | Unset = UNSET
    is_base: bool | Unset = UNSET
    is_active: bool | Unset = UNSET
    selling_price: float | None | Unset = UNSET
    barcode: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        unit_id: str | Unset = UNSET
        if not isinstance(self.unit_id, Unset):
            unit_id = str(self.unit_id)

        unit_code: None | str | Unset
        if isinstance(self.unit_code, Unset):
            unit_code = UNSET
        else:
            unit_code = self.unit_code

        unit_name: None | str | Unset
        if isinstance(self.unit_name, Unset):
            unit_name = UNSET
        else:
            unit_name = self.unit_name

        conversion_to_base = self.conversion_to_base

        is_base = self.is_base

        is_active = self.is_active

        selling_price: float | None | Unset
        if isinstance(self.selling_price, Unset):
            selling_price = UNSET
        else:
            selling_price = self.selling_price

        barcode: None | str | Unset
        if isinstance(self.barcode, Unset):
            barcode = UNSET
        else:
            barcode = self.barcode


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if unit_id is not UNSET:
            field_dict["unitId"] = unit_id
        if unit_code is not UNSET:
            field_dict["unitCode"] = unit_code
        if unit_name is not UNSET:
            field_dict["unitName"] = unit_name
        if conversion_to_base is not UNSET:
            field_dict["conversionToBase"] = conversion_to_base
        if is_base is not UNSET:
            field_dict["isBase"] = is_base
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if selling_price is not UNSET:
            field_dict["sellingPrice"] = selling_price
        if barcode is not UNSET:
            field_dict["barcode"] = barcode

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




        _unit_id = d.pop("unitId", UNSET)
        unit_id: UUID | Unset
        if isinstance(_unit_id,  Unset):
            unit_id = UNSET
        else:
            unit_id = UUID(_unit_id)




        def _parse_unit_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit_code = _parse_unit_code(d.pop("unitCode", UNSET))


        def _parse_unit_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit_name = _parse_unit_name(d.pop("unitName", UNSET))


        conversion_to_base = d.pop("conversionToBase", UNSET)

        is_base = d.pop("isBase", UNSET)

        is_active = d.pop("isActive", UNSET)

        def _parse_selling_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        selling_price = _parse_selling_price(d.pop("sellingPrice", UNSET))


        def _parse_barcode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        barcode = _parse_barcode(d.pop("barcode", UNSET))


        product_unit_conversion_dto = cls(
            id=id,
            unit_id=unit_id,
            unit_code=unit_code,
            unit_name=unit_name,
            conversion_to_base=conversion_to_base,
            is_base=is_base,
            is_active=is_active,
            selling_price=selling_price,
            barcode=barcode,
        )

        return product_unit_conversion_dto


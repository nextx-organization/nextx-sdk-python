from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CatalogUnitConversionDto")



@_attrs_define
class CatalogUnitConversionDto:
    

    unit_code: None | str | Unset = UNSET
    unit_name: None | str | Unset = UNSET
    is_base: bool | Unset = UNSET
    conversion_to_base: float | Unset = UNSET
    selling_price: int | None | Unset = UNSET
    barcode: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
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

        is_base = self.is_base

        conversion_to_base = self.conversion_to_base

        selling_price: int | None | Unset
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
        if unit_code is not UNSET:
            field_dict["unitCode"] = unit_code
        if unit_name is not UNSET:
            field_dict["unitName"] = unit_name
        if is_base is not UNSET:
            field_dict["isBase"] = is_base
        if conversion_to_base is not UNSET:
            field_dict["conversionToBase"] = conversion_to_base
        if selling_price is not UNSET:
            field_dict["sellingPrice"] = selling_price
        if barcode is not UNSET:
            field_dict["barcode"] = barcode

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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


        is_base = d.pop("isBase", UNSET)

        conversion_to_base = d.pop("conversionToBase", UNSET)

        def _parse_selling_price(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        selling_price = _parse_selling_price(d.pop("sellingPrice", UNSET))


        def _parse_barcode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        barcode = _parse_barcode(d.pop("barcode", UNSET))


        catalog_unit_conversion_dto = cls(
            unit_code=unit_code,
            unit_name=unit_name,
            is_base=is_base,
            conversion_to_base=conversion_to_base,
            selling_price=selling_price,
            barcode=barcode,
        )

        return catalog_unit_conversion_dto


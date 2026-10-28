from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="CatalogProductVariantDto")



@_attrs_define
class CatalogProductVariantDto:
    

    variant_id: UUID | Unset = UNSET
    sku: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    current_price: float | Unset = UNSET
    qty_available: int | Unset = UNSET
    sku_id: None | str | Unset = UNSET
    barcode: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        variant_id: str | Unset = UNSET
        if not isinstance(self.variant_id, Unset):
            variant_id = str(self.variant_id)

        sku: None | str | Unset
        if isinstance(self.sku, Unset):
            sku = UNSET
        else:
            sku = self.sku

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        current_price = self.current_price

        qty_available = self.qty_available

        sku_id: None | str | Unset
        if isinstance(self.sku_id, Unset):
            sku_id = UNSET
        else:
            sku_id = self.sku_id

        barcode: None | str | Unset
        if isinstance(self.barcode, Unset):
            barcode = UNSET
        else:
            barcode = self.barcode


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if variant_id is not UNSET:
            field_dict["variantId"] = variant_id
        if sku is not UNSET:
            field_dict["sku"] = sku
        if name is not UNSET:
            field_dict["name"] = name
        if current_price is not UNSET:
            field_dict["currentPrice"] = current_price
        if qty_available is not UNSET:
            field_dict["qtyAvailable"] = qty_available
        if sku_id is not UNSET:
            field_dict["skuId"] = sku_id
        if barcode is not UNSET:
            field_dict["barcode"] = barcode

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _variant_id = d.pop("variantId", UNSET)
        variant_id: UUID | Unset
        if isinstance(_variant_id,  Unset):
            variant_id = UNSET
        else:
            variant_id = UUID(_variant_id)




        def _parse_sku(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sku = _parse_sku(d.pop("sku", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        current_price = d.pop("currentPrice", UNSET)

        qty_available = d.pop("qtyAvailable", UNSET)

        def _parse_sku_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sku_id = _parse_sku_id(d.pop("skuId", UNSET))


        def _parse_barcode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        barcode = _parse_barcode(d.pop("barcode", UNSET))


        catalog_product_variant_dto = cls(
            variant_id=variant_id,
            sku=sku,
            name=name,
            current_price=current_price,
            qty_available=qty_available,
            sku_id=sku_id,
            barcode=barcode,
        )

        return catalog_product_variant_dto


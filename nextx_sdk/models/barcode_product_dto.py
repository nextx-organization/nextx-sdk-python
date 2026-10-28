from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="BarcodeProductDto")



@_attrs_define
class BarcodeProductDto:
    

    id: UUID | Unset = UNSET
    code: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    image_url: None | str | Unset = UNSET
    tracking_type: None | str | Unset = UNSET
    selling_price: float | None | Unset = UNSET
    stock_quantity: float | None | Unset = UNSET
    barcode: None | str | Unset = UNSET
    tax_rate: float | None | Unset = UNSET
    unit_code: None | str | Unset = UNSET
    matched_unit_code: None | str | Unset = UNSET
    variant_id: None | Unset | UUID = UNSET
    sku_id: None | Unset | UUID = UNSET
    variant_name: None | str | Unset = UNSET
    variant_is_active: bool | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        image_url: None | str | Unset
        if isinstance(self.image_url, Unset):
            image_url = UNSET
        else:
            image_url = self.image_url

        tracking_type: None | str | Unset
        if isinstance(self.tracking_type, Unset):
            tracking_type = UNSET
        else:
            tracking_type = self.tracking_type

        selling_price: float | None | Unset
        if isinstance(self.selling_price, Unset):
            selling_price = UNSET
        else:
            selling_price = self.selling_price

        stock_quantity: float | None | Unset
        if isinstance(self.stock_quantity, Unset):
            stock_quantity = UNSET
        else:
            stock_quantity = self.stock_quantity

        barcode: None | str | Unset
        if isinstance(self.barcode, Unset):
            barcode = UNSET
        else:
            barcode = self.barcode

        tax_rate: float | None | Unset
        if isinstance(self.tax_rate, Unset):
            tax_rate = UNSET
        else:
            tax_rate = self.tax_rate

        unit_code: None | str | Unset
        if isinstance(self.unit_code, Unset):
            unit_code = UNSET
        else:
            unit_code = self.unit_code

        matched_unit_code: None | str | Unset
        if isinstance(self.matched_unit_code, Unset):
            matched_unit_code = UNSET
        else:
            matched_unit_code = self.matched_unit_code

        variant_id: None | str | Unset
        if isinstance(self.variant_id, Unset):
            variant_id = UNSET
        elif isinstance(self.variant_id, UUID):
            variant_id = str(self.variant_id)
        else:
            variant_id = self.variant_id

        sku_id: None | str | Unset
        if isinstance(self.sku_id, Unset):
            sku_id = UNSET
        elif isinstance(self.sku_id, UUID):
            sku_id = str(self.sku_id)
        else:
            sku_id = self.sku_id

        variant_name: None | str | Unset
        if isinstance(self.variant_name, Unset):
            variant_name = UNSET
        else:
            variant_name = self.variant_name

        variant_is_active: bool | None | Unset
        if isinstance(self.variant_is_active, Unset):
            variant_is_active = UNSET
        else:
            variant_is_active = self.variant_is_active


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if tracking_type is not UNSET:
            field_dict["trackingType"] = tracking_type
        if selling_price is not UNSET:
            field_dict["sellingPrice"] = selling_price
        if stock_quantity is not UNSET:
            field_dict["stockQuantity"] = stock_quantity
        if barcode is not UNSET:
            field_dict["barcode"] = barcode
        if tax_rate is not UNSET:
            field_dict["taxRate"] = tax_rate
        if unit_code is not UNSET:
            field_dict["unitCode"] = unit_code
        if matched_unit_code is not UNSET:
            field_dict["matchedUnitCode"] = matched_unit_code
        if variant_id is not UNSET:
            field_dict["variantId"] = variant_id
        if sku_id is not UNSET:
            field_dict["skuId"] = sku_id
        if variant_name is not UNSET:
            field_dict["variantName"] = variant_name
        if variant_is_active is not UNSET:
            field_dict["variantIsActive"] = variant_is_active

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




        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_image_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_url = _parse_image_url(d.pop("imageUrl", UNSET))


        def _parse_tracking_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tracking_type = _parse_tracking_type(d.pop("trackingType", UNSET))


        def _parse_selling_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        selling_price = _parse_selling_price(d.pop("sellingPrice", UNSET))


        def _parse_stock_quantity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        stock_quantity = _parse_stock_quantity(d.pop("stockQuantity", UNSET))


        def _parse_barcode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        barcode = _parse_barcode(d.pop("barcode", UNSET))


        def _parse_tax_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        tax_rate = _parse_tax_rate(d.pop("taxRate", UNSET))


        def _parse_unit_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit_code = _parse_unit_code(d.pop("unitCode", UNSET))


        def _parse_matched_unit_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        matched_unit_code = _parse_matched_unit_code(d.pop("matchedUnitCode", UNSET))


        def _parse_variant_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                variant_id_type_0 = UUID(data)



                return variant_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        variant_id = _parse_variant_id(d.pop("variantId", UNSET))


        def _parse_sku_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sku_id_type_0 = UUID(data)



                return sku_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        sku_id = _parse_sku_id(d.pop("skuId", UNSET))


        def _parse_variant_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        variant_name = _parse_variant_name(d.pop("variantName", UNSET))


        def _parse_variant_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        variant_is_active = _parse_variant_is_active(d.pop("variantIsActive", UNSET))


        barcode_product_dto = cls(
            id=id,
            code=code,
            name=name,
            image_url=image_url,
            tracking_type=tracking_type,
            selling_price=selling_price,
            stock_quantity=stock_quantity,
            barcode=barcode,
            tax_rate=tax_rate,
            unit_code=unit_code,
            matched_unit_code=matched_unit_code,
            variant_id=variant_id,
            sku_id=sku_id,
            variant_name=variant_name,
            variant_is_active=variant_is_active,
        )

        return barcode_product_dto


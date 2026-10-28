from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.catalog_product_variant_dto import CatalogProductVariantDto
  from ..models.catalog_unit_conversion_dto import CatalogUnitConversionDto





T = TypeVar("T", bound="CatalogProductDto")



@_attrs_define
class CatalogProductDto:
    

    id: UUID | Unset = UNSET
    name: None | str | Unset = UNSET
    sku: None | str | Unset = UNSET
    unit: None | str | Unset = UNSET
    price: float | Unset = UNSET
    category_id: None | Unset | UUID = UNSET
    tracking_type: None | str | Unset = UNSET
    tax_rate: float | Unset = UNSET
    default_sku_id: None | str | Unset = UNSET
    unit_conversions: list[CatalogUnitConversionDto] | None | Unset = UNSET
    variants: list[CatalogProductVariantDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.catalog_product_variant_dto import CatalogProductVariantDto # noqa: PLC0415
        from ..models.catalog_unit_conversion_dto import CatalogUnitConversionDto # noqa: PLC0415
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        sku: None | str | Unset
        if isinstance(self.sku, Unset):
            sku = UNSET
        else:
            sku = self.sku

        unit: None | str | Unset
        if isinstance(self.unit, Unset):
            unit = UNSET
        else:
            unit = self.unit

        price = self.price

        category_id: None | str | Unset
        if isinstance(self.category_id, Unset):
            category_id = UNSET
        elif isinstance(self.category_id, UUID):
            category_id = str(self.category_id)
        else:
            category_id = self.category_id

        tracking_type: None | str | Unset
        if isinstance(self.tracking_type, Unset):
            tracking_type = UNSET
        else:
            tracking_type = self.tracking_type

        tax_rate = self.tax_rate

        default_sku_id: None | str | Unset
        if isinstance(self.default_sku_id, Unset):
            default_sku_id = UNSET
        else:
            default_sku_id = self.default_sku_id

        unit_conversions: list[dict[str, Any]] | None | Unset
        if isinstance(self.unit_conversions, Unset):
            unit_conversions = UNSET
        elif isinstance(self.unit_conversions, list):
            unit_conversions = []
            for unit_conversions_type_0_item_data in self.unit_conversions:
                unit_conversions_type_0_item = unit_conversions_type_0_item_data.to_dict()
                unit_conversions.append(unit_conversions_type_0_item)


        else:
            unit_conversions = self.unit_conversions

        variants: list[dict[str, Any]] | None | Unset
        if isinstance(self.variants, Unset):
            variants = UNSET
        elif isinstance(self.variants, list):
            variants = []
            for variants_type_0_item_data in self.variants:
                variants_type_0_item = variants_type_0_item_data.to_dict()
                variants.append(variants_type_0_item)


        else:
            variants = self.variants


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if sku is not UNSET:
            field_dict["sku"] = sku
        if unit is not UNSET:
            field_dict["unit"] = unit
        if price is not UNSET:
            field_dict["price"] = price
        if category_id is not UNSET:
            field_dict["categoryId"] = category_id
        if tracking_type is not UNSET:
            field_dict["trackingType"] = tracking_type
        if tax_rate is not UNSET:
            field_dict["taxRate"] = tax_rate
        if default_sku_id is not UNSET:
            field_dict["defaultSkuId"] = default_sku_id
        if unit_conversions is not UNSET:
            field_dict["unitConversions"] = unit_conversions
        if variants is not UNSET:
            field_dict["variants"] = variants

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_product_variant_dto import CatalogProductVariantDto # noqa: PLC0415
        from ..models.catalog_unit_conversion_dto import CatalogUnitConversionDto # noqa: PLC0415
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_sku(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sku = _parse_sku(d.pop("sku", UNSET))


        def _parse_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit = _parse_unit(d.pop("unit", UNSET))


        price = d.pop("price", UNSET)

        def _parse_category_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                category_id_type_0 = UUID(data)



                return category_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        category_id = _parse_category_id(d.pop("categoryId", UNSET))


        def _parse_tracking_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tracking_type = _parse_tracking_type(d.pop("trackingType", UNSET))


        tax_rate = d.pop("taxRate", UNSET)

        def _parse_default_sku_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_sku_id = _parse_default_sku_id(d.pop("defaultSkuId", UNSET))


        def _parse_unit_conversions(data: object) -> list[CatalogUnitConversionDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                unit_conversions_type_0 = []
                _unit_conversions_type_0 = data
                for unit_conversions_type_0_item_data in (_unit_conversions_type_0):
                    unit_conversions_type_0_item = CatalogUnitConversionDto.from_dict(unit_conversions_type_0_item_data)



                    unit_conversions_type_0.append(unit_conversions_type_0_item)

                return unit_conversions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CatalogUnitConversionDto] | None | Unset, data)

        unit_conversions = _parse_unit_conversions(d.pop("unitConversions", UNSET))


        def _parse_variants(data: object) -> list[CatalogProductVariantDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                variants_type_0 = []
                _variants_type_0 = data
                for variants_type_0_item_data in (_variants_type_0):
                    variants_type_0_item = CatalogProductVariantDto.from_dict(variants_type_0_item_data)



                    variants_type_0.append(variants_type_0_item)

                return variants_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CatalogProductVariantDto] | None | Unset, data)

        variants = _parse_variants(d.pop("variants", UNSET))


        catalog_product_dto = cls(
            id=id,
            name=name,
            sku=sku,
            unit=unit,
            price=price,
            category_id=category_id,
            tracking_type=tracking_type,
            tax_rate=tax_rate,
            default_sku_id=default_sku_id,
            unit_conversions=unit_conversions,
            variants=variants,
        )

        return catalog_product_dto


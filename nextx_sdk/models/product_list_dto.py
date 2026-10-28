from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.category_ref_dto import CategoryRefDto
  from ..models.product_list_dto_custom_fields_type_0 import ProductListDtoCustomFieldsType0
  from ..models.product_unit_conversion_dto import ProductUnitConversionDto
  from ..models.unit_ref_dto import UnitRefDto





T = TypeVar("T", bound="ProductListDto")



@_attrs_define
class ProductListDto:
    

    id: UUID | Unset = UNSET
    code: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    product_type: None | str | Unset = UNSET
    tracking_type: None | str | Unset = UNSET
    category: CategoryRefDto | Unset = UNSET
    unit: UnitRefDto | Unset = UNSET
    current_price: float | None | Unset = UNSET
    current_cost: float | None | Unset = UNSET
    wholesale_price: float | None | Unset = UNSET
    min_price: float | None | Unset = UNSET
    max_price: float | None | Unset = UNSET
    stock_quantity: float | Unset = UNSET
    opening_stock: float | Unset = UNSET
    status: None | str | Unset = UNSET
    image_key: None | str | Unset = UNSET
    image_url: None | str | Unset = UNSET
    warranty_months: int | Unset = UNSET
    variant_count: int | Unset = UNSET
    attributes: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    unit_conversions: list[ProductUnitConversionDto] | None | Unset = UNSET
    is_lot_tracked: bool | Unset = UNSET
    is_serial_tracked: bool | Unset = UNSET
    tax_rate: float | Unset = UNSET
    sell_price_includes_vat: bool | Unset = UNSET
    default_sku_id: None | Unset | UUID = UNSET
    barcode: None | str | Unset = UNSET
    custom_fields: None | ProductListDtoCustomFieldsType0 | Unset = UNSET
    sku: None | str | Unset = UNSET
    brand_id: None | Unset | UUID = UNSET
    brand_name: None | str | Unset = UNSET
    min_stock_level: float | None | Unset = UNSET
    max_stock_level: float | None | Unset = UNSET
    reserved: float | Unset = UNSET
    location: None | str | Unset = UNSET
    weight: float | None | Unset = UNSET
    weight_unit: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    source_ref: None | str | Unset = UNSET
    package_kind: None | str | Unset = UNSET
    duration_months: int | None | Unset = UNSET
    package_services_json: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.category_ref_dto import CategoryRefDto # noqa: PLC0415
        from ..models.product_list_dto_custom_fields_type_0 import ProductListDtoCustomFieldsType0 # noqa: PLC0415
        from ..models.product_unit_conversion_dto import ProductUnitConversionDto # noqa: PLC0415
        from ..models.unit_ref_dto import UnitRefDto # noqa: PLC0415
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

        product_type: None | str | Unset
        if isinstance(self.product_type, Unset):
            product_type = UNSET
        else:
            product_type = self.product_type

        tracking_type: None | str | Unset
        if isinstance(self.tracking_type, Unset):
            tracking_type = UNSET
        else:
            tracking_type = self.tracking_type

        category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        unit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.to_dict()

        current_price: float | None | Unset
        if isinstance(self.current_price, Unset):
            current_price = UNSET
        else:
            current_price = self.current_price

        current_cost: float | None | Unset
        if isinstance(self.current_cost, Unset):
            current_cost = UNSET
        else:
            current_cost = self.current_cost

        wholesale_price: float | None | Unset
        if isinstance(self.wholesale_price, Unset):
            wholesale_price = UNSET
        else:
            wholesale_price = self.wholesale_price

        min_price: float | None | Unset
        if isinstance(self.min_price, Unset):
            min_price = UNSET
        else:
            min_price = self.min_price

        max_price: float | None | Unset
        if isinstance(self.max_price, Unset):
            max_price = UNSET
        else:
            max_price = self.max_price

        stock_quantity = self.stock_quantity

        opening_stock = self.opening_stock

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        image_key: None | str | Unset
        if isinstance(self.image_key, Unset):
            image_key = UNSET
        else:
            image_key = self.image_key

        image_url: None | str | Unset
        if isinstance(self.image_url, Unset):
            image_url = UNSET
        else:
            image_url = self.image_url

        warranty_months = self.warranty_months

        variant_count = self.variant_count

        attributes: None | str | Unset
        if isinstance(self.attributes, Unset):
            attributes = UNSET
        else:
            attributes = self.attributes

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

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

        is_lot_tracked = self.is_lot_tracked

        is_serial_tracked = self.is_serial_tracked

        tax_rate = self.tax_rate

        sell_price_includes_vat = self.sell_price_includes_vat

        default_sku_id: None | str | Unset
        if isinstance(self.default_sku_id, Unset):
            default_sku_id = UNSET
        elif isinstance(self.default_sku_id, UUID):
            default_sku_id = str(self.default_sku_id)
        else:
            default_sku_id = self.default_sku_id

        barcode: None | str | Unset
        if isinstance(self.barcode, Unset):
            barcode = UNSET
        else:
            barcode = self.barcode

        custom_fields: dict[str, Any] | None | Unset
        if isinstance(self.custom_fields, Unset):
            custom_fields = UNSET
        elif isinstance(self.custom_fields, ProductListDtoCustomFieldsType0):
            custom_fields = self.custom_fields.to_dict()
        else:
            custom_fields = self.custom_fields

        sku: None | str | Unset
        if isinstance(self.sku, Unset):
            sku = UNSET
        else:
            sku = self.sku

        brand_id: None | str | Unset
        if isinstance(self.brand_id, Unset):
            brand_id = UNSET
        elif isinstance(self.brand_id, UUID):
            brand_id = str(self.brand_id)
        else:
            brand_id = self.brand_id

        brand_name: None | str | Unset
        if isinstance(self.brand_name, Unset):
            brand_name = UNSET
        else:
            brand_name = self.brand_name

        min_stock_level: float | None | Unset
        if isinstance(self.min_stock_level, Unset):
            min_stock_level = UNSET
        else:
            min_stock_level = self.min_stock_level

        max_stock_level: float | None | Unset
        if isinstance(self.max_stock_level, Unset):
            max_stock_level = UNSET
        else:
            max_stock_level = self.max_stock_level

        reserved = self.reserved

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        weight: float | None | Unset
        if isinstance(self.weight, Unset):
            weight = UNSET
        else:
            weight = self.weight

        weight_unit: None | str | Unset
        if isinstance(self.weight_unit, Unset):
            weight_unit = UNSET
        else:
            weight_unit = self.weight_unit

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        source_ref: None | str | Unset
        if isinstance(self.source_ref, Unset):
            source_ref = UNSET
        else:
            source_ref = self.source_ref

        package_kind: None | str | Unset
        if isinstance(self.package_kind, Unset):
            package_kind = UNSET
        else:
            package_kind = self.package_kind

        duration_months: int | None | Unset
        if isinstance(self.duration_months, Unset):
            duration_months = UNSET
        else:
            duration_months = self.duration_months

        package_services_json: None | str | Unset
        if isinstance(self.package_services_json, Unset):
            package_services_json = UNSET
        else:
            package_services_json = self.package_services_json


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name
        if product_type is not UNSET:
            field_dict["productType"] = product_type
        if tracking_type is not UNSET:
            field_dict["trackingType"] = tracking_type
        if category is not UNSET:
            field_dict["category"] = category
        if unit is not UNSET:
            field_dict["unit"] = unit
        if current_price is not UNSET:
            field_dict["currentPrice"] = current_price
        if current_cost is not UNSET:
            field_dict["currentCost"] = current_cost
        if wholesale_price is not UNSET:
            field_dict["wholesalePrice"] = wholesale_price
        if min_price is not UNSET:
            field_dict["minPrice"] = min_price
        if max_price is not UNSET:
            field_dict["maxPrice"] = max_price
        if stock_quantity is not UNSET:
            field_dict["stockQuantity"] = stock_quantity
        if opening_stock is not UNSET:
            field_dict["openingStock"] = opening_stock
        if status is not UNSET:
            field_dict["status"] = status
        if image_key is not UNSET:
            field_dict["imageKey"] = image_key
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if warranty_months is not UNSET:
            field_dict["warrantyMonths"] = warranty_months
        if variant_count is not UNSET:
            field_dict["variantCount"] = variant_count
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if unit_conversions is not UNSET:
            field_dict["unitConversions"] = unit_conversions
        if is_lot_tracked is not UNSET:
            field_dict["isLotTracked"] = is_lot_tracked
        if is_serial_tracked is not UNSET:
            field_dict["isSerialTracked"] = is_serial_tracked
        if tax_rate is not UNSET:
            field_dict["taxRate"] = tax_rate
        if sell_price_includes_vat is not UNSET:
            field_dict["sellPriceIncludesVat"] = sell_price_includes_vat
        if default_sku_id is not UNSET:
            field_dict["defaultSkuId"] = default_sku_id
        if barcode is not UNSET:
            field_dict["barcode"] = barcode
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if sku is not UNSET:
            field_dict["sku"] = sku
        if brand_id is not UNSET:
            field_dict["brandId"] = brand_id
        if brand_name is not UNSET:
            field_dict["brandName"] = brand_name
        if min_stock_level is not UNSET:
            field_dict["minStockLevel"] = min_stock_level
        if max_stock_level is not UNSET:
            field_dict["maxStockLevel"] = max_stock_level
        if reserved is not UNSET:
            field_dict["reserved"] = reserved
        if location is not UNSET:
            field_dict["location"] = location
        if weight is not UNSET:
            field_dict["weight"] = weight
        if weight_unit is not UNSET:
            field_dict["weightUnit"] = weight_unit
        if notes is not UNSET:
            field_dict["notes"] = notes
        if source is not UNSET:
            field_dict["source"] = source
        if source_ref is not UNSET:
            field_dict["sourceRef"] = source_ref
        if package_kind is not UNSET:
            field_dict["packageKind"] = package_kind
        if duration_months is not UNSET:
            field_dict["durationMonths"] = duration_months
        if package_services_json is not UNSET:
            field_dict["packageServicesJson"] = package_services_json

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.category_ref_dto import CategoryRefDto # noqa: PLC0415
        from ..models.product_list_dto_custom_fields_type_0 import ProductListDtoCustomFieldsType0 # noqa: PLC0415
        from ..models.product_unit_conversion_dto import ProductUnitConversionDto # noqa: PLC0415
        from ..models.unit_ref_dto import UnitRefDto # noqa: PLC0415
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


        def _parse_product_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_type = _parse_product_type(d.pop("productType", UNSET))


        def _parse_tracking_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tracking_type = _parse_tracking_type(d.pop("trackingType", UNSET))


        _category = d.pop("category", UNSET)
        category: CategoryRefDto | Unset
        if isinstance(_category,  Unset):
            category = UNSET
        else:
            category = CategoryRefDto.from_dict(_category)




        _unit = d.pop("unit", UNSET)
        unit: UnitRefDto | Unset
        if isinstance(_unit,  Unset):
            unit = UNSET
        else:
            unit = UnitRefDto.from_dict(_unit)




        def _parse_current_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        current_price = _parse_current_price(d.pop("currentPrice", UNSET))


        def _parse_current_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        current_cost = _parse_current_cost(d.pop("currentCost", UNSET))


        def _parse_wholesale_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wholesale_price = _parse_wholesale_price(d.pop("wholesalePrice", UNSET))


        def _parse_min_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_price = _parse_min_price(d.pop("minPrice", UNSET))


        def _parse_max_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_price = _parse_max_price(d.pop("maxPrice", UNSET))


        stock_quantity = d.pop("stockQuantity", UNSET)

        opening_stock = d.pop("openingStock", UNSET)

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_image_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_key = _parse_image_key(d.pop("imageKey", UNSET))


        def _parse_image_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_url = _parse_image_url(d.pop("imageUrl", UNSET))


        warranty_months = d.pop("warrantyMonths", UNSET)

        variant_count = d.pop("variantCount", UNSET)

        def _parse_attributes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        attributes = _parse_attributes(d.pop("attributes", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_unit_conversions(data: object) -> list[ProductUnitConversionDto] | None | Unset:
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
                    unit_conversions_type_0_item = ProductUnitConversionDto.from_dict(unit_conversions_type_0_item_data)



                    unit_conversions_type_0.append(unit_conversions_type_0_item)

                return unit_conversions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProductUnitConversionDto] | None | Unset, data)

        unit_conversions = _parse_unit_conversions(d.pop("unitConversions", UNSET))


        is_lot_tracked = d.pop("isLotTracked", UNSET)

        is_serial_tracked = d.pop("isSerialTracked", UNSET)

        tax_rate = d.pop("taxRate", UNSET)

        sell_price_includes_vat = d.pop("sellPriceIncludesVat", UNSET)

        def _parse_default_sku_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                default_sku_id_type_0 = UUID(data)



                return default_sku_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        default_sku_id = _parse_default_sku_id(d.pop("defaultSkuId", UNSET))


        def _parse_barcode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        barcode = _parse_barcode(d.pop("barcode", UNSET))


        def _parse_custom_fields(data: object) -> None | ProductListDtoCustomFieldsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_fields_type_0 = ProductListDtoCustomFieldsType0.from_dict(data)



                return custom_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProductListDtoCustomFieldsType0 | Unset, data)

        custom_fields = _parse_custom_fields(d.pop("customFields", UNSET))


        def _parse_sku(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sku = _parse_sku(d.pop("sku", UNSET))


        def _parse_brand_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                brand_id_type_0 = UUID(data)



                return brand_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        brand_id = _parse_brand_id(d.pop("brandId", UNSET))


        def _parse_brand_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        brand_name = _parse_brand_name(d.pop("brandName", UNSET))


        def _parse_min_stock_level(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_stock_level = _parse_min_stock_level(d.pop("minStockLevel", UNSET))


        def _parse_max_stock_level(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_stock_level = _parse_max_stock_level(d.pop("maxStockLevel", UNSET))


        reserved = d.pop("reserved", UNSET)

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))


        def _parse_weight(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        weight = _parse_weight(d.pop("weight", UNSET))


        def _parse_weight_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        weight_unit = _parse_weight_unit(d.pop("weightUnit", UNSET))


        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))


        def _parse_source_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_ref = _parse_source_ref(d.pop("sourceRef", UNSET))


        def _parse_package_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        package_kind = _parse_package_kind(d.pop("packageKind", UNSET))


        def _parse_duration_months(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_months = _parse_duration_months(d.pop("durationMonths", UNSET))


        def _parse_package_services_json(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        package_services_json = _parse_package_services_json(d.pop("packageServicesJson", UNSET))


        product_list_dto = cls(
            id=id,
            code=code,
            name=name,
            product_type=product_type,
            tracking_type=tracking_type,
            category=category,
            unit=unit,
            current_price=current_price,
            current_cost=current_cost,
            wholesale_price=wholesale_price,
            min_price=min_price,
            max_price=max_price,
            stock_quantity=stock_quantity,
            opening_stock=opening_stock,
            status=status,
            image_key=image_key,
            image_url=image_url,
            warranty_months=warranty_months,
            variant_count=variant_count,
            attributes=attributes,
            created_at=created_at,
            unit_conversions=unit_conversions,
            is_lot_tracked=is_lot_tracked,
            is_serial_tracked=is_serial_tracked,
            tax_rate=tax_rate,
            sell_price_includes_vat=sell_price_includes_vat,
            default_sku_id=default_sku_id,
            barcode=barcode,
            custom_fields=custom_fields,
            sku=sku,
            brand_id=brand_id,
            brand_name=brand_name,
            min_stock_level=min_stock_level,
            max_stock_level=max_stock_level,
            reserved=reserved,
            location=location,
            weight=weight,
            weight_unit=weight_unit,
            notes=notes,
            source=source,
            source_ref=source_ref,
            package_kind=package_kind,
            duration_months=duration_months,
            package_services_json=package_services_json,
        )

        return product_list_dto


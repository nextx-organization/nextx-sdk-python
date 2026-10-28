from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.product_detail_dto_kit_price_mode import check_product_detail_dto_kit_price_mode
from ..models.product_detail_dto_kit_price_mode import ProductDetailDtoKitPriceMode
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.brand_ref_dto import BrandRefDto
  from ..models.category_ref_dto import CategoryRefDto
  from ..models.location_ref_dto import LocationRefDto
  from ..models.product_branch_stock_detail_dto import ProductBranchStockDetailDto
  from ..models.product_detail_dto_custom_fields_type_0 import ProductDetailDtoCustomFieldsType0
  from ..models.unit_ref_dto import UnitRefDto





T = TypeVar("T", bound="ProductDetailDto")



@_attrs_define
class ProductDetailDto:
    

    id: UUID | Unset = UNSET
    code: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    product_type: None | str | Unset = UNSET
    tracking_type: None | str | Unset = UNSET
    barcode: None | str | Unset = UNSET
    category: CategoryRefDto | Unset = UNSET
    brand: BrandRefDto | Unset = UNSET
    unit: UnitRefDto | Unset = UNSET
    current_price: float | None | Unset = UNSET
    current_cost: float | None | Unset = UNSET
    wholesale_price: float | None | Unset = UNSET
    tax_rate: float | Unset = UNSET
    sell_price_includes_vat: bool | Unset = UNSET
    stock_quantity: float | Unset = UNSET
    warranty_months: int | Unset = UNSET
    status: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    image_key: None | str | Unset = UNSET
    image_url: None | str | Unset = UNSET
    image_keys: list[str] | None | Unset = UNSET
    image_urls: list[str] | None | Unset = UNSET
    variant_count: int | Unset = UNSET
    attributes: None | str | Unset = UNSET
    min_price: float | None | Unset = UNSET
    max_price: float | None | Unset = UNSET
    default_sku_id: None | Unset | UUID = UNSET
    is_lot_tracked: bool | Unset = UNSET
    is_serial_tracked: bool | Unset = UNSET
    is_sold_directly: bool | Unset = UNSET
    is_delete_protected: bool | Unset = UNSET
    notes: None | str | Unset = UNSET
    kit_price_mode: ProductDetailDtoKitPriceMode | Unset = UNSET
    kit_price_override: float | None | Unset = UNSET
    stock_by_branch: list[ProductBranchStockDetailDto] | None | Unset = UNSET
    min_stock_level: float | None | Unset = UNSET
    max_stock_level: float | None | Unset = UNSET
    weight: float | None | Unset = UNSET
    weight_unit: None | str | Unset = UNSET
    length_cm: float | None | Unset = UNSET
    width_cm: float | None | Unset = UNSET
    height_cm: float | None | Unset = UNSET
    locations: list[LocationRefDto] | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    custom_fields: None | ProductDetailDtoCustomFieldsType0 | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.brand_ref_dto import BrandRefDto # noqa: PLC0415
        from ..models.category_ref_dto import CategoryRefDto # noqa: PLC0415
        from ..models.location_ref_dto import LocationRefDto # noqa: PLC0415
        from ..models.product_branch_stock_detail_dto import ProductBranchStockDetailDto # noqa: PLC0415
        from ..models.product_detail_dto_custom_fields_type_0 import ProductDetailDtoCustomFieldsType0 # noqa: PLC0415
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

        barcode: None | str | Unset
        if isinstance(self.barcode, Unset):
            barcode = UNSET
        else:
            barcode = self.barcode

        category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        brand: dict[str, Any] | Unset = UNSET
        if not isinstance(self.brand, Unset):
            brand = self.brand.to_dict()

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

        tax_rate = self.tax_rate

        sell_price_includes_vat = self.sell_price_includes_vat

        stock_quantity = self.stock_quantity

        warranty_months = self.warranty_months

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

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

        image_keys: list[str] | None | Unset
        if isinstance(self.image_keys, Unset):
            image_keys = UNSET
        elif isinstance(self.image_keys, list):
            image_keys = self.image_keys


        else:
            image_keys = self.image_keys

        image_urls: list[str] | None | Unset
        if isinstance(self.image_urls, Unset):
            image_urls = UNSET
        elif isinstance(self.image_urls, list):
            image_urls = self.image_urls


        else:
            image_urls = self.image_urls

        variant_count = self.variant_count

        attributes: None | str | Unset
        if isinstance(self.attributes, Unset):
            attributes = UNSET
        else:
            attributes = self.attributes

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

        default_sku_id: None | str | Unset
        if isinstance(self.default_sku_id, Unset):
            default_sku_id = UNSET
        elif isinstance(self.default_sku_id, UUID):
            default_sku_id = str(self.default_sku_id)
        else:
            default_sku_id = self.default_sku_id

        is_lot_tracked = self.is_lot_tracked

        is_serial_tracked = self.is_serial_tracked

        is_sold_directly = self.is_sold_directly

        is_delete_protected = self.is_delete_protected

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        kit_price_mode: str | Unset = UNSET
        if not isinstance(self.kit_price_mode, Unset):
            kit_price_mode = self.kit_price_mode


        kit_price_override: float | None | Unset
        if isinstance(self.kit_price_override, Unset):
            kit_price_override = UNSET
        else:
            kit_price_override = self.kit_price_override

        stock_by_branch: list[dict[str, Any]] | None | Unset
        if isinstance(self.stock_by_branch, Unset):
            stock_by_branch = UNSET
        elif isinstance(self.stock_by_branch, list):
            stock_by_branch = []
            for stock_by_branch_type_0_item_data in self.stock_by_branch:
                stock_by_branch_type_0_item = stock_by_branch_type_0_item_data.to_dict()
                stock_by_branch.append(stock_by_branch_type_0_item)


        else:
            stock_by_branch = self.stock_by_branch

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

        length_cm: float | None | Unset
        if isinstance(self.length_cm, Unset):
            length_cm = UNSET
        else:
            length_cm = self.length_cm

        width_cm: float | None | Unset
        if isinstance(self.width_cm, Unset):
            width_cm = UNSET
        else:
            width_cm = self.width_cm

        height_cm: float | None | Unset
        if isinstance(self.height_cm, Unset):
            height_cm = UNSET
        else:
            height_cm = self.height_cm

        locations: list[dict[str, Any]] | None | Unset
        if isinstance(self.locations, Unset):
            locations = UNSET
        elif isinstance(self.locations, list):
            locations = []
            for locations_type_0_item_data in self.locations:
                locations_type_0_item = locations_type_0_item_data.to_dict()
                locations.append(locations_type_0_item)


        else:
            locations = self.locations

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        custom_fields: dict[str, Any] | None | Unset
        if isinstance(self.custom_fields, Unset):
            custom_fields = UNSET
        elif isinstance(self.custom_fields, ProductDetailDtoCustomFieldsType0):
            custom_fields = self.custom_fields.to_dict()
        else:
            custom_fields = self.custom_fields


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
        if barcode is not UNSET:
            field_dict["barcode"] = barcode
        if category is not UNSET:
            field_dict["category"] = category
        if brand is not UNSET:
            field_dict["brand"] = brand
        if unit is not UNSET:
            field_dict["unit"] = unit
        if current_price is not UNSET:
            field_dict["currentPrice"] = current_price
        if current_cost is not UNSET:
            field_dict["currentCost"] = current_cost
        if wholesale_price is not UNSET:
            field_dict["wholesalePrice"] = wholesale_price
        if tax_rate is not UNSET:
            field_dict["taxRate"] = tax_rate
        if sell_price_includes_vat is not UNSET:
            field_dict["sellPriceIncludesVat"] = sell_price_includes_vat
        if stock_quantity is not UNSET:
            field_dict["stockQuantity"] = stock_quantity
        if warranty_months is not UNSET:
            field_dict["warrantyMonths"] = warranty_months
        if status is not UNSET:
            field_dict["status"] = status
        if description is not UNSET:
            field_dict["description"] = description
        if image_key is not UNSET:
            field_dict["imageKey"] = image_key
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if image_keys is not UNSET:
            field_dict["imageKeys"] = image_keys
        if image_urls is not UNSET:
            field_dict["imageUrls"] = image_urls
        if variant_count is not UNSET:
            field_dict["variantCount"] = variant_count
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if min_price is not UNSET:
            field_dict["minPrice"] = min_price
        if max_price is not UNSET:
            field_dict["maxPrice"] = max_price
        if default_sku_id is not UNSET:
            field_dict["defaultSkuId"] = default_sku_id
        if is_lot_tracked is not UNSET:
            field_dict["isLotTracked"] = is_lot_tracked
        if is_serial_tracked is not UNSET:
            field_dict["isSerialTracked"] = is_serial_tracked
        if is_sold_directly is not UNSET:
            field_dict["isSoldDirectly"] = is_sold_directly
        if is_delete_protected is not UNSET:
            field_dict["isDeleteProtected"] = is_delete_protected
        if notes is not UNSET:
            field_dict["notes"] = notes
        if kit_price_mode is not UNSET:
            field_dict["kitPriceMode"] = kit_price_mode
        if kit_price_override is not UNSET:
            field_dict["kitPriceOverride"] = kit_price_override
        if stock_by_branch is not UNSET:
            field_dict["stockByBranch"] = stock_by_branch
        if min_stock_level is not UNSET:
            field_dict["minStockLevel"] = min_stock_level
        if max_stock_level is not UNSET:
            field_dict["maxStockLevel"] = max_stock_level
        if weight is not UNSET:
            field_dict["weight"] = weight
        if weight_unit is not UNSET:
            field_dict["weightUnit"] = weight_unit
        if length_cm is not UNSET:
            field_dict["lengthCm"] = length_cm
        if width_cm is not UNSET:
            field_dict["widthCm"] = width_cm
        if height_cm is not UNSET:
            field_dict["heightCm"] = height_cm
        if locations is not UNSET:
            field_dict["locations"] = locations
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brand_ref_dto import BrandRefDto # noqa: PLC0415
        from ..models.category_ref_dto import CategoryRefDto # noqa: PLC0415
        from ..models.location_ref_dto import LocationRefDto # noqa: PLC0415
        from ..models.product_branch_stock_detail_dto import ProductBranchStockDetailDto # noqa: PLC0415
        from ..models.product_detail_dto_custom_fields_type_0 import ProductDetailDtoCustomFieldsType0 # noqa: PLC0415
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


        def _parse_barcode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        barcode = _parse_barcode(d.pop("barcode", UNSET))


        _category = d.pop("category", UNSET)
        category: CategoryRefDto | Unset
        if isinstance(_category,  Unset):
            category = UNSET
        else:
            category = CategoryRefDto.from_dict(_category)




        _brand = d.pop("brand", UNSET)
        brand: BrandRefDto | Unset
        if isinstance(_brand,  Unset):
            brand = UNSET
        else:
            brand = BrandRefDto.from_dict(_brand)




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


        tax_rate = d.pop("taxRate", UNSET)

        sell_price_includes_vat = d.pop("sellPriceIncludesVat", UNSET)

        stock_quantity = d.pop("stockQuantity", UNSET)

        warranty_months = d.pop("warrantyMonths", UNSET)

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


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


        def _parse_image_keys(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                image_keys_type_0 = cast(list[str], data)

                return image_keys_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        image_keys = _parse_image_keys(d.pop("imageKeys", UNSET))


        def _parse_image_urls(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                image_urls_type_0 = cast(list[str], data)

                return image_urls_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        image_urls = _parse_image_urls(d.pop("imageUrls", UNSET))


        variant_count = d.pop("variantCount", UNSET)

        def _parse_attributes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        attributes = _parse_attributes(d.pop("attributes", UNSET))


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


        is_lot_tracked = d.pop("isLotTracked", UNSET)

        is_serial_tracked = d.pop("isSerialTracked", UNSET)

        is_sold_directly = d.pop("isSoldDirectly", UNSET)

        is_delete_protected = d.pop("isDeleteProtected", UNSET)

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


        _kit_price_mode = d.pop("kitPriceMode", UNSET)
        kit_price_mode: ProductDetailDtoKitPriceMode | Unset
        if isinstance(_kit_price_mode,  Unset):
            kit_price_mode = UNSET
        else:
            kit_price_mode = check_product_detail_dto_kit_price_mode(_kit_price_mode)




        def _parse_kit_price_override(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        kit_price_override = _parse_kit_price_override(d.pop("kitPriceOverride", UNSET))


        def _parse_stock_by_branch(data: object) -> list[ProductBranchStockDetailDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                stock_by_branch_type_0 = []
                _stock_by_branch_type_0 = data
                for stock_by_branch_type_0_item_data in (_stock_by_branch_type_0):
                    stock_by_branch_type_0_item = ProductBranchStockDetailDto.from_dict(stock_by_branch_type_0_item_data)



                    stock_by_branch_type_0.append(stock_by_branch_type_0_item)

                return stock_by_branch_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProductBranchStockDetailDto] | None | Unset, data)

        stock_by_branch = _parse_stock_by_branch(d.pop("stockByBranch", UNSET))


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


        def _parse_length_cm(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        length_cm = _parse_length_cm(d.pop("lengthCm", UNSET))


        def _parse_width_cm(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        width_cm = _parse_width_cm(d.pop("widthCm", UNSET))


        def _parse_height_cm(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        height_cm = _parse_height_cm(d.pop("heightCm", UNSET))


        def _parse_locations(data: object) -> list[LocationRefDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                locations_type_0 = []
                _locations_type_0 = data
                for locations_type_0_item_data in (_locations_type_0):
                    locations_type_0_item = LocationRefDto.from_dict(locations_type_0_item_data)



                    locations_type_0.append(locations_type_0_item)

                return locations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LocationRefDto] | None | Unset, data)

        locations = _parse_locations(d.pop("locations", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)




        def _parse_custom_fields(data: object) -> None | ProductDetailDtoCustomFieldsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_fields_type_0 = ProductDetailDtoCustomFieldsType0.from_dict(data)



                return custom_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProductDetailDtoCustomFieldsType0 | Unset, data)

        custom_fields = _parse_custom_fields(d.pop("customFields", UNSET))


        product_detail_dto = cls(
            id=id,
            code=code,
            name=name,
            product_type=product_type,
            tracking_type=tracking_type,
            barcode=barcode,
            category=category,
            brand=brand,
            unit=unit,
            current_price=current_price,
            current_cost=current_cost,
            wholesale_price=wholesale_price,
            tax_rate=tax_rate,
            sell_price_includes_vat=sell_price_includes_vat,
            stock_quantity=stock_quantity,
            warranty_months=warranty_months,
            status=status,
            description=description,
            image_key=image_key,
            image_url=image_url,
            image_keys=image_keys,
            image_urls=image_urls,
            variant_count=variant_count,
            attributes=attributes,
            min_price=min_price,
            max_price=max_price,
            default_sku_id=default_sku_id,
            is_lot_tracked=is_lot_tracked,
            is_serial_tracked=is_serial_tracked,
            is_sold_directly=is_sold_directly,
            is_delete_protected=is_delete_protected,
            notes=notes,
            kit_price_mode=kit_price_mode,
            kit_price_override=kit_price_override,
            stock_by_branch=stock_by_branch,
            min_stock_level=min_stock_level,
            max_stock_level=max_stock_level,
            weight=weight,
            weight_unit=weight_unit,
            length_cm=length_cm,
            width_cm=width_cm,
            height_cm=height_cm,
            locations=locations,
            created_at=created_at,
            updated_at=updated_at,
            custom_fields=custom_fields,
        )

        return product_detail_dto


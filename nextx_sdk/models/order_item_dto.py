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
  from ..models.order_item_component_dto import OrderItemComponentDto
  from ..models.order_item_discount_dto import OrderItemDiscountDto
  from ..models.order_item_return_lot_dto import OrderItemReturnLotDto
  from ..models.order_item_tax_dto import OrderItemTaxDto
  from ..models.order_item_tracking_dto import OrderItemTrackingDto





T = TypeVar("T", bound="OrderItemDto")



@_attrs_define
class OrderItemDto:
    

    id: UUID | Unset = UNSET
    product_id: UUID | Unset = UNSET
    product_name: None | str | Unset = UNSET
    sku: None | str | Unset = UNSET
    variant_id: None | Unset | UUID = UNSET
    variant_name: None | str | Unset = UNSET
    unit_code: None | str | Unset = UNSET
    unit_name: None | str | Unset = UNSET
    quantity: float | Unset = UNSET
    unit_price: float | Unset = UNSET
    subtotal: float | Unset = UNSET
    total: float | Unset = UNSET
    notes: None | str | Unset = UNSET
    discount: OrderItemDiscountDto | Unset = UNSET
    tax: OrderItemTaxDto | Unset = UNSET
    tracking: OrderItemTrackingDto | Unset = UNSET
    variant_code: None | str | Unset = UNSET
    fulfilled_quantity: float | Unset = UNSET
    unfulfilled_quantity: float | Unset = UNSET
    converted_qty: float | Unset = UNSET
    remaining_convert_qty: float | Unset = UNSET
    product_type: None | str | Unset = UNSET
    returned_quantity: float | Unset = UNSET
    item_note: None | str | Unset = UNSET
    is_gift: bool | Unset = UNSET
    product_group: None | str | Unset = UNSET
    weight: float | None | Unset = UNSET
    weight_unit: None | str | Unset = UNSET
    product_item_code: None | str | Unset = UNSET
    sku_code: None | str | Unset = UNSET
    open_return_quantity: float | Unset = UNSET
    open_return_codes: list[str] | None | Unset = UNSET
    kit_components: list[OrderItemComponentDto] | None | Unset = UNSET
    sku_id: None | Unset | UUID = UNSET
    lots: list[OrderItemReturnLotDto] | None | Unset = UNSET
    price_includes_vat: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.order_item_component_dto import OrderItemComponentDto # noqa: PLC0415
        from ..models.order_item_discount_dto import OrderItemDiscountDto # noqa: PLC0415
        from ..models.order_item_return_lot_dto import OrderItemReturnLotDto # noqa: PLC0415
        from ..models.order_item_tax_dto import OrderItemTaxDto # noqa: PLC0415
        from ..models.order_item_tracking_dto import OrderItemTrackingDto # noqa: PLC0415
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        product_id: str | Unset = UNSET
        if not isinstance(self.product_id, Unset):
            product_id = str(self.product_id)

        product_name: None | str | Unset
        if isinstance(self.product_name, Unset):
            product_name = UNSET
        else:
            product_name = self.product_name

        sku: None | str | Unset
        if isinstance(self.sku, Unset):
            sku = UNSET
        else:
            sku = self.sku

        variant_id: None | str | Unset
        if isinstance(self.variant_id, Unset):
            variant_id = UNSET
        elif isinstance(self.variant_id, UUID):
            variant_id = str(self.variant_id)
        else:
            variant_id = self.variant_id

        variant_name: None | str | Unset
        if isinstance(self.variant_name, Unset):
            variant_name = UNSET
        else:
            variant_name = self.variant_name

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

        quantity = self.quantity

        unit_price = self.unit_price

        subtotal = self.subtotal

        total = self.total

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        discount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.discount, Unset):
            discount = self.discount.to_dict()

        tax: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tax, Unset):
            tax = self.tax.to_dict()

        tracking: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tracking, Unset):
            tracking = self.tracking.to_dict()

        variant_code: None | str | Unset
        if isinstance(self.variant_code, Unset):
            variant_code = UNSET
        else:
            variant_code = self.variant_code

        fulfilled_quantity = self.fulfilled_quantity

        unfulfilled_quantity = self.unfulfilled_quantity

        converted_qty = self.converted_qty

        remaining_convert_qty = self.remaining_convert_qty

        product_type: None | str | Unset
        if isinstance(self.product_type, Unset):
            product_type = UNSET
        else:
            product_type = self.product_type

        returned_quantity = self.returned_quantity

        item_note: None | str | Unset
        if isinstance(self.item_note, Unset):
            item_note = UNSET
        else:
            item_note = self.item_note

        is_gift = self.is_gift

        product_group: None | str | Unset
        if isinstance(self.product_group, Unset):
            product_group = UNSET
        else:
            product_group = self.product_group

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

        product_item_code: None | str | Unset
        if isinstance(self.product_item_code, Unset):
            product_item_code = UNSET
        else:
            product_item_code = self.product_item_code

        sku_code: None | str | Unset
        if isinstance(self.sku_code, Unset):
            sku_code = UNSET
        else:
            sku_code = self.sku_code

        open_return_quantity = self.open_return_quantity

        open_return_codes: list[str] | None | Unset
        if isinstance(self.open_return_codes, Unset):
            open_return_codes = UNSET
        elif isinstance(self.open_return_codes, list):
            open_return_codes = self.open_return_codes


        else:
            open_return_codes = self.open_return_codes

        kit_components: list[dict[str, Any]] | None | Unset
        if isinstance(self.kit_components, Unset):
            kit_components = UNSET
        elif isinstance(self.kit_components, list):
            kit_components = []
            for kit_components_type_0_item_data in self.kit_components:
                kit_components_type_0_item = kit_components_type_0_item_data.to_dict()
                kit_components.append(kit_components_type_0_item)


        else:
            kit_components = self.kit_components

        sku_id: None | str | Unset
        if isinstance(self.sku_id, Unset):
            sku_id = UNSET
        elif isinstance(self.sku_id, UUID):
            sku_id = str(self.sku_id)
        else:
            sku_id = self.sku_id

        lots: list[dict[str, Any]] | None | Unset
        if isinstance(self.lots, Unset):
            lots = UNSET
        elif isinstance(self.lots, list):
            lots = []
            for lots_type_0_item_data in self.lots:
                lots_type_0_item = lots_type_0_item_data.to_dict()
                lots.append(lots_type_0_item)


        else:
            lots = self.lots

        price_includes_vat = self.price_includes_vat


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if product_name is not UNSET:
            field_dict["productName"] = product_name
        if sku is not UNSET:
            field_dict["sku"] = sku
        if variant_id is not UNSET:
            field_dict["variantId"] = variant_id
        if variant_name is not UNSET:
            field_dict["variantName"] = variant_name
        if unit_code is not UNSET:
            field_dict["unitCode"] = unit_code
        if unit_name is not UNSET:
            field_dict["unitName"] = unit_name
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if subtotal is not UNSET:
            field_dict["subtotal"] = subtotal
        if total is not UNSET:
            field_dict["total"] = total
        if notes is not UNSET:
            field_dict["notes"] = notes
        if discount is not UNSET:
            field_dict["discount"] = discount
        if tax is not UNSET:
            field_dict["tax"] = tax
        if tracking is not UNSET:
            field_dict["tracking"] = tracking
        if variant_code is not UNSET:
            field_dict["variantCode"] = variant_code
        if fulfilled_quantity is not UNSET:
            field_dict["fulfilledQuantity"] = fulfilled_quantity
        if unfulfilled_quantity is not UNSET:
            field_dict["unfulfilledQuantity"] = unfulfilled_quantity
        if converted_qty is not UNSET:
            field_dict["convertedQty"] = converted_qty
        if remaining_convert_qty is not UNSET:
            field_dict["remainingConvertQty"] = remaining_convert_qty
        if product_type is not UNSET:
            field_dict["productType"] = product_type
        if returned_quantity is not UNSET:
            field_dict["returnedQuantity"] = returned_quantity
        if item_note is not UNSET:
            field_dict["itemNote"] = item_note
        if is_gift is not UNSET:
            field_dict["isGift"] = is_gift
        if product_group is not UNSET:
            field_dict["productGroup"] = product_group
        if weight is not UNSET:
            field_dict["weight"] = weight
        if weight_unit is not UNSET:
            field_dict["weightUnit"] = weight_unit
        if product_item_code is not UNSET:
            field_dict["productItemCode"] = product_item_code
        if sku_code is not UNSET:
            field_dict["skuCode"] = sku_code
        if open_return_quantity is not UNSET:
            field_dict["openReturnQuantity"] = open_return_quantity
        if open_return_codes is not UNSET:
            field_dict["openReturnCodes"] = open_return_codes
        if kit_components is not UNSET:
            field_dict["kitComponents"] = kit_components
        if sku_id is not UNSET:
            field_dict["skuId"] = sku_id
        if lots is not UNSET:
            field_dict["lots"] = lots
        if price_includes_vat is not UNSET:
            field_dict["priceIncludesVat"] = price_includes_vat

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.order_item_component_dto import OrderItemComponentDto # noqa: PLC0415
        from ..models.order_item_discount_dto import OrderItemDiscountDto # noqa: PLC0415
        from ..models.order_item_return_lot_dto import OrderItemReturnLotDto # noqa: PLC0415
        from ..models.order_item_tax_dto import OrderItemTaxDto # noqa: PLC0415
        from ..models.order_item_tracking_dto import OrderItemTrackingDto # noqa: PLC0415
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        _product_id = d.pop("productId", UNSET)
        product_id: UUID | Unset
        if isinstance(_product_id,  Unset):
            product_id = UNSET
        else:
            product_id = UUID(_product_id)




        def _parse_product_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_name = _parse_product_name(d.pop("productName", UNSET))


        def _parse_sku(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sku = _parse_sku(d.pop("sku", UNSET))


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


        def _parse_variant_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        variant_name = _parse_variant_name(d.pop("variantName", UNSET))


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


        quantity = d.pop("quantity", UNSET)

        unit_price = d.pop("unitPrice", UNSET)

        subtotal = d.pop("subtotal", UNSET)

        total = d.pop("total", UNSET)

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


        _discount = d.pop("discount", UNSET)
        discount: OrderItemDiscountDto | Unset
        if isinstance(_discount,  Unset):
            discount = UNSET
        else:
            discount = OrderItemDiscountDto.from_dict(_discount)




        _tax = d.pop("tax", UNSET)
        tax: OrderItemTaxDto | Unset
        if isinstance(_tax,  Unset):
            tax = UNSET
        else:
            tax = OrderItemTaxDto.from_dict(_tax)




        _tracking = d.pop("tracking", UNSET)
        tracking: OrderItemTrackingDto | Unset
        if isinstance(_tracking,  Unset):
            tracking = UNSET
        else:
            tracking = OrderItemTrackingDto.from_dict(_tracking)




        def _parse_variant_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        variant_code = _parse_variant_code(d.pop("variantCode", UNSET))


        fulfilled_quantity = d.pop("fulfilledQuantity", UNSET)

        unfulfilled_quantity = d.pop("unfulfilledQuantity", UNSET)

        converted_qty = d.pop("convertedQty", UNSET)

        remaining_convert_qty = d.pop("remainingConvertQty", UNSET)

        def _parse_product_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_type = _parse_product_type(d.pop("productType", UNSET))


        returned_quantity = d.pop("returnedQuantity", UNSET)

        def _parse_item_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        item_note = _parse_item_note(d.pop("itemNote", UNSET))


        is_gift = d.pop("isGift", UNSET)

        def _parse_product_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_group = _parse_product_group(d.pop("productGroup", UNSET))


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


        def _parse_product_item_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_item_code = _parse_product_item_code(d.pop("productItemCode", UNSET))


        def _parse_sku_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sku_code = _parse_sku_code(d.pop("skuCode", UNSET))


        open_return_quantity = d.pop("openReturnQuantity", UNSET)

        def _parse_open_return_codes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                open_return_codes_type_0 = cast(list[str], data)

                return open_return_codes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        open_return_codes = _parse_open_return_codes(d.pop("openReturnCodes", UNSET))


        def _parse_kit_components(data: object) -> list[OrderItemComponentDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                kit_components_type_0 = []
                _kit_components_type_0 = data
                for kit_components_type_0_item_data in (_kit_components_type_0):
                    kit_components_type_0_item = OrderItemComponentDto.from_dict(kit_components_type_0_item_data)



                    kit_components_type_0.append(kit_components_type_0_item)

                return kit_components_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OrderItemComponentDto] | None | Unset, data)

        kit_components = _parse_kit_components(d.pop("kitComponents", UNSET))


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


        def _parse_lots(data: object) -> list[OrderItemReturnLotDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                lots_type_0 = []
                _lots_type_0 = data
                for lots_type_0_item_data in (_lots_type_0):
                    lots_type_0_item = OrderItemReturnLotDto.from_dict(lots_type_0_item_data)



                    lots_type_0.append(lots_type_0_item)

                return lots_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OrderItemReturnLotDto] | None | Unset, data)

        lots = _parse_lots(d.pop("lots", UNSET))


        price_includes_vat = d.pop("priceIncludesVat", UNSET)

        order_item_dto = cls(
            id=id,
            product_id=product_id,
            product_name=product_name,
            sku=sku,
            variant_id=variant_id,
            variant_name=variant_name,
            unit_code=unit_code,
            unit_name=unit_name,
            quantity=quantity,
            unit_price=unit_price,
            subtotal=subtotal,
            total=total,
            notes=notes,
            discount=discount,
            tax=tax,
            tracking=tracking,
            variant_code=variant_code,
            fulfilled_quantity=fulfilled_quantity,
            unfulfilled_quantity=unfulfilled_quantity,
            converted_qty=converted_qty,
            remaining_convert_qty=remaining_convert_qty,
            product_type=product_type,
            returned_quantity=returned_quantity,
            item_note=item_note,
            is_gift=is_gift,
            product_group=product_group,
            weight=weight,
            weight_unit=weight_unit,
            product_item_code=product_item_code,
            sku_code=sku_code,
            open_return_quantity=open_return_quantity,
            open_return_codes=open_return_codes,
            kit_components=kit_components,
            sku_id=sku_id,
            lots=lots,
            price_includes_vat=price_includes_vat,
        )

        return order_item_dto


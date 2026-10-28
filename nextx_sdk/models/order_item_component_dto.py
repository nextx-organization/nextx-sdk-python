from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OrderItemComponentDto")



@_attrs_define
class OrderItemComponentDto:
    

    id: UUID | Unset = UNSET
    component_sku_id: UUID | Unset = UNSET
    product_id: UUID | Unset = UNSET
    variant_id: None | Unset | UUID = UNSET
    product_name: None | str | Unset = UNSET
    variant_name: None | str | Unset = UNSET
    sku_code: None | str | Unset = UNSET
    tracking_type: None | str | Unset = UNSET
    unit_code: None | str | Unset = UNSET
    quantity_per_set: float | Unset = UNSET
    quantity: float | Unset = UNSET
    allocated_amount: float | Unset = UNSET
    refund_per_unit: float | Unset = UNSET
    returned_quantity: float | Unset = UNSET
    returnable_quantity: float | Unset = UNSET
    serial_numbers: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        component_sku_id: str | Unset = UNSET
        if not isinstance(self.component_sku_id, Unset):
            component_sku_id = str(self.component_sku_id)

        product_id: str | Unset = UNSET
        if not isinstance(self.product_id, Unset):
            product_id = str(self.product_id)

        variant_id: None | str | Unset
        if isinstance(self.variant_id, Unset):
            variant_id = UNSET
        elif isinstance(self.variant_id, UUID):
            variant_id = str(self.variant_id)
        else:
            variant_id = self.variant_id

        product_name: None | str | Unset
        if isinstance(self.product_name, Unset):
            product_name = UNSET
        else:
            product_name = self.product_name

        variant_name: None | str | Unset
        if isinstance(self.variant_name, Unset):
            variant_name = UNSET
        else:
            variant_name = self.variant_name

        sku_code: None | str | Unset
        if isinstance(self.sku_code, Unset):
            sku_code = UNSET
        else:
            sku_code = self.sku_code

        tracking_type: None | str | Unset
        if isinstance(self.tracking_type, Unset):
            tracking_type = UNSET
        else:
            tracking_type = self.tracking_type

        unit_code: None | str | Unset
        if isinstance(self.unit_code, Unset):
            unit_code = UNSET
        else:
            unit_code = self.unit_code

        quantity_per_set = self.quantity_per_set

        quantity = self.quantity

        allocated_amount = self.allocated_amount

        refund_per_unit = self.refund_per_unit

        returned_quantity = self.returned_quantity

        returnable_quantity = self.returnable_quantity

        serial_numbers: list[str] | None | Unset
        if isinstance(self.serial_numbers, Unset):
            serial_numbers = UNSET
        elif isinstance(self.serial_numbers, list):
            serial_numbers = self.serial_numbers


        else:
            serial_numbers = self.serial_numbers


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if component_sku_id is not UNSET:
            field_dict["componentSkuId"] = component_sku_id
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if variant_id is not UNSET:
            field_dict["variantId"] = variant_id
        if product_name is not UNSET:
            field_dict["productName"] = product_name
        if variant_name is not UNSET:
            field_dict["variantName"] = variant_name
        if sku_code is not UNSET:
            field_dict["skuCode"] = sku_code
        if tracking_type is not UNSET:
            field_dict["trackingType"] = tracking_type
        if unit_code is not UNSET:
            field_dict["unitCode"] = unit_code
        if quantity_per_set is not UNSET:
            field_dict["quantityPerSet"] = quantity_per_set
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if allocated_amount is not UNSET:
            field_dict["allocatedAmount"] = allocated_amount
        if refund_per_unit is not UNSET:
            field_dict["refundPerUnit"] = refund_per_unit
        if returned_quantity is not UNSET:
            field_dict["returnedQuantity"] = returned_quantity
        if returnable_quantity is not UNSET:
            field_dict["returnableQuantity"] = returnable_quantity
        if serial_numbers is not UNSET:
            field_dict["serialNumbers"] = serial_numbers

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




        _component_sku_id = d.pop("componentSkuId", UNSET)
        component_sku_id: UUID | Unset
        if isinstance(_component_sku_id,  Unset):
            component_sku_id = UNSET
        else:
            component_sku_id = UUID(_component_sku_id)




        _product_id = d.pop("productId", UNSET)
        product_id: UUID | Unset
        if isinstance(_product_id,  Unset):
            product_id = UNSET
        else:
            product_id = UUID(_product_id)




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


        def _parse_product_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_name = _parse_product_name(d.pop("productName", UNSET))


        def _parse_variant_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        variant_name = _parse_variant_name(d.pop("variantName", UNSET))


        def _parse_sku_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sku_code = _parse_sku_code(d.pop("skuCode", UNSET))


        def _parse_tracking_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tracking_type = _parse_tracking_type(d.pop("trackingType", UNSET))


        def _parse_unit_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit_code = _parse_unit_code(d.pop("unitCode", UNSET))


        quantity_per_set = d.pop("quantityPerSet", UNSET)

        quantity = d.pop("quantity", UNSET)

        allocated_amount = d.pop("allocatedAmount", UNSET)

        refund_per_unit = d.pop("refundPerUnit", UNSET)

        returned_quantity = d.pop("returnedQuantity", UNSET)

        returnable_quantity = d.pop("returnableQuantity", UNSET)

        def _parse_serial_numbers(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                serial_numbers_type_0 = cast(list[str], data)

                return serial_numbers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        serial_numbers = _parse_serial_numbers(d.pop("serialNumbers", UNSET))


        order_item_component_dto = cls(
            id=id,
            component_sku_id=component_sku_id,
            product_id=product_id,
            variant_id=variant_id,
            product_name=product_name,
            variant_name=variant_name,
            sku_code=sku_code,
            tracking_type=tracking_type,
            unit_code=unit_code,
            quantity_per_set=quantity_per_set,
            quantity=quantity,
            allocated_amount=allocated_amount,
            refund_per_unit=refund_per_unit,
            returned_quantity=returned_quantity,
            returnable_quantity=returnable_quantity,
            serial_numbers=serial_numbers,
        )

        return order_item_component_dto


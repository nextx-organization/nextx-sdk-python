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
  from ..models.open_api_order_customer_request import OpenApiOrderCustomerRequest
  from ..models.open_api_order_item_request import OpenApiOrderItemRequest





T = TypeVar("T", bound="CreateOpenApiOrderRequest")



@_attrs_define
class CreateOpenApiOrderRequest:
    

    external_order_id: None | str | Unset = UNSET
    branch_id: None | Unset | UUID = UNSET
    customer: OpenApiOrderCustomerRequest | Unset = UNSET
    items: list[OpenApiOrderItemRequest] | None | Unset = UNSET
    shipping_fee: float | None | Unset = UNSET
    paid_amount: float | None | Unset = UNSET
    cod_amount: float | None | Unset = UNSET
    payment_method: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    delivery_name: None | str | Unset = UNSET
    delivery_phone: None | str | Unset = UNSET
    delivery_address_line: None | str | Unset = UNSET
    delivery_province: None | str | Unset = UNSET
    delivery_district: None | str | Unset = UNSET
    delivery_ward: None | str | Unset = UNSET
    order_date: datetime.datetime | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.open_api_order_customer_request import OpenApiOrderCustomerRequest # noqa: PLC0415
        from ..models.open_api_order_item_request import OpenApiOrderItemRequest # noqa: PLC0415
        external_order_id: None | str | Unset
        if isinstance(self.external_order_id, Unset):
            external_order_id = UNSET
        else:
            external_order_id = self.external_order_id

        branch_id: None | str | Unset
        if isinstance(self.branch_id, Unset):
            branch_id = UNSET
        elif isinstance(self.branch_id, UUID):
            branch_id = str(self.branch_id)
        else:
            branch_id = self.branch_id

        customer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        items: list[dict[str, Any]] | None | Unset
        if isinstance(self.items, Unset):
            items = UNSET
        elif isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)


        else:
            items = self.items

        shipping_fee: float | None | Unset
        if isinstance(self.shipping_fee, Unset):
            shipping_fee = UNSET
        else:
            shipping_fee = self.shipping_fee

        paid_amount: float | None | Unset
        if isinstance(self.paid_amount, Unset):
            paid_amount = UNSET
        else:
            paid_amount = self.paid_amount

        cod_amount: float | None | Unset
        if isinstance(self.cod_amount, Unset):
            cod_amount = UNSET
        else:
            cod_amount = self.cod_amount

        payment_method: None | str | Unset
        if isinstance(self.payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = self.payment_method

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        delivery_name: None | str | Unset
        if isinstance(self.delivery_name, Unset):
            delivery_name = UNSET
        else:
            delivery_name = self.delivery_name

        delivery_phone: None | str | Unset
        if isinstance(self.delivery_phone, Unset):
            delivery_phone = UNSET
        else:
            delivery_phone = self.delivery_phone

        delivery_address_line: None | str | Unset
        if isinstance(self.delivery_address_line, Unset):
            delivery_address_line = UNSET
        else:
            delivery_address_line = self.delivery_address_line

        delivery_province: None | str | Unset
        if isinstance(self.delivery_province, Unset):
            delivery_province = UNSET
        else:
            delivery_province = self.delivery_province

        delivery_district: None | str | Unset
        if isinstance(self.delivery_district, Unset):
            delivery_district = UNSET
        else:
            delivery_district = self.delivery_district

        delivery_ward: None | str | Unset
        if isinstance(self.delivery_ward, Unset):
            delivery_ward = UNSET
        else:
            delivery_ward = self.delivery_ward

        order_date: None | str | Unset
        if isinstance(self.order_date, Unset):
            order_date = UNSET
        elif isinstance(self.order_date, datetime.datetime):
            order_date = self.order_date.isoformat()
        else:
            order_date = self.order_date


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if external_order_id is not UNSET:
            field_dict["externalOrderId"] = external_order_id
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id
        if customer is not UNSET:
            field_dict["customer"] = customer
        if items is not UNSET:
            field_dict["items"] = items
        if shipping_fee is not UNSET:
            field_dict["shippingFee"] = shipping_fee
        if paid_amount is not UNSET:
            field_dict["paidAmount"] = paid_amount
        if cod_amount is not UNSET:
            field_dict["codAmount"] = cod_amount
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method
        if notes is not UNSET:
            field_dict["notes"] = notes
        if delivery_name is not UNSET:
            field_dict["deliveryName"] = delivery_name
        if delivery_phone is not UNSET:
            field_dict["deliveryPhone"] = delivery_phone
        if delivery_address_line is not UNSET:
            field_dict["deliveryAddressLine"] = delivery_address_line
        if delivery_province is not UNSET:
            field_dict["deliveryProvince"] = delivery_province
        if delivery_district is not UNSET:
            field_dict["deliveryDistrict"] = delivery_district
        if delivery_ward is not UNSET:
            field_dict["deliveryWard"] = delivery_ward
        if order_date is not UNSET:
            field_dict["orderDate"] = order_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_api_order_customer_request import OpenApiOrderCustomerRequest # noqa: PLC0415
        from ..models.open_api_order_item_request import OpenApiOrderItemRequest # noqa: PLC0415
        d = dict(src_dict)
        def _parse_external_order_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_order_id = _parse_external_order_id(d.pop("externalOrderId", UNSET))


        def _parse_branch_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                branch_id_type_0 = UUID(data)



                return branch_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        branch_id = _parse_branch_id(d.pop("branchId", UNSET))


        _customer = d.pop("customer", UNSET)
        customer: OpenApiOrderCustomerRequest | Unset
        if isinstance(_customer,  Unset):
            customer = UNSET
        else:
            customer = OpenApiOrderCustomerRequest.from_dict(_customer)




        def _parse_items(data: object) -> list[OpenApiOrderItemRequest] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in (_items_type_0):
                    items_type_0_item = OpenApiOrderItemRequest.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OpenApiOrderItemRequest] | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))


        def _parse_shipping_fee(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shipping_fee = _parse_shipping_fee(d.pop("shippingFee", UNSET))


        def _parse_paid_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        paid_amount = _parse_paid_amount(d.pop("paidAmount", UNSET))


        def _parse_cod_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cod_amount = _parse_cod_amount(d.pop("codAmount", UNSET))


        def _parse_payment_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_method = _parse_payment_method(d.pop("paymentMethod", UNSET))


        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


        def _parse_delivery_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        delivery_name = _parse_delivery_name(d.pop("deliveryName", UNSET))


        def _parse_delivery_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        delivery_phone = _parse_delivery_phone(d.pop("deliveryPhone", UNSET))


        def _parse_delivery_address_line(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        delivery_address_line = _parse_delivery_address_line(d.pop("deliveryAddressLine", UNSET))


        def _parse_delivery_province(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        delivery_province = _parse_delivery_province(d.pop("deliveryProvince", UNSET))


        def _parse_delivery_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        delivery_district = _parse_delivery_district(d.pop("deliveryDistrict", UNSET))


        def _parse_delivery_ward(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        delivery_ward = _parse_delivery_ward(d.pop("deliveryWard", UNSET))


        def _parse_order_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                order_date_type_0 = datetime.datetime.fromisoformat(data)



                return order_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        order_date = _parse_order_date(d.pop("orderDate", UNSET))


        create_open_api_order_request = cls(
            external_order_id=external_order_id,
            branch_id=branch_id,
            customer=customer,
            items=items,
            shipping_fee=shipping_fee,
            paid_amount=paid_amount,
            cod_amount=cod_amount,
            payment_method=payment_method,
            notes=notes,
            delivery_name=delivery_name,
            delivery_phone=delivery_phone,
            delivery_address_line=delivery_address_line,
            delivery_province=delivery_province,
            delivery_district=delivery_district,
            delivery_ward=delivery_ward,
            order_date=order_date,
        )

        return create_open_api_order_request


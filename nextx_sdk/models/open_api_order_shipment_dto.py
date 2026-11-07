from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OpenApiOrderShipmentDto")



@_attrs_define
class OpenApiOrderShipmentDto:
    

    carrier_code: None | str | Unset = UNSET
    tracking_code: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    shipping_fee: float | Unset = UNSET
    cod_amount: float | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        carrier_code: None | str | Unset
        if isinstance(self.carrier_code, Unset):
            carrier_code = UNSET
        else:
            carrier_code = self.carrier_code

        tracking_code: None | str | Unset
        if isinstance(self.tracking_code, Unset):
            tracking_code = UNSET
        else:
            tracking_code = self.tracking_code

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        shipping_fee = self.shipping_fee

        cod_amount: float | None | Unset
        if isinstance(self.cod_amount, Unset):
            cod_amount = UNSET
        else:
            cod_amount = self.cod_amount


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if carrier_code is not UNSET:
            field_dict["carrierCode"] = carrier_code
        if tracking_code is not UNSET:
            field_dict["trackingCode"] = tracking_code
        if status is not UNSET:
            field_dict["status"] = status
        if shipping_fee is not UNSET:
            field_dict["shippingFee"] = shipping_fee
        if cod_amount is not UNSET:
            field_dict["codAmount"] = cod_amount

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_carrier_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        carrier_code = _parse_carrier_code(d.pop("carrierCode", UNSET))


        def _parse_tracking_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tracking_code = _parse_tracking_code(d.pop("trackingCode", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        shipping_fee = d.pop("shippingFee", UNSET)

        def _parse_cod_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cod_amount = _parse_cod_amount(d.pop("codAmount", UNSET))


        open_api_order_shipment_dto = cls(
            carrier_code=carrier_code,
            tracking_code=tracking_code,
            status=status,
            shipping_fee=shipping_fee,
            cod_amount=cod_amount,
        )

        return open_api_order_shipment_dto


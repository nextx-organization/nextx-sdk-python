from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OrderShippingPlanDto")



@_attrs_define
class OrderShippingPlanDto:
    

    carrier_code: None | str | Unset = UNSET
    carrier_config_id: None | Unset | UUID = UNSET
    service_type: None | str | Unset = UNSET
    weight_grams: int | None | Unset = UNSET
    length_cm: int | None | Unset = UNSET
    width_cm: int | None | Unset = UNSET
    height_cm: int | None | Unset = UNSET
    carrier_options: Any | Unset = UNSET
    estimated_fee: float | None | Unset = UNSET
    freeship_code: None | str | Unset = UNSET
    note: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        carrier_code: None | str | Unset
        if isinstance(self.carrier_code, Unset):
            carrier_code = UNSET
        else:
            carrier_code = self.carrier_code

        carrier_config_id: None | str | Unset
        if isinstance(self.carrier_config_id, Unset):
            carrier_config_id = UNSET
        elif isinstance(self.carrier_config_id, UUID):
            carrier_config_id = str(self.carrier_config_id)
        else:
            carrier_config_id = self.carrier_config_id

        service_type: None | str | Unset
        if isinstance(self.service_type, Unset):
            service_type = UNSET
        else:
            service_type = self.service_type

        weight_grams: int | None | Unset
        if isinstance(self.weight_grams, Unset):
            weight_grams = UNSET
        else:
            weight_grams = self.weight_grams

        length_cm: int | None | Unset
        if isinstance(self.length_cm, Unset):
            length_cm = UNSET
        else:
            length_cm = self.length_cm

        width_cm: int | None | Unset
        if isinstance(self.width_cm, Unset):
            width_cm = UNSET
        else:
            width_cm = self.width_cm

        height_cm: int | None | Unset
        if isinstance(self.height_cm, Unset):
            height_cm = UNSET
        else:
            height_cm = self.height_cm

        carrier_options = self.carrier_options

        estimated_fee: float | None | Unset
        if isinstance(self.estimated_fee, Unset):
            estimated_fee = UNSET
        else:
            estimated_fee = self.estimated_fee

        freeship_code: None | str | Unset
        if isinstance(self.freeship_code, Unset):
            freeship_code = UNSET
        else:
            freeship_code = self.freeship_code

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if carrier_code is not UNSET:
            field_dict["carrierCode"] = carrier_code
        if carrier_config_id is not UNSET:
            field_dict["carrierConfigId"] = carrier_config_id
        if service_type is not UNSET:
            field_dict["serviceType"] = service_type
        if weight_grams is not UNSET:
            field_dict["weightGrams"] = weight_grams
        if length_cm is not UNSET:
            field_dict["lengthCm"] = length_cm
        if width_cm is not UNSET:
            field_dict["widthCm"] = width_cm
        if height_cm is not UNSET:
            field_dict["heightCm"] = height_cm
        if carrier_options is not UNSET:
            field_dict["carrierOptions"] = carrier_options
        if estimated_fee is not UNSET:
            field_dict["estimatedFee"] = estimated_fee
        if freeship_code is not UNSET:
            field_dict["freeshipCode"] = freeship_code
        if note is not UNSET:
            field_dict["note"] = note

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


        def _parse_carrier_config_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                carrier_config_id_type_0 = UUID(data)



                return carrier_config_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        carrier_config_id = _parse_carrier_config_id(d.pop("carrierConfigId", UNSET))


        def _parse_service_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_type = _parse_service_type(d.pop("serviceType", UNSET))


        def _parse_weight_grams(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        weight_grams = _parse_weight_grams(d.pop("weightGrams", UNSET))


        def _parse_length_cm(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        length_cm = _parse_length_cm(d.pop("lengthCm", UNSET))


        def _parse_width_cm(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        width_cm = _parse_width_cm(d.pop("widthCm", UNSET))


        def _parse_height_cm(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        height_cm = _parse_height_cm(d.pop("heightCm", UNSET))


        carrier_options = d.pop("carrierOptions", UNSET)

        def _parse_estimated_fee(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        estimated_fee = _parse_estimated_fee(d.pop("estimatedFee", UNSET))


        def _parse_freeship_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        freeship_code = _parse_freeship_code(d.pop("freeshipCode", UNSET))


        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        order_shipping_plan_dto = cls(
            carrier_code=carrier_code,
            carrier_config_id=carrier_config_id,
            service_type=service_type,
            weight_grams=weight_grams,
            length_cm=length_cm,
            width_cm=width_cm,
            height_cm=height_cm,
            carrier_options=carrier_options,
            estimated_fee=estimated_fee,
            freeship_code=freeship_code,
            note=note,
        )

        return order_shipping_plan_dto


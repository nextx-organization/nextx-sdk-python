from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OrderItemTrackingDto")



@_attrs_define
class OrderItemTrackingDto:
    

    type_: None | str | Unset = UNSET
    lot_id: None | Unset | UUID = UNSET
    lot_number: None | str | Unset = UNSET
    imei_serial: None | str | Unset = UNSET
    imei_serials: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        lot_id: None | str | Unset
        if isinstance(self.lot_id, Unset):
            lot_id = UNSET
        elif isinstance(self.lot_id, UUID):
            lot_id = str(self.lot_id)
        else:
            lot_id = self.lot_id

        lot_number: None | str | Unset
        if isinstance(self.lot_number, Unset):
            lot_number = UNSET
        else:
            lot_number = self.lot_number

        imei_serial: None | str | Unset
        if isinstance(self.imei_serial, Unset):
            imei_serial = UNSET
        else:
            imei_serial = self.imei_serial

        imei_serials: list[str] | None | Unset
        if isinstance(self.imei_serials, Unset):
            imei_serials = UNSET
        elif isinstance(self.imei_serials, list):
            imei_serials = self.imei_serials


        else:
            imei_serials = self.imei_serials


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if lot_id is not UNSET:
            field_dict["lotId"] = lot_id
        if lot_number is not UNSET:
            field_dict["lotNumber"] = lot_number
        if imei_serial is not UNSET:
            field_dict["imeiSerial"] = imei_serial
        if imei_serials is not UNSET:
            field_dict["imeiSerials"] = imei_serials

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))


        def _parse_lot_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                lot_id_type_0 = UUID(data)



                return lot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        lot_id = _parse_lot_id(d.pop("lotId", UNSET))


        def _parse_lot_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lot_number = _parse_lot_number(d.pop("lotNumber", UNSET))


        def _parse_imei_serial(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        imei_serial = _parse_imei_serial(d.pop("imeiSerial", UNSET))


        def _parse_imei_serials(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                imei_serials_type_0 = cast(list[str], data)

                return imei_serials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        imei_serials = _parse_imei_serials(d.pop("imeiSerials", UNSET))


        order_item_tracking_dto = cls(
            type_=type_,
            lot_id=lot_id,
            lot_number=lot_number,
            imei_serial=imei_serial,
            imei_serials=imei_serials,
        )

        return order_item_tracking_dto


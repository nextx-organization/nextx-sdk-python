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






T = TypeVar("T", bound="TimelineEventRow")



@_attrs_define
class TimelineEventRow:
    

    punch_id: None | Unset | UUID = UNSET
    clock_record_id: None | Unset | UUID = UNSET
    at: datetime.datetime | Unset = UNSET
    type_: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    is_manual: bool | Unset = UNSET
    device_name: None | str | Unset = UNSET
    credential_type: None | str | Unset = UNSET
    photo_storage_key: None | str | Unset = UNSET
    photo_url: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        punch_id: None | str | Unset
        if isinstance(self.punch_id, Unset):
            punch_id = UNSET
        elif isinstance(self.punch_id, UUID):
            punch_id = str(self.punch_id)
        else:
            punch_id = self.punch_id

        clock_record_id: None | str | Unset
        if isinstance(self.clock_record_id, Unset):
            clock_record_id = UNSET
        elif isinstance(self.clock_record_id, UUID):
            clock_record_id = str(self.clock_record_id)
        else:
            clock_record_id = self.clock_record_id

        at: str | Unset = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.isoformat()

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        is_manual = self.is_manual

        device_name: None | str | Unset
        if isinstance(self.device_name, Unset):
            device_name = UNSET
        else:
            device_name = self.device_name

        credential_type: None | str | Unset
        if isinstance(self.credential_type, Unset):
            credential_type = UNSET
        else:
            credential_type = self.credential_type

        photo_storage_key: None | str | Unset
        if isinstance(self.photo_storage_key, Unset):
            photo_storage_key = UNSET
        else:
            photo_storage_key = self.photo_storage_key

        photo_url: None | str | Unset
        if isinstance(self.photo_url, Unset):
            photo_url = UNSET
        else:
            photo_url = self.photo_url


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if punch_id is not UNSET:
            field_dict["punchId"] = punch_id
        if clock_record_id is not UNSET:
            field_dict["clockRecordId"] = clock_record_id
        if at is not UNSET:
            field_dict["at"] = at
        if type_ is not UNSET:
            field_dict["type"] = type_
        if source is not UNSET:
            field_dict["source"] = source
        if is_manual is not UNSET:
            field_dict["isManual"] = is_manual
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if credential_type is not UNSET:
            field_dict["credentialType"] = credential_type
        if photo_storage_key is not UNSET:
            field_dict["photoStorageKey"] = photo_storage_key
        if photo_url is not UNSET:
            field_dict["photoUrl"] = photo_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_punch_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                punch_id_type_0 = UUID(data)



                return punch_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        punch_id = _parse_punch_id(d.pop("punchId", UNSET))


        def _parse_clock_record_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                clock_record_id_type_0 = UUID(data)



                return clock_record_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        clock_record_id = _parse_clock_record_id(d.pop("clockRecordId", UNSET))


        _at = d.pop("at", UNSET)
        at: datetime.datetime | Unset
        if isinstance(_at,  Unset):
            at = UNSET
        else:
            at = datetime.datetime.fromisoformat(_at)




        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))


        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))


        is_manual = d.pop("isManual", UNSET)

        def _parse_device_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_name = _parse_device_name(d.pop("deviceName", UNSET))


        def _parse_credential_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        credential_type = _parse_credential_type(d.pop("credentialType", UNSET))


        def _parse_photo_storage_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        photo_storage_key = _parse_photo_storage_key(d.pop("photoStorageKey", UNSET))


        def _parse_photo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        photo_url = _parse_photo_url(d.pop("photoUrl", UNSET))


        timeline_event_row = cls(
            punch_id=punch_id,
            clock_record_id=clock_record_id,
            at=at,
            type_=type_,
            source=source,
            is_manual=is_manual,
            device_name=device_name,
            credential_type=credential_type,
            photo_storage_key=photo_storage_key,
            photo_url=photo_url,
        )

        return timeline_event_row


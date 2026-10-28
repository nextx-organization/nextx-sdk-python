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






T = TypeVar("T", bound="AttendanceRawPunchDto")



@_attrs_define
class AttendanceRawPunchDto:
    

    id: UUID | Unset = UNSET
    employee_id: None | Unset | UUID = UNSET
    employee_name: None | str | Unset = UNSET
    employee_code: None | str | Unset = UNSET
    device_id: None | Unset | UUID = UNSET
    device_serial: None | str | Unset = UNSET
    device_name: None | str | Unset = UNSET
    device_user_id: None | str | Unset = UNSET
    punched_at: datetime.datetime | Unset = UNSET
    credential_type: None | str | Unset = UNSET
    ingest_source: None | str | Unset = UNSET
    process_status: None | str | Unset = UNSET
    process_error: None | str | Unset = UNSET
    photo_storage_key: None | str | Unset = UNSET
    photo_url: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    master_punch_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        employee_id: None | str | Unset
        if isinstance(self.employee_id, Unset):
            employee_id = UNSET
        elif isinstance(self.employee_id, UUID):
            employee_id = str(self.employee_id)
        else:
            employee_id = self.employee_id

        employee_name: None | str | Unset
        if isinstance(self.employee_name, Unset):
            employee_name = UNSET
        else:
            employee_name = self.employee_name

        employee_code: None | str | Unset
        if isinstance(self.employee_code, Unset):
            employee_code = UNSET
        else:
            employee_code = self.employee_code

        device_id: None | str | Unset
        if isinstance(self.device_id, Unset):
            device_id = UNSET
        elif isinstance(self.device_id, UUID):
            device_id = str(self.device_id)
        else:
            device_id = self.device_id

        device_serial: None | str | Unset
        if isinstance(self.device_serial, Unset):
            device_serial = UNSET
        else:
            device_serial = self.device_serial

        device_name: None | str | Unset
        if isinstance(self.device_name, Unset):
            device_name = UNSET
        else:
            device_name = self.device_name

        device_user_id: None | str | Unset
        if isinstance(self.device_user_id, Unset):
            device_user_id = UNSET
        else:
            device_user_id = self.device_user_id

        punched_at: str | Unset = UNSET
        if not isinstance(self.punched_at, Unset):
            punched_at = self.punched_at.isoformat()

        credential_type: None | str | Unset
        if isinstance(self.credential_type, Unset):
            credential_type = UNSET
        else:
            credential_type = self.credential_type

        ingest_source: None | str | Unset
        if isinstance(self.ingest_source, Unset):
            ingest_source = UNSET
        else:
            ingest_source = self.ingest_source

        process_status: None | str | Unset
        if isinstance(self.process_status, Unset):
            process_status = UNSET
        else:
            process_status = self.process_status

        process_error: None | str | Unset
        if isinstance(self.process_error, Unset):
            process_error = UNSET
        else:
            process_error = self.process_error

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

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        master_punch_id: None | str | Unset
        if isinstance(self.master_punch_id, Unset):
            master_punch_id = UNSET
        elif isinstance(self.master_punch_id, UUID):
            master_punch_id = str(self.master_punch_id)
        else:
            master_punch_id = self.master_punch_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if employee_id is not UNSET:
            field_dict["employeeId"] = employee_id
        if employee_name is not UNSET:
            field_dict["employeeName"] = employee_name
        if employee_code is not UNSET:
            field_dict["employeeCode"] = employee_code
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if device_serial is not UNSET:
            field_dict["deviceSerial"] = device_serial
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if device_user_id is not UNSET:
            field_dict["deviceUserId"] = device_user_id
        if punched_at is not UNSET:
            field_dict["punchedAt"] = punched_at
        if credential_type is not UNSET:
            field_dict["credentialType"] = credential_type
        if ingest_source is not UNSET:
            field_dict["ingestSource"] = ingest_source
        if process_status is not UNSET:
            field_dict["processStatus"] = process_status
        if process_error is not UNSET:
            field_dict["processError"] = process_error
        if photo_storage_key is not UNSET:
            field_dict["photoStorageKey"] = photo_storage_key
        if photo_url is not UNSET:
            field_dict["photoUrl"] = photo_url
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if master_punch_id is not UNSET:
            field_dict["masterPunchId"] = master_punch_id

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




        def _parse_employee_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                employee_id_type_0 = UUID(data)



                return employee_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        employee_id = _parse_employee_id(d.pop("employeeId", UNSET))


        def _parse_employee_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        employee_name = _parse_employee_name(d.pop("employeeName", UNSET))


        def _parse_employee_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        employee_code = _parse_employee_code(d.pop("employeeCode", UNSET))


        def _parse_device_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                device_id_type_0 = UUID(data)



                return device_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        device_id = _parse_device_id(d.pop("deviceId", UNSET))


        def _parse_device_serial(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_serial = _parse_device_serial(d.pop("deviceSerial", UNSET))


        def _parse_device_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_name = _parse_device_name(d.pop("deviceName", UNSET))


        def _parse_device_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_user_id = _parse_device_user_id(d.pop("deviceUserId", UNSET))


        _punched_at = d.pop("punchedAt", UNSET)
        punched_at: datetime.datetime | Unset
        if isinstance(_punched_at,  Unset):
            punched_at = UNSET
        else:
            punched_at = datetime.datetime.fromisoformat(_punched_at)




        def _parse_credential_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        credential_type = _parse_credential_type(d.pop("credentialType", UNSET))


        def _parse_ingest_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ingest_source = _parse_ingest_source(d.pop("ingestSource", UNSET))


        def _parse_process_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        process_status = _parse_process_status(d.pop("processStatus", UNSET))


        def _parse_process_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        process_error = _parse_process_error(d.pop("processError", UNSET))


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


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_master_punch_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                master_punch_id_type_0 = UUID(data)



                return master_punch_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        master_punch_id = _parse_master_punch_id(d.pop("masterPunchId", UNSET))


        attendance_raw_punch_dto = cls(
            id=id,
            employee_id=employee_id,
            employee_name=employee_name,
            employee_code=employee_code,
            device_id=device_id,
            device_serial=device_serial,
            device_name=device_name,
            device_user_id=device_user_id,
            punched_at=punched_at,
            credential_type=credential_type,
            ingest_source=ingest_source,
            process_status=process_status,
            process_error=process_error,
            photo_storage_key=photo_storage_key,
            photo_url=photo_url,
            created_at=created_at,
            master_punch_id=master_punch_id,
        )

        return attendance_raw_punch_dto


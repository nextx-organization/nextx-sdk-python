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






T = TypeVar("T", bound="EmployeeDeviceCredentialDto")



@_attrs_define
class EmployeeDeviceCredentialDto:
    

    id: UUID | Unset = UNSET
    employee_id: UUID | Unset = UNSET
    device_id: UUID | Unset = UNSET
    device_user_id: None | str | Unset = UNSET
    credential_type: None | str | Unset = UNSET
    finger_index: int | None | Unset = UNSET
    device_vendor: None | str | Unset = UNSET
    sync_status: None | str | Unset = UNSET
    synced_at: datetime.datetime | None | Unset = UNSET
    sync_error: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    device_name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        employee_id: str | Unset = UNSET
        if not isinstance(self.employee_id, Unset):
            employee_id = str(self.employee_id)

        device_id: str | Unset = UNSET
        if not isinstance(self.device_id, Unset):
            device_id = str(self.device_id)

        device_user_id: None | str | Unset
        if isinstance(self.device_user_id, Unset):
            device_user_id = UNSET
        else:
            device_user_id = self.device_user_id

        credential_type: None | str | Unset
        if isinstance(self.credential_type, Unset):
            credential_type = UNSET
        else:
            credential_type = self.credential_type

        finger_index: int | None | Unset
        if isinstance(self.finger_index, Unset):
            finger_index = UNSET
        else:
            finger_index = self.finger_index

        device_vendor: None | str | Unset
        if isinstance(self.device_vendor, Unset):
            device_vendor = UNSET
        else:
            device_vendor = self.device_vendor

        sync_status: None | str | Unset
        if isinstance(self.sync_status, Unset):
            sync_status = UNSET
        else:
            sync_status = self.sync_status

        synced_at: None | str | Unset
        if isinstance(self.synced_at, Unset):
            synced_at = UNSET
        elif isinstance(self.synced_at, datetime.datetime):
            synced_at = self.synced_at.isoformat()
        else:
            synced_at = self.synced_at

        sync_error: None | str | Unset
        if isinstance(self.sync_error, Unset):
            sync_error = UNSET
        else:
            sync_error = self.sync_error

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        device_name: None | str | Unset
        if isinstance(self.device_name, Unset):
            device_name = UNSET
        else:
            device_name = self.device_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if employee_id is not UNSET:
            field_dict["employeeId"] = employee_id
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if device_user_id is not UNSET:
            field_dict["deviceUserId"] = device_user_id
        if credential_type is not UNSET:
            field_dict["credentialType"] = credential_type
        if finger_index is not UNSET:
            field_dict["fingerIndex"] = finger_index
        if device_vendor is not UNSET:
            field_dict["deviceVendor"] = device_vendor
        if sync_status is not UNSET:
            field_dict["syncStatus"] = sync_status
        if synced_at is not UNSET:
            field_dict["syncedAt"] = synced_at
        if sync_error is not UNSET:
            field_dict["syncError"] = sync_error
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name

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




        _employee_id = d.pop("employeeId", UNSET)
        employee_id: UUID | Unset
        if isinstance(_employee_id,  Unset):
            employee_id = UNSET
        else:
            employee_id = UUID(_employee_id)




        _device_id = d.pop("deviceId", UNSET)
        device_id: UUID | Unset
        if isinstance(_device_id,  Unset):
            device_id = UNSET
        else:
            device_id = UUID(_device_id)




        def _parse_device_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_user_id = _parse_device_user_id(d.pop("deviceUserId", UNSET))


        def _parse_credential_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        credential_type = _parse_credential_type(d.pop("credentialType", UNSET))


        def _parse_finger_index(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        finger_index = _parse_finger_index(d.pop("fingerIndex", UNSET))


        def _parse_device_vendor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_vendor = _parse_device_vendor(d.pop("deviceVendor", UNSET))


        def _parse_sync_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sync_status = _parse_sync_status(d.pop("syncStatus", UNSET))


        def _parse_synced_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                synced_at_type_0 = datetime.datetime.fromisoformat(data)



                return synced_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        synced_at = _parse_synced_at(d.pop("syncedAt", UNSET))


        def _parse_sync_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sync_error = _parse_sync_error(d.pop("syncError", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_device_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_name = _parse_device_name(d.pop("deviceName", UNSET))


        employee_device_credential_dto = cls(
            id=id,
            employee_id=employee_id,
            device_id=device_id,
            device_user_id=device_user_id,
            credential_type=credential_type,
            finger_index=finger_index,
            device_vendor=device_vendor,
            sync_status=sync_status,
            synced_at=synced_at,
            sync_error=sync_error,
            created_at=created_at,
            device_name=device_name,
        )

        return employee_device_credential_dto


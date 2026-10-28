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






T = TypeVar("T", bound="AttendanceDeviceDto")



@_attrs_define
class AttendanceDeviceDto:
    

    id: UUID | Unset = UNSET
    device_name: None | str | Unset = UNSET
    device_serial: None | str | Unset = UNSET
    branch_id: None | Unset | UUID = UNSET
    vendor: None | str | Unset = UNSET
    protocol: None | str | Unset = UNSET
    ip_address: None | str | Unset = UNSET
    port: int | Unset = UNSET
    model_name: None | str | Unset = UNSET
    is_online: bool | Unset = UNSET
    is_active: bool | Unset = UNSET
    last_ping_at: datetime.datetime | None | Unset = UNSET
    last_event_at: datetime.datetime | None | Unset = UNSET
    role: None | str | Unset = UNSET
    supports_face: bool | Unset = UNSET
    supports_fingerprint: bool | Unset = UNSET
    supports_card: bool | Unset = UNSET
    supports_qr: bool | Unset = UNSET
    firmware_version: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    hik_username: None | str | Unset = UNSET
    auth_blocked: bool | Unset = UNSET
    auth_blocked_reason: None | str | Unset = UNSET
    face_used: int | None | Unset = UNSET
    face_max: int | None | Unset = UNSET
    supports_capture_face_data: bool | None | Unset = UNSET
    last_punch_at: datetime.datetime | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        device_name: None | str | Unset
        if isinstance(self.device_name, Unset):
            device_name = UNSET
        else:
            device_name = self.device_name

        device_serial: None | str | Unset
        if isinstance(self.device_serial, Unset):
            device_serial = UNSET
        else:
            device_serial = self.device_serial

        branch_id: None | str | Unset
        if isinstance(self.branch_id, Unset):
            branch_id = UNSET
        elif isinstance(self.branch_id, UUID):
            branch_id = str(self.branch_id)
        else:
            branch_id = self.branch_id

        vendor: None | str | Unset
        if isinstance(self.vendor, Unset):
            vendor = UNSET
        else:
            vendor = self.vendor

        protocol: None | str | Unset
        if isinstance(self.protocol, Unset):
            protocol = UNSET
        else:
            protocol = self.protocol

        ip_address: None | str | Unset
        if isinstance(self.ip_address, Unset):
            ip_address = UNSET
        else:
            ip_address = self.ip_address

        port = self.port

        model_name: None | str | Unset
        if isinstance(self.model_name, Unset):
            model_name = UNSET
        else:
            model_name = self.model_name

        is_online = self.is_online

        is_active = self.is_active

        last_ping_at: None | str | Unset
        if isinstance(self.last_ping_at, Unset):
            last_ping_at = UNSET
        elif isinstance(self.last_ping_at, datetime.datetime):
            last_ping_at = self.last_ping_at.isoformat()
        else:
            last_ping_at = self.last_ping_at

        last_event_at: None | str | Unset
        if isinstance(self.last_event_at, Unset):
            last_event_at = UNSET
        elif isinstance(self.last_event_at, datetime.datetime):
            last_event_at = self.last_event_at.isoformat()
        else:
            last_event_at = self.last_event_at

        role: None | str | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        supports_face = self.supports_face

        supports_fingerprint = self.supports_fingerprint

        supports_card = self.supports_card

        supports_qr = self.supports_qr

        firmware_version: None | str | Unset
        if isinstance(self.firmware_version, Unset):
            firmware_version = UNSET
        else:
            firmware_version = self.firmware_version

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        hik_username: None | str | Unset
        if isinstance(self.hik_username, Unset):
            hik_username = UNSET
        else:
            hik_username = self.hik_username

        auth_blocked = self.auth_blocked

        auth_blocked_reason: None | str | Unset
        if isinstance(self.auth_blocked_reason, Unset):
            auth_blocked_reason = UNSET
        else:
            auth_blocked_reason = self.auth_blocked_reason

        face_used: int | None | Unset
        if isinstance(self.face_used, Unset):
            face_used = UNSET
        else:
            face_used = self.face_used

        face_max: int | None | Unset
        if isinstance(self.face_max, Unset):
            face_max = UNSET
        else:
            face_max = self.face_max

        supports_capture_face_data: bool | None | Unset
        if isinstance(self.supports_capture_face_data, Unset):
            supports_capture_face_data = UNSET
        else:
            supports_capture_face_data = self.supports_capture_face_data

        last_punch_at: None | str | Unset
        if isinstance(self.last_punch_at, Unset):
            last_punch_at = UNSET
        elif isinstance(self.last_punch_at, datetime.datetime):
            last_punch_at = self.last_punch_at.isoformat()
        else:
            last_punch_at = self.last_punch_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if device_serial is not UNSET:
            field_dict["deviceSerial"] = device_serial
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address
        if port is not UNSET:
            field_dict["port"] = port
        if model_name is not UNSET:
            field_dict["modelName"] = model_name
        if is_online is not UNSET:
            field_dict["isOnline"] = is_online
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if last_ping_at is not UNSET:
            field_dict["lastPingAt"] = last_ping_at
        if last_event_at is not UNSET:
            field_dict["lastEventAt"] = last_event_at
        if role is not UNSET:
            field_dict["role"] = role
        if supports_face is not UNSET:
            field_dict["supportsFace"] = supports_face
        if supports_fingerprint is not UNSET:
            field_dict["supportsFingerprint"] = supports_fingerprint
        if supports_card is not UNSET:
            field_dict["supportsCard"] = supports_card
        if supports_qr is not UNSET:
            field_dict["supportsQr"] = supports_qr
        if firmware_version is not UNSET:
            field_dict["firmwareVersion"] = firmware_version
        if notes is not UNSET:
            field_dict["notes"] = notes
        if hik_username is not UNSET:
            field_dict["hikUsername"] = hik_username
        if auth_blocked is not UNSET:
            field_dict["authBlocked"] = auth_blocked
        if auth_blocked_reason is not UNSET:
            field_dict["authBlockedReason"] = auth_blocked_reason
        if face_used is not UNSET:
            field_dict["faceUsed"] = face_used
        if face_max is not UNSET:
            field_dict["faceMax"] = face_max
        if supports_capture_face_data is not UNSET:
            field_dict["supportsCaptureFaceData"] = supports_capture_face_data
        if last_punch_at is not UNSET:
            field_dict["lastPunchAt"] = last_punch_at

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




        def _parse_device_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_name = _parse_device_name(d.pop("deviceName", UNSET))


        def _parse_device_serial(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_serial = _parse_device_serial(d.pop("deviceSerial", UNSET))


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


        def _parse_vendor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vendor = _parse_vendor(d.pop("vendor", UNSET))


        def _parse_protocol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        protocol = _parse_protocol(d.pop("protocol", UNSET))


        def _parse_ip_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip_address = _parse_ip_address(d.pop("ipAddress", UNSET))


        port = d.pop("port", UNSET)

        def _parse_model_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_name = _parse_model_name(d.pop("modelName", UNSET))


        is_online = d.pop("isOnline", UNSET)

        is_active = d.pop("isActive", UNSET)

        def _parse_last_ping_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_ping_at_type_0 = datetime.datetime.fromisoformat(data)



                return last_ping_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_ping_at = _parse_last_ping_at(d.pop("lastPingAt", UNSET))


        def _parse_last_event_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_event_at_type_0 = datetime.datetime.fromisoformat(data)



                return last_event_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_event_at = _parse_last_event_at(d.pop("lastEventAt", UNSET))


        def _parse_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role = _parse_role(d.pop("role", UNSET))


        supports_face = d.pop("supportsFace", UNSET)

        supports_fingerprint = d.pop("supportsFingerprint", UNSET)

        supports_card = d.pop("supportsCard", UNSET)

        supports_qr = d.pop("supportsQr", UNSET)

        def _parse_firmware_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        firmware_version = _parse_firmware_version(d.pop("firmwareVersion", UNSET))


        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


        def _parse_hik_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hik_username = _parse_hik_username(d.pop("hikUsername", UNSET))


        auth_blocked = d.pop("authBlocked", UNSET)

        def _parse_auth_blocked_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        auth_blocked_reason = _parse_auth_blocked_reason(d.pop("authBlockedReason", UNSET))


        def _parse_face_used(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        face_used = _parse_face_used(d.pop("faceUsed", UNSET))


        def _parse_face_max(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        face_max = _parse_face_max(d.pop("faceMax", UNSET))


        def _parse_supports_capture_face_data(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        supports_capture_face_data = _parse_supports_capture_face_data(d.pop("supportsCaptureFaceData", UNSET))


        def _parse_last_punch_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_punch_at_type_0 = datetime.datetime.fromisoformat(data)



                return last_punch_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_punch_at = _parse_last_punch_at(d.pop("lastPunchAt", UNSET))


        attendance_device_dto = cls(
            id=id,
            device_name=device_name,
            device_serial=device_serial,
            branch_id=branch_id,
            vendor=vendor,
            protocol=protocol,
            ip_address=ip_address,
            port=port,
            model_name=model_name,
            is_online=is_online,
            is_active=is_active,
            last_ping_at=last_ping_at,
            last_event_at=last_event_at,
            role=role,
            supports_face=supports_face,
            supports_fingerprint=supports_fingerprint,
            supports_card=supports_card,
            supports_qr=supports_qr,
            firmware_version=firmware_version,
            notes=notes,
            hik_username=hik_username,
            auth_blocked=auth_blocked,
            auth_blocked_reason=auth_blocked_reason,
            face_used=face_used,
            face_max=face_max,
            supports_capture_face_data=supports_capture_face_data,
            last_punch_at=last_punch_at,
        )

        return attendance_device_dto


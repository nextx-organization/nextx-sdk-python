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






T = TypeVar("T", bound="CheckInDto")



@_attrs_define
class CheckInDto:
    

    id: UUID | Unset = UNSET
    branch_id: None | Unset | UUID = UNSET
    gym_profile_id: UUID | Unset = UNSET
    member_code: None | str | Unset = UNSET
    member_name: None | str | Unset = UNSET
    checkin_type: None | str | Unset = UNSET
    credential_type: None | str | Unset = UNSET
    checkin_time: datetime.datetime | Unset = UNSET
    checkout_time: datetime.datetime | None | Unset = UNSET
    is_valid: bool | Unset = UNSET
    invalid_reason: None | str | Unset = UNSET
    is_manual_override: bool | Unset = UNSET
    device_name: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    zone_id: None | Unset | UUID = UNSET
    access_decision: None | str | Unset = UNSET
    deny_reason: None | str | Unset = UNSET
    ticket_id: None | Unset | UUID = UNSET
    ticket_code: None | str | Unset = UNSET
    guest_name: None | str | Unset = UNSET
    guest_phone: None | str | Unset = UNSET
    subscription_id: None | Unset | UUID = UNSET
    contract_code: None | str | Unset = UNSET
    package_name: None | str | Unset = UNSET
    avatar_key: None | str | Unset = UNSET
    branch_name: None | str | Unset = UNSET
    avatar_url: None | str | Unset = UNSET
    subscription_status: None | str | Unset = UNSET
    subscription_expire_date: datetime.date | None | Unset = UNSET
    subscription_total_sessions: int | None | Unset = UNSET
    subscription_used_sessions: int | None | Unset = UNSET
    package_mode: None | str | Unset = UNSET
    sessions_remaining_snapshot: int | None | Unset = UNSET
    pt_id: None | Unset | UUID = UNSET
    pt_name: None | str | Unset = UNSET
    sessions_deducted: int | None | Unset = UNSET
    service_code: None | str | Unset = UNSET
    checkin_source: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    package_type: None | str | Unset = UNSET
    group_member_allocation: int | None | Unset = UNSET
    group_member_remaining: int | None | Unset = UNSET
    has_photo: bool | Unset = UNSET
    photo_url: None | str | Unset = UNSET
    registered_face_url: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    debt_remaining: float | None | Unset = UNSET
    checkin_count_today: int | None | Unset = UNSET
    member_note: None | str | Unset = UNSET
    contract_note: None | str | Unset = UNSET
    package_note: None | str | Unset = UNSET
    pt_code: None | str | Unset = UNSET
    pt_avatar_url: None | str | Unset = UNSET
    gym_hours: None | str | Unset = UNSET
    sale_staff_name: None | str | Unset = UNSET
    days_remaining: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        branch_id: None | str | Unset
        if isinstance(self.branch_id, Unset):
            branch_id = UNSET
        elif isinstance(self.branch_id, UUID):
            branch_id = str(self.branch_id)
        else:
            branch_id = self.branch_id

        gym_profile_id: str | Unset = UNSET
        if not isinstance(self.gym_profile_id, Unset):
            gym_profile_id = str(self.gym_profile_id)

        member_code: None | str | Unset
        if isinstance(self.member_code, Unset):
            member_code = UNSET
        else:
            member_code = self.member_code

        member_name: None | str | Unset
        if isinstance(self.member_name, Unset):
            member_name = UNSET
        else:
            member_name = self.member_name

        checkin_type: None | str | Unset
        if isinstance(self.checkin_type, Unset):
            checkin_type = UNSET
        else:
            checkin_type = self.checkin_type

        credential_type: None | str | Unset
        if isinstance(self.credential_type, Unset):
            credential_type = UNSET
        else:
            credential_type = self.credential_type

        checkin_time: str | Unset = UNSET
        if not isinstance(self.checkin_time, Unset):
            checkin_time = self.checkin_time.isoformat()

        checkout_time: None | str | Unset
        if isinstance(self.checkout_time, Unset):
            checkout_time = UNSET
        elif isinstance(self.checkout_time, datetime.datetime):
            checkout_time = self.checkout_time.isoformat()
        else:
            checkout_time = self.checkout_time

        is_valid = self.is_valid

        invalid_reason: None | str | Unset
        if isinstance(self.invalid_reason, Unset):
            invalid_reason = UNSET
        else:
            invalid_reason = self.invalid_reason

        is_manual_override = self.is_manual_override

        device_name: None | str | Unset
        if isinstance(self.device_name, Unset):
            device_name = UNSET
        else:
            device_name = self.device_name

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        zone_id: None | str | Unset
        if isinstance(self.zone_id, Unset):
            zone_id = UNSET
        elif isinstance(self.zone_id, UUID):
            zone_id = str(self.zone_id)
        else:
            zone_id = self.zone_id

        access_decision: None | str | Unset
        if isinstance(self.access_decision, Unset):
            access_decision = UNSET
        else:
            access_decision = self.access_decision

        deny_reason: None | str | Unset
        if isinstance(self.deny_reason, Unset):
            deny_reason = UNSET
        else:
            deny_reason = self.deny_reason

        ticket_id: None | str | Unset
        if isinstance(self.ticket_id, Unset):
            ticket_id = UNSET
        elif isinstance(self.ticket_id, UUID):
            ticket_id = str(self.ticket_id)
        else:
            ticket_id = self.ticket_id

        ticket_code: None | str | Unset
        if isinstance(self.ticket_code, Unset):
            ticket_code = UNSET
        else:
            ticket_code = self.ticket_code

        guest_name: None | str | Unset
        if isinstance(self.guest_name, Unset):
            guest_name = UNSET
        else:
            guest_name = self.guest_name

        guest_phone: None | str | Unset
        if isinstance(self.guest_phone, Unset):
            guest_phone = UNSET
        else:
            guest_phone = self.guest_phone

        subscription_id: None | str | Unset
        if isinstance(self.subscription_id, Unset):
            subscription_id = UNSET
        elif isinstance(self.subscription_id, UUID):
            subscription_id = str(self.subscription_id)
        else:
            subscription_id = self.subscription_id

        contract_code: None | str | Unset
        if isinstance(self.contract_code, Unset):
            contract_code = UNSET
        else:
            contract_code = self.contract_code

        package_name: None | str | Unset
        if isinstance(self.package_name, Unset):
            package_name = UNSET
        else:
            package_name = self.package_name

        avatar_key: None | str | Unset
        if isinstance(self.avatar_key, Unset):
            avatar_key = UNSET
        else:
            avatar_key = self.avatar_key

        branch_name: None | str | Unset
        if isinstance(self.branch_name, Unset):
            branch_name = UNSET
        else:
            branch_name = self.branch_name

        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        subscription_status: None | str | Unset
        if isinstance(self.subscription_status, Unset):
            subscription_status = UNSET
        else:
            subscription_status = self.subscription_status

        subscription_expire_date: None | str | Unset
        if isinstance(self.subscription_expire_date, Unset):
            subscription_expire_date = UNSET
        elif isinstance(self.subscription_expire_date, datetime.date):
            subscription_expire_date = self.subscription_expire_date.isoformat()
        else:
            subscription_expire_date = self.subscription_expire_date

        subscription_total_sessions: int | None | Unset
        if isinstance(self.subscription_total_sessions, Unset):
            subscription_total_sessions = UNSET
        else:
            subscription_total_sessions = self.subscription_total_sessions

        subscription_used_sessions: int | None | Unset
        if isinstance(self.subscription_used_sessions, Unset):
            subscription_used_sessions = UNSET
        else:
            subscription_used_sessions = self.subscription_used_sessions

        package_mode: None | str | Unset
        if isinstance(self.package_mode, Unset):
            package_mode = UNSET
        else:
            package_mode = self.package_mode

        sessions_remaining_snapshot: int | None | Unset
        if isinstance(self.sessions_remaining_snapshot, Unset):
            sessions_remaining_snapshot = UNSET
        else:
            sessions_remaining_snapshot = self.sessions_remaining_snapshot

        pt_id: None | str | Unset
        if isinstance(self.pt_id, Unset):
            pt_id = UNSET
        elif isinstance(self.pt_id, UUID):
            pt_id = str(self.pt_id)
        else:
            pt_id = self.pt_id

        pt_name: None | str | Unset
        if isinstance(self.pt_name, Unset):
            pt_name = UNSET
        else:
            pt_name = self.pt_name

        sessions_deducted: int | None | Unset
        if isinstance(self.sessions_deducted, Unset):
            sessions_deducted = UNSET
        else:
            sessions_deducted = self.sessions_deducted

        service_code: None | str | Unset
        if isinstance(self.service_code, Unset):
            service_code = UNSET
        else:
            service_code = self.service_code

        checkin_source: None | str | Unset
        if isinstance(self.checkin_source, Unset):
            checkin_source = UNSET
        else:
            checkin_source = self.checkin_source

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        package_type: None | str | Unset
        if isinstance(self.package_type, Unset):
            package_type = UNSET
        else:
            package_type = self.package_type

        group_member_allocation: int | None | Unset
        if isinstance(self.group_member_allocation, Unset):
            group_member_allocation = UNSET
        else:
            group_member_allocation = self.group_member_allocation

        group_member_remaining: int | None | Unset
        if isinstance(self.group_member_remaining, Unset):
            group_member_remaining = UNSET
        else:
            group_member_remaining = self.group_member_remaining

        has_photo = self.has_photo

        photo_url: None | str | Unset
        if isinstance(self.photo_url, Unset):
            photo_url = UNSET
        else:
            photo_url = self.photo_url

        registered_face_url: None | str | Unset
        if isinstance(self.registered_face_url, Unset):
            registered_face_url = UNSET
        else:
            registered_face_url = self.registered_face_url

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        debt_remaining: float | None | Unset
        if isinstance(self.debt_remaining, Unset):
            debt_remaining = UNSET
        else:
            debt_remaining = self.debt_remaining

        checkin_count_today: int | None | Unset
        if isinstance(self.checkin_count_today, Unset):
            checkin_count_today = UNSET
        else:
            checkin_count_today = self.checkin_count_today

        member_note: None | str | Unset
        if isinstance(self.member_note, Unset):
            member_note = UNSET
        else:
            member_note = self.member_note

        contract_note: None | str | Unset
        if isinstance(self.contract_note, Unset):
            contract_note = UNSET
        else:
            contract_note = self.contract_note

        package_note: None | str | Unset
        if isinstance(self.package_note, Unset):
            package_note = UNSET
        else:
            package_note = self.package_note

        pt_code: None | str | Unset
        if isinstance(self.pt_code, Unset):
            pt_code = UNSET
        else:
            pt_code = self.pt_code

        pt_avatar_url: None | str | Unset
        if isinstance(self.pt_avatar_url, Unset):
            pt_avatar_url = UNSET
        else:
            pt_avatar_url = self.pt_avatar_url

        gym_hours: None | str | Unset
        if isinstance(self.gym_hours, Unset):
            gym_hours = UNSET
        else:
            gym_hours = self.gym_hours

        sale_staff_name: None | str | Unset
        if isinstance(self.sale_staff_name, Unset):
            sale_staff_name = UNSET
        else:
            sale_staff_name = self.sale_staff_name

        days_remaining: int | None | Unset
        if isinstance(self.days_remaining, Unset):
            days_remaining = UNSET
        else:
            days_remaining = self.days_remaining


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id
        if gym_profile_id is not UNSET:
            field_dict["gymProfileId"] = gym_profile_id
        if member_code is not UNSET:
            field_dict["memberCode"] = member_code
        if member_name is not UNSET:
            field_dict["memberName"] = member_name
        if checkin_type is not UNSET:
            field_dict["checkinType"] = checkin_type
        if credential_type is not UNSET:
            field_dict["credentialType"] = credential_type
        if checkin_time is not UNSET:
            field_dict["checkinTime"] = checkin_time
        if checkout_time is not UNSET:
            field_dict["checkoutTime"] = checkout_time
        if is_valid is not UNSET:
            field_dict["isValid"] = is_valid
        if invalid_reason is not UNSET:
            field_dict["invalidReason"] = invalid_reason
        if is_manual_override is not UNSET:
            field_dict["isManualOverride"] = is_manual_override
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if zone_id is not UNSET:
            field_dict["zoneId"] = zone_id
        if access_decision is not UNSET:
            field_dict["accessDecision"] = access_decision
        if deny_reason is not UNSET:
            field_dict["denyReason"] = deny_reason
        if ticket_id is not UNSET:
            field_dict["ticketId"] = ticket_id
        if ticket_code is not UNSET:
            field_dict["ticketCode"] = ticket_code
        if guest_name is not UNSET:
            field_dict["guestName"] = guest_name
        if guest_phone is not UNSET:
            field_dict["guestPhone"] = guest_phone
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if contract_code is not UNSET:
            field_dict["contractCode"] = contract_code
        if package_name is not UNSET:
            field_dict["packageName"] = package_name
        if avatar_key is not UNSET:
            field_dict["avatarKey"] = avatar_key
        if branch_name is not UNSET:
            field_dict["branchName"] = branch_name
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if subscription_status is not UNSET:
            field_dict["subscriptionStatus"] = subscription_status
        if subscription_expire_date is not UNSET:
            field_dict["subscriptionExpireDate"] = subscription_expire_date
        if subscription_total_sessions is not UNSET:
            field_dict["subscriptionTotalSessions"] = subscription_total_sessions
        if subscription_used_sessions is not UNSET:
            field_dict["subscriptionUsedSessions"] = subscription_used_sessions
        if package_mode is not UNSET:
            field_dict["packageMode"] = package_mode
        if sessions_remaining_snapshot is not UNSET:
            field_dict["sessionsRemainingSnapshot"] = sessions_remaining_snapshot
        if pt_id is not UNSET:
            field_dict["ptId"] = pt_id
        if pt_name is not UNSET:
            field_dict["ptName"] = pt_name
        if sessions_deducted is not UNSET:
            field_dict["sessionsDeducted"] = sessions_deducted
        if service_code is not UNSET:
            field_dict["serviceCode"] = service_code
        if checkin_source is not UNSET:
            field_dict["checkinSource"] = checkin_source
        if notes is not UNSET:
            field_dict["notes"] = notes
        if package_type is not UNSET:
            field_dict["packageType"] = package_type
        if group_member_allocation is not UNSET:
            field_dict["groupMemberAllocation"] = group_member_allocation
        if group_member_remaining is not UNSET:
            field_dict["groupMemberRemaining"] = group_member_remaining
        if has_photo is not UNSET:
            field_dict["hasPhoto"] = has_photo
        if photo_url is not UNSET:
            field_dict["photoUrl"] = photo_url
        if registered_face_url is not UNSET:
            field_dict["registeredFaceUrl"] = registered_face_url
        if phone is not UNSET:
            field_dict["phone"] = phone
        if debt_remaining is not UNSET:
            field_dict["debtRemaining"] = debt_remaining
        if checkin_count_today is not UNSET:
            field_dict["checkinCountToday"] = checkin_count_today
        if member_note is not UNSET:
            field_dict["memberNote"] = member_note
        if contract_note is not UNSET:
            field_dict["contractNote"] = contract_note
        if package_note is not UNSET:
            field_dict["packageNote"] = package_note
        if pt_code is not UNSET:
            field_dict["ptCode"] = pt_code
        if pt_avatar_url is not UNSET:
            field_dict["ptAvatarUrl"] = pt_avatar_url
        if gym_hours is not UNSET:
            field_dict["gymHours"] = gym_hours
        if sale_staff_name is not UNSET:
            field_dict["saleStaffName"] = sale_staff_name
        if days_remaining is not UNSET:
            field_dict["daysRemaining"] = days_remaining

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


        _gym_profile_id = d.pop("gymProfileId", UNSET)
        gym_profile_id: UUID | Unset
        if isinstance(_gym_profile_id,  Unset):
            gym_profile_id = UNSET
        else:
            gym_profile_id = UUID(_gym_profile_id)




        def _parse_member_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_code = _parse_member_code(d.pop("memberCode", UNSET))


        def _parse_member_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_name = _parse_member_name(d.pop("memberName", UNSET))


        def _parse_checkin_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        checkin_type = _parse_checkin_type(d.pop("checkinType", UNSET))


        def _parse_credential_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        credential_type = _parse_credential_type(d.pop("credentialType", UNSET))


        _checkin_time = d.pop("checkinTime", UNSET)
        checkin_time: datetime.datetime | Unset
        if isinstance(_checkin_time,  Unset):
            checkin_time = UNSET
        else:
            checkin_time = datetime.datetime.fromisoformat(_checkin_time)




        def _parse_checkout_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                checkout_time_type_0 = datetime.datetime.fromisoformat(data)



                return checkout_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        checkout_time = _parse_checkout_time(d.pop("checkoutTime", UNSET))


        is_valid = d.pop("isValid", UNSET)

        def _parse_invalid_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        invalid_reason = _parse_invalid_reason(d.pop("invalidReason", UNSET))


        is_manual_override = d.pop("isManualOverride", UNSET)

        def _parse_device_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_name = _parse_device_name(d.pop("deviceName", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_zone_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                zone_id_type_0 = UUID(data)



                return zone_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        zone_id = _parse_zone_id(d.pop("zoneId", UNSET))


        def _parse_access_decision(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        access_decision = _parse_access_decision(d.pop("accessDecision", UNSET))


        def _parse_deny_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deny_reason = _parse_deny_reason(d.pop("denyReason", UNSET))


        def _parse_ticket_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ticket_id_type_0 = UUID(data)



                return ticket_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        ticket_id = _parse_ticket_id(d.pop("ticketId", UNSET))


        def _parse_ticket_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ticket_code = _parse_ticket_code(d.pop("ticketCode", UNSET))


        def _parse_guest_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guest_name = _parse_guest_name(d.pop("guestName", UNSET))


        def _parse_guest_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guest_phone = _parse_guest_phone(d.pop("guestPhone", UNSET))


        def _parse_subscription_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subscription_id_type_0 = UUID(data)



                return subscription_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        subscription_id = _parse_subscription_id(d.pop("subscriptionId", UNSET))


        def _parse_contract_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contract_code = _parse_contract_code(d.pop("contractCode", UNSET))


        def _parse_package_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        package_name = _parse_package_name(d.pop("packageName", UNSET))


        def _parse_avatar_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_key = _parse_avatar_key(d.pop("avatarKey", UNSET))


        def _parse_branch_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch_name = _parse_branch_name(d.pop("branchName", UNSET))


        def _parse_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url = _parse_avatar_url(d.pop("avatarUrl", UNSET))


        def _parse_subscription_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subscription_status = _parse_subscription_status(d.pop("subscriptionStatus", UNSET))


        def _parse_subscription_expire_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subscription_expire_date_type_0 = datetime.date.fromisoformat(data)



                return subscription_expire_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        subscription_expire_date = _parse_subscription_expire_date(d.pop("subscriptionExpireDate", UNSET))


        def _parse_subscription_total_sessions(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        subscription_total_sessions = _parse_subscription_total_sessions(d.pop("subscriptionTotalSessions", UNSET))


        def _parse_subscription_used_sessions(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        subscription_used_sessions = _parse_subscription_used_sessions(d.pop("subscriptionUsedSessions", UNSET))


        def _parse_package_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        package_mode = _parse_package_mode(d.pop("packageMode", UNSET))


        def _parse_sessions_remaining_snapshot(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sessions_remaining_snapshot = _parse_sessions_remaining_snapshot(d.pop("sessionsRemainingSnapshot", UNSET))


        def _parse_pt_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pt_id_type_0 = UUID(data)



                return pt_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        pt_id = _parse_pt_id(d.pop("ptId", UNSET))


        def _parse_pt_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pt_name = _parse_pt_name(d.pop("ptName", UNSET))


        def _parse_sessions_deducted(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sessions_deducted = _parse_sessions_deducted(d.pop("sessionsDeducted", UNSET))


        def _parse_service_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_code = _parse_service_code(d.pop("serviceCode", UNSET))


        def _parse_checkin_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        checkin_source = _parse_checkin_source(d.pop("checkinSource", UNSET))


        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


        def _parse_package_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        package_type = _parse_package_type(d.pop("packageType", UNSET))


        def _parse_group_member_allocation(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        group_member_allocation = _parse_group_member_allocation(d.pop("groupMemberAllocation", UNSET))


        def _parse_group_member_remaining(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        group_member_remaining = _parse_group_member_remaining(d.pop("groupMemberRemaining", UNSET))


        has_photo = d.pop("hasPhoto", UNSET)

        def _parse_photo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        photo_url = _parse_photo_url(d.pop("photoUrl", UNSET))


        def _parse_registered_face_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registered_face_url = _parse_registered_face_url(d.pop("registeredFaceUrl", UNSET))


        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))


        def _parse_debt_remaining(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        debt_remaining = _parse_debt_remaining(d.pop("debtRemaining", UNSET))


        def _parse_checkin_count_today(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        checkin_count_today = _parse_checkin_count_today(d.pop("checkinCountToday", UNSET))


        def _parse_member_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_note = _parse_member_note(d.pop("memberNote", UNSET))


        def _parse_contract_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contract_note = _parse_contract_note(d.pop("contractNote", UNSET))


        def _parse_package_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        package_note = _parse_package_note(d.pop("packageNote", UNSET))


        def _parse_pt_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pt_code = _parse_pt_code(d.pop("ptCode", UNSET))


        def _parse_pt_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pt_avatar_url = _parse_pt_avatar_url(d.pop("ptAvatarUrl", UNSET))


        def _parse_gym_hours(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gym_hours = _parse_gym_hours(d.pop("gymHours", UNSET))


        def _parse_sale_staff_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sale_staff_name = _parse_sale_staff_name(d.pop("saleStaffName", UNSET))


        def _parse_days_remaining(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        days_remaining = _parse_days_remaining(d.pop("daysRemaining", UNSET))


        check_in_dto = cls(
            id=id,
            branch_id=branch_id,
            gym_profile_id=gym_profile_id,
            member_code=member_code,
            member_name=member_name,
            checkin_type=checkin_type,
            credential_type=credential_type,
            checkin_time=checkin_time,
            checkout_time=checkout_time,
            is_valid=is_valid,
            invalid_reason=invalid_reason,
            is_manual_override=is_manual_override,
            device_name=device_name,
            created_at=created_at,
            zone_id=zone_id,
            access_decision=access_decision,
            deny_reason=deny_reason,
            ticket_id=ticket_id,
            ticket_code=ticket_code,
            guest_name=guest_name,
            guest_phone=guest_phone,
            subscription_id=subscription_id,
            contract_code=contract_code,
            package_name=package_name,
            avatar_key=avatar_key,
            branch_name=branch_name,
            avatar_url=avatar_url,
            subscription_status=subscription_status,
            subscription_expire_date=subscription_expire_date,
            subscription_total_sessions=subscription_total_sessions,
            subscription_used_sessions=subscription_used_sessions,
            package_mode=package_mode,
            sessions_remaining_snapshot=sessions_remaining_snapshot,
            pt_id=pt_id,
            pt_name=pt_name,
            sessions_deducted=sessions_deducted,
            service_code=service_code,
            checkin_source=checkin_source,
            notes=notes,
            package_type=package_type,
            group_member_allocation=group_member_allocation,
            group_member_remaining=group_member_remaining,
            has_photo=has_photo,
            photo_url=photo_url,
            registered_face_url=registered_face_url,
            phone=phone,
            debt_remaining=debt_remaining,
            checkin_count_today=checkin_count_today,
            member_note=member_note,
            contract_note=contract_note,
            package_note=package_note,
            pt_code=pt_code,
            pt_avatar_url=pt_avatar_url,
            gym_hours=gym_hours,
            sale_staff_name=sale_staff_name,
            days_remaining=days_remaining,
        )

        return check_in_dto


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






T = TypeVar("T", bound="MemberSummaryDto")



@_attrs_define
class MemberSummaryDto:
    

    id: UUID | Unset = UNSET
    branch_id: UUID | Unset = UNSET
    contact_id: UUID | Unset = UNSET
    member_code: None | str | Unset = UNSET
    full_name: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    avatar_url: None | str | Unset = UNSET
    joined_date: datetime.date | Unset = UNSET
    is_active: bool | Unset = UNSET
    active_subscription_type: None | str | Unset = UNSET
    active_subscription_start_date: datetime.date | None | Unset = UNSET
    active_subscription_end_date: datetime.date | None | Unset = UNSET
    source_id: None | Unset | UUID = UNSET
    source_name: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    assigned_staff_id: None | Unset | UUID = UNSET
    assigned_staff_name: None | str | Unset = UNSET
    assigned_staff_code: None | str | Unset = UNSET
    date_of_birth: datetime.date | None | Unset = UNSET
    gender: None | str | Unset = UNSET
    is_group_membership: bool | Unset = UNSET
    group_role: None | str | Unset = UNSET
    group_contract_code: None | str | Unset = UNSET
    group_package_name: None | str | Unset = UNSET
    group_member_count: int | None | Unset = UNSET
    group_max_members: int | None | Unset = UNSET
    branch_name: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    industry_name: None | str | Unset = UNSET
    customer_group_name: None | str | Unset = UNSET
    contact_person_name: None | str | Unset = UNSET
    contact_person_phone: None | str | Unset = UNSET
    contact_person_relationship: None | str | Unset = UNSET
    standard_expiry: datetime.date | None | Unset = UNSET
    class_expiry: datetime.date | None | Unset = UNSET
    pt_expiry: datetime.date | None | Unset = UNSET
    training_branch_names: list[str] | None | Unset = UNSET
    training_all_branches: bool | Unset = UNSET
    member_display_status: None | str | Unset = UNSET
    tax_code: None | str | Unset = UNSET
    total_sales: float | Unset = UNSET
    total_paid: float | Unset = UNSET
    total_debt: float | Unset = UNSET
    last_checkin_date: datetime.date | None | Unset = UNSET
    days_since_last_checkin: int | None | Unset = UNSET
    loyalty_tier_name: None | str | Unset = UNSET
    identity_number: None | str | Unset = UNSET
    identity_issued_date: datetime.date | None | Unset = UNSET
    identity_issued_place: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    card_code: None | str | Unset = UNSET
    device_pin: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    district: None | str | Unset = UNSET
    ward: None | str | Unset = UNSET
    phone2: None | str | Unset = UNSET
    phone3: None | str | Unset = UNSET
    referrer_name: None | str | Unset = UNSET
    referrer_member_code: None | str | Unset = UNSET
    created_by_name: None | str | Unset = UNSET
    has_card_credential: bool | Unset = UNSET
    has_face_credential: bool | Unset = UNSET
    has_fingerprint_credential: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        branch_id: str | Unset = UNSET
        if not isinstance(self.branch_id, Unset):
            branch_id = str(self.branch_id)

        contact_id: str | Unset = UNSET
        if not isinstance(self.contact_id, Unset):
            contact_id = str(self.contact_id)

        member_code: None | str | Unset
        if isinstance(self.member_code, Unset):
            member_code = UNSET
        else:
            member_code = self.member_code

        full_name: None | str | Unset
        if isinstance(self.full_name, Unset):
            full_name = UNSET
        else:
            full_name = self.full_name

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        joined_date: str | Unset = UNSET
        if not isinstance(self.joined_date, Unset):
            joined_date = self.joined_date.isoformat()

        is_active = self.is_active

        active_subscription_type: None | str | Unset
        if isinstance(self.active_subscription_type, Unset):
            active_subscription_type = UNSET
        else:
            active_subscription_type = self.active_subscription_type

        active_subscription_start_date: None | str | Unset
        if isinstance(self.active_subscription_start_date, Unset):
            active_subscription_start_date = UNSET
        elif isinstance(self.active_subscription_start_date, datetime.date):
            active_subscription_start_date = self.active_subscription_start_date.isoformat()
        else:
            active_subscription_start_date = self.active_subscription_start_date

        active_subscription_end_date: None | str | Unset
        if isinstance(self.active_subscription_end_date, Unset):
            active_subscription_end_date = UNSET
        elif isinstance(self.active_subscription_end_date, datetime.date):
            active_subscription_end_date = self.active_subscription_end_date.isoformat()
        else:
            active_subscription_end_date = self.active_subscription_end_date

        source_id: None | str | Unset
        if isinstance(self.source_id, Unset):
            source_id = UNSET
        elif isinstance(self.source_id, UUID):
            source_id = str(self.source_id)
        else:
            source_id = self.source_id

        source_name: None | str | Unset
        if isinstance(self.source_name, Unset):
            source_name = UNSET
        else:
            source_name = self.source_name

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        assigned_staff_id: None | str | Unset
        if isinstance(self.assigned_staff_id, Unset):
            assigned_staff_id = UNSET
        elif isinstance(self.assigned_staff_id, UUID):
            assigned_staff_id = str(self.assigned_staff_id)
        else:
            assigned_staff_id = self.assigned_staff_id

        assigned_staff_name: None | str | Unset
        if isinstance(self.assigned_staff_name, Unset):
            assigned_staff_name = UNSET
        else:
            assigned_staff_name = self.assigned_staff_name

        assigned_staff_code: None | str | Unset
        if isinstance(self.assigned_staff_code, Unset):
            assigned_staff_code = UNSET
        else:
            assigned_staff_code = self.assigned_staff_code

        date_of_birth: None | str | Unset
        if isinstance(self.date_of_birth, Unset):
            date_of_birth = UNSET
        elif isinstance(self.date_of_birth, datetime.date):
            date_of_birth = self.date_of_birth.isoformat()
        else:
            date_of_birth = self.date_of_birth

        gender: None | str | Unset
        if isinstance(self.gender, Unset):
            gender = UNSET
        else:
            gender = self.gender

        is_group_membership = self.is_group_membership

        group_role: None | str | Unset
        if isinstance(self.group_role, Unset):
            group_role = UNSET
        else:
            group_role = self.group_role

        group_contract_code: None | str | Unset
        if isinstance(self.group_contract_code, Unset):
            group_contract_code = UNSET
        else:
            group_contract_code = self.group_contract_code

        group_package_name: None | str | Unset
        if isinstance(self.group_package_name, Unset):
            group_package_name = UNSET
        else:
            group_package_name = self.group_package_name

        group_member_count: int | None | Unset
        if isinstance(self.group_member_count, Unset):
            group_member_count = UNSET
        else:
            group_member_count = self.group_member_count

        group_max_members: int | None | Unset
        if isinstance(self.group_max_members, Unset):
            group_max_members = UNSET
        else:
            group_max_members = self.group_max_members

        branch_name: None | str | Unset
        if isinstance(self.branch_name, Unset):
            branch_name = UNSET
        else:
            branch_name = self.branch_name

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        industry_name: None | str | Unset
        if isinstance(self.industry_name, Unset):
            industry_name = UNSET
        else:
            industry_name = self.industry_name

        customer_group_name: None | str | Unset
        if isinstance(self.customer_group_name, Unset):
            customer_group_name = UNSET
        else:
            customer_group_name = self.customer_group_name

        contact_person_name: None | str | Unset
        if isinstance(self.contact_person_name, Unset):
            contact_person_name = UNSET
        else:
            contact_person_name = self.contact_person_name

        contact_person_phone: None | str | Unset
        if isinstance(self.contact_person_phone, Unset):
            contact_person_phone = UNSET
        else:
            contact_person_phone = self.contact_person_phone

        contact_person_relationship: None | str | Unset
        if isinstance(self.contact_person_relationship, Unset):
            contact_person_relationship = UNSET
        else:
            contact_person_relationship = self.contact_person_relationship

        standard_expiry: None | str | Unset
        if isinstance(self.standard_expiry, Unset):
            standard_expiry = UNSET
        elif isinstance(self.standard_expiry, datetime.date):
            standard_expiry = self.standard_expiry.isoformat()
        else:
            standard_expiry = self.standard_expiry

        class_expiry: None | str | Unset
        if isinstance(self.class_expiry, Unset):
            class_expiry = UNSET
        elif isinstance(self.class_expiry, datetime.date):
            class_expiry = self.class_expiry.isoformat()
        else:
            class_expiry = self.class_expiry

        pt_expiry: None | str | Unset
        if isinstance(self.pt_expiry, Unset):
            pt_expiry = UNSET
        elif isinstance(self.pt_expiry, datetime.date):
            pt_expiry = self.pt_expiry.isoformat()
        else:
            pt_expiry = self.pt_expiry

        training_branch_names: list[str] | None | Unset
        if isinstance(self.training_branch_names, Unset):
            training_branch_names = UNSET
        elif isinstance(self.training_branch_names, list):
            training_branch_names = self.training_branch_names


        else:
            training_branch_names = self.training_branch_names

        training_all_branches = self.training_all_branches

        member_display_status: None | str | Unset
        if isinstance(self.member_display_status, Unset):
            member_display_status = UNSET
        else:
            member_display_status = self.member_display_status

        tax_code: None | str | Unset
        if isinstance(self.tax_code, Unset):
            tax_code = UNSET
        else:
            tax_code = self.tax_code

        total_sales = self.total_sales

        total_paid = self.total_paid

        total_debt = self.total_debt

        last_checkin_date: None | str | Unset
        if isinstance(self.last_checkin_date, Unset):
            last_checkin_date = UNSET
        elif isinstance(self.last_checkin_date, datetime.date):
            last_checkin_date = self.last_checkin_date.isoformat()
        else:
            last_checkin_date = self.last_checkin_date

        days_since_last_checkin: int | None | Unset
        if isinstance(self.days_since_last_checkin, Unset):
            days_since_last_checkin = UNSET
        else:
            days_since_last_checkin = self.days_since_last_checkin

        loyalty_tier_name: None | str | Unset
        if isinstance(self.loyalty_tier_name, Unset):
            loyalty_tier_name = UNSET
        else:
            loyalty_tier_name = self.loyalty_tier_name

        identity_number: None | str | Unset
        if isinstance(self.identity_number, Unset):
            identity_number = UNSET
        else:
            identity_number = self.identity_number

        identity_issued_date: None | str | Unset
        if isinstance(self.identity_issued_date, Unset):
            identity_issued_date = UNSET
        elif isinstance(self.identity_issued_date, datetime.date):
            identity_issued_date = self.identity_issued_date.isoformat()
        else:
            identity_issued_date = self.identity_issued_date

        identity_issued_place: None | str | Unset
        if isinstance(self.identity_issued_place, Unset):
            identity_issued_place = UNSET
        else:
            identity_issued_place = self.identity_issued_place

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        card_code: None | str | Unset
        if isinstance(self.card_code, Unset):
            card_code = UNSET
        else:
            card_code = self.card_code

        device_pin: None | str | Unset
        if isinstance(self.device_pin, Unset):
            device_pin = UNSET
        else:
            device_pin = self.device_pin

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        district: None | str | Unset
        if isinstance(self.district, Unset):
            district = UNSET
        else:
            district = self.district

        ward: None | str | Unset
        if isinstance(self.ward, Unset):
            ward = UNSET
        else:
            ward = self.ward

        phone2: None | str | Unset
        if isinstance(self.phone2, Unset):
            phone2 = UNSET
        else:
            phone2 = self.phone2

        phone3: None | str | Unset
        if isinstance(self.phone3, Unset):
            phone3 = UNSET
        else:
            phone3 = self.phone3

        referrer_name: None | str | Unset
        if isinstance(self.referrer_name, Unset):
            referrer_name = UNSET
        else:
            referrer_name = self.referrer_name

        referrer_member_code: None | str | Unset
        if isinstance(self.referrer_member_code, Unset):
            referrer_member_code = UNSET
        else:
            referrer_member_code = self.referrer_member_code

        created_by_name: None | str | Unset
        if isinstance(self.created_by_name, Unset):
            created_by_name = UNSET
        else:
            created_by_name = self.created_by_name

        has_card_credential = self.has_card_credential

        has_face_credential = self.has_face_credential

        has_fingerprint_credential = self.has_fingerprint_credential


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id
        if contact_id is not UNSET:
            field_dict["contactId"] = contact_id
        if member_code is not UNSET:
            field_dict["memberCode"] = member_code
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if email is not UNSET:
            field_dict["email"] = email
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if joined_date is not UNSET:
            field_dict["joinedDate"] = joined_date
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if active_subscription_type is not UNSET:
            field_dict["activeSubscriptionType"] = active_subscription_type
        if active_subscription_start_date is not UNSET:
            field_dict["activeSubscriptionStartDate"] = active_subscription_start_date
        if active_subscription_end_date is not UNSET:
            field_dict["activeSubscriptionEndDate"] = active_subscription_end_date
        if source_id is not UNSET:
            field_dict["sourceId"] = source_id
        if source_name is not UNSET:
            field_dict["sourceName"] = source_name
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if assigned_staff_id is not UNSET:
            field_dict["assignedStaffId"] = assigned_staff_id
        if assigned_staff_name is not UNSET:
            field_dict["assignedStaffName"] = assigned_staff_name
        if assigned_staff_code is not UNSET:
            field_dict["assignedStaffCode"] = assigned_staff_code
        if date_of_birth is not UNSET:
            field_dict["dateOfBirth"] = date_of_birth
        if gender is not UNSET:
            field_dict["gender"] = gender
        if is_group_membership is not UNSET:
            field_dict["isGroupMembership"] = is_group_membership
        if group_role is not UNSET:
            field_dict["groupRole"] = group_role
        if group_contract_code is not UNSET:
            field_dict["groupContractCode"] = group_contract_code
        if group_package_name is not UNSET:
            field_dict["groupPackageName"] = group_package_name
        if group_member_count is not UNSET:
            field_dict["groupMemberCount"] = group_member_count
        if group_max_members is not UNSET:
            field_dict["groupMaxMembers"] = group_max_members
        if branch_name is not UNSET:
            field_dict["branchName"] = branch_name
        if address is not UNSET:
            field_dict["address"] = address
        if industry_name is not UNSET:
            field_dict["industryName"] = industry_name
        if customer_group_name is not UNSET:
            field_dict["customerGroupName"] = customer_group_name
        if contact_person_name is not UNSET:
            field_dict["contactPersonName"] = contact_person_name
        if contact_person_phone is not UNSET:
            field_dict["contactPersonPhone"] = contact_person_phone
        if contact_person_relationship is not UNSET:
            field_dict["contactPersonRelationship"] = contact_person_relationship
        if standard_expiry is not UNSET:
            field_dict["standardExpiry"] = standard_expiry
        if class_expiry is not UNSET:
            field_dict["classExpiry"] = class_expiry
        if pt_expiry is not UNSET:
            field_dict["ptExpiry"] = pt_expiry
        if training_branch_names is not UNSET:
            field_dict["trainingBranchNames"] = training_branch_names
        if training_all_branches is not UNSET:
            field_dict["trainingAllBranches"] = training_all_branches
        if member_display_status is not UNSET:
            field_dict["memberDisplayStatus"] = member_display_status
        if tax_code is not UNSET:
            field_dict["taxCode"] = tax_code
        if total_sales is not UNSET:
            field_dict["totalSales"] = total_sales
        if total_paid is not UNSET:
            field_dict["totalPaid"] = total_paid
        if total_debt is not UNSET:
            field_dict["totalDebt"] = total_debt
        if last_checkin_date is not UNSET:
            field_dict["lastCheckinDate"] = last_checkin_date
        if days_since_last_checkin is not UNSET:
            field_dict["daysSinceLastCheckin"] = days_since_last_checkin
        if loyalty_tier_name is not UNSET:
            field_dict["loyaltyTierName"] = loyalty_tier_name
        if identity_number is not UNSET:
            field_dict["identityNumber"] = identity_number
        if identity_issued_date is not UNSET:
            field_dict["identityIssuedDate"] = identity_issued_date
        if identity_issued_place is not UNSET:
            field_dict["identityIssuedPlace"] = identity_issued_place
        if notes is not UNSET:
            field_dict["notes"] = notes
        if card_code is not UNSET:
            field_dict["cardCode"] = card_code
        if device_pin is not UNSET:
            field_dict["devicePin"] = device_pin
        if city is not UNSET:
            field_dict["city"] = city
        if district is not UNSET:
            field_dict["district"] = district
        if ward is not UNSET:
            field_dict["ward"] = ward
        if phone2 is not UNSET:
            field_dict["phone2"] = phone2
        if phone3 is not UNSET:
            field_dict["phone3"] = phone3
        if referrer_name is not UNSET:
            field_dict["referrerName"] = referrer_name
        if referrer_member_code is not UNSET:
            field_dict["referrerMemberCode"] = referrer_member_code
        if created_by_name is not UNSET:
            field_dict["createdByName"] = created_by_name
        if has_card_credential is not UNSET:
            field_dict["hasCardCredential"] = has_card_credential
        if has_face_credential is not UNSET:
            field_dict["hasFaceCredential"] = has_face_credential
        if has_fingerprint_credential is not UNSET:
            field_dict["hasFingerprintCredential"] = has_fingerprint_credential

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




        _branch_id = d.pop("branchId", UNSET)
        branch_id: UUID | Unset
        if isinstance(_branch_id,  Unset):
            branch_id = UNSET
        else:
            branch_id = UUID(_branch_id)




        _contact_id = d.pop("contactId", UNSET)
        contact_id: UUID | Unset
        if isinstance(_contact_id,  Unset):
            contact_id = UNSET
        else:
            contact_id = UUID(_contact_id)




        def _parse_member_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_code = _parse_member_code(d.pop("memberCode", UNSET))


        def _parse_full_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        full_name = _parse_full_name(d.pop("fullName", UNSET))


        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))


        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))


        def _parse_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url = _parse_avatar_url(d.pop("avatarUrl", UNSET))


        _joined_date = d.pop("joinedDate", UNSET)
        joined_date: datetime.date | Unset
        if isinstance(_joined_date,  Unset):
            joined_date = UNSET
        else:
            joined_date = datetime.date.fromisoformat(_joined_date)




        is_active = d.pop("isActive", UNSET)

        def _parse_active_subscription_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        active_subscription_type = _parse_active_subscription_type(d.pop("activeSubscriptionType", UNSET))


        def _parse_active_subscription_start_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                active_subscription_start_date_type_0 = datetime.date.fromisoformat(data)



                return active_subscription_start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        active_subscription_start_date = _parse_active_subscription_start_date(d.pop("activeSubscriptionStartDate", UNSET))


        def _parse_active_subscription_end_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                active_subscription_end_date_type_0 = datetime.date.fromisoformat(data)



                return active_subscription_end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        active_subscription_end_date = _parse_active_subscription_end_date(d.pop("activeSubscriptionEndDate", UNSET))


        def _parse_source_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_id_type_0 = UUID(data)



                return source_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        source_id = _parse_source_id(d.pop("sourceId", UNSET))


        def _parse_source_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_name = _parse_source_name(d.pop("sourceName", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_assigned_staff_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                assigned_staff_id_type_0 = UUID(data)



                return assigned_staff_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        assigned_staff_id = _parse_assigned_staff_id(d.pop("assignedStaffId", UNSET))


        def _parse_assigned_staff_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assigned_staff_name = _parse_assigned_staff_name(d.pop("assignedStaffName", UNSET))


        def _parse_assigned_staff_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assigned_staff_code = _parse_assigned_staff_code(d.pop("assignedStaffCode", UNSET))


        def _parse_date_of_birth(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_of_birth_type_0 = datetime.date.fromisoformat(data)



                return date_of_birth_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        date_of_birth = _parse_date_of_birth(d.pop("dateOfBirth", UNSET))


        def _parse_gender(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gender = _parse_gender(d.pop("gender", UNSET))


        is_group_membership = d.pop("isGroupMembership", UNSET)

        def _parse_group_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_role = _parse_group_role(d.pop("groupRole", UNSET))


        def _parse_group_contract_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_contract_code = _parse_group_contract_code(d.pop("groupContractCode", UNSET))


        def _parse_group_package_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_package_name = _parse_group_package_name(d.pop("groupPackageName", UNSET))


        def _parse_group_member_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        group_member_count = _parse_group_member_count(d.pop("groupMemberCount", UNSET))


        def _parse_group_max_members(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        group_max_members = _parse_group_max_members(d.pop("groupMaxMembers", UNSET))


        def _parse_branch_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch_name = _parse_branch_name(d.pop("branchName", UNSET))


        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))


        def _parse_industry_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        industry_name = _parse_industry_name(d.pop("industryName", UNSET))


        def _parse_customer_group_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_group_name = _parse_customer_group_name(d.pop("customerGroupName", UNSET))


        def _parse_contact_person_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_person_name = _parse_contact_person_name(d.pop("contactPersonName", UNSET))


        def _parse_contact_person_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_person_phone = _parse_contact_person_phone(d.pop("contactPersonPhone", UNSET))


        def _parse_contact_person_relationship(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_person_relationship = _parse_contact_person_relationship(d.pop("contactPersonRelationship", UNSET))


        def _parse_standard_expiry(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                standard_expiry_type_0 = datetime.date.fromisoformat(data)



                return standard_expiry_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        standard_expiry = _parse_standard_expiry(d.pop("standardExpiry", UNSET))


        def _parse_class_expiry(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                class_expiry_type_0 = datetime.date.fromisoformat(data)



                return class_expiry_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        class_expiry = _parse_class_expiry(d.pop("classExpiry", UNSET))


        def _parse_pt_expiry(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pt_expiry_type_0 = datetime.date.fromisoformat(data)



                return pt_expiry_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        pt_expiry = _parse_pt_expiry(d.pop("ptExpiry", UNSET))


        def _parse_training_branch_names(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                training_branch_names_type_0 = cast(list[str], data)

                return training_branch_names_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        training_branch_names = _parse_training_branch_names(d.pop("trainingBranchNames", UNSET))


        training_all_branches = d.pop("trainingAllBranches", UNSET)

        def _parse_member_display_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_display_status = _parse_member_display_status(d.pop("memberDisplayStatus", UNSET))


        def _parse_tax_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tax_code = _parse_tax_code(d.pop("taxCode", UNSET))


        total_sales = d.pop("totalSales", UNSET)

        total_paid = d.pop("totalPaid", UNSET)

        total_debt = d.pop("totalDebt", UNSET)

        def _parse_last_checkin_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_checkin_date_type_0 = datetime.date.fromisoformat(data)



                return last_checkin_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        last_checkin_date = _parse_last_checkin_date(d.pop("lastCheckinDate", UNSET))


        def _parse_days_since_last_checkin(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        days_since_last_checkin = _parse_days_since_last_checkin(d.pop("daysSinceLastCheckin", UNSET))


        def _parse_loyalty_tier_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        loyalty_tier_name = _parse_loyalty_tier_name(d.pop("loyaltyTierName", UNSET))


        def _parse_identity_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        identity_number = _parse_identity_number(d.pop("identityNumber", UNSET))


        def _parse_identity_issued_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                identity_issued_date_type_0 = datetime.date.fromisoformat(data)



                return identity_issued_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        identity_issued_date = _parse_identity_issued_date(d.pop("identityIssuedDate", UNSET))


        def _parse_identity_issued_place(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        identity_issued_place = _parse_identity_issued_place(d.pop("identityIssuedPlace", UNSET))


        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


        def _parse_card_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        card_code = _parse_card_code(d.pop("cardCode", UNSET))


        def _parse_device_pin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_pin = _parse_device_pin(d.pop("devicePin", UNSET))


        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))


        def _parse_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district = _parse_district(d.pop("district", UNSET))


        def _parse_ward(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ward = _parse_ward(d.pop("ward", UNSET))


        def _parse_phone2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone2 = _parse_phone2(d.pop("phone2", UNSET))


        def _parse_phone3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone3 = _parse_phone3(d.pop("phone3", UNSET))


        def _parse_referrer_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        referrer_name = _parse_referrer_name(d.pop("referrerName", UNSET))


        def _parse_referrer_member_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        referrer_member_code = _parse_referrer_member_code(d.pop("referrerMemberCode", UNSET))


        def _parse_created_by_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by_name = _parse_created_by_name(d.pop("createdByName", UNSET))


        has_card_credential = d.pop("hasCardCredential", UNSET)

        has_face_credential = d.pop("hasFaceCredential", UNSET)

        has_fingerprint_credential = d.pop("hasFingerprintCredential", UNSET)

        member_summary_dto = cls(
            id=id,
            branch_id=branch_id,
            contact_id=contact_id,
            member_code=member_code,
            full_name=full_name,
            phone=phone,
            email=email,
            avatar_url=avatar_url,
            joined_date=joined_date,
            is_active=is_active,
            active_subscription_type=active_subscription_type,
            active_subscription_start_date=active_subscription_start_date,
            active_subscription_end_date=active_subscription_end_date,
            source_id=source_id,
            source_name=source_name,
            created_at=created_at,
            assigned_staff_id=assigned_staff_id,
            assigned_staff_name=assigned_staff_name,
            assigned_staff_code=assigned_staff_code,
            date_of_birth=date_of_birth,
            gender=gender,
            is_group_membership=is_group_membership,
            group_role=group_role,
            group_contract_code=group_contract_code,
            group_package_name=group_package_name,
            group_member_count=group_member_count,
            group_max_members=group_max_members,
            branch_name=branch_name,
            address=address,
            industry_name=industry_name,
            customer_group_name=customer_group_name,
            contact_person_name=contact_person_name,
            contact_person_phone=contact_person_phone,
            contact_person_relationship=contact_person_relationship,
            standard_expiry=standard_expiry,
            class_expiry=class_expiry,
            pt_expiry=pt_expiry,
            training_branch_names=training_branch_names,
            training_all_branches=training_all_branches,
            member_display_status=member_display_status,
            tax_code=tax_code,
            total_sales=total_sales,
            total_paid=total_paid,
            total_debt=total_debt,
            last_checkin_date=last_checkin_date,
            days_since_last_checkin=days_since_last_checkin,
            loyalty_tier_name=loyalty_tier_name,
            identity_number=identity_number,
            identity_issued_date=identity_issued_date,
            identity_issued_place=identity_issued_place,
            notes=notes,
            card_code=card_code,
            device_pin=device_pin,
            city=city,
            district=district,
            ward=ward,
            phone2=phone2,
            phone3=phone3,
            referrer_name=referrer_name,
            referrer_member_code=referrer_member_code,
            created_by_name=created_by_name,
            has_card_credential=has_card_credential,
            has_face_credential=has_face_credential,
            has_fingerprint_credential=has_fingerprint_credential,
        )

        return member_summary_dto


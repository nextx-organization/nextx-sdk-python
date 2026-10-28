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
  from ..models.subscription_summary_dto import SubscriptionSummaryDto





T = TypeVar("T", bound="MemberDetailDto")



@_attrs_define
class MemberDetailDto:
    

    id: UUID | Unset = UNSET
    branch_id: UUID | Unset = UNSET
    contact_id: UUID | Unset = UNSET
    member_code: None | str | Unset = UNSET
    full_name: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    date_of_birth: datetime.date | None | Unset = UNSET
    gender: None | str | Unset = UNSET
    avatar_url: None | str | Unset = UNSET
    joined_date: datetime.date | Unset = UNSET
    notes: None | str | Unset = UNSET
    is_active: bool | Unset = UNSET
    subscriptions: list[SubscriptionSummaryDto] | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    identity_number: None | str | Unset = UNSET
    identity_issued_date: datetime.date | None | Unset = UNSET
    identity_issued_place: None | str | Unset = UNSET
    ward: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    phone2: None | str | Unset = UNSET
    phone3: None | str | Unset = UNSET
    assigned_staff_id: None | Unset | UUID = UNSET
    assigned_staff_name: None | str | Unset = UNSET
    assigned_staff_code: None | str | Unset = UNSET
    industry_id: None | Unset | UUID = UNSET
    industry_name: None | str | Unset = UNSET
    customer_group_id: None | Unset | UUID = UNSET
    customer_group_name: None | str | Unset = UNSET
    source_id: None | Unset | UUID = UNSET
    source_name: None | str | Unset = UNSET
    referred_by_member_id: None | Unset | UUID = UNSET
    referred_by_member_name: None | str | Unset = UNSET
    referred_by_member_code: None | str | Unset = UNSET
    card_code: None | str | Unset = UNSET
    branch_name: None | str | Unset = UNSET
    contact_person_name: None | str | Unset = UNSET
    contact_person_phone: None | str | Unset = UNSET
    contact_person_relationship: None | str | Unset = UNSET
    device_employee_no: None | str | Unset = UNSET
    tax_code: None | str | Unset = UNSET
    device_pin: None | str | Unset = UNSET
    app_account_warning: None | str | Unset = UNSET
    contact_sync_warning: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.subscription_summary_dto import SubscriptionSummaryDto # noqa: PLC0415
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

        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        joined_date: str | Unset = UNSET
        if not isinstance(self.joined_date, Unset):
            joined_date = self.joined_date.isoformat()

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        is_active = self.is_active

        subscriptions: list[dict[str, Any]] | None | Unset
        if isinstance(self.subscriptions, Unset):
            subscriptions = UNSET
        elif isinstance(self.subscriptions, list):
            subscriptions = []
            for subscriptions_type_0_item_data in self.subscriptions:
                subscriptions_type_0_item = subscriptions_type_0_item_data.to_dict()
                subscriptions.append(subscriptions_type_0_item)


        else:
            subscriptions = self.subscriptions

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

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

        ward: None | str | Unset
        if isinstance(self.ward, Unset):
            ward = UNSET
        else:
            ward = self.ward

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

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

        industry_id: None | str | Unset
        if isinstance(self.industry_id, Unset):
            industry_id = UNSET
        elif isinstance(self.industry_id, UUID):
            industry_id = str(self.industry_id)
        else:
            industry_id = self.industry_id

        industry_name: None | str | Unset
        if isinstance(self.industry_name, Unset):
            industry_name = UNSET
        else:
            industry_name = self.industry_name

        customer_group_id: None | str | Unset
        if isinstance(self.customer_group_id, Unset):
            customer_group_id = UNSET
        elif isinstance(self.customer_group_id, UUID):
            customer_group_id = str(self.customer_group_id)
        else:
            customer_group_id = self.customer_group_id

        customer_group_name: None | str | Unset
        if isinstance(self.customer_group_name, Unset):
            customer_group_name = UNSET
        else:
            customer_group_name = self.customer_group_name

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

        referred_by_member_id: None | str | Unset
        if isinstance(self.referred_by_member_id, Unset):
            referred_by_member_id = UNSET
        elif isinstance(self.referred_by_member_id, UUID):
            referred_by_member_id = str(self.referred_by_member_id)
        else:
            referred_by_member_id = self.referred_by_member_id

        referred_by_member_name: None | str | Unset
        if isinstance(self.referred_by_member_name, Unset):
            referred_by_member_name = UNSET
        else:
            referred_by_member_name = self.referred_by_member_name

        referred_by_member_code: None | str | Unset
        if isinstance(self.referred_by_member_code, Unset):
            referred_by_member_code = UNSET
        else:
            referred_by_member_code = self.referred_by_member_code

        card_code: None | str | Unset
        if isinstance(self.card_code, Unset):
            card_code = UNSET
        else:
            card_code = self.card_code

        branch_name: None | str | Unset
        if isinstance(self.branch_name, Unset):
            branch_name = UNSET
        else:
            branch_name = self.branch_name

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

        device_employee_no: None | str | Unset
        if isinstance(self.device_employee_no, Unset):
            device_employee_no = UNSET
        else:
            device_employee_no = self.device_employee_no

        tax_code: None | str | Unset
        if isinstance(self.tax_code, Unset):
            tax_code = UNSET
        else:
            tax_code = self.tax_code

        device_pin: None | str | Unset
        if isinstance(self.device_pin, Unset):
            device_pin = UNSET
        else:
            device_pin = self.device_pin

        app_account_warning: None | str | Unset
        if isinstance(self.app_account_warning, Unset):
            app_account_warning = UNSET
        else:
            app_account_warning = self.app_account_warning

        contact_sync_warning: None | str | Unset
        if isinstance(self.contact_sync_warning, Unset):
            contact_sync_warning = UNSET
        else:
            contact_sync_warning = self.contact_sync_warning


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
        if date_of_birth is not UNSET:
            field_dict["dateOfBirth"] = date_of_birth
        if gender is not UNSET:
            field_dict["gender"] = gender
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if joined_date is not UNSET:
            field_dict["joinedDate"] = joined_date
        if notes is not UNSET:
            field_dict["notes"] = notes
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if identity_number is not UNSET:
            field_dict["identityNumber"] = identity_number
        if identity_issued_date is not UNSET:
            field_dict["identityIssuedDate"] = identity_issued_date
        if identity_issued_place is not UNSET:
            field_dict["identityIssuedPlace"] = identity_issued_place
        if ward is not UNSET:
            field_dict["ward"] = ward
        if address is not UNSET:
            field_dict["address"] = address
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if phone2 is not UNSET:
            field_dict["phone2"] = phone2
        if phone3 is not UNSET:
            field_dict["phone3"] = phone3
        if assigned_staff_id is not UNSET:
            field_dict["assignedStaffId"] = assigned_staff_id
        if assigned_staff_name is not UNSET:
            field_dict["assignedStaffName"] = assigned_staff_name
        if assigned_staff_code is not UNSET:
            field_dict["assignedStaffCode"] = assigned_staff_code
        if industry_id is not UNSET:
            field_dict["industryId"] = industry_id
        if industry_name is not UNSET:
            field_dict["industryName"] = industry_name
        if customer_group_id is not UNSET:
            field_dict["customerGroupId"] = customer_group_id
        if customer_group_name is not UNSET:
            field_dict["customerGroupName"] = customer_group_name
        if source_id is not UNSET:
            field_dict["sourceId"] = source_id
        if source_name is not UNSET:
            field_dict["sourceName"] = source_name
        if referred_by_member_id is not UNSET:
            field_dict["referredByMemberId"] = referred_by_member_id
        if referred_by_member_name is not UNSET:
            field_dict["referredByMemberName"] = referred_by_member_name
        if referred_by_member_code is not UNSET:
            field_dict["referredByMemberCode"] = referred_by_member_code
        if card_code is not UNSET:
            field_dict["cardCode"] = card_code
        if branch_name is not UNSET:
            field_dict["branchName"] = branch_name
        if contact_person_name is not UNSET:
            field_dict["contactPersonName"] = contact_person_name
        if contact_person_phone is not UNSET:
            field_dict["contactPersonPhone"] = contact_person_phone
        if contact_person_relationship is not UNSET:
            field_dict["contactPersonRelationship"] = contact_person_relationship
        if device_employee_no is not UNSET:
            field_dict["deviceEmployeeNo"] = device_employee_no
        if tax_code is not UNSET:
            field_dict["taxCode"] = tax_code
        if device_pin is not UNSET:
            field_dict["devicePin"] = device_pin
        if app_account_warning is not UNSET:
            field_dict["appAccountWarning"] = app_account_warning
        if contact_sync_warning is not UNSET:
            field_dict["contactSyncWarning"] = contact_sync_warning

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscription_summary_dto import SubscriptionSummaryDto # noqa: PLC0415
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




        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


        is_active = d.pop("isActive", UNSET)

        def _parse_subscriptions(data: object) -> list[SubscriptionSummaryDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                subscriptions_type_0 = []
                _subscriptions_type_0 = data
                for subscriptions_type_0_item_data in (_subscriptions_type_0):
                    subscriptions_type_0_item = SubscriptionSummaryDto.from_dict(subscriptions_type_0_item_data)



                    subscriptions_type_0.append(subscriptions_type_0_item)

                return subscriptions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SubscriptionSummaryDto] | None | Unset, data)

        subscriptions = _parse_subscriptions(d.pop("subscriptions", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)




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


        def _parse_ward(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ward = _parse_ward(d.pop("ward", UNSET))


        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))


        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))


        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))


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


        def _parse_industry_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                industry_id_type_0 = UUID(data)



                return industry_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        industry_id = _parse_industry_id(d.pop("industryId", UNSET))


        def _parse_industry_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        industry_name = _parse_industry_name(d.pop("industryName", UNSET))


        def _parse_customer_group_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                customer_group_id_type_0 = UUID(data)



                return customer_group_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        customer_group_id = _parse_customer_group_id(d.pop("customerGroupId", UNSET))


        def _parse_customer_group_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_group_name = _parse_customer_group_name(d.pop("customerGroupName", UNSET))


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


        def _parse_referred_by_member_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                referred_by_member_id_type_0 = UUID(data)



                return referred_by_member_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        referred_by_member_id = _parse_referred_by_member_id(d.pop("referredByMemberId", UNSET))


        def _parse_referred_by_member_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        referred_by_member_name = _parse_referred_by_member_name(d.pop("referredByMemberName", UNSET))


        def _parse_referred_by_member_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        referred_by_member_code = _parse_referred_by_member_code(d.pop("referredByMemberCode", UNSET))


        def _parse_card_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        card_code = _parse_card_code(d.pop("cardCode", UNSET))


        def _parse_branch_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch_name = _parse_branch_name(d.pop("branchName", UNSET))


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


        def _parse_device_employee_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_employee_no = _parse_device_employee_no(d.pop("deviceEmployeeNo", UNSET))


        def _parse_tax_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tax_code = _parse_tax_code(d.pop("taxCode", UNSET))


        def _parse_device_pin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_pin = _parse_device_pin(d.pop("devicePin", UNSET))


        def _parse_app_account_warning(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        app_account_warning = _parse_app_account_warning(d.pop("appAccountWarning", UNSET))


        def _parse_contact_sync_warning(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_sync_warning = _parse_contact_sync_warning(d.pop("contactSyncWarning", UNSET))


        member_detail_dto = cls(
            id=id,
            branch_id=branch_id,
            contact_id=contact_id,
            member_code=member_code,
            full_name=full_name,
            phone=phone,
            email=email,
            date_of_birth=date_of_birth,
            gender=gender,
            avatar_url=avatar_url,
            joined_date=joined_date,
            notes=notes,
            is_active=is_active,
            subscriptions=subscriptions,
            created_at=created_at,
            updated_at=updated_at,
            identity_number=identity_number,
            identity_issued_date=identity_issued_date,
            identity_issued_place=identity_issued_place,
            ward=ward,
            address=address,
            city=city,
            country=country,
            phone2=phone2,
            phone3=phone3,
            assigned_staff_id=assigned_staff_id,
            assigned_staff_name=assigned_staff_name,
            assigned_staff_code=assigned_staff_code,
            industry_id=industry_id,
            industry_name=industry_name,
            customer_group_id=customer_group_id,
            customer_group_name=customer_group_name,
            source_id=source_id,
            source_name=source_name,
            referred_by_member_id=referred_by_member_id,
            referred_by_member_name=referred_by_member_name,
            referred_by_member_code=referred_by_member_code,
            card_code=card_code,
            branch_name=branch_name,
            contact_person_name=contact_person_name,
            contact_person_phone=contact_person_phone,
            contact_person_relationship=contact_person_relationship,
            device_employee_no=device_employee_no,
            tax_code=tax_code,
            device_pin=device_pin,
            app_account_warning=app_account_warning,
            contact_sync_warning=contact_sync_warning,
        )

        return member_detail_dto


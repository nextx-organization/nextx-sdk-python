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
  from ..models.contact_detail_dto_custom_fields_type_0 import ContactDetailDtoCustomFieldsType0
  from ..models.contact_first_touch_dto import ContactFirstTouchDto
  from ..models.customer_profile_dto import CustomerProfileDto
  from ..models.supplier_info_ref_dto import SupplierInfoRefDto
  from ..models.tag_dto import TagDto





T = TypeVar("T", bound="ContactDetailDto")



@_attrs_define
class ContactDetailDto:
    

    id: UUID | Unset = UNSET
    code: None | str | Unset = UNSET
    contact_type: None | str | Unset = UNSET
    full_name: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    job_title: None | str | Unset = UNSET
    company_name: None | str | Unset = UNSET
    website: None | str | Unset = UNSET
    avatar_url: None | str | Unset = UNSET
    gender: None | str | Unset = UNSET
    dob: datetime.date | None | Unset = UNSET
    address: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    identity_number: None | str | Unset = UNSET
    identity_issued_date: datetime.date | None | Unset = UNSET
    identity_issued_place: None | str | Unset = UNSET
    ward: None | str | Unset = UNSET
    phone2: None | str | Unset = UNSET
    phone3: None | str | Unset = UNSET
    linkedin_url: None | str | Unset = UNSET
    tier: None | str | Unset = UNSET
    is_decision_maker: bool | Unset = UNSET
    custom_fields: ContactDetailDtoCustomFieldsType0 | None | Unset = UNSET
    source_ref: None | str | Unset = UNSET
    tags: list[TagDto] | None | Unset = UNSET
    customer_profile: CustomerProfileDto | Unset = UNSET
    supplier_info: SupplierInfoRefDto | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    lifecycle_stage: None | str | Unset = UNSET
    industry_id: None | Unset | UUID = UNSET
    source_id: None | Unset | UUID = UNSET
    customer_group_id: None | Unset | UUID = UNSET
    contact_person_name: None | str | Unset = UNSET
    contact_person_phone: None | str | Unset = UNSET
    contact_person_relationship: None | str | Unset = UNSET
    province_code: None | str | Unset = UNSET
    district_code: None | str | Unset = UNSET
    ward_code: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    group_name: None | str | Unset = UNSET
    group_icon: None | str | Unset = UNSET
    group_color: None | str | Unset = UNSET
    assignee_id: None | Unset | UUID = UNSET
    assignee_name: None | str | Unset = UNSET
    assigned_at: datetime.datetime | None | Unset = UNSET
    status_label: None | str | Unset = UNSET
    status_icon: None | str | Unset = UNSET
    status_color: None | str | Unset = UNSET
    contact_status_id: None | Unset | UUID = UNSET
    branch_id: None | Unset | UUID = UNSET
    branch_name: None | str | Unset = UNSET
    tax_code: None | str | Unset = UNSET
    bank_account_number: None | str | Unset = UNSET
    bank_name: None | str | Unset = UNSET
    bank_branch: None | str | Unset = UNSET
    lead_score: int | Unset = UNSET
    lead_tier: None | str | Unset = UNSET
    referral_code_id: None | Unset | UUID = UNSET
    referral_code_kind: None | str | Unset = UNSET
    referral_code: None | str | Unset = UNSET
    first_touch: ContactFirstTouchDto | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.contact_detail_dto_custom_fields_type_0 import ContactDetailDtoCustomFieldsType0 # noqa: PLC0415
        from ..models.contact_first_touch_dto import ContactFirstTouchDto # noqa: PLC0415
        from ..models.customer_profile_dto import CustomerProfileDto # noqa: PLC0415
        from ..models.supplier_info_ref_dto import SupplierInfoRefDto # noqa: PLC0415
        from ..models.tag_dto import TagDto # noqa: PLC0415
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        contact_type: None | str | Unset
        if isinstance(self.contact_type, Unset):
            contact_type = UNSET
        else:
            contact_type = self.contact_type

        full_name: None | str | Unset
        if isinstance(self.full_name, Unset):
            full_name = UNSET
        else:
            full_name = self.full_name

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        job_title: None | str | Unset
        if isinstance(self.job_title, Unset):
            job_title = UNSET
        else:
            job_title = self.job_title

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        gender: None | str | Unset
        if isinstance(self.gender, Unset):
            gender = UNSET
        else:
            gender = self.gender

        dob: None | str | Unset
        if isinstance(self.dob, Unset):
            dob = UNSET
        elif isinstance(self.dob, datetime.date):
            dob = self.dob.isoformat()
        else:
            dob = self.dob

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

        linkedin_url: None | str | Unset
        if isinstance(self.linkedin_url, Unset):
            linkedin_url = UNSET
        else:
            linkedin_url = self.linkedin_url

        tier: None | str | Unset
        if isinstance(self.tier, Unset):
            tier = UNSET
        else:
            tier = self.tier

        is_decision_maker = self.is_decision_maker

        custom_fields: dict[str, Any] | None | Unset
        if isinstance(self.custom_fields, Unset):
            custom_fields = UNSET
        elif isinstance(self.custom_fields, ContactDetailDtoCustomFieldsType0):
            custom_fields = self.custom_fields.to_dict()
        else:
            custom_fields = self.custom_fields

        source_ref: None | str | Unset
        if isinstance(self.source_ref, Unset):
            source_ref = UNSET
        else:
            source_ref = self.source_ref

        tags: list[dict[str, Any]] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = []
            for tags_type_0_item_data in self.tags:
                tags_type_0_item = tags_type_0_item_data.to_dict()
                tags.append(tags_type_0_item)


        else:
            tags = self.tags

        customer_profile: dict[str, Any] | Unset = UNSET
        if not isinstance(self.customer_profile, Unset):
            customer_profile = self.customer_profile.to_dict()

        supplier_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.supplier_info, Unset):
            supplier_info = self.supplier_info.to_dict()

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        lifecycle_stage: None | str | Unset
        if isinstance(self.lifecycle_stage, Unset):
            lifecycle_stage = UNSET
        else:
            lifecycle_stage = self.lifecycle_stage

        industry_id: None | str | Unset
        if isinstance(self.industry_id, Unset):
            industry_id = UNSET
        elif isinstance(self.industry_id, UUID):
            industry_id = str(self.industry_id)
        else:
            industry_id = self.industry_id

        source_id: None | str | Unset
        if isinstance(self.source_id, Unset):
            source_id = UNSET
        elif isinstance(self.source_id, UUID):
            source_id = str(self.source_id)
        else:
            source_id = self.source_id

        customer_group_id: None | str | Unset
        if isinstance(self.customer_group_id, Unset):
            customer_group_id = UNSET
        elif isinstance(self.customer_group_id, UUID):
            customer_group_id = str(self.customer_group_id)
        else:
            customer_group_id = self.customer_group_id

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

        province_code: None | str | Unset
        if isinstance(self.province_code, Unset):
            province_code = UNSET
        else:
            province_code = self.province_code

        district_code: None | str | Unset
        if isinstance(self.district_code, Unset):
            district_code = UNSET
        else:
            district_code = self.district_code

        ward_code: None | str | Unset
        if isinstance(self.ward_code, Unset):
            ward_code = UNSET
        else:
            ward_code = self.ward_code

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        group_name: None | str | Unset
        if isinstance(self.group_name, Unset):
            group_name = UNSET
        else:
            group_name = self.group_name

        group_icon: None | str | Unset
        if isinstance(self.group_icon, Unset):
            group_icon = UNSET
        else:
            group_icon = self.group_icon

        group_color: None | str | Unset
        if isinstance(self.group_color, Unset):
            group_color = UNSET
        else:
            group_color = self.group_color

        assignee_id: None | str | Unset
        if isinstance(self.assignee_id, Unset):
            assignee_id = UNSET
        elif isinstance(self.assignee_id, UUID):
            assignee_id = str(self.assignee_id)
        else:
            assignee_id = self.assignee_id

        assignee_name: None | str | Unset
        if isinstance(self.assignee_name, Unset):
            assignee_name = UNSET
        else:
            assignee_name = self.assignee_name

        assigned_at: None | str | Unset
        if isinstance(self.assigned_at, Unset):
            assigned_at = UNSET
        elif isinstance(self.assigned_at, datetime.datetime):
            assigned_at = self.assigned_at.isoformat()
        else:
            assigned_at = self.assigned_at

        status_label: None | str | Unset
        if isinstance(self.status_label, Unset):
            status_label = UNSET
        else:
            status_label = self.status_label

        status_icon: None | str | Unset
        if isinstance(self.status_icon, Unset):
            status_icon = UNSET
        else:
            status_icon = self.status_icon

        status_color: None | str | Unset
        if isinstance(self.status_color, Unset):
            status_color = UNSET
        else:
            status_color = self.status_color

        contact_status_id: None | str | Unset
        if isinstance(self.contact_status_id, Unset):
            contact_status_id = UNSET
        elif isinstance(self.contact_status_id, UUID):
            contact_status_id = str(self.contact_status_id)
        else:
            contact_status_id = self.contact_status_id

        branch_id: None | str | Unset
        if isinstance(self.branch_id, Unset):
            branch_id = UNSET
        elif isinstance(self.branch_id, UUID):
            branch_id = str(self.branch_id)
        else:
            branch_id = self.branch_id

        branch_name: None | str | Unset
        if isinstance(self.branch_name, Unset):
            branch_name = UNSET
        else:
            branch_name = self.branch_name

        tax_code: None | str | Unset
        if isinstance(self.tax_code, Unset):
            tax_code = UNSET
        else:
            tax_code = self.tax_code

        bank_account_number: None | str | Unset
        if isinstance(self.bank_account_number, Unset):
            bank_account_number = UNSET
        else:
            bank_account_number = self.bank_account_number

        bank_name: None | str | Unset
        if isinstance(self.bank_name, Unset):
            bank_name = UNSET
        else:
            bank_name = self.bank_name

        bank_branch: None | str | Unset
        if isinstance(self.bank_branch, Unset):
            bank_branch = UNSET
        else:
            bank_branch = self.bank_branch

        lead_score = self.lead_score

        lead_tier: None | str | Unset
        if isinstance(self.lead_tier, Unset):
            lead_tier = UNSET
        else:
            lead_tier = self.lead_tier

        referral_code_id: None | str | Unset
        if isinstance(self.referral_code_id, Unset):
            referral_code_id = UNSET
        elif isinstance(self.referral_code_id, UUID):
            referral_code_id = str(self.referral_code_id)
        else:
            referral_code_id = self.referral_code_id

        referral_code_kind: None | str | Unset
        if isinstance(self.referral_code_kind, Unset):
            referral_code_kind = UNSET
        else:
            referral_code_kind = self.referral_code_kind

        referral_code: None | str | Unset
        if isinstance(self.referral_code, Unset):
            referral_code = UNSET
        else:
            referral_code = self.referral_code

        first_touch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.first_touch, Unset):
            first_touch = self.first_touch.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if code is not UNSET:
            field_dict["code"] = code
        if contact_type is not UNSET:
            field_dict["contactType"] = contact_type
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if job_title is not UNSET:
            field_dict["jobTitle"] = job_title
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if website is not UNSET:
            field_dict["website"] = website
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if gender is not UNSET:
            field_dict["gender"] = gender
        if dob is not UNSET:
            field_dict["dob"] = dob
        if address is not UNSET:
            field_dict["address"] = address
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if identity_number is not UNSET:
            field_dict["identityNumber"] = identity_number
        if identity_issued_date is not UNSET:
            field_dict["identityIssuedDate"] = identity_issued_date
        if identity_issued_place is not UNSET:
            field_dict["identityIssuedPlace"] = identity_issued_place
        if ward is not UNSET:
            field_dict["ward"] = ward
        if phone2 is not UNSET:
            field_dict["phone2"] = phone2
        if phone3 is not UNSET:
            field_dict["phone3"] = phone3
        if linkedin_url is not UNSET:
            field_dict["linkedinUrl"] = linkedin_url
        if tier is not UNSET:
            field_dict["tier"] = tier
        if is_decision_maker is not UNSET:
            field_dict["isDecisionMaker"] = is_decision_maker
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if source_ref is not UNSET:
            field_dict["sourceRef"] = source_ref
        if tags is not UNSET:
            field_dict["tags"] = tags
        if customer_profile is not UNSET:
            field_dict["customerProfile"] = customer_profile
        if supplier_info is not UNSET:
            field_dict["supplierInfo"] = supplier_info
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if lifecycle_stage is not UNSET:
            field_dict["lifecycleStage"] = lifecycle_stage
        if industry_id is not UNSET:
            field_dict["industryId"] = industry_id
        if source_id is not UNSET:
            field_dict["sourceId"] = source_id
        if customer_group_id is not UNSET:
            field_dict["customerGroupId"] = customer_group_id
        if contact_person_name is not UNSET:
            field_dict["contactPersonName"] = contact_person_name
        if contact_person_phone is not UNSET:
            field_dict["contactPersonPhone"] = contact_person_phone
        if contact_person_relationship is not UNSET:
            field_dict["contactPersonRelationship"] = contact_person_relationship
        if province_code is not UNSET:
            field_dict["provinceCode"] = province_code
        if district_code is not UNSET:
            field_dict["districtCode"] = district_code
        if ward_code is not UNSET:
            field_dict["wardCode"] = ward_code
        if notes is not UNSET:
            field_dict["notes"] = notes
        if group_name is not UNSET:
            field_dict["groupName"] = group_name
        if group_icon is not UNSET:
            field_dict["groupIcon"] = group_icon
        if group_color is not UNSET:
            field_dict["groupColor"] = group_color
        if assignee_id is not UNSET:
            field_dict["assigneeId"] = assignee_id
        if assignee_name is not UNSET:
            field_dict["assigneeName"] = assignee_name
        if assigned_at is not UNSET:
            field_dict["assignedAt"] = assigned_at
        if status_label is not UNSET:
            field_dict["statusLabel"] = status_label
        if status_icon is not UNSET:
            field_dict["statusIcon"] = status_icon
        if status_color is not UNSET:
            field_dict["statusColor"] = status_color
        if contact_status_id is not UNSET:
            field_dict["contactStatusId"] = contact_status_id
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id
        if branch_name is not UNSET:
            field_dict["branchName"] = branch_name
        if tax_code is not UNSET:
            field_dict["taxCode"] = tax_code
        if bank_account_number is not UNSET:
            field_dict["bankAccountNumber"] = bank_account_number
        if bank_name is not UNSET:
            field_dict["bankName"] = bank_name
        if bank_branch is not UNSET:
            field_dict["bankBranch"] = bank_branch
        if lead_score is not UNSET:
            field_dict["leadScore"] = lead_score
        if lead_tier is not UNSET:
            field_dict["leadTier"] = lead_tier
        if referral_code_id is not UNSET:
            field_dict["referralCodeId"] = referral_code_id
        if referral_code_kind is not UNSET:
            field_dict["referralCodeKind"] = referral_code_kind
        if referral_code is not UNSET:
            field_dict["referralCode"] = referral_code
        if first_touch is not UNSET:
            field_dict["firstTouch"] = first_touch

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_detail_dto_custom_fields_type_0 import ContactDetailDtoCustomFieldsType0 # noqa: PLC0415
        from ..models.contact_first_touch_dto import ContactFirstTouchDto # noqa: PLC0415
        from ..models.customer_profile_dto import CustomerProfileDto # noqa: PLC0415
        from ..models.supplier_info_ref_dto import SupplierInfoRefDto # noqa: PLC0415
        from ..models.tag_dto import TagDto # noqa: PLC0415
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        def _parse_contact_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_type = _parse_contact_type(d.pop("contactType", UNSET))


        def _parse_full_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        full_name = _parse_full_name(d.pop("fullName", UNSET))


        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))


        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))


        def _parse_job_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_title = _parse_job_title(d.pop("jobTitle", UNSET))


        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("companyName", UNSET))


        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("website", UNSET))


        def _parse_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url = _parse_avatar_url(d.pop("avatarUrl", UNSET))


        def _parse_gender(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gender = _parse_gender(d.pop("gender", UNSET))


        def _parse_dob(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dob_type_0 = datetime.date.fromisoformat(data)



                return dob_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        dob = _parse_dob(d.pop("dob", UNSET))


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


        def _parse_linkedin_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedinUrl", UNSET))


        def _parse_tier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tier = _parse_tier(d.pop("tier", UNSET))


        is_decision_maker = d.pop("isDecisionMaker", UNSET)

        def _parse_custom_fields(data: object) -> ContactDetailDtoCustomFieldsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_fields_type_0 = ContactDetailDtoCustomFieldsType0.from_dict(data)



                return custom_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ContactDetailDtoCustomFieldsType0 | None | Unset, data)

        custom_fields = _parse_custom_fields(d.pop("customFields", UNSET))


        def _parse_source_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_ref = _parse_source_ref(d.pop("sourceRef", UNSET))


        def _parse_tags(data: object) -> list[TagDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = []
                _tags_type_0 = data
                for tags_type_0_item_data in (_tags_type_0):
                    tags_type_0_item = TagDto.from_dict(tags_type_0_item_data)



                    tags_type_0.append(tags_type_0_item)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TagDto] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))


        _customer_profile = d.pop("customerProfile", UNSET)
        customer_profile: CustomerProfileDto | Unset
        if isinstance(_customer_profile,  Unset):
            customer_profile = UNSET
        else:
            customer_profile = CustomerProfileDto.from_dict(_customer_profile)




        _supplier_info = d.pop("supplierInfo", UNSET)
        supplier_info: SupplierInfoRefDto | Unset
        if isinstance(_supplier_info,  Unset):
            supplier_info = UNSET
        else:
            supplier_info = SupplierInfoRefDto.from_dict(_supplier_info)




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




        def _parse_lifecycle_stage(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lifecycle_stage = _parse_lifecycle_stage(d.pop("lifecycleStage", UNSET))


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


        def _parse_province_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        province_code = _parse_province_code(d.pop("provinceCode", UNSET))


        def _parse_district_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_code = _parse_district_code(d.pop("districtCode", UNSET))


        def _parse_ward_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ward_code = _parse_ward_code(d.pop("wardCode", UNSET))


        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


        def _parse_group_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_name = _parse_group_name(d.pop("groupName", UNSET))


        def _parse_group_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_icon = _parse_group_icon(d.pop("groupIcon", UNSET))


        def _parse_group_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_color = _parse_group_color(d.pop("groupColor", UNSET))


        def _parse_assignee_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                assignee_id_type_0 = UUID(data)



                return assignee_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        assignee_id = _parse_assignee_id(d.pop("assigneeId", UNSET))


        def _parse_assignee_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assignee_name = _parse_assignee_name(d.pop("assigneeName", UNSET))


        def _parse_assigned_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                assigned_at_type_0 = datetime.datetime.fromisoformat(data)



                return assigned_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        assigned_at = _parse_assigned_at(d.pop("assignedAt", UNSET))


        def _parse_status_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_label = _parse_status_label(d.pop("statusLabel", UNSET))


        def _parse_status_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_icon = _parse_status_icon(d.pop("statusIcon", UNSET))


        def _parse_status_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_color = _parse_status_color(d.pop("statusColor", UNSET))


        def _parse_contact_status_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                contact_status_id_type_0 = UUID(data)



                return contact_status_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        contact_status_id = _parse_contact_status_id(d.pop("contactStatusId", UNSET))


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


        def _parse_branch_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch_name = _parse_branch_name(d.pop("branchName", UNSET))


        def _parse_tax_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tax_code = _parse_tax_code(d.pop("taxCode", UNSET))


        def _parse_bank_account_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bank_account_number = _parse_bank_account_number(d.pop("bankAccountNumber", UNSET))


        def _parse_bank_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bank_name = _parse_bank_name(d.pop("bankName", UNSET))


        def _parse_bank_branch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bank_branch = _parse_bank_branch(d.pop("bankBranch", UNSET))


        lead_score = d.pop("leadScore", UNSET)

        def _parse_lead_tier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lead_tier = _parse_lead_tier(d.pop("leadTier", UNSET))


        def _parse_referral_code_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                referral_code_id_type_0 = UUID(data)



                return referral_code_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        referral_code_id = _parse_referral_code_id(d.pop("referralCodeId", UNSET))


        def _parse_referral_code_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        referral_code_kind = _parse_referral_code_kind(d.pop("referralCodeKind", UNSET))


        def _parse_referral_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        referral_code = _parse_referral_code(d.pop("referralCode", UNSET))


        _first_touch = d.pop("firstTouch", UNSET)
        first_touch: ContactFirstTouchDto | Unset
        if isinstance(_first_touch,  Unset):
            first_touch = UNSET
        else:
            first_touch = ContactFirstTouchDto.from_dict(_first_touch)




        contact_detail_dto = cls(
            id=id,
            code=code,
            contact_type=contact_type,
            full_name=full_name,
            email=email,
            phone=phone,
            job_title=job_title,
            company_name=company_name,
            website=website,
            avatar_url=avatar_url,
            gender=gender,
            dob=dob,
            address=address,
            city=city,
            country=country,
            identity_number=identity_number,
            identity_issued_date=identity_issued_date,
            identity_issued_place=identity_issued_place,
            ward=ward,
            phone2=phone2,
            phone3=phone3,
            linkedin_url=linkedin_url,
            tier=tier,
            is_decision_maker=is_decision_maker,
            custom_fields=custom_fields,
            source_ref=source_ref,
            tags=tags,
            customer_profile=customer_profile,
            supplier_info=supplier_info,
            created_at=created_at,
            updated_at=updated_at,
            lifecycle_stage=lifecycle_stage,
            industry_id=industry_id,
            source_id=source_id,
            customer_group_id=customer_group_id,
            contact_person_name=contact_person_name,
            contact_person_phone=contact_person_phone,
            contact_person_relationship=contact_person_relationship,
            province_code=province_code,
            district_code=district_code,
            ward_code=ward_code,
            notes=notes,
            group_name=group_name,
            group_icon=group_icon,
            group_color=group_color,
            assignee_id=assignee_id,
            assignee_name=assignee_name,
            assigned_at=assigned_at,
            status_label=status_label,
            status_icon=status_icon,
            status_color=status_color,
            contact_status_id=contact_status_id,
            branch_id=branch_id,
            branch_name=branch_name,
            tax_code=tax_code,
            bank_account_number=bank_account_number,
            bank_name=bank_name,
            bank_branch=bank_branch,
            lead_score=lead_score,
            lead_tier=lead_tier,
            referral_code_id=referral_code_id,
            referral_code_kind=referral_code_kind,
            referral_code=referral_code,
            first_touch=first_touch,
        )

        return contact_detail_dto


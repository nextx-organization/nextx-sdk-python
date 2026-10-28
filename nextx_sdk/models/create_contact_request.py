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
  from ..models.create_contact_request_custom_fields_type_0 import CreateContactRequestCustomFieldsType0





T = TypeVar("T", bound="CreateContactRequest")



@_attrs_define
class CreateContactRequest:
    

    contact_type: None | str | Unset = UNSET
    full_name: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    job_title: None | str | Unset = UNSET
    company_name: None | str | Unset = UNSET
    website: None | str | Unset = UNSET
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
    is_decision_maker: bool | Unset = UNSET
    custom_fields: CreateContactRequestCustomFieldsType0 | None | Unset = UNSET
    code: None | str | Unset = UNSET
    source_id: None | Unset | UUID = UNSET
    source_channel_type: None | str | Unset = UNSET
    branch_id: None | Unset | UUID = UNSET
    keep_unassigned: bool | Unset = UNSET
    lifecycle_stage: None | str | Unset = UNSET
    assignee_id: None | Unset | UUID = UNSET
    tax_code: None | str | Unset = UNSET
    bank_account_number: None | str | Unset = UNSET
    bank_name: None | str | Unset = UNSET
    bank_branch: None | str | Unset = UNSET
    referral_code_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_contact_request_custom_fields_type_0 import CreateContactRequestCustomFieldsType0 # noqa: PLC0415
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

        is_decision_maker = self.is_decision_maker

        custom_fields: dict[str, Any] | None | Unset
        if isinstance(self.custom_fields, Unset):
            custom_fields = UNSET
        elif isinstance(self.custom_fields, CreateContactRequestCustomFieldsType0):
            custom_fields = self.custom_fields.to_dict()
        else:
            custom_fields = self.custom_fields

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        source_id: None | str | Unset
        if isinstance(self.source_id, Unset):
            source_id = UNSET
        elif isinstance(self.source_id, UUID):
            source_id = str(self.source_id)
        else:
            source_id = self.source_id

        source_channel_type: None | str | Unset
        if isinstance(self.source_channel_type, Unset):
            source_channel_type = UNSET
        else:
            source_channel_type = self.source_channel_type

        branch_id: None | str | Unset
        if isinstance(self.branch_id, Unset):
            branch_id = UNSET
        elif isinstance(self.branch_id, UUID):
            branch_id = str(self.branch_id)
        else:
            branch_id = self.branch_id

        keep_unassigned = self.keep_unassigned

        lifecycle_stage: None | str | Unset
        if isinstance(self.lifecycle_stage, Unset):
            lifecycle_stage = UNSET
        else:
            lifecycle_stage = self.lifecycle_stage

        assignee_id: None | str | Unset
        if isinstance(self.assignee_id, Unset):
            assignee_id = UNSET
        elif isinstance(self.assignee_id, UUID):
            assignee_id = str(self.assignee_id)
        else:
            assignee_id = self.assignee_id

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

        referral_code_id: None | str | Unset
        if isinstance(self.referral_code_id, Unset):
            referral_code_id = UNSET
        elif isinstance(self.referral_code_id, UUID):
            referral_code_id = str(self.referral_code_id)
        else:
            referral_code_id = self.referral_code_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
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
        if is_decision_maker is not UNSET:
            field_dict["isDecisionMaker"] = is_decision_maker
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if code is not UNSET:
            field_dict["code"] = code
        if source_id is not UNSET:
            field_dict["sourceId"] = source_id
        if source_channel_type is not UNSET:
            field_dict["sourceChannelType"] = source_channel_type
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id
        if keep_unassigned is not UNSET:
            field_dict["keepUnassigned"] = keep_unassigned
        if lifecycle_stage is not UNSET:
            field_dict["lifecycleStage"] = lifecycle_stage
        if assignee_id is not UNSET:
            field_dict["assigneeId"] = assignee_id
        if tax_code is not UNSET:
            field_dict["taxCode"] = tax_code
        if bank_account_number is not UNSET:
            field_dict["bankAccountNumber"] = bank_account_number
        if bank_name is not UNSET:
            field_dict["bankName"] = bank_name
        if bank_branch is not UNSET:
            field_dict["bankBranch"] = bank_branch
        if referral_code_id is not UNSET:
            field_dict["referralCodeId"] = referral_code_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_contact_request_custom_fields_type_0 import CreateContactRequestCustomFieldsType0 # noqa: PLC0415
        d = dict(src_dict)
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


        is_decision_maker = d.pop("isDecisionMaker", UNSET)

        def _parse_custom_fields(data: object) -> CreateContactRequestCustomFieldsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_fields_type_0 = CreateContactRequestCustomFieldsType0.from_dict(data)



                return custom_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateContactRequestCustomFieldsType0 | None | Unset, data)

        custom_fields = _parse_custom_fields(d.pop("customFields", UNSET))


        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


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


        def _parse_source_channel_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_channel_type = _parse_source_channel_type(d.pop("sourceChannelType", UNSET))


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


        keep_unassigned = d.pop("keepUnassigned", UNSET)

        def _parse_lifecycle_stage(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lifecycle_stage = _parse_lifecycle_stage(d.pop("lifecycleStage", UNSET))


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


        create_contact_request = cls(
            contact_type=contact_type,
            full_name=full_name,
            email=email,
            phone=phone,
            job_title=job_title,
            company_name=company_name,
            website=website,
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
            is_decision_maker=is_decision_maker,
            custom_fields=custom_fields,
            code=code,
            source_id=source_id,
            source_channel_type=source_channel_type,
            branch_id=branch_id,
            keep_unassigned=keep_unassigned,
            lifecycle_stage=lifecycle_stage,
            assignee_id=assignee_id,
            tax_code=tax_code,
            bank_account_number=bank_account_number,
            bank_name=bank_name,
            bank_branch=bank_branch,
            referral_code_id=referral_code_id,
        )

        return create_contact_request


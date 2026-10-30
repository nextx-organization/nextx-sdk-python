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
  from ..models.contract_category_dto import ContractCategoryDto
  from ..models.contract_relation_dto import ContractRelationDto
  from ..models.contract_search_match_dto import ContractSearchMatchDto





T = TypeVar("T", bound="ContractSummaryDto")



@_attrs_define
class ContractSummaryDto:
    

    id: UUID | Unset = UNSET
    branch_id: UUID | Unset = UNSET
    branch_name: None | str | Unset = UNSET
    contract_code: None | str | Unset = UNSET
    gym_profile_id: UUID | Unset = UNSET
    member_code: None | str | Unset = UNSET
    member_name: None | str | Unset = UNSET
    package_name: None | str | Unset = UNSET
    package_type: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    scheduled_start_date: datetime.date | None | Unset = UNSET
    sale_staff_id: None | Unset | UUID = UNSET
    sale_staff_name: None | str | Unset = UNSET
    start_date: datetime.date | None | Unset = UNSET
    end_date: datetime.date | None | Unset = UNSET
    sessions_total: int | None | Unset = UNSET
    sessions_used: int | Unset = UNSET
    total_paid: float | Unset = UNSET
    debt_remaining: float | Unset = UNSET
    contract_date: datetime.date | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    discount_percent: float | None | Unset = UNSET
    total_discount_amount: float | Unset = UNSET
    activation_status: None | str | Unset = UNSET
    category: ContractCategoryDto | Unset = UNSET
    original_price: float | Unset = UNSET
    total_with_vat: float | Unset = UNSET
    duration_months: int | None | Unset = UNSET
    duration_days: int | Unset = UNSET
    is_renewal: bool | Unset = UNSET
    pt_id: None | Unset | UUID = UNSET
    pt_staff_name: None | str | Unset = UNSET
    order_channel: None | str | Unset = UNSET
    member_url: None | str | Unset = UNSET
    registration_date: datetime.date | None | Unset = UNSET
    training_branch_names: list[str] | None | Unset = UNSET
    training_all_branches: bool | Unset = UNSET
    sale_staff_code: None | str | Unset = UNSET
    pt_staff_code: None | str | Unset = UNSET
    search_matches: list[ContractSearchMatchDto] | None | Unset = UNSET
    package_unit_snapshot: None | str | Unset = UNSET
    bonus_months: int | Unset = UNSET
    bonus_days: int | Unset = UNSET
    bonus_sessions: int | Unset = UNSET
    service_value: float | None | Unset = UNSET
    carried_value_amount: float | Unset = UNSET
    pure_discount_amount: float | Unset = UNSET
    carried_from_contract_code: None | str | Unset = UNSET
    relation_from: ContractRelationDto | Unset = UNSET
    relation_to: ContractRelationDto | Unset = UNSET
    extension_value: float | Unset = UNSET
    is_branch_transfer: bool | Unset = UNSET
    is_branch_transfer_target: bool | Unset = UNSET
    is_session_exhausted: bool | Unset = UNSET
    approval_status: None | str | Unset = UNSET
    member_date_of_birth: datetime.date | None | Unset = UNSET
    member_phone: None | str | Unset = UNSET
    member_email: None | str | Unset = UNSET
    member_address: None | str | Unset = UNSET
    member_gender: None | str | Unset = UNSET
    member_group_name: None | str | Unset = UNSET
    member_source: None | str | Unset = UNSET
    member_device_pin: None | str | Unset = UNSET
    member_card_code: None | str | Unset = UNSET
    contract_kind: None | str | Unset = UNSET
    activated_at: datetime.datetime | None | Unset = UNSET
    notes: None | str | Unset = UNSET
    promotion_name: None | str | Unset = UNSET
    is_signed: bool | Unset = UNSET
    signed_at: datetime.datetime | None | Unset = UNSET
    signed_by_name: None | str | Unset = UNSET
    created_by_name: None | str | Unset = UNSET
    updated_by_name: None | str | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    max_members: int | Unset = UNSET
    group_member_names: list[str] | None | Unset = UNSET
    remaining_value: float | Unset = UNSET
    used_value: float | Unset = UNSET
    consumed_freeze_days: int | Unset = UNSET
    invoice_requested: bool | Unset = UNSET
    invoice_tax_code: None | str | Unset = UNSET
    invoice_company_name: None | str | Unset = UNSET
    invoice_address: None | str | Unset = UNSET
    invoice_buyer_name: None | str | Unset = UNSET
    invoice_email: None | str | Unset = UNSET
    auto_renew_status: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.contract_category_dto import ContractCategoryDto # noqa: PLC0415
        from ..models.contract_relation_dto import ContractRelationDto # noqa: PLC0415
        from ..models.contract_search_match_dto import ContractSearchMatchDto # noqa: PLC0415
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        branch_id: str | Unset = UNSET
        if not isinstance(self.branch_id, Unset):
            branch_id = str(self.branch_id)

        branch_name: None | str | Unset
        if isinstance(self.branch_name, Unset):
            branch_name = UNSET
        else:
            branch_name = self.branch_name

        contract_code: None | str | Unset
        if isinstance(self.contract_code, Unset):
            contract_code = UNSET
        else:
            contract_code = self.contract_code

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

        package_name: None | str | Unset
        if isinstance(self.package_name, Unset):
            package_name = UNSET
        else:
            package_name = self.package_name

        package_type: None | str | Unset
        if isinstance(self.package_type, Unset):
            package_type = UNSET
        else:
            package_type = self.package_type

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        scheduled_start_date: None | str | Unset
        if isinstance(self.scheduled_start_date, Unset):
            scheduled_start_date = UNSET
        elif isinstance(self.scheduled_start_date, datetime.date):
            scheduled_start_date = self.scheduled_start_date.isoformat()
        else:
            scheduled_start_date = self.scheduled_start_date

        sale_staff_id: None | str | Unset
        if isinstance(self.sale_staff_id, Unset):
            sale_staff_id = UNSET
        elif isinstance(self.sale_staff_id, UUID):
            sale_staff_id = str(self.sale_staff_id)
        else:
            sale_staff_id = self.sale_staff_id

        sale_staff_name: None | str | Unset
        if isinstance(self.sale_staff_name, Unset):
            sale_staff_name = UNSET
        else:
            sale_staff_name = self.sale_staff_name

        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.date):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.date):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        sessions_total: int | None | Unset
        if isinstance(self.sessions_total, Unset):
            sessions_total = UNSET
        else:
            sessions_total = self.sessions_total

        sessions_used = self.sessions_used

        total_paid = self.total_paid

        debt_remaining = self.debt_remaining

        contract_date: None | str | Unset
        if isinstance(self.contract_date, Unset):
            contract_date = UNSET
        elif isinstance(self.contract_date, datetime.date):
            contract_date = self.contract_date.isoformat()
        else:
            contract_date = self.contract_date

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        discount_percent: float | None | Unset
        if isinstance(self.discount_percent, Unset):
            discount_percent = UNSET
        else:
            discount_percent = self.discount_percent

        total_discount_amount = self.total_discount_amount

        activation_status: None | str | Unset
        if isinstance(self.activation_status, Unset):
            activation_status = UNSET
        else:
            activation_status = self.activation_status

        category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        original_price = self.original_price

        total_with_vat = self.total_with_vat

        duration_months: int | None | Unset
        if isinstance(self.duration_months, Unset):
            duration_months = UNSET
        else:
            duration_months = self.duration_months

        duration_days = self.duration_days

        is_renewal = self.is_renewal

        pt_id: None | str | Unset
        if isinstance(self.pt_id, Unset):
            pt_id = UNSET
        elif isinstance(self.pt_id, UUID):
            pt_id = str(self.pt_id)
        else:
            pt_id = self.pt_id

        pt_staff_name: None | str | Unset
        if isinstance(self.pt_staff_name, Unset):
            pt_staff_name = UNSET
        else:
            pt_staff_name = self.pt_staff_name

        order_channel: None | str | Unset
        if isinstance(self.order_channel, Unset):
            order_channel = UNSET
        else:
            order_channel = self.order_channel

        member_url: None | str | Unset
        if isinstance(self.member_url, Unset):
            member_url = UNSET
        else:
            member_url = self.member_url

        registration_date: None | str | Unset
        if isinstance(self.registration_date, Unset):
            registration_date = UNSET
        elif isinstance(self.registration_date, datetime.date):
            registration_date = self.registration_date.isoformat()
        else:
            registration_date = self.registration_date

        training_branch_names: list[str] | None | Unset
        if isinstance(self.training_branch_names, Unset):
            training_branch_names = UNSET
        elif isinstance(self.training_branch_names, list):
            training_branch_names = self.training_branch_names


        else:
            training_branch_names = self.training_branch_names

        training_all_branches = self.training_all_branches

        sale_staff_code: None | str | Unset
        if isinstance(self.sale_staff_code, Unset):
            sale_staff_code = UNSET
        else:
            sale_staff_code = self.sale_staff_code

        pt_staff_code: None | str | Unset
        if isinstance(self.pt_staff_code, Unset):
            pt_staff_code = UNSET
        else:
            pt_staff_code = self.pt_staff_code

        search_matches: list[dict[str, Any]] | None | Unset
        if isinstance(self.search_matches, Unset):
            search_matches = UNSET
        elif isinstance(self.search_matches, list):
            search_matches = []
            for search_matches_type_0_item_data in self.search_matches:
                search_matches_type_0_item = search_matches_type_0_item_data.to_dict()
                search_matches.append(search_matches_type_0_item)


        else:
            search_matches = self.search_matches

        package_unit_snapshot: None | str | Unset
        if isinstance(self.package_unit_snapshot, Unset):
            package_unit_snapshot = UNSET
        else:
            package_unit_snapshot = self.package_unit_snapshot

        bonus_months = self.bonus_months

        bonus_days = self.bonus_days

        bonus_sessions = self.bonus_sessions

        service_value: float | None | Unset
        if isinstance(self.service_value, Unset):
            service_value = UNSET
        else:
            service_value = self.service_value

        carried_value_amount = self.carried_value_amount

        pure_discount_amount = self.pure_discount_amount

        carried_from_contract_code: None | str | Unset
        if isinstance(self.carried_from_contract_code, Unset):
            carried_from_contract_code = UNSET
        else:
            carried_from_contract_code = self.carried_from_contract_code

        relation_from: dict[str, Any] | Unset = UNSET
        if not isinstance(self.relation_from, Unset):
            relation_from = self.relation_from.to_dict()

        relation_to: dict[str, Any] | Unset = UNSET
        if not isinstance(self.relation_to, Unset):
            relation_to = self.relation_to.to_dict()

        extension_value = self.extension_value

        is_branch_transfer = self.is_branch_transfer

        is_branch_transfer_target = self.is_branch_transfer_target

        is_session_exhausted = self.is_session_exhausted

        approval_status: None | str | Unset
        if isinstance(self.approval_status, Unset):
            approval_status = UNSET
        else:
            approval_status = self.approval_status

        member_date_of_birth: None | str | Unset
        if isinstance(self.member_date_of_birth, Unset):
            member_date_of_birth = UNSET
        elif isinstance(self.member_date_of_birth, datetime.date):
            member_date_of_birth = self.member_date_of_birth.isoformat()
        else:
            member_date_of_birth = self.member_date_of_birth

        member_phone: None | str | Unset
        if isinstance(self.member_phone, Unset):
            member_phone = UNSET
        else:
            member_phone = self.member_phone

        member_email: None | str | Unset
        if isinstance(self.member_email, Unset):
            member_email = UNSET
        else:
            member_email = self.member_email

        member_address: None | str | Unset
        if isinstance(self.member_address, Unset):
            member_address = UNSET
        else:
            member_address = self.member_address

        member_gender: None | str | Unset
        if isinstance(self.member_gender, Unset):
            member_gender = UNSET
        else:
            member_gender = self.member_gender

        member_group_name: None | str | Unset
        if isinstance(self.member_group_name, Unset):
            member_group_name = UNSET
        else:
            member_group_name = self.member_group_name

        member_source: None | str | Unset
        if isinstance(self.member_source, Unset):
            member_source = UNSET
        else:
            member_source = self.member_source

        member_device_pin: None | str | Unset
        if isinstance(self.member_device_pin, Unset):
            member_device_pin = UNSET
        else:
            member_device_pin = self.member_device_pin

        member_card_code: None | str | Unset
        if isinstance(self.member_card_code, Unset):
            member_card_code = UNSET
        else:
            member_card_code = self.member_card_code

        contract_kind: None | str | Unset
        if isinstance(self.contract_kind, Unset):
            contract_kind = UNSET
        else:
            contract_kind = self.contract_kind

        activated_at: None | str | Unset
        if isinstance(self.activated_at, Unset):
            activated_at = UNSET
        elif isinstance(self.activated_at, datetime.datetime):
            activated_at = self.activated_at.isoformat()
        else:
            activated_at = self.activated_at

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        promotion_name: None | str | Unset
        if isinstance(self.promotion_name, Unset):
            promotion_name = UNSET
        else:
            promotion_name = self.promotion_name

        is_signed = self.is_signed

        signed_at: None | str | Unset
        if isinstance(self.signed_at, Unset):
            signed_at = UNSET
        elif isinstance(self.signed_at, datetime.datetime):
            signed_at = self.signed_at.isoformat()
        else:
            signed_at = self.signed_at

        signed_by_name: None | str | Unset
        if isinstance(self.signed_by_name, Unset):
            signed_by_name = UNSET
        else:
            signed_by_name = self.signed_by_name

        created_by_name: None | str | Unset
        if isinstance(self.created_by_name, Unset):
            created_by_name = UNSET
        else:
            created_by_name = self.created_by_name

        updated_by_name: None | str | Unset
        if isinstance(self.updated_by_name, Unset):
            updated_by_name = UNSET
        else:
            updated_by_name = self.updated_by_name

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        max_members = self.max_members

        group_member_names: list[str] | None | Unset
        if isinstance(self.group_member_names, Unset):
            group_member_names = UNSET
        elif isinstance(self.group_member_names, list):
            group_member_names = self.group_member_names


        else:
            group_member_names = self.group_member_names

        remaining_value = self.remaining_value

        used_value = self.used_value

        consumed_freeze_days = self.consumed_freeze_days

        invoice_requested = self.invoice_requested

        invoice_tax_code: None | str | Unset
        if isinstance(self.invoice_tax_code, Unset):
            invoice_tax_code = UNSET
        else:
            invoice_tax_code = self.invoice_tax_code

        invoice_company_name: None | str | Unset
        if isinstance(self.invoice_company_name, Unset):
            invoice_company_name = UNSET
        else:
            invoice_company_name = self.invoice_company_name

        invoice_address: None | str | Unset
        if isinstance(self.invoice_address, Unset):
            invoice_address = UNSET
        else:
            invoice_address = self.invoice_address

        invoice_buyer_name: None | str | Unset
        if isinstance(self.invoice_buyer_name, Unset):
            invoice_buyer_name = UNSET
        else:
            invoice_buyer_name = self.invoice_buyer_name

        invoice_email: None | str | Unset
        if isinstance(self.invoice_email, Unset):
            invoice_email = UNSET
        else:
            invoice_email = self.invoice_email

        auto_renew_status: None | str | Unset
        if isinstance(self.auto_renew_status, Unset):
            auto_renew_status = UNSET
        else:
            auto_renew_status = self.auto_renew_status


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id
        if branch_name is not UNSET:
            field_dict["branchName"] = branch_name
        if contract_code is not UNSET:
            field_dict["contractCode"] = contract_code
        if gym_profile_id is not UNSET:
            field_dict["gymProfileId"] = gym_profile_id
        if member_code is not UNSET:
            field_dict["memberCode"] = member_code
        if member_name is not UNSET:
            field_dict["memberName"] = member_name
        if package_name is not UNSET:
            field_dict["packageName"] = package_name
        if package_type is not UNSET:
            field_dict["packageType"] = package_type
        if status is not UNSET:
            field_dict["status"] = status
        if scheduled_start_date is not UNSET:
            field_dict["scheduledStartDate"] = scheduled_start_date
        if sale_staff_id is not UNSET:
            field_dict["saleStaffId"] = sale_staff_id
        if sale_staff_name is not UNSET:
            field_dict["saleStaffName"] = sale_staff_name
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if sessions_total is not UNSET:
            field_dict["sessionsTotal"] = sessions_total
        if sessions_used is not UNSET:
            field_dict["sessionsUsed"] = sessions_used
        if total_paid is not UNSET:
            field_dict["totalPaid"] = total_paid
        if debt_remaining is not UNSET:
            field_dict["debtRemaining"] = debt_remaining
        if contract_date is not UNSET:
            field_dict["contractDate"] = contract_date
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if discount_percent is not UNSET:
            field_dict["discountPercent"] = discount_percent
        if total_discount_amount is not UNSET:
            field_dict["totalDiscountAmount"] = total_discount_amount
        if activation_status is not UNSET:
            field_dict["activationStatus"] = activation_status
        if category is not UNSET:
            field_dict["category"] = category
        if original_price is not UNSET:
            field_dict["originalPrice"] = original_price
        if total_with_vat is not UNSET:
            field_dict["totalWithVat"] = total_with_vat
        if duration_months is not UNSET:
            field_dict["durationMonths"] = duration_months
        if duration_days is not UNSET:
            field_dict["durationDays"] = duration_days
        if is_renewal is not UNSET:
            field_dict["isRenewal"] = is_renewal
        if pt_id is not UNSET:
            field_dict["ptId"] = pt_id
        if pt_staff_name is not UNSET:
            field_dict["ptStaffName"] = pt_staff_name
        if order_channel is not UNSET:
            field_dict["orderChannel"] = order_channel
        if member_url is not UNSET:
            field_dict["memberUrl"] = member_url
        if registration_date is not UNSET:
            field_dict["registrationDate"] = registration_date
        if training_branch_names is not UNSET:
            field_dict["trainingBranchNames"] = training_branch_names
        if training_all_branches is not UNSET:
            field_dict["trainingAllBranches"] = training_all_branches
        if sale_staff_code is not UNSET:
            field_dict["saleStaffCode"] = sale_staff_code
        if pt_staff_code is not UNSET:
            field_dict["ptStaffCode"] = pt_staff_code
        if search_matches is not UNSET:
            field_dict["searchMatches"] = search_matches
        if package_unit_snapshot is not UNSET:
            field_dict["packageUnitSnapshot"] = package_unit_snapshot
        if bonus_months is not UNSET:
            field_dict["bonusMonths"] = bonus_months
        if bonus_days is not UNSET:
            field_dict["bonusDays"] = bonus_days
        if bonus_sessions is not UNSET:
            field_dict["bonusSessions"] = bonus_sessions
        if service_value is not UNSET:
            field_dict["serviceValue"] = service_value
        if carried_value_amount is not UNSET:
            field_dict["carriedValueAmount"] = carried_value_amount
        if pure_discount_amount is not UNSET:
            field_dict["pureDiscountAmount"] = pure_discount_amount
        if carried_from_contract_code is not UNSET:
            field_dict["carriedFromContractCode"] = carried_from_contract_code
        if relation_from is not UNSET:
            field_dict["relationFrom"] = relation_from
        if relation_to is not UNSET:
            field_dict["relationTo"] = relation_to
        if extension_value is not UNSET:
            field_dict["extensionValue"] = extension_value
        if is_branch_transfer is not UNSET:
            field_dict["isBranchTransfer"] = is_branch_transfer
        if is_branch_transfer_target is not UNSET:
            field_dict["isBranchTransferTarget"] = is_branch_transfer_target
        if is_session_exhausted is not UNSET:
            field_dict["isSessionExhausted"] = is_session_exhausted
        if approval_status is not UNSET:
            field_dict["approvalStatus"] = approval_status
        if member_date_of_birth is not UNSET:
            field_dict["memberDateOfBirth"] = member_date_of_birth
        if member_phone is not UNSET:
            field_dict["memberPhone"] = member_phone
        if member_email is not UNSET:
            field_dict["memberEmail"] = member_email
        if member_address is not UNSET:
            field_dict["memberAddress"] = member_address
        if member_gender is not UNSET:
            field_dict["memberGender"] = member_gender
        if member_group_name is not UNSET:
            field_dict["memberGroupName"] = member_group_name
        if member_source is not UNSET:
            field_dict["memberSource"] = member_source
        if member_device_pin is not UNSET:
            field_dict["memberDevicePin"] = member_device_pin
        if member_card_code is not UNSET:
            field_dict["memberCardCode"] = member_card_code
        if contract_kind is not UNSET:
            field_dict["contractKind"] = contract_kind
        if activated_at is not UNSET:
            field_dict["activatedAt"] = activated_at
        if notes is not UNSET:
            field_dict["notes"] = notes
        if promotion_name is not UNSET:
            field_dict["promotionName"] = promotion_name
        if is_signed is not UNSET:
            field_dict["isSigned"] = is_signed
        if signed_at is not UNSET:
            field_dict["signedAt"] = signed_at
        if signed_by_name is not UNSET:
            field_dict["signedByName"] = signed_by_name
        if created_by_name is not UNSET:
            field_dict["createdByName"] = created_by_name
        if updated_by_name is not UNSET:
            field_dict["updatedByName"] = updated_by_name
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if max_members is not UNSET:
            field_dict["maxMembers"] = max_members
        if group_member_names is not UNSET:
            field_dict["groupMemberNames"] = group_member_names
        if remaining_value is not UNSET:
            field_dict["remainingValue"] = remaining_value
        if used_value is not UNSET:
            field_dict["usedValue"] = used_value
        if consumed_freeze_days is not UNSET:
            field_dict["consumedFreezeDays"] = consumed_freeze_days
        if invoice_requested is not UNSET:
            field_dict["invoiceRequested"] = invoice_requested
        if invoice_tax_code is not UNSET:
            field_dict["invoiceTaxCode"] = invoice_tax_code
        if invoice_company_name is not UNSET:
            field_dict["invoiceCompanyName"] = invoice_company_name
        if invoice_address is not UNSET:
            field_dict["invoiceAddress"] = invoice_address
        if invoice_buyer_name is not UNSET:
            field_dict["invoiceBuyerName"] = invoice_buyer_name
        if invoice_email is not UNSET:
            field_dict["invoiceEmail"] = invoice_email
        if auto_renew_status is not UNSET:
            field_dict["autoRenewStatus"] = auto_renew_status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contract_category_dto import ContractCategoryDto # noqa: PLC0415
        from ..models.contract_relation_dto import ContractRelationDto # noqa: PLC0415
        from ..models.contract_search_match_dto import ContractSearchMatchDto # noqa: PLC0415
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




        def _parse_branch_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch_name = _parse_branch_name(d.pop("branchName", UNSET))


        def _parse_contract_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contract_code = _parse_contract_code(d.pop("contractCode", UNSET))


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


        def _parse_package_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        package_name = _parse_package_name(d.pop("packageName", UNSET))


        def _parse_package_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        package_type = _parse_package_type(d.pop("packageType", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_scheduled_start_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scheduled_start_date_type_0 = datetime.date.fromisoformat(data)



                return scheduled_start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        scheduled_start_date = _parse_scheduled_start_date(d.pop("scheduledStartDate", UNSET))


        def _parse_sale_staff_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sale_staff_id_type_0 = UUID(data)



                return sale_staff_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        sale_staff_id = _parse_sale_staff_id(d.pop("saleStaffId", UNSET))


        def _parse_sale_staff_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sale_staff_name = _parse_sale_staff_name(d.pop("saleStaffName", UNSET))


        def _parse_start_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = datetime.date.fromisoformat(data)



                return start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        start_date = _parse_start_date(d.pop("startDate", UNSET))


        def _parse_end_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = datetime.date.fromisoformat(data)



                return end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        end_date = _parse_end_date(d.pop("endDate", UNSET))


        def _parse_sessions_total(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sessions_total = _parse_sessions_total(d.pop("sessionsTotal", UNSET))


        sessions_used = d.pop("sessionsUsed", UNSET)

        total_paid = d.pop("totalPaid", UNSET)

        debt_remaining = d.pop("debtRemaining", UNSET)

        def _parse_contract_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                contract_date_type_0 = datetime.date.fromisoformat(data)



                return contract_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        contract_date = _parse_contract_date(d.pop("contractDate", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_discount_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        discount_percent = _parse_discount_percent(d.pop("discountPercent", UNSET))


        total_discount_amount = d.pop("totalDiscountAmount", UNSET)

        def _parse_activation_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        activation_status = _parse_activation_status(d.pop("activationStatus", UNSET))


        _category = d.pop("category", UNSET)
        category: ContractCategoryDto | Unset
        if isinstance(_category,  Unset):
            category = UNSET
        else:
            category = ContractCategoryDto.from_dict(_category)




        original_price = d.pop("originalPrice", UNSET)

        total_with_vat = d.pop("totalWithVat", UNSET)

        def _parse_duration_months(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_months = _parse_duration_months(d.pop("durationMonths", UNSET))


        duration_days = d.pop("durationDays", UNSET)

        is_renewal = d.pop("isRenewal", UNSET)

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


        def _parse_pt_staff_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pt_staff_name = _parse_pt_staff_name(d.pop("ptStaffName", UNSET))


        def _parse_order_channel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        order_channel = _parse_order_channel(d.pop("orderChannel", UNSET))


        def _parse_member_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_url = _parse_member_url(d.pop("memberUrl", UNSET))


        def _parse_registration_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                registration_date_type_0 = datetime.date.fromisoformat(data)



                return registration_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        registration_date = _parse_registration_date(d.pop("registrationDate", UNSET))


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

        def _parse_sale_staff_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sale_staff_code = _parse_sale_staff_code(d.pop("saleStaffCode", UNSET))


        def _parse_pt_staff_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pt_staff_code = _parse_pt_staff_code(d.pop("ptStaffCode", UNSET))


        def _parse_search_matches(data: object) -> list[ContractSearchMatchDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                search_matches_type_0 = []
                _search_matches_type_0 = data
                for search_matches_type_0_item_data in (_search_matches_type_0):
                    search_matches_type_0_item = ContractSearchMatchDto.from_dict(search_matches_type_0_item_data)



                    search_matches_type_0.append(search_matches_type_0_item)

                return search_matches_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ContractSearchMatchDto] | None | Unset, data)

        search_matches = _parse_search_matches(d.pop("searchMatches", UNSET))


        def _parse_package_unit_snapshot(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        package_unit_snapshot = _parse_package_unit_snapshot(d.pop("packageUnitSnapshot", UNSET))


        bonus_months = d.pop("bonusMonths", UNSET)

        bonus_days = d.pop("bonusDays", UNSET)

        bonus_sessions = d.pop("bonusSessions", UNSET)

        def _parse_service_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        service_value = _parse_service_value(d.pop("serviceValue", UNSET))


        carried_value_amount = d.pop("carriedValueAmount", UNSET)

        pure_discount_amount = d.pop("pureDiscountAmount", UNSET)

        def _parse_carried_from_contract_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        carried_from_contract_code = _parse_carried_from_contract_code(d.pop("carriedFromContractCode", UNSET))


        _relation_from = d.pop("relationFrom", UNSET)
        relation_from: ContractRelationDto | Unset
        if isinstance(_relation_from,  Unset):
            relation_from = UNSET
        else:
            relation_from = ContractRelationDto.from_dict(_relation_from)




        _relation_to = d.pop("relationTo", UNSET)
        relation_to: ContractRelationDto | Unset
        if isinstance(_relation_to,  Unset):
            relation_to = UNSET
        else:
            relation_to = ContractRelationDto.from_dict(_relation_to)




        extension_value = d.pop("extensionValue", UNSET)

        is_branch_transfer = d.pop("isBranchTransfer", UNSET)

        is_branch_transfer_target = d.pop("isBranchTransferTarget", UNSET)

        is_session_exhausted = d.pop("isSessionExhausted", UNSET)

        def _parse_approval_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        approval_status = _parse_approval_status(d.pop("approvalStatus", UNSET))


        def _parse_member_date_of_birth(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                member_date_of_birth_type_0 = datetime.date.fromisoformat(data)



                return member_date_of_birth_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        member_date_of_birth = _parse_member_date_of_birth(d.pop("memberDateOfBirth", UNSET))


        def _parse_member_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_phone = _parse_member_phone(d.pop("memberPhone", UNSET))


        def _parse_member_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_email = _parse_member_email(d.pop("memberEmail", UNSET))


        def _parse_member_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_address = _parse_member_address(d.pop("memberAddress", UNSET))


        def _parse_member_gender(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_gender = _parse_member_gender(d.pop("memberGender", UNSET))


        def _parse_member_group_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_group_name = _parse_member_group_name(d.pop("memberGroupName", UNSET))


        def _parse_member_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_source = _parse_member_source(d.pop("memberSource", UNSET))


        def _parse_member_device_pin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_device_pin = _parse_member_device_pin(d.pop("memberDevicePin", UNSET))


        def _parse_member_card_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_card_code = _parse_member_card_code(d.pop("memberCardCode", UNSET))


        def _parse_contract_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contract_kind = _parse_contract_kind(d.pop("contractKind", UNSET))


        def _parse_activated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                activated_at_type_0 = datetime.datetime.fromisoformat(data)



                return activated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        activated_at = _parse_activated_at(d.pop("activatedAt", UNSET))


        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


        def _parse_promotion_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        promotion_name = _parse_promotion_name(d.pop("promotionName", UNSET))


        is_signed = d.pop("isSigned", UNSET)

        def _parse_signed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                signed_at_type_0 = datetime.datetime.fromisoformat(data)



                return signed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        signed_at = _parse_signed_at(d.pop("signedAt", UNSET))


        def _parse_signed_by_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        signed_by_name = _parse_signed_by_name(d.pop("signedByName", UNSET))


        def _parse_created_by_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by_name = _parse_created_by_name(d.pop("createdByName", UNSET))


        def _parse_updated_by_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_by_name = _parse_updated_by_name(d.pop("updatedByName", UNSET))


        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)



                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))


        max_members = d.pop("maxMembers", UNSET)

        def _parse_group_member_names(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                group_member_names_type_0 = cast(list[str], data)

                return group_member_names_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        group_member_names = _parse_group_member_names(d.pop("groupMemberNames", UNSET))


        remaining_value = d.pop("remainingValue", UNSET)

        used_value = d.pop("usedValue", UNSET)

        consumed_freeze_days = d.pop("consumedFreezeDays", UNSET)

        invoice_requested = d.pop("invoiceRequested", UNSET)

        def _parse_invoice_tax_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        invoice_tax_code = _parse_invoice_tax_code(d.pop("invoiceTaxCode", UNSET))


        def _parse_invoice_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        invoice_company_name = _parse_invoice_company_name(d.pop("invoiceCompanyName", UNSET))


        def _parse_invoice_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        invoice_address = _parse_invoice_address(d.pop("invoiceAddress", UNSET))


        def _parse_invoice_buyer_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        invoice_buyer_name = _parse_invoice_buyer_name(d.pop("invoiceBuyerName", UNSET))


        def _parse_invoice_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        invoice_email = _parse_invoice_email(d.pop("invoiceEmail", UNSET))


        def _parse_auto_renew_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        auto_renew_status = _parse_auto_renew_status(d.pop("autoRenewStatus", UNSET))


        contract_summary_dto = cls(
            id=id,
            branch_id=branch_id,
            branch_name=branch_name,
            contract_code=contract_code,
            gym_profile_id=gym_profile_id,
            member_code=member_code,
            member_name=member_name,
            package_name=package_name,
            package_type=package_type,
            status=status,
            scheduled_start_date=scheduled_start_date,
            sale_staff_id=sale_staff_id,
            sale_staff_name=sale_staff_name,
            start_date=start_date,
            end_date=end_date,
            sessions_total=sessions_total,
            sessions_used=sessions_used,
            total_paid=total_paid,
            debt_remaining=debt_remaining,
            contract_date=contract_date,
            created_at=created_at,
            discount_percent=discount_percent,
            total_discount_amount=total_discount_amount,
            activation_status=activation_status,
            category=category,
            original_price=original_price,
            total_with_vat=total_with_vat,
            duration_months=duration_months,
            duration_days=duration_days,
            is_renewal=is_renewal,
            pt_id=pt_id,
            pt_staff_name=pt_staff_name,
            order_channel=order_channel,
            member_url=member_url,
            registration_date=registration_date,
            training_branch_names=training_branch_names,
            training_all_branches=training_all_branches,
            sale_staff_code=sale_staff_code,
            pt_staff_code=pt_staff_code,
            search_matches=search_matches,
            package_unit_snapshot=package_unit_snapshot,
            bonus_months=bonus_months,
            bonus_days=bonus_days,
            bonus_sessions=bonus_sessions,
            service_value=service_value,
            carried_value_amount=carried_value_amount,
            pure_discount_amount=pure_discount_amount,
            carried_from_contract_code=carried_from_contract_code,
            relation_from=relation_from,
            relation_to=relation_to,
            extension_value=extension_value,
            is_branch_transfer=is_branch_transfer,
            is_branch_transfer_target=is_branch_transfer_target,
            is_session_exhausted=is_session_exhausted,
            approval_status=approval_status,
            member_date_of_birth=member_date_of_birth,
            member_phone=member_phone,
            member_email=member_email,
            member_address=member_address,
            member_gender=member_gender,
            member_group_name=member_group_name,
            member_source=member_source,
            member_device_pin=member_device_pin,
            member_card_code=member_card_code,
            contract_kind=contract_kind,
            activated_at=activated_at,
            notes=notes,
            promotion_name=promotion_name,
            is_signed=is_signed,
            signed_at=signed_at,
            signed_by_name=signed_by_name,
            created_by_name=created_by_name,
            updated_by_name=updated_by_name,
            updated_at=updated_at,
            max_members=max_members,
            group_member_names=group_member_names,
            remaining_value=remaining_value,
            used_value=used_value,
            consumed_freeze_days=consumed_freeze_days,
            invoice_requested=invoice_requested,
            invoice_tax_code=invoice_tax_code,
            invoice_company_name=invoice_company_name,
            invoice_address=invoice_address,
            invoice_buyer_name=invoice_buyer_name,
            invoice_email=invoice_email,
            auto_renew_status=auto_renew_status,
        )

        return contract_summary_dto


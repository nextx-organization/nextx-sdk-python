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






T = TypeVar("T", bound="SubscriptionSummaryDto")



@_attrs_define
class SubscriptionSummaryDto:
    

    id: UUID | Unset = UNSET
    contract_code: None | str | Unset = UNSET
    package_name: None | str | Unset = UNSET
    package_type: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    start_date: datetime.date | None | Unset = UNSET
    end_date: datetime.date | None | Unset = UNSET
    sessions_total: int | None | Unset = UNSET
    sessions_used: int | None | Unset = UNSET
    price_paid: float | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    is_group: bool | Unset = UNSET
    max_members: int | Unset = UNSET
    group_member_count: int | None | Unset = UNSET
    group_role: None | str | Unset = UNSET
    pt_id: None | Unset | UUID = UNSET
    approval_status: None | str | Unset = UNSET
    activation_status: None | str | Unset = UNSET
    debt_remaining: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

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

        sessions_used: int | None | Unset
        if isinstance(self.sessions_used, Unset):
            sessions_used = UNSET
        else:
            sessions_used = self.sessions_used

        price_paid = self.price_paid

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        is_group = self.is_group

        max_members = self.max_members

        group_member_count: int | None | Unset
        if isinstance(self.group_member_count, Unset):
            group_member_count = UNSET
        else:
            group_member_count = self.group_member_count

        group_role: None | str | Unset
        if isinstance(self.group_role, Unset):
            group_role = UNSET
        else:
            group_role = self.group_role

        pt_id: None | str | Unset
        if isinstance(self.pt_id, Unset):
            pt_id = UNSET
        elif isinstance(self.pt_id, UUID):
            pt_id = str(self.pt_id)
        else:
            pt_id = self.pt_id

        approval_status: None | str | Unset
        if isinstance(self.approval_status, Unset):
            approval_status = UNSET
        else:
            approval_status = self.approval_status

        activation_status: None | str | Unset
        if isinstance(self.activation_status, Unset):
            activation_status = UNSET
        else:
            activation_status = self.activation_status

        debt_remaining = self.debt_remaining


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if contract_code is not UNSET:
            field_dict["contractCode"] = contract_code
        if package_name is not UNSET:
            field_dict["packageName"] = package_name
        if package_type is not UNSET:
            field_dict["packageType"] = package_type
        if status is not UNSET:
            field_dict["status"] = status
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if sessions_total is not UNSET:
            field_dict["sessionsTotal"] = sessions_total
        if sessions_used is not UNSET:
            field_dict["sessionsUsed"] = sessions_used
        if price_paid is not UNSET:
            field_dict["pricePaid"] = price_paid
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if is_group is not UNSET:
            field_dict["isGroup"] = is_group
        if max_members is not UNSET:
            field_dict["maxMembers"] = max_members
        if group_member_count is not UNSET:
            field_dict["groupMemberCount"] = group_member_count
        if group_role is not UNSET:
            field_dict["groupRole"] = group_role
        if pt_id is not UNSET:
            field_dict["ptId"] = pt_id
        if approval_status is not UNSET:
            field_dict["approvalStatus"] = approval_status
        if activation_status is not UNSET:
            field_dict["activationStatus"] = activation_status
        if debt_remaining is not UNSET:
            field_dict["debtRemaining"] = debt_remaining

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


        def _parse_sessions_used(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sessions_used = _parse_sessions_used(d.pop("sessionsUsed", UNSET))


        price_paid = d.pop("pricePaid", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        is_group = d.pop("isGroup", UNSET)

        max_members = d.pop("maxMembers", UNSET)

        def _parse_group_member_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        group_member_count = _parse_group_member_count(d.pop("groupMemberCount", UNSET))


        def _parse_group_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_role = _parse_group_role(d.pop("groupRole", UNSET))


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


        def _parse_approval_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        approval_status = _parse_approval_status(d.pop("approvalStatus", UNSET))


        def _parse_activation_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        activation_status = _parse_activation_status(d.pop("activationStatus", UNSET))


        debt_remaining = d.pop("debtRemaining", UNSET)

        subscription_summary_dto = cls(
            id=id,
            contract_code=contract_code,
            package_name=package_name,
            package_type=package_type,
            status=status,
            start_date=start_date,
            end_date=end_date,
            sessions_total=sessions_total,
            sessions_used=sessions_used,
            price_paid=price_paid,
            created_at=created_at,
            is_group=is_group,
            max_members=max_members,
            group_member_count=group_member_count,
            group_role=group_role,
            pt_id=pt_id,
            approval_status=approval_status,
            activation_status=activation_status,
            debt_remaining=debt_remaining,
        )

        return subscription_summary_dto


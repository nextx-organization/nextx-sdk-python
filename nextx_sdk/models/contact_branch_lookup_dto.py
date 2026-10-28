from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="ContactBranchLookupDto")



@_attrs_define
class ContactBranchLookupDto:
    

    contact_id: UUID | Unset = UNSET
    code: None | str | Unset = UNSET
    full_name: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    lifecycle_stage: None | str | Unset = UNSET
    branch_id: None | Unset | UUID = UNSET
    branch_name: None | str | Unset = UNSET
    assignee_id: None | Unset | UUID = UNSET
    assignee_name: None | str | Unset = UNSET
    visible_to_you: bool | Unset = UNSET
    can_claim: bool | Unset = UNSET
    can_transfer: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        contact_id: str | Unset = UNSET
        if not isinstance(self.contact_id, Unset):
            contact_id = str(self.contact_id)

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

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

        lifecycle_stage: None | str | Unset
        if isinstance(self.lifecycle_stage, Unset):
            lifecycle_stage = UNSET
        else:
            lifecycle_stage = self.lifecycle_stage

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

        visible_to_you = self.visible_to_you

        can_claim = self.can_claim

        can_transfer = self.can_transfer


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if contact_id is not UNSET:
            field_dict["contactId"] = contact_id
        if code is not UNSET:
            field_dict["code"] = code
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if lifecycle_stage is not UNSET:
            field_dict["lifecycleStage"] = lifecycle_stage
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id
        if branch_name is not UNSET:
            field_dict["branchName"] = branch_name
        if assignee_id is not UNSET:
            field_dict["assigneeId"] = assignee_id
        if assignee_name is not UNSET:
            field_dict["assigneeName"] = assignee_name
        if visible_to_you is not UNSET:
            field_dict["visibleToYou"] = visible_to_you
        if can_claim is not UNSET:
            field_dict["canClaim"] = can_claim
        if can_transfer is not UNSET:
            field_dict["canTransfer"] = can_transfer

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _contact_id = d.pop("contactId", UNSET)
        contact_id: UUID | Unset
        if isinstance(_contact_id,  Unset):
            contact_id = UNSET
        else:
            contact_id = UUID(_contact_id)




        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


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


        def _parse_lifecycle_stage(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lifecycle_stage = _parse_lifecycle_stage(d.pop("lifecycleStage", UNSET))


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


        visible_to_you = d.pop("visibleToYou", UNSET)

        can_claim = d.pop("canClaim", UNSET)

        can_transfer = d.pop("canTransfer", UNSET)

        contact_branch_lookup_dto = cls(
            contact_id=contact_id,
            code=code,
            full_name=full_name,
            phone=phone,
            lifecycle_stage=lifecycle_stage,
            branch_id=branch_id,
            branch_name=branch_name,
            assignee_id=assignee_id,
            assignee_name=assignee_name,
            visible_to_you=visible_to_you,
            can_claim=can_claim,
            can_transfer=can_transfer,
        )

        return contact_branch_lookup_dto


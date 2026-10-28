from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ContractSearchMatchDto")



@_attrs_define
class ContractSearchMatchDto:
    

    member_name: None | str | Unset = UNSET
    member_code: None | str | Unset = UNSET
    matched_field: None | str | Unset = UNSET
    is_group_member: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        member_name: None | str | Unset
        if isinstance(self.member_name, Unset):
            member_name = UNSET
        else:
            member_name = self.member_name

        member_code: None | str | Unset
        if isinstance(self.member_code, Unset):
            member_code = UNSET
        else:
            member_code = self.member_code

        matched_field: None | str | Unset
        if isinstance(self.matched_field, Unset):
            matched_field = UNSET
        else:
            matched_field = self.matched_field

        is_group_member = self.is_group_member


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if member_name is not UNSET:
            field_dict["memberName"] = member_name
        if member_code is not UNSET:
            field_dict["memberCode"] = member_code
        if matched_field is not UNSET:
            field_dict["matchedField"] = matched_field
        if is_group_member is not UNSET:
            field_dict["isGroupMember"] = is_group_member

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_member_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_name = _parse_member_name(d.pop("memberName", UNSET))


        def _parse_member_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_code = _parse_member_code(d.pop("memberCode", UNSET))


        def _parse_matched_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        matched_field = _parse_matched_field(d.pop("matchedField", UNSET))


        is_group_member = d.pop("isGroupMember", UNSET)

        contract_search_match_dto = cls(
            member_name=member_name,
            member_code=member_code,
            matched_field=matched_field,
            is_group_member=is_group_member,
        )

        return contract_search_match_dto


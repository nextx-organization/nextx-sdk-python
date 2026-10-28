from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.member_lookup_dto import MemberLookupDto





T = TypeVar("T", bound="MemberDuplicateCheckDto")



@_attrs_define
class MemberDuplicateCheckDto:
    

    phone_rule: None | str | Unset = UNSET
    email_rule: None | str | Unset = UNSET
    phone_matches: list[MemberLookupDto] | None | Unset = UNSET
    email_matches: list[MemberLookupDto] | None | Unset = UNSET
    identity_rule: None | str | Unset = UNSET
    identity_matches: list[MemberLookupDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.member_lookup_dto import MemberLookupDto # noqa: PLC0415
        phone_rule: None | str | Unset
        if isinstance(self.phone_rule, Unset):
            phone_rule = UNSET
        else:
            phone_rule = self.phone_rule

        email_rule: None | str | Unset
        if isinstance(self.email_rule, Unset):
            email_rule = UNSET
        else:
            email_rule = self.email_rule

        phone_matches: list[dict[str, Any]] | None | Unset
        if isinstance(self.phone_matches, Unset):
            phone_matches = UNSET
        elif isinstance(self.phone_matches, list):
            phone_matches = []
            for phone_matches_type_0_item_data in self.phone_matches:
                phone_matches_type_0_item = phone_matches_type_0_item_data.to_dict()
                phone_matches.append(phone_matches_type_0_item)


        else:
            phone_matches = self.phone_matches

        email_matches: list[dict[str, Any]] | None | Unset
        if isinstance(self.email_matches, Unset):
            email_matches = UNSET
        elif isinstance(self.email_matches, list):
            email_matches = []
            for email_matches_type_0_item_data in self.email_matches:
                email_matches_type_0_item = email_matches_type_0_item_data.to_dict()
                email_matches.append(email_matches_type_0_item)


        else:
            email_matches = self.email_matches

        identity_rule: None | str | Unset
        if isinstance(self.identity_rule, Unset):
            identity_rule = UNSET
        else:
            identity_rule = self.identity_rule

        identity_matches: list[dict[str, Any]] | None | Unset
        if isinstance(self.identity_matches, Unset):
            identity_matches = UNSET
        elif isinstance(self.identity_matches, list):
            identity_matches = []
            for identity_matches_type_0_item_data in self.identity_matches:
                identity_matches_type_0_item = identity_matches_type_0_item_data.to_dict()
                identity_matches.append(identity_matches_type_0_item)


        else:
            identity_matches = self.identity_matches


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if phone_rule is not UNSET:
            field_dict["phoneRule"] = phone_rule
        if email_rule is not UNSET:
            field_dict["emailRule"] = email_rule
        if phone_matches is not UNSET:
            field_dict["phoneMatches"] = phone_matches
        if email_matches is not UNSET:
            field_dict["emailMatches"] = email_matches
        if identity_rule is not UNSET:
            field_dict["identityRule"] = identity_rule
        if identity_matches is not UNSET:
            field_dict["identityMatches"] = identity_matches

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.member_lookup_dto import MemberLookupDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_phone_rule(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone_rule = _parse_phone_rule(d.pop("phoneRule", UNSET))


        def _parse_email_rule(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_rule = _parse_email_rule(d.pop("emailRule", UNSET))


        def _parse_phone_matches(data: object) -> list[MemberLookupDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                phone_matches_type_0 = []
                _phone_matches_type_0 = data
                for phone_matches_type_0_item_data in (_phone_matches_type_0):
                    phone_matches_type_0_item = MemberLookupDto.from_dict(phone_matches_type_0_item_data)



                    phone_matches_type_0.append(phone_matches_type_0_item)

                return phone_matches_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MemberLookupDto] | None | Unset, data)

        phone_matches = _parse_phone_matches(d.pop("phoneMatches", UNSET))


        def _parse_email_matches(data: object) -> list[MemberLookupDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                email_matches_type_0 = []
                _email_matches_type_0 = data
                for email_matches_type_0_item_data in (_email_matches_type_0):
                    email_matches_type_0_item = MemberLookupDto.from_dict(email_matches_type_0_item_data)



                    email_matches_type_0.append(email_matches_type_0_item)

                return email_matches_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MemberLookupDto] | None | Unset, data)

        email_matches = _parse_email_matches(d.pop("emailMatches", UNSET))


        def _parse_identity_rule(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        identity_rule = _parse_identity_rule(d.pop("identityRule", UNSET))


        def _parse_identity_matches(data: object) -> list[MemberLookupDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                identity_matches_type_0 = []
                _identity_matches_type_0 = data
                for identity_matches_type_0_item_data in (_identity_matches_type_0):
                    identity_matches_type_0_item = MemberLookupDto.from_dict(identity_matches_type_0_item_data)



                    identity_matches_type_0.append(identity_matches_type_0_item)

                return identity_matches_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MemberLookupDto] | None | Unset, data)

        identity_matches = _parse_identity_matches(d.pop("identityMatches", UNSET))


        member_duplicate_check_dto = cls(
            phone_rule=phone_rule,
            email_rule=email_rule,
            phone_matches=phone_matches,
            email_matches=email_matches,
            identity_rule=identity_rule,
            identity_matches=identity_matches,
        )

        return member_duplicate_check_dto


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="MemberStatsDto")



@_attrs_define
class MemberStatsDto:
    

    total: int | Unset = UNSET
    joined_today: int | Unset = UNSET
    active: int | Unset = UNSET
    expiring_soon: int | Unset = UNSET
    no_contract: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        total = self.total

        joined_today = self.joined_today

        active = self.active

        expiring_soon = self.expiring_soon

        no_contract = self.no_contract


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if total is not UNSET:
            field_dict["total"] = total
        if joined_today is not UNSET:
            field_dict["joinedToday"] = joined_today
        if active is not UNSET:
            field_dict["active"] = active
        if expiring_soon is not UNSET:
            field_dict["expiringSoon"] = expiring_soon
        if no_contract is not UNSET:
            field_dict["noContract"] = no_contract

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total", UNSET)

        joined_today = d.pop("joinedToday", UNSET)

        active = d.pop("active", UNSET)

        expiring_soon = d.pop("expiringSoon", UNSET)

        no_contract = d.pop("noContract", UNSET)

        member_stats_dto = cls(
            total=total,
            joined_today=joined_today,
            active=active,
            expiring_soon=expiring_soon,
            no_contract=no_contract,
        )

        return member_stats_dto


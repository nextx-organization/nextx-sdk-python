from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OrderAssigneeDto")



@_attrs_define
class OrderAssigneeDto:
    

    user_id: UUID | Unset = UNSET
    name: None | str | Unset = UNSET
    commission_percent: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        commission_percent = self.commission_percent


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if name is not UNSET:
            field_dict["name"] = name
        if commission_percent is not UNSET:
            field_dict["commissionPercent"] = commission_percent

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _user_id = d.pop("userId", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id,  Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)




        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        commission_percent = d.pop("commissionPercent", UNSET)

        order_assignee_dto = cls(
            user_id=user_id,
            name=name,
            commission_percent=commission_percent,
        )

        return order_assignee_dto


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="BookableClassSubscriptionDto")



@_attrs_define
class BookableClassSubscriptionDto:
    

    subscription_id: UUID | Unset = UNSET
    package_id: UUID | Unset = UNSET
    package_name: None | str | Unset = UNSET
    sessions_total: int | None | Unset = UNSET
    sessions_used: int | Unset = UNSET
    sessions_remaining: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        subscription_id: str | Unset = UNSET
        if not isinstance(self.subscription_id, Unset):
            subscription_id = str(self.subscription_id)

        package_id: str | Unset = UNSET
        if not isinstance(self.package_id, Unset):
            package_id = str(self.package_id)

        package_name: None | str | Unset
        if isinstance(self.package_name, Unset):
            package_name = UNSET
        else:
            package_name = self.package_name

        sessions_total: int | None | Unset
        if isinstance(self.sessions_total, Unset):
            sessions_total = UNSET
        else:
            sessions_total = self.sessions_total

        sessions_used = self.sessions_used

        sessions_remaining: int | None | Unset
        if isinstance(self.sessions_remaining, Unset):
            sessions_remaining = UNSET
        else:
            sessions_remaining = self.sessions_remaining


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if package_id is not UNSET:
            field_dict["packageId"] = package_id
        if package_name is not UNSET:
            field_dict["packageName"] = package_name
        if sessions_total is not UNSET:
            field_dict["sessionsTotal"] = sessions_total
        if sessions_used is not UNSET:
            field_dict["sessionsUsed"] = sessions_used
        if sessions_remaining is not UNSET:
            field_dict["sessionsRemaining"] = sessions_remaining

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _subscription_id = d.pop("subscriptionId", UNSET)
        subscription_id: UUID | Unset
        if isinstance(_subscription_id,  Unset):
            subscription_id = UNSET
        else:
            subscription_id = UUID(_subscription_id)




        _package_id = d.pop("packageId", UNSET)
        package_id: UUID | Unset
        if isinstance(_package_id,  Unset):
            package_id = UNSET
        else:
            package_id = UUID(_package_id)




        def _parse_package_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        package_name = _parse_package_name(d.pop("packageName", UNSET))


        def _parse_sessions_total(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sessions_total = _parse_sessions_total(d.pop("sessionsTotal", UNSET))


        sessions_used = d.pop("sessionsUsed", UNSET)

        def _parse_sessions_remaining(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sessions_remaining = _parse_sessions_remaining(d.pop("sessionsRemaining", UNSET))


        bookable_class_subscription_dto = cls(
            subscription_id=subscription_id,
            package_id=package_id,
            package_name=package_name,
            sessions_total=sessions_total,
            sessions_used=sessions_used,
            sessions_remaining=sessions_remaining,
        )

        return bookable_class_subscription_dto


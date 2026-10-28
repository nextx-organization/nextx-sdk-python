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






T = TypeVar("T", bound="CustomerProfileDto")



@_attrs_define
class CustomerProfileDto:
    

    id: UUID | Unset = UNSET
    tier: None | str | Unset = UNSET
    customer_status: None | str | Unset = UNSET
    lifetime_value: float | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        tier: None | str | Unset
        if isinstance(self.tier, Unset):
            tier = UNSET
        else:
            tier = self.tier

        customer_status: None | str | Unset
        if isinstance(self.customer_status, Unset):
            customer_status = UNSET
        else:
            customer_status = self.customer_status

        lifetime_value = self.lifetime_value

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if tier is not UNSET:
            field_dict["tier"] = tier
        if customer_status is not UNSET:
            field_dict["customerStatus"] = customer_status
        if lifetime_value is not UNSET:
            field_dict["lifetimeValue"] = lifetime_value
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

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




        def _parse_tier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tier = _parse_tier(d.pop("tier", UNSET))


        def _parse_customer_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_status = _parse_customer_status(d.pop("customerStatus", UNSET))


        lifetime_value = d.pop("lifetimeValue", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        customer_profile_dto = cls(
            id=id,
            tier=tier,
            customer_status=customer_status,
            lifetime_value=lifetime_value,
            created_at=created_at,
        )

        return customer_profile_dto


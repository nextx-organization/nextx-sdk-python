from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.contact_list_stats_dto_by_contact_status_type_0 import ContactListStatsDtoByContactStatusType0
  from ..models.contact_list_stats_dto_by_lifecycle_stage_type_0 import ContactListStatsDtoByLifecycleStageType0
  from ..models.contact_list_stats_dto_by_tier_type_0 import ContactListStatsDtoByTierType0





T = TypeVar("T", bound="ContactListStatsDto")



@_attrs_define
class ContactListStatsDto:
    

    total: int | Unset = UNSET
    with_customer_profile: int | Unset = UNSET
    by_tier: ContactListStatsDtoByTierType0 | None | Unset = UNSET
    by_lifecycle_stage: ContactListStatsDtoByLifecycleStageType0 | None | Unset = UNSET
    by_contact_status: ContactListStatsDtoByContactStatusType0 | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.contact_list_stats_dto_by_contact_status_type_0 import ContactListStatsDtoByContactStatusType0 # noqa: PLC0415
        from ..models.contact_list_stats_dto_by_lifecycle_stage_type_0 import ContactListStatsDtoByLifecycleStageType0 # noqa: PLC0415
        from ..models.contact_list_stats_dto_by_tier_type_0 import ContactListStatsDtoByTierType0 # noqa: PLC0415
        total = self.total

        with_customer_profile = self.with_customer_profile

        by_tier: dict[str, Any] | None | Unset
        if isinstance(self.by_tier, Unset):
            by_tier = UNSET
        elif isinstance(self.by_tier, ContactListStatsDtoByTierType0):
            by_tier = self.by_tier.to_dict()
        else:
            by_tier = self.by_tier

        by_lifecycle_stage: dict[str, Any] | None | Unset
        if isinstance(self.by_lifecycle_stage, Unset):
            by_lifecycle_stage = UNSET
        elif isinstance(self.by_lifecycle_stage, ContactListStatsDtoByLifecycleStageType0):
            by_lifecycle_stage = self.by_lifecycle_stage.to_dict()
        else:
            by_lifecycle_stage = self.by_lifecycle_stage

        by_contact_status: dict[str, Any] | None | Unset
        if isinstance(self.by_contact_status, Unset):
            by_contact_status = UNSET
        elif isinstance(self.by_contact_status, ContactListStatsDtoByContactStatusType0):
            by_contact_status = self.by_contact_status.to_dict()
        else:
            by_contact_status = self.by_contact_status


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if total is not UNSET:
            field_dict["total"] = total
        if with_customer_profile is not UNSET:
            field_dict["withCustomerProfile"] = with_customer_profile
        if by_tier is not UNSET:
            field_dict["byTier"] = by_tier
        if by_lifecycle_stage is not UNSET:
            field_dict["byLifecycleStage"] = by_lifecycle_stage
        if by_contact_status is not UNSET:
            field_dict["byContactStatus"] = by_contact_status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_list_stats_dto_by_contact_status_type_0 import ContactListStatsDtoByContactStatusType0 # noqa: PLC0415
        from ..models.contact_list_stats_dto_by_lifecycle_stage_type_0 import ContactListStatsDtoByLifecycleStageType0 # noqa: PLC0415
        from ..models.contact_list_stats_dto_by_tier_type_0 import ContactListStatsDtoByTierType0 # noqa: PLC0415
        d = dict(src_dict)
        total = d.pop("total", UNSET)

        with_customer_profile = d.pop("withCustomerProfile", UNSET)

        def _parse_by_tier(data: object) -> ContactListStatsDtoByTierType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                by_tier_type_0 = ContactListStatsDtoByTierType0.from_dict(data)



                return by_tier_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ContactListStatsDtoByTierType0 | None | Unset, data)

        by_tier = _parse_by_tier(d.pop("byTier", UNSET))


        def _parse_by_lifecycle_stage(data: object) -> ContactListStatsDtoByLifecycleStageType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                by_lifecycle_stage_type_0 = ContactListStatsDtoByLifecycleStageType0.from_dict(data)



                return by_lifecycle_stage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ContactListStatsDtoByLifecycleStageType0 | None | Unset, data)

        by_lifecycle_stage = _parse_by_lifecycle_stage(d.pop("byLifecycleStage", UNSET))


        def _parse_by_contact_status(data: object) -> ContactListStatsDtoByContactStatusType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                by_contact_status_type_0 = ContactListStatsDtoByContactStatusType0.from_dict(data)



                return by_contact_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ContactListStatsDtoByContactStatusType0 | None | Unset, data)

        by_contact_status = _parse_by_contact_status(d.pop("byContactStatus", UNSET))


        contact_list_stats_dto = cls(
            total=total,
            with_customer_profile=with_customer_profile,
            by_tier=by_tier,
            by_lifecycle_stage=by_lifecycle_stage,
            by_contact_status=by_contact_status,
        )

        return contact_list_stats_dto


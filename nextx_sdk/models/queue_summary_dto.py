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






T = TypeVar("T", bound="QueueSummaryDto")



@_attrs_define
class QueueSummaryDto:
    

    id: UUID | Unset = UNSET
    name: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    strategy: None | str | Unset = UNSET
    max_wait_sec: int | Unset = UNSET
    ring_timeout_sec: int | Unset = UNSET
    overflow_action: None | str | Unset = UNSET
    service_level_threshold_sec: int | Unset = UNSET
    service_level_target: float | Unset = UNSET
    is_active: bool | Unset = UNSET
    agent_count: int | Unset = UNSET
    active_callers: int | Unset = UNSET
    in_use: bool | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        strategy: None | str | Unset
        if isinstance(self.strategy, Unset):
            strategy = UNSET
        else:
            strategy = self.strategy

        max_wait_sec = self.max_wait_sec

        ring_timeout_sec = self.ring_timeout_sec

        overflow_action: None | str | Unset
        if isinstance(self.overflow_action, Unset):
            overflow_action = UNSET
        else:
            overflow_action = self.overflow_action

        service_level_threshold_sec = self.service_level_threshold_sec

        service_level_target = self.service_level_target

        is_active = self.is_active

        agent_count = self.agent_count

        active_callers = self.active_callers

        in_use = self.in_use

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if strategy is not UNSET:
            field_dict["strategy"] = strategy
        if max_wait_sec is not UNSET:
            field_dict["maxWaitSec"] = max_wait_sec
        if ring_timeout_sec is not UNSET:
            field_dict["ringTimeoutSec"] = ring_timeout_sec
        if overflow_action is not UNSET:
            field_dict["overflowAction"] = overflow_action
        if service_level_threshold_sec is not UNSET:
            field_dict["serviceLevelThresholdSec"] = service_level_threshold_sec
        if service_level_target is not UNSET:
            field_dict["serviceLevelTarget"] = service_level_target
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if agent_count is not UNSET:
            field_dict["agentCount"] = agent_count
        if active_callers is not UNSET:
            field_dict["activeCallers"] = active_callers
        if in_use is not UNSET:
            field_dict["inUse"] = in_use
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




        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))


        def _parse_strategy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        strategy = _parse_strategy(d.pop("strategy", UNSET))


        max_wait_sec = d.pop("maxWaitSec", UNSET)

        ring_timeout_sec = d.pop("ringTimeoutSec", UNSET)

        def _parse_overflow_action(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        overflow_action = _parse_overflow_action(d.pop("overflowAction", UNSET))


        service_level_threshold_sec = d.pop("serviceLevelThresholdSec", UNSET)

        service_level_target = d.pop("serviceLevelTarget", UNSET)

        is_active = d.pop("isActive", UNSET)

        agent_count = d.pop("agentCount", UNSET)

        active_callers = d.pop("activeCallers", UNSET)

        in_use = d.pop("inUse", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        queue_summary_dto = cls(
            id=id,
            name=name,
            type_=type_,
            strategy=strategy,
            max_wait_sec=max_wait_sec,
            ring_timeout_sec=ring_timeout_sec,
            overflow_action=overflow_action,
            service_level_threshold_sec=service_level_threshold_sec,
            service_level_target=service_level_target,
            is_active=is_active,
            agent_count=agent_count,
            active_callers=active_callers,
            in_use=in_use,
            created_at=created_at,
        )

        return queue_summary_dto


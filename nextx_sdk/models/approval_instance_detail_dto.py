from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.approval_instance_dto import ApprovalInstanceDto
  from ..models.approval_task_dto import ApprovalTaskDto
  from ..models.approval_timeline_dto import ApprovalTimelineDto





T = TypeVar("T", bound="ApprovalInstanceDetailDto")



@_attrs_define
class ApprovalInstanceDetailDto:
    

    instance: ApprovalInstanceDto | Unset = UNSET
    tasks: list[ApprovalTaskDto] | None | Unset = UNSET
    timeline: list[ApprovalTimelineDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.approval_instance_dto import ApprovalInstanceDto # noqa: PLC0415
        from ..models.approval_task_dto import ApprovalTaskDto # noqa: PLC0415
        from ..models.approval_timeline_dto import ApprovalTimelineDto # noqa: PLC0415
        instance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.instance, Unset):
            instance = self.instance.to_dict()

        tasks: list[dict[str, Any]] | None | Unset
        if isinstance(self.tasks, Unset):
            tasks = UNSET
        elif isinstance(self.tasks, list):
            tasks = []
            for tasks_type_0_item_data in self.tasks:
                tasks_type_0_item = tasks_type_0_item_data.to_dict()
                tasks.append(tasks_type_0_item)


        else:
            tasks = self.tasks

        timeline: list[dict[str, Any]] | None | Unset
        if isinstance(self.timeline, Unset):
            timeline = UNSET
        elif isinstance(self.timeline, list):
            timeline = []
            for timeline_type_0_item_data in self.timeline:
                timeline_type_0_item = timeline_type_0_item_data.to_dict()
                timeline.append(timeline_type_0_item)


        else:
            timeline = self.timeline


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if instance is not UNSET:
            field_dict["instance"] = instance
        if tasks is not UNSET:
            field_dict["tasks"] = tasks
        if timeline is not UNSET:
            field_dict["timeline"] = timeline

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.approval_instance_dto import ApprovalInstanceDto # noqa: PLC0415
        from ..models.approval_task_dto import ApprovalTaskDto # noqa: PLC0415
        from ..models.approval_timeline_dto import ApprovalTimelineDto # noqa: PLC0415
        d = dict(src_dict)
        _instance = d.pop("instance", UNSET)
        instance: ApprovalInstanceDto | Unset
        if isinstance(_instance,  Unset):
            instance = UNSET
        else:
            instance = ApprovalInstanceDto.from_dict(_instance)




        def _parse_tasks(data: object) -> list[ApprovalTaskDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tasks_type_0 = []
                _tasks_type_0 = data
                for tasks_type_0_item_data in (_tasks_type_0):
                    tasks_type_0_item = ApprovalTaskDto.from_dict(tasks_type_0_item_data)



                    tasks_type_0.append(tasks_type_0_item)

                return tasks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ApprovalTaskDto] | None | Unset, data)

        tasks = _parse_tasks(d.pop("tasks", UNSET))


        def _parse_timeline(data: object) -> list[ApprovalTimelineDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                timeline_type_0 = []
                _timeline_type_0 = data
                for timeline_type_0_item_data in (_timeline_type_0):
                    timeline_type_0_item = ApprovalTimelineDto.from_dict(timeline_type_0_item_data)



                    timeline_type_0.append(timeline_type_0_item)

                return timeline_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ApprovalTimelineDto] | None | Unset, data)

        timeline = _parse_timeline(d.pop("timeline", UNSET))


        approval_instance_detail_dto = cls(
            instance=instance,
            tasks=tasks,
            timeline=timeline,
        )

        return approval_instance_detail_dto


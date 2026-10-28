from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="PipelineStageDistributionDto")



@_attrs_define
class PipelineStageDistributionDto:
    

    stage_id: UUID | Unset = UNSET
    stage_name: None | str | Unset = UNSET
    stage_color: None | str | Unset = UNSET
    count: int | Unset = UNSET
    total_value: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        stage_id: str | Unset = UNSET
        if not isinstance(self.stage_id, Unset):
            stage_id = str(self.stage_id)

        stage_name: None | str | Unset
        if isinstance(self.stage_name, Unset):
            stage_name = UNSET
        else:
            stage_name = self.stage_name

        stage_color: None | str | Unset
        if isinstance(self.stage_color, Unset):
            stage_color = UNSET
        else:
            stage_color = self.stage_color

        count = self.count

        total_value = self.total_value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if stage_id is not UNSET:
            field_dict["stageId"] = stage_id
        if stage_name is not UNSET:
            field_dict["stageName"] = stage_name
        if stage_color is not UNSET:
            field_dict["stageColor"] = stage_color
        if count is not UNSET:
            field_dict["count"] = count
        if total_value is not UNSET:
            field_dict["totalValue"] = total_value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _stage_id = d.pop("stageId", UNSET)
        stage_id: UUID | Unset
        if isinstance(_stage_id,  Unset):
            stage_id = UNSET
        else:
            stage_id = UUID(_stage_id)




        def _parse_stage_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stage_name = _parse_stage_name(d.pop("stageName", UNSET))


        def _parse_stage_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stage_color = _parse_stage_color(d.pop("stageColor", UNSET))


        count = d.pop("count", UNSET)

        total_value = d.pop("totalValue", UNSET)

        pipeline_stage_distribution_dto = cls(
            stage_id=stage_id,
            stage_name=stage_name,
            stage_color=stage_color,
            count=count,
            total_value=total_value,
        )

        return pipeline_stage_distribution_dto


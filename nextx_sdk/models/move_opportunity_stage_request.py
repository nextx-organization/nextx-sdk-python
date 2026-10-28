from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="MoveOpportunityStageRequest")



@_attrs_define
class MoveOpportunityStageRequest:
    

    pipeline_stage_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        pipeline_stage_id: str | Unset = UNSET
        if not isinstance(self.pipeline_stage_id, Unset):
            pipeline_stage_id = str(self.pipeline_stage_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if pipeline_stage_id is not UNSET:
            field_dict["pipelineStageId"] = pipeline_stage_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _pipeline_stage_id = d.pop("pipelineStageId", UNSET)
        pipeline_stage_id: UUID | Unset
        if isinstance(_pipeline_stage_id,  Unset):
            pipeline_stage_id = UNSET
        else:
            pipeline_stage_id = UUID(_pipeline_stage_id)




        move_opportunity_stage_request = cls(
            pipeline_stage_id=pipeline_stage_id,
        )

        return move_opportunity_stage_request


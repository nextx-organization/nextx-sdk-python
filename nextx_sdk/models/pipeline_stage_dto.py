from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="PipelineStageDto")



@_attrs_define
class PipelineStageDto:
    

    id: UUID | Unset = UNSET
    name: None | str | Unset = UNSET
    order_index: int | Unset = UNSET
    conversion_rate: float | None | Unset = UNSET
    color: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        order_index = self.order_index

        conversion_rate: float | None | Unset
        if isinstance(self.conversion_rate, Unset):
            conversion_rate = UNSET
        else:
            conversion_rate = self.conversion_rate

        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if order_index is not UNSET:
            field_dict["orderIndex"] = order_index
        if conversion_rate is not UNSET:
            field_dict["conversionRate"] = conversion_rate
        if color is not UNSET:
            field_dict["color"] = color

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


        order_index = d.pop("orderIndex", UNSET)

        def _parse_conversion_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        conversion_rate = _parse_conversion_rate(d.pop("conversionRate", UNSET))


        def _parse_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color = _parse_color(d.pop("color", UNSET))


        pipeline_stage_dto = cls(
            id=id,
            name=name,
            order_index=order_index,
            conversion_rate=conversion_rate,
            color=color,
        )

        return pipeline_stage_dto


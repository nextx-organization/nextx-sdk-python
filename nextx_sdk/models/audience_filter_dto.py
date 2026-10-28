from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.filter_condition_dto import FilterConditionDto





T = TypeVar("T", bound="AudienceFilterDto")



@_attrs_define
class AudienceFilterDto:
    

    logic: None | str | Unset = UNSET
    conditions: list[FilterConditionDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.filter_condition_dto import FilterConditionDto # noqa: PLC0415
        logic: None | str | Unset
        if isinstance(self.logic, Unset):
            logic = UNSET
        else:
            logic = self.logic

        conditions: list[dict[str, Any]] | None | Unset
        if isinstance(self.conditions, Unset):
            conditions = UNSET
        elif isinstance(self.conditions, list):
            conditions = []
            for conditions_type_0_item_data in self.conditions:
                conditions_type_0_item = conditions_type_0_item_data.to_dict()
                conditions.append(conditions_type_0_item)


        else:
            conditions = self.conditions


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if logic is not UNSET:
            field_dict["logic"] = logic
        if conditions is not UNSET:
            field_dict["conditions"] = conditions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_condition_dto import FilterConditionDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_logic(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logic = _parse_logic(d.pop("logic", UNSET))


        def _parse_conditions(data: object) -> list[FilterConditionDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                conditions_type_0 = []
                _conditions_type_0 = data
                for conditions_type_0_item_data in (_conditions_type_0):
                    conditions_type_0_item = FilterConditionDto.from_dict(conditions_type_0_item_data)



                    conditions_type_0.append(conditions_type_0_item)

                return conditions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FilterConditionDto] | None | Unset, data)

        conditions = _parse_conditions(d.pop("conditions", UNSET))


        audience_filter_dto = cls(
            logic=logic,
            conditions=conditions,
        )

        return audience_filter_dto


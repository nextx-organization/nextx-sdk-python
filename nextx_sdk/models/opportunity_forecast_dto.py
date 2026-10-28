from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OpportunityForecastDto")



@_attrs_define
class OpportunityForecastDto:
    

    weighted_value: float | Unset = UNSET
    open_count: int | Unset = UNSET
    total_open_estimated_value: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        weighted_value = self.weighted_value

        open_count = self.open_count

        total_open_estimated_value = self.total_open_estimated_value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if weighted_value is not UNSET:
            field_dict["weightedValue"] = weighted_value
        if open_count is not UNSET:
            field_dict["openCount"] = open_count
        if total_open_estimated_value is not UNSET:
            field_dict["totalOpenEstimatedValue"] = total_open_estimated_value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        weighted_value = d.pop("weightedValue", UNSET)

        open_count = d.pop("openCount", UNSET)

        total_open_estimated_value = d.pop("totalOpenEstimatedValue", UNSET)

        opportunity_forecast_dto = cls(
            weighted_value=weighted_value,
            open_count=open_count,
            total_open_estimated_value=total_open_estimated_value,
        )

        return opportunity_forecast_dto


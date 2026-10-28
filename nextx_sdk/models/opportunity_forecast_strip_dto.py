from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OpportunityForecastStripDto")



@_attrs_define
class OpportunityForecastStripDto:
    

    total_count: int | Unset = UNSET
    open_count: int | Unset = UNSET
    overdue_count: int | Unset = UNSET
    total_estimated_value: float | Unset = UNSET
    weighted_value: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        open_count = self.open_count

        overdue_count = self.overdue_count

        total_estimated_value = self.total_estimated_value

        weighted_value = self.weighted_value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count
        if open_count is not UNSET:
            field_dict["openCount"] = open_count
        if overdue_count is not UNSET:
            field_dict["overdueCount"] = overdue_count
        if total_estimated_value is not UNSET:
            field_dict["totalEstimatedValue"] = total_estimated_value
        if weighted_value is not UNSET:
            field_dict["weightedValue"] = weighted_value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_count = d.pop("totalCount", UNSET)

        open_count = d.pop("openCount", UNSET)

        overdue_count = d.pop("overdueCount", UNSET)

        total_estimated_value = d.pop("totalEstimatedValue", UNSET)

        weighted_value = d.pop("weightedValue", UNSET)

        opportunity_forecast_strip_dto = cls(
            total_count=total_count,
            open_count=open_count,
            overdue_count=overdue_count,
            total_estimated_value=total_estimated_value,
            weighted_value=weighted_value,
        )

        return opportunity_forecast_strip_dto


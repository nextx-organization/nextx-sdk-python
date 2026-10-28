from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.my_week_day_dto import MyWeekDayDto





T = TypeVar("T", bound="MyWeekScheduleDto")



@_attrs_define
class MyWeekScheduleDto:
    

    days: list[MyWeekDayDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.my_week_day_dto import MyWeekDayDto # noqa: PLC0415
        days: list[dict[str, Any]] | None | Unset
        if isinstance(self.days, Unset):
            days = UNSET
        elif isinstance(self.days, list):
            days = []
            for days_type_0_item_data in self.days:
                days_type_0_item = days_type_0_item_data.to_dict()
                days.append(days_type_0_item)


        else:
            days = self.days


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if days is not UNSET:
            field_dict["days"] = days

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.my_week_day_dto import MyWeekDayDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_days(data: object) -> list[MyWeekDayDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                days_type_0 = []
                _days_type_0 = data
                for days_type_0_item_data in (_days_type_0):
                    days_type_0_item = MyWeekDayDto.from_dict(days_type_0_item_data)



                    days_type_0.append(days_type_0_item)

                return days_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MyWeekDayDto] | None | Unset, data)

        days = _parse_days(d.pop("days", UNSET))


        my_week_schedule_dto = cls(
            days=days,
        )

        return my_week_schedule_dto


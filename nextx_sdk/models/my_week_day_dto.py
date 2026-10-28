from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.my_week_route_dto import MyWeekRouteDto





T = TypeVar("T", bound="MyWeekDayDto")



@_attrs_define
class MyWeekDayDto:
    

    day_of_week: int | Unset = UNSET
    routes: list[MyWeekRouteDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.my_week_route_dto import MyWeekRouteDto # noqa: PLC0415
        day_of_week = self.day_of_week

        routes: list[dict[str, Any]] | None | Unset
        if isinstance(self.routes, Unset):
            routes = UNSET
        elif isinstance(self.routes, list):
            routes = []
            for routes_type_0_item_data in self.routes:
                routes_type_0_item = routes_type_0_item_data.to_dict()
                routes.append(routes_type_0_item)


        else:
            routes = self.routes


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if day_of_week is not UNSET:
            field_dict["dayOfWeek"] = day_of_week
        if routes is not UNSET:
            field_dict["routes"] = routes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.my_week_route_dto import MyWeekRouteDto # noqa: PLC0415
        d = dict(src_dict)
        day_of_week = d.pop("dayOfWeek", UNSET)

        def _parse_routes(data: object) -> list[MyWeekRouteDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                routes_type_0 = []
                _routes_type_0 = data
                for routes_type_0_item_data in (_routes_type_0):
                    routes_type_0_item = MyWeekRouteDto.from_dict(routes_type_0_item_data)



                    routes_type_0.append(routes_type_0_item)

                return routes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MyWeekRouteDto] | None | Unset, data)

        routes = _parse_routes(d.pop("routes", UNSET))


        my_week_day_dto = cls(
            day_of_week=day_of_week,
            routes=routes,
        )

        return my_week_day_dto


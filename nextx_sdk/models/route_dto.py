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






T = TypeVar("T", bound="RouteDto")



@_attrs_define
class RouteDto:
    

    id: UUID | Unset = UNSET
    route_code: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    channel_code: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    zone_id: None | Unset | UUID = UNSET
    branch_id: UUID | Unset = UNSET
    day_of_week: list[int] | None | Unset = UNSET
    visit_frequency: None | str | Unset = UNSET
    vehicle_type: None | str | Unset = UNSET
    color_hex: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    stop_count: int | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    assigned_count: int | Unset = UNSET
    start_date: datetime.date | None | Unset = UNSET
    today_visit_count: int | Unset = UNSET
    today_completed_count: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        route_code: None | str | Unset
        if isinstance(self.route_code, Unset):
            route_code = UNSET
        else:
            route_code = self.route_code

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        channel_code: None | str | Unset
        if isinstance(self.channel_code, Unset):
            channel_code = UNSET
        else:
            channel_code = self.channel_code

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        zone_id: None | str | Unset
        if isinstance(self.zone_id, Unset):
            zone_id = UNSET
        elif isinstance(self.zone_id, UUID):
            zone_id = str(self.zone_id)
        else:
            zone_id = self.zone_id

        branch_id: str | Unset = UNSET
        if not isinstance(self.branch_id, Unset):
            branch_id = str(self.branch_id)

        day_of_week: list[int] | None | Unset
        if isinstance(self.day_of_week, Unset):
            day_of_week = UNSET
        elif isinstance(self.day_of_week, list):
            day_of_week = self.day_of_week


        else:
            day_of_week = self.day_of_week

        visit_frequency: None | str | Unset
        if isinstance(self.visit_frequency, Unset):
            visit_frequency = UNSET
        else:
            visit_frequency = self.visit_frequency

        vehicle_type: None | str | Unset
        if isinstance(self.vehicle_type, Unset):
            vehicle_type = UNSET
        else:
            vehicle_type = self.vehicle_type

        color_hex: None | str | Unset
        if isinstance(self.color_hex, Unset):
            color_hex = UNSET
        else:
            color_hex = self.color_hex

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        stop_count = self.stop_count

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        assigned_count = self.assigned_count

        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.date):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        today_visit_count = self.today_visit_count

        today_completed_count = self.today_completed_count


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if route_code is not UNSET:
            field_dict["routeCode"] = route_code
        if name is not UNSET:
            field_dict["name"] = name
        if channel_code is not UNSET:
            field_dict["channelCode"] = channel_code
        if status is not UNSET:
            field_dict["status"] = status
        if zone_id is not UNSET:
            field_dict["zoneId"] = zone_id
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id
        if day_of_week is not UNSET:
            field_dict["dayOfWeek"] = day_of_week
        if visit_frequency is not UNSET:
            field_dict["visitFrequency"] = visit_frequency
        if vehicle_type is not UNSET:
            field_dict["vehicleType"] = vehicle_type
        if color_hex is not UNSET:
            field_dict["colorHex"] = color_hex
        if description is not UNSET:
            field_dict["description"] = description
        if stop_count is not UNSET:
            field_dict["stopCount"] = stop_count
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if assigned_count is not UNSET:
            field_dict["assignedCount"] = assigned_count
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if today_visit_count is not UNSET:
            field_dict["todayVisitCount"] = today_visit_count
        if today_completed_count is not UNSET:
            field_dict["todayCompletedCount"] = today_completed_count

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




        def _parse_route_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        route_code = _parse_route_code(d.pop("routeCode", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_channel_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel_code = _parse_channel_code(d.pop("channelCode", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_zone_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                zone_id_type_0 = UUID(data)



                return zone_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        zone_id = _parse_zone_id(d.pop("zoneId", UNSET))


        _branch_id = d.pop("branchId", UNSET)
        branch_id: UUID | Unset
        if isinstance(_branch_id,  Unset):
            branch_id = UNSET
        else:
            branch_id = UUID(_branch_id)




        def _parse_day_of_week(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                day_of_week_type_0 = cast(list[int], data)

                return day_of_week_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        day_of_week = _parse_day_of_week(d.pop("dayOfWeek", UNSET))


        def _parse_visit_frequency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        visit_frequency = _parse_visit_frequency(d.pop("visitFrequency", UNSET))


        def _parse_vehicle_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vehicle_type = _parse_vehicle_type(d.pop("vehicleType", UNSET))


        def _parse_color_hex(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color_hex = _parse_color_hex(d.pop("colorHex", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        stop_count = d.pop("stopCount", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        assigned_count = d.pop("assignedCount", UNSET)

        def _parse_start_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = datetime.date.fromisoformat(data)



                return start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        start_date = _parse_start_date(d.pop("startDate", UNSET))


        today_visit_count = d.pop("todayVisitCount", UNSET)

        today_completed_count = d.pop("todayCompletedCount", UNSET)

        route_dto = cls(
            id=id,
            route_code=route_code,
            name=name,
            channel_code=channel_code,
            status=status,
            zone_id=zone_id,
            branch_id=branch_id,
            day_of_week=day_of_week,
            visit_frequency=visit_frequency,
            vehicle_type=vehicle_type,
            color_hex=color_hex,
            description=description,
            stop_count=stop_count,
            created_at=created_at,
            assigned_count=assigned_count,
            start_date=start_date,
            today_visit_count=today_visit_count,
            today_completed_count=today_completed_count,
        )

        return route_dto


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

if TYPE_CHECKING:
  from ..models.dms_my_day_stop_dto import DmsMyDayStopDto
  from ..models.route_summary import RouteSummary





T = TypeVar("T", bound="DmsMyDayPlanDto")



@_attrs_define
class DmsMyDayPlanDto:
    

    id: UUID | Unset = UNSET
    employee_id: UUID | Unset = UNSET
    plan_date: datetime.date | Unset = UNSET
    status: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    routes: list[RouteSummary] | None | Unset = UNSET
    total_stops: int | Unset = UNSET
    completed_stops: int | Unset = UNSET
    skipped_stops: int | Unset = UNSET
    stops: list[DmsMyDayStopDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.dms_my_day_stop_dto import DmsMyDayStopDto # noqa: PLC0415
        from ..models.route_summary import RouteSummary # noqa: PLC0415
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        employee_id: str | Unset = UNSET
        if not isinstance(self.employee_id, Unset):
            employee_id = str(self.employee_id)

        plan_date: str | Unset = UNSET
        if not isinstance(self.plan_date, Unset):
            plan_date = self.plan_date.isoformat()

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

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

        total_stops = self.total_stops

        completed_stops = self.completed_stops

        skipped_stops = self.skipped_stops

        stops: list[dict[str, Any]] | None | Unset
        if isinstance(self.stops, Unset):
            stops = UNSET
        elif isinstance(self.stops, list):
            stops = []
            for stops_type_0_item_data in self.stops:
                stops_type_0_item = stops_type_0_item_data.to_dict()
                stops.append(stops_type_0_item)


        else:
            stops = self.stops


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if employee_id is not UNSET:
            field_dict["employeeId"] = employee_id
        if plan_date is not UNSET:
            field_dict["planDate"] = plan_date
        if status is not UNSET:
            field_dict["status"] = status
        if notes is not UNSET:
            field_dict["notes"] = notes
        if routes is not UNSET:
            field_dict["routes"] = routes
        if total_stops is not UNSET:
            field_dict["totalStops"] = total_stops
        if completed_stops is not UNSET:
            field_dict["completedStops"] = completed_stops
        if skipped_stops is not UNSET:
            field_dict["skippedStops"] = skipped_stops
        if stops is not UNSET:
            field_dict["stops"] = stops

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dms_my_day_stop_dto import DmsMyDayStopDto # noqa: PLC0415
        from ..models.route_summary import RouteSummary # noqa: PLC0415
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        _employee_id = d.pop("employeeId", UNSET)
        employee_id: UUID | Unset
        if isinstance(_employee_id,  Unset):
            employee_id = UNSET
        else:
            employee_id = UUID(_employee_id)




        _plan_date = d.pop("planDate", UNSET)
        plan_date: datetime.date | Unset
        if isinstance(_plan_date,  Unset):
            plan_date = UNSET
        else:
            plan_date = datetime.date.fromisoformat(_plan_date)




        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


        def _parse_routes(data: object) -> list[RouteSummary] | None | Unset:
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
                    routes_type_0_item = RouteSummary.from_dict(routes_type_0_item_data)



                    routes_type_0.append(routes_type_0_item)

                return routes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RouteSummary] | None | Unset, data)

        routes = _parse_routes(d.pop("routes", UNSET))


        total_stops = d.pop("totalStops", UNSET)

        completed_stops = d.pop("completedStops", UNSET)

        skipped_stops = d.pop("skippedStops", UNSET)

        def _parse_stops(data: object) -> list[DmsMyDayStopDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                stops_type_0 = []
                _stops_type_0 = data
                for stops_type_0_item_data in (_stops_type_0):
                    stops_type_0_item = DmsMyDayStopDto.from_dict(stops_type_0_item_data)



                    stops_type_0.append(stops_type_0_item)

                return stops_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DmsMyDayStopDto] | None | Unset, data)

        stops = _parse_stops(d.pop("stops", UNSET))


        dms_my_day_plan_dto = cls(
            id=id,
            employee_id=employee_id,
            plan_date=plan_date,
            status=status,
            notes=notes,
            routes=routes,
            total_stops=total_stops,
            completed_stops=completed_stops,
            skipped_stops=skipped_stops,
            stops=stops,
        )

        return dms_my_day_plan_dto


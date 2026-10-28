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
  from ..models.route_summary import RouteSummary





T = TypeVar("T", bound="DailyPlanDto")



@_attrs_define
class DailyPlanDto:
    

    id: UUID | Unset = UNSET
    employee_id: UUID | Unset = UNSET
    employee_name: None | str | Unset = UNSET
    plan_date: datetime.date | Unset = UNSET
    routes: list[RouteSummary] | None | Unset = UNSET
    status: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    total_stops: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.route_summary import RouteSummary # noqa: PLC0415
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        employee_id: str | Unset = UNSET
        if not isinstance(self.employee_id, Unset):
            employee_id = str(self.employee_id)

        employee_name: None | str | Unset
        if isinstance(self.employee_name, Unset):
            employee_name = UNSET
        else:
            employee_name = self.employee_name

        plan_date: str | Unset = UNSET
        if not isinstance(self.plan_date, Unset):
            plan_date = self.plan_date.isoformat()

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

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        total_stops = self.total_stops


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if employee_id is not UNSET:
            field_dict["employeeId"] = employee_id
        if employee_name is not UNSET:
            field_dict["employeeName"] = employee_name
        if plan_date is not UNSET:
            field_dict["planDate"] = plan_date
        if routes is not UNSET:
            field_dict["routes"] = routes
        if status is not UNSET:
            field_dict["status"] = status
        if notes is not UNSET:
            field_dict["notes"] = notes
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if total_stops is not UNSET:
            field_dict["totalStops"] = total_stops

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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




        def _parse_employee_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        employee_name = _parse_employee_name(d.pop("employeeName", UNSET))


        _plan_date = d.pop("planDate", UNSET)
        plan_date: datetime.date | Unset
        if isinstance(_plan_date,  Unset):
            plan_date = UNSET
        else:
            plan_date = datetime.date.fromisoformat(_plan_date)




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


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        total_stops = d.pop("totalStops", UNSET)

        daily_plan_dto = cls(
            id=id,
            employee_id=employee_id,
            employee_name=employee_name,
            plan_date=plan_date,
            routes=routes,
            status=status,
            notes=notes,
            created_at=created_at,
            total_stops=total_stops,
        )

        return daily_plan_dto


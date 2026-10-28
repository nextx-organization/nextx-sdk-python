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






T = TypeVar("T", bound="DailyPlanSuggestionDto")



@_attrs_define
class DailyPlanSuggestionDto:
    

    id: UUID | Unset = UNSET
    suggested_date: datetime.date | Unset = UNSET
    outlet_id: UUID | Unset = UNSET
    employee_id: None | Unset | UUID = UNSET
    visit_frequency: None | str | Unset = UNSET
    days_since_last_visit: int | Unset = UNSET
    priority: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        suggested_date: str | Unset = UNSET
        if not isinstance(self.suggested_date, Unset):
            suggested_date = self.suggested_date.isoformat()

        outlet_id: str | Unset = UNSET
        if not isinstance(self.outlet_id, Unset):
            outlet_id = str(self.outlet_id)

        employee_id: None | str | Unset
        if isinstance(self.employee_id, Unset):
            employee_id = UNSET
        elif isinstance(self.employee_id, UUID):
            employee_id = str(self.employee_id)
        else:
            employee_id = self.employee_id

        visit_frequency: None | str | Unset
        if isinstance(self.visit_frequency, Unset):
            visit_frequency = UNSET
        else:
            visit_frequency = self.visit_frequency

        days_since_last_visit = self.days_since_last_visit

        priority: None | str | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if suggested_date is not UNSET:
            field_dict["suggestedDate"] = suggested_date
        if outlet_id is not UNSET:
            field_dict["outletId"] = outlet_id
        if employee_id is not UNSET:
            field_dict["employeeId"] = employee_id
        if visit_frequency is not UNSET:
            field_dict["visitFrequency"] = visit_frequency
        if days_since_last_visit is not UNSET:
            field_dict["daysSinceLastVisit"] = days_since_last_visit
        if priority is not UNSET:
            field_dict["priority"] = priority
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

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




        _suggested_date = d.pop("suggestedDate", UNSET)
        suggested_date: datetime.date | Unset
        if isinstance(_suggested_date,  Unset):
            suggested_date = UNSET
        else:
            suggested_date = datetime.date.fromisoformat(_suggested_date)




        _outlet_id = d.pop("outletId", UNSET)
        outlet_id: UUID | Unset
        if isinstance(_outlet_id,  Unset):
            outlet_id = UNSET
        else:
            outlet_id = UUID(_outlet_id)




        def _parse_employee_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                employee_id_type_0 = UUID(data)



                return employee_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        employee_id = _parse_employee_id(d.pop("employeeId", UNSET))


        def _parse_visit_frequency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        visit_frequency = _parse_visit_frequency(d.pop("visitFrequency", UNSET))


        days_since_last_visit = d.pop("daysSinceLastVisit", UNSET)

        def _parse_priority(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        daily_plan_suggestion_dto = cls(
            id=id,
            suggested_date=suggested_date,
            outlet_id=outlet_id,
            employee_id=employee_id,
            visit_frequency=visit_frequency,
            days_since_last_visit=days_since_last_visit,
            priority=priority,
            status=status,
            created_at=created_at,
        )

        return daily_plan_suggestion_dto


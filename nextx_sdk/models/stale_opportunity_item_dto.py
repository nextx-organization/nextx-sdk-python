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






T = TypeVar("T", bound="StaleOpportunityItemDto")



@_attrs_define
class StaleOpportunityItemDto:
    

    id: UUID | Unset = UNSET
    code: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    estimated_value: float | None | Unset = UNSET
    expected_close_date: datetime.date | Unset = UNSET
    days_overdue: int | Unset = UNSET
    assignee_id: UUID | Unset = UNSET
    last_updated_at: datetime.datetime | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        estimated_value: float | None | Unset
        if isinstance(self.estimated_value, Unset):
            estimated_value = UNSET
        else:
            estimated_value = self.estimated_value

        expected_close_date: str | Unset = UNSET
        if not isinstance(self.expected_close_date, Unset):
            expected_close_date = self.expected_close_date.isoformat()

        days_overdue = self.days_overdue

        assignee_id: str | Unset = UNSET
        if not isinstance(self.assignee_id, Unset):
            assignee_id = str(self.assignee_id)

        last_updated_at: None | str | Unset
        if isinstance(self.last_updated_at, Unset):
            last_updated_at = UNSET
        elif isinstance(self.last_updated_at, datetime.datetime):
            last_updated_at = self.last_updated_at.isoformat()
        else:
            last_updated_at = self.last_updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name
        if estimated_value is not UNSET:
            field_dict["estimatedValue"] = estimated_value
        if expected_close_date is not UNSET:
            field_dict["expectedCloseDate"] = expected_close_date
        if days_overdue is not UNSET:
            field_dict["daysOverdue"] = days_overdue
        if assignee_id is not UNSET:
            field_dict["assigneeId"] = assignee_id
        if last_updated_at is not UNSET:
            field_dict["lastUpdatedAt"] = last_updated_at

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




        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_estimated_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        estimated_value = _parse_estimated_value(d.pop("estimatedValue", UNSET))


        _expected_close_date = d.pop("expectedCloseDate", UNSET)
        expected_close_date: datetime.date | Unset
        if isinstance(_expected_close_date,  Unset):
            expected_close_date = UNSET
        else:
            expected_close_date = datetime.date.fromisoformat(_expected_close_date)




        days_overdue = d.pop("daysOverdue", UNSET)

        _assignee_id = d.pop("assigneeId", UNSET)
        assignee_id: UUID | Unset
        if isinstance(_assignee_id,  Unset):
            assignee_id = UNSET
        else:
            assignee_id = UUID(_assignee_id)




        def _parse_last_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_updated_at_type_0 = datetime.datetime.fromisoformat(data)



                return last_updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_updated_at = _parse_last_updated_at(d.pop("lastUpdatedAt", UNSET))


        stale_opportunity_item_dto = cls(
            id=id,
            code=code,
            name=name,
            estimated_value=estimated_value,
            expected_close_date=expected_close_date,
            days_overdue=days_overdue,
            assignee_id=assignee_id,
            last_updated_at=last_updated_at,
        )

        return stale_opportunity_item_dto


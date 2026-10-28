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






T = TypeVar("T", bound="DailyClockRow")



@_attrs_define
class DailyClockRow:
    

    employee_id: UUID | Unset = UNSET
    employee_code: None | str | Unset = UNSET
    employee_name: None | str | Unset = UNSET
    date: datetime.date | Unset = UNSET
    first_in: datetime.datetime | None | Unset = UNSET
    last_out: datetime.datetime | None | Unset = UNSET
    scan_count: int | Unset = UNSET
    manual_entry_count: int | Unset = UNSET
    sources: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        employee_id: str | Unset = UNSET
        if not isinstance(self.employee_id, Unset):
            employee_id = str(self.employee_id)

        employee_code: None | str | Unset
        if isinstance(self.employee_code, Unset):
            employee_code = UNSET
        else:
            employee_code = self.employee_code

        employee_name: None | str | Unset
        if isinstance(self.employee_name, Unset):
            employee_name = UNSET
        else:
            employee_name = self.employee_name

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        first_in: None | str | Unset
        if isinstance(self.first_in, Unset):
            first_in = UNSET
        elif isinstance(self.first_in, datetime.datetime):
            first_in = self.first_in.isoformat()
        else:
            first_in = self.first_in

        last_out: None | str | Unset
        if isinstance(self.last_out, Unset):
            last_out = UNSET
        elif isinstance(self.last_out, datetime.datetime):
            last_out = self.last_out.isoformat()
        else:
            last_out = self.last_out

        scan_count = self.scan_count

        manual_entry_count = self.manual_entry_count

        sources: None | str | Unset
        if isinstance(self.sources, Unset):
            sources = UNSET
        else:
            sources = self.sources


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if employee_id is not UNSET:
            field_dict["employeeId"] = employee_id
        if employee_code is not UNSET:
            field_dict["employeeCode"] = employee_code
        if employee_name is not UNSET:
            field_dict["employeeName"] = employee_name
        if date is not UNSET:
            field_dict["date"] = date
        if first_in is not UNSET:
            field_dict["firstIn"] = first_in
        if last_out is not UNSET:
            field_dict["lastOut"] = last_out
        if scan_count is not UNSET:
            field_dict["scanCount"] = scan_count
        if manual_entry_count is not UNSET:
            field_dict["manualEntryCount"] = manual_entry_count
        if sources is not UNSET:
            field_dict["sources"] = sources

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _employee_id = d.pop("employeeId", UNSET)
        employee_id: UUID | Unset
        if isinstance(_employee_id,  Unset):
            employee_id = UNSET
        else:
            employee_id = UUID(_employee_id)




        def _parse_employee_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        employee_code = _parse_employee_code(d.pop("employeeCode", UNSET))


        def _parse_employee_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        employee_name = _parse_employee_name(d.pop("employeeName", UNSET))


        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date,  Unset):
            date = UNSET
        else:
            date = datetime.date.fromisoformat(_date)




        def _parse_first_in(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_in_type_0 = datetime.datetime.fromisoformat(data)



                return first_in_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        first_in = _parse_first_in(d.pop("firstIn", UNSET))


        def _parse_last_out(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_out_type_0 = datetime.datetime.fromisoformat(data)



                return last_out_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_out = _parse_last_out(d.pop("lastOut", UNSET))


        scan_count = d.pop("scanCount", UNSET)

        manual_entry_count = d.pop("manualEntryCount", UNSET)

        def _parse_sources(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sources = _parse_sources(d.pop("sources", UNSET))


        daily_clock_row = cls(
            employee_id=employee_id,
            employee_code=employee_code,
            employee_name=employee_name,
            date=date,
            first_in=first_in,
            last_out=last_out,
            scan_count=scan_count,
            manual_entry_count=manual_entry_count,
            sources=sources,
        )

        return daily_clock_row


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ReportByDayDto")



@_attrs_define
class ReportByDayDto:
    

    date: None | str | Unset = UNSET
    sent: int | Unset = UNSET
    opens: int | Unset = UNSET
    clicks: int | Unset = UNSET
    conversions: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        else:
            date = self.date

        sent = self.sent

        opens = self.opens

        clicks = self.clicks

        conversions = self.conversions


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if date is not UNSET:
            field_dict["date"] = date
        if sent is not UNSET:
            field_dict["sent"] = sent
        if opens is not UNSET:
            field_dict["opens"] = opens
        if clicks is not UNSET:
            field_dict["clicks"] = clicks
        if conversions is not UNSET:
            field_dict["conversions"] = conversions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date = _parse_date(d.pop("date", UNSET))


        sent = d.pop("sent", UNSET)

        opens = d.pop("opens", UNSET)

        clicks = d.pop("clicks", UNSET)

        conversions = d.pop("conversions", UNSET)

        report_by_day_dto = cls(
            date=date,
            sent=sent,
            opens=opens,
            clicks=clicks,
            conversions=conversions,
        )

        return report_by_day_dto


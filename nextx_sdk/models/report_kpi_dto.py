from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ReportKpiDto")



@_attrs_define
class ReportKpiDto:
    

    total_sent: int | Unset = UNSET
    delivered_rate: float | Unset = UNSET
    open_rate: float | Unset = UNSET
    click_rate: float | Unset = UNSET
    conversion_rate: float | Unset = UNSET
    revenue: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        total_sent = self.total_sent

        delivered_rate = self.delivered_rate

        open_rate = self.open_rate

        click_rate = self.click_rate

        conversion_rate = self.conversion_rate

        revenue = self.revenue


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if total_sent is not UNSET:
            field_dict["totalSent"] = total_sent
        if delivered_rate is not UNSET:
            field_dict["deliveredRate"] = delivered_rate
        if open_rate is not UNSET:
            field_dict["openRate"] = open_rate
        if click_rate is not UNSET:
            field_dict["clickRate"] = click_rate
        if conversion_rate is not UNSET:
            field_dict["conversionRate"] = conversion_rate
        if revenue is not UNSET:
            field_dict["revenue"] = revenue

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_sent = d.pop("totalSent", UNSET)

        delivered_rate = d.pop("deliveredRate", UNSET)

        open_rate = d.pop("openRate", UNSET)

        click_rate = d.pop("clickRate", UNSET)

        conversion_rate = d.pop("conversionRate", UNSET)

        revenue = d.pop("revenue", UNSET)

        report_kpi_dto = cls(
            total_sent=total_sent,
            delivered_rate=delivered_rate,
            open_rate=open_rate,
            click_rate=click_rate,
            conversion_rate=conversion_rate,
            revenue=revenue,
        )

        return report_kpi_dto


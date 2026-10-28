from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.report_by_channel_dto import ReportByChannelDto
  from ..models.report_by_day_dto import ReportByDayDto
  from ..models.report_kpi_dto import ReportKpiDto
  from ..models.report_period_dto import ReportPeriodDto





T = TypeVar("T", bound="ReportOverviewDto")



@_attrs_define
class ReportOverviewDto:
    

    period: ReportPeriodDto | Unset = UNSET
    kpis: ReportKpiDto | Unset = UNSET
    by_day: list[ReportByDayDto] | None | Unset = UNSET
    by_channel: list[ReportByChannelDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.report_by_channel_dto import ReportByChannelDto # noqa: PLC0415
        from ..models.report_by_day_dto import ReportByDayDto # noqa: PLC0415
        from ..models.report_kpi_dto import ReportKpiDto # noqa: PLC0415
        from ..models.report_period_dto import ReportPeriodDto # noqa: PLC0415
        period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.to_dict()

        kpis: dict[str, Any] | Unset = UNSET
        if not isinstance(self.kpis, Unset):
            kpis = self.kpis.to_dict()

        by_day: list[dict[str, Any]] | None | Unset
        if isinstance(self.by_day, Unset):
            by_day = UNSET
        elif isinstance(self.by_day, list):
            by_day = []
            for by_day_type_0_item_data in self.by_day:
                by_day_type_0_item = by_day_type_0_item_data.to_dict()
                by_day.append(by_day_type_0_item)


        else:
            by_day = self.by_day

        by_channel: list[dict[str, Any]] | None | Unset
        if isinstance(self.by_channel, Unset):
            by_channel = UNSET
        elif isinstance(self.by_channel, list):
            by_channel = []
            for by_channel_type_0_item_data in self.by_channel:
                by_channel_type_0_item = by_channel_type_0_item_data.to_dict()
                by_channel.append(by_channel_type_0_item)


        else:
            by_channel = self.by_channel


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if period is not UNSET:
            field_dict["period"] = period
        if kpis is not UNSET:
            field_dict["kpis"] = kpis
        if by_day is not UNSET:
            field_dict["byDay"] = by_day
        if by_channel is not UNSET:
            field_dict["byChannel"] = by_channel

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.report_by_channel_dto import ReportByChannelDto # noqa: PLC0415
        from ..models.report_by_day_dto import ReportByDayDto # noqa: PLC0415
        from ..models.report_kpi_dto import ReportKpiDto # noqa: PLC0415
        from ..models.report_period_dto import ReportPeriodDto # noqa: PLC0415
        d = dict(src_dict)
        _period = d.pop("period", UNSET)
        period: ReportPeriodDto | Unset
        if isinstance(_period,  Unset):
            period = UNSET
        else:
            period = ReportPeriodDto.from_dict(_period)




        _kpis = d.pop("kpis", UNSET)
        kpis: ReportKpiDto | Unset
        if isinstance(_kpis,  Unset):
            kpis = UNSET
        else:
            kpis = ReportKpiDto.from_dict(_kpis)




        def _parse_by_day(data: object) -> list[ReportByDayDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                by_day_type_0 = []
                _by_day_type_0 = data
                for by_day_type_0_item_data in (_by_day_type_0):
                    by_day_type_0_item = ReportByDayDto.from_dict(by_day_type_0_item_data)



                    by_day_type_0.append(by_day_type_0_item)

                return by_day_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ReportByDayDto] | None | Unset, data)

        by_day = _parse_by_day(d.pop("byDay", UNSET))


        def _parse_by_channel(data: object) -> list[ReportByChannelDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                by_channel_type_0 = []
                _by_channel_type_0 = data
                for by_channel_type_0_item_data in (_by_channel_type_0):
                    by_channel_type_0_item = ReportByChannelDto.from_dict(by_channel_type_0_item_data)



                    by_channel_type_0.append(by_channel_type_0_item)

                return by_channel_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ReportByChannelDto] | None | Unset, data)

        by_channel = _parse_by_channel(d.pop("byChannel", UNSET))


        report_overview_dto = cls(
            period=period,
            kpis=kpis,
            by_day=by_day,
            by_channel=by_channel,
        )

        return report_overview_dto


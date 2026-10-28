from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ReportByChannelDto")



@_attrs_define
class ReportByChannelDto:
    

    channel: None | str | Unset = UNSET
    sent: int | Unset = UNSET
    open_rate: float | Unset = UNSET
    click_rate: float | Unset = UNSET
    conversion_rate: float | Unset = UNSET
    delivered: int | Unset = UNSET
    failed: int | Unset = UNSET
    revenue: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        channel: None | str | Unset
        if isinstance(self.channel, Unset):
            channel = UNSET
        else:
            channel = self.channel

        sent = self.sent

        open_rate = self.open_rate

        click_rate = self.click_rate

        conversion_rate = self.conversion_rate

        delivered = self.delivered

        failed = self.failed

        revenue = self.revenue


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if channel is not UNSET:
            field_dict["channel"] = channel
        if sent is not UNSET:
            field_dict["sent"] = sent
        if open_rate is not UNSET:
            field_dict["openRate"] = open_rate
        if click_rate is not UNSET:
            field_dict["clickRate"] = click_rate
        if conversion_rate is not UNSET:
            field_dict["conversionRate"] = conversion_rate
        if delivered is not UNSET:
            field_dict["delivered"] = delivered
        if failed is not UNSET:
            field_dict["failed"] = failed
        if revenue is not UNSET:
            field_dict["revenue"] = revenue

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_channel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel = _parse_channel(d.pop("channel", UNSET))


        sent = d.pop("sent", UNSET)

        open_rate = d.pop("openRate", UNSET)

        click_rate = d.pop("clickRate", UNSET)

        conversion_rate = d.pop("conversionRate", UNSET)

        delivered = d.pop("delivered", UNSET)

        failed = d.pop("failed", UNSET)

        revenue = d.pop("revenue", UNSET)

        report_by_channel_dto = cls(
            channel=channel,
            sent=sent,
            open_rate=open_rate,
            click_rate=click_rate,
            conversion_rate=conversion_rate,
            delivered=delivered,
            failed=failed,
            revenue=revenue,
        )

        return report_by_channel_dto


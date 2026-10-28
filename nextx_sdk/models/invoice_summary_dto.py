from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.source_breakdown_dto import SourceBreakdownDto





T = TypeVar("T", bound="InvoiceSummaryDto")



@_attrs_define
class InvoiceSummaryDto:
    

    total_all: int | Unset = UNSET
    total_issued: int | Unset = UNSET
    total_pending: int | Unset = UNSET
    total_draft: int | Unset = UNSET
    total_error: int | Unset = UNSET
    total_cancelled: int | Unset = UNSET
    total_amount: float | Unset = UNSET
    total_tax_amount: float | Unset = UNSET
    by_source: list[SourceBreakdownDto] | None | Unset = UNSET
    period_from: datetime.date | None | Unset = UNSET
    period_to: datetime.date | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.source_breakdown_dto import SourceBreakdownDto # noqa: PLC0415
        total_all = self.total_all

        total_issued = self.total_issued

        total_pending = self.total_pending

        total_draft = self.total_draft

        total_error = self.total_error

        total_cancelled = self.total_cancelled

        total_amount = self.total_amount

        total_tax_amount = self.total_tax_amount

        by_source: list[dict[str, Any]] | None | Unset
        if isinstance(self.by_source, Unset):
            by_source = UNSET
        elif isinstance(self.by_source, list):
            by_source = []
            for by_source_type_0_item_data in self.by_source:
                by_source_type_0_item = by_source_type_0_item_data.to_dict()
                by_source.append(by_source_type_0_item)


        else:
            by_source = self.by_source

        period_from: None | str | Unset
        if isinstance(self.period_from, Unset):
            period_from = UNSET
        elif isinstance(self.period_from, datetime.date):
            period_from = self.period_from.isoformat()
        else:
            period_from = self.period_from

        period_to: None | str | Unset
        if isinstance(self.period_to, Unset):
            period_to = UNSET
        elif isinstance(self.period_to, datetime.date):
            period_to = self.period_to.isoformat()
        else:
            period_to = self.period_to


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if total_all is not UNSET:
            field_dict["totalAll"] = total_all
        if total_issued is not UNSET:
            field_dict["totalIssued"] = total_issued
        if total_pending is not UNSET:
            field_dict["totalPending"] = total_pending
        if total_draft is not UNSET:
            field_dict["totalDraft"] = total_draft
        if total_error is not UNSET:
            field_dict["totalError"] = total_error
        if total_cancelled is not UNSET:
            field_dict["totalCancelled"] = total_cancelled
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if total_tax_amount is not UNSET:
            field_dict["totalTaxAmount"] = total_tax_amount
        if by_source is not UNSET:
            field_dict["bySource"] = by_source
        if period_from is not UNSET:
            field_dict["periodFrom"] = period_from
        if period_to is not UNSET:
            field_dict["periodTo"] = period_to

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.source_breakdown_dto import SourceBreakdownDto # noqa: PLC0415
        d = dict(src_dict)
        total_all = d.pop("totalAll", UNSET)

        total_issued = d.pop("totalIssued", UNSET)

        total_pending = d.pop("totalPending", UNSET)

        total_draft = d.pop("totalDraft", UNSET)

        total_error = d.pop("totalError", UNSET)

        total_cancelled = d.pop("totalCancelled", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        total_tax_amount = d.pop("totalTaxAmount", UNSET)

        def _parse_by_source(data: object) -> list[SourceBreakdownDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                by_source_type_0 = []
                _by_source_type_0 = data
                for by_source_type_0_item_data in (_by_source_type_0):
                    by_source_type_0_item = SourceBreakdownDto.from_dict(by_source_type_0_item_data)



                    by_source_type_0.append(by_source_type_0_item)

                return by_source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SourceBreakdownDto] | None | Unset, data)

        by_source = _parse_by_source(d.pop("bySource", UNSET))


        def _parse_period_from(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                period_from_type_0 = datetime.date.fromisoformat(data)



                return period_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        period_from = _parse_period_from(d.pop("periodFrom", UNSET))


        def _parse_period_to(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                period_to_type_0 = datetime.date.fromisoformat(data)



                return period_to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        period_to = _parse_period_to(d.pop("periodTo", UNSET))


        invoice_summary_dto = cls(
            total_all=total_all,
            total_issued=total_issued,
            total_pending=total_pending,
            total_draft=total_draft,
            total_error=total_error,
            total_cancelled=total_cancelled,
            total_amount=total_amount,
            total_tax_amount=total_tax_amount,
            by_source=by_source,
            period_from=period_from,
            period_to=period_to,
        )

        return invoice_summary_dto


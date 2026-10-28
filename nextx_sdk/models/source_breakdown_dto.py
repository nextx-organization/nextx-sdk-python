from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SourceBreakdownDto")



@_attrs_define
class SourceBreakdownDto:
    

    source: None | str | Unset = UNSET
    count: int | Unset = UNSET
    amount: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        count = self.count

        amount = self.amount


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if source is not UNSET:
            field_dict["source"] = source
        if count is not UNSET:
            field_dict["count"] = count
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))


        count = d.pop("count", UNSET)

        amount = d.pop("amount", UNSET)

        source_breakdown_dto = cls(
            source=source,
            count=count,
            amount=amount,
        )

        return source_breakdown_dto


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ReferenceTypeBreakdownDto")



@_attrs_define
class ReferenceTypeBreakdownDto:
    

    reference_type: None | str | Unset = UNSET
    count: int | Unset = UNSET
    total_amount: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        reference_type: None | str | Unset
        if isinstance(self.reference_type, Unset):
            reference_type = UNSET
        else:
            reference_type = self.reference_type

        count = self.count

        total_amount = self.total_amount


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if reference_type is not UNSET:
            field_dict["referenceType"] = reference_type
        if count is not UNSET:
            field_dict["count"] = count
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_reference_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reference_type = _parse_reference_type(d.pop("referenceType", UNSET))


        count = d.pop("count", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        reference_type_breakdown_dto = cls(
            reference_type=reference_type,
            count=count,
            total_amount=total_amount,
        )

        return reference_type_breakdown_dto


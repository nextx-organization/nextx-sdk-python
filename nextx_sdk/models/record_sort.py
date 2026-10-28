from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="RecordSort")



@_attrs_define
class RecordSort:
    

    field_id: None | str | Unset = UNSET
    descending: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        field_id: None | str | Unset
        if isinstance(self.field_id, Unset):
            field_id = UNSET
        else:
            field_id = self.field_id

        descending = self.descending


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if field_id is not UNSET:
            field_dict["fieldId"] = field_id
        if descending is not UNSET:
            field_dict["descending"] = descending

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_field_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_id = _parse_field_id(d.pop("fieldId", UNSET))


        descending = d.pop("descending", UNSET)

        record_sort = cls(
            field_id=field_id,
            descending=descending,
        )

        return record_sort


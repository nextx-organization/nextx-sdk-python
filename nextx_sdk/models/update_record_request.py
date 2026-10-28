from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdateRecordRequest")



@_attrs_define
class UpdateRecordRequest:
    

    data: Any | Unset = UNSET
    replace: bool | Unset = UNSET
    expected_values: Any | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        data = self.data

        replace = self.replace

        expected_values = self.expected_values


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if data is not UNSET:
            field_dict["data"] = data
        if replace is not UNSET:
            field_dict["replace"] = replace
        if expected_values is not UNSET:
            field_dict["expectedValues"] = expected_values

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data = d.pop("data", UNSET)

        replace = d.pop("replace", UNSET)

        expected_values = d.pop("expectedValues", UNSET)

        update_record_request = cls(
            data=data,
            replace=replace,
            expected_values=expected_values,
        )

        return update_record_request


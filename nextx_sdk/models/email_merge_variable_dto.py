from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="EmailMergeVariableDto")



@_attrs_define
class EmailMergeVariableDto:
    

    token: None | str | Unset = UNSET
    key: None | str | Unset = UNSET
    label: None | str | Unset = UNSET
    example: None | str | Unset = UNSET
    is_alias: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        token: None | str | Unset
        if isinstance(self.token, Unset):
            token = UNSET
        else:
            token = self.token

        key: None | str | Unset
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        example: None | str | Unset
        if isinstance(self.example, Unset):
            example = UNSET
        else:
            example = self.example

        is_alias = self.is_alias


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if token is not UNSET:
            field_dict["token"] = token
        if key is not UNSET:
            field_dict["key"] = key
        if label is not UNSET:
            field_dict["label"] = label
        if example is not UNSET:
            field_dict["example"] = example
        if is_alias is not UNSET:
            field_dict["isAlias"] = is_alias

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        token = _parse_token(d.pop("token", UNSET))


        def _parse_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key = _parse_key(d.pop("key", UNSET))


        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))


        def _parse_example(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        example = _parse_example(d.pop("example", UNSET))


        is_alias = d.pop("isAlias", UNSET)

        email_merge_variable_dto = cls(
            token=token,
            key=key,
            label=label,
            example=example,
            is_alias=is_alias,
        )

        return email_merge_variable_dto


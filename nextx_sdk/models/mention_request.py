from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MentionRequest")



@_attrs_define
class MentionRequest:
    

    uid: None | str | Unset = UNSET
    offset: int | Unset = UNSET
    length: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        uid: None | str | Unset
        if isinstance(self.uid, Unset):
            uid = UNSET
        else:
            uid = self.uid

        offset = self.offset

        length = self.length


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if uid is not UNSET:
            field_dict["uid"] = uid
        if offset is not UNSET:
            field_dict["offset"] = offset
        if length is not UNSET:
            field_dict["length"] = length

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_uid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        uid = _parse_uid(d.pop("uid", UNSET))


        offset = d.pop("offset", UNSET)

        length = d.pop("length", UNSET)

        mention_request = cls(
            uid=uid,
            offset=offset,
            length=length,
        )

        return mention_request


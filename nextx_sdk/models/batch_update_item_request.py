from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="BatchUpdateItemRequest")



@_attrs_define
class BatchUpdateItemRequest:
    

    id: UUID | Unset = UNSET
    data: Any | Unset = UNSET
    replace: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        data = self.data

        replace = self.replace


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if data is not UNSET:
            field_dict["data"] = data
        if replace is not UNSET:
            field_dict["replace"] = replace

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        data = d.pop("data", UNSET)

        replace = d.pop("replace", UNSET)

        batch_update_item_request = cls(
            id=id,
            data=data,
            replace=replace,
        )

        return batch_update_item_request


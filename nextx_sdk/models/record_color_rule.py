from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.record_filter import RecordFilter





T = TypeVar("T", bound="RecordColorRule")



@_attrs_define
class RecordColorRule:
    

    color: None | str | Unset = UNSET
    filter_: RecordFilter | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.record_filter import RecordFilter # noqa: PLC0415
        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if color is not UNSET:
            field_dict["color"] = color
        if filter_ is not UNSET:
            field_dict["filter"] = filter_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.record_filter import RecordFilter # noqa: PLC0415
        d = dict(src_dict)
        def _parse_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color = _parse_color(d.pop("color", UNSET))


        _filter_ = d.pop("filter", UNSET)
        filter_: RecordFilter | Unset
        if isinstance(_filter_,  Unset):
            filter_ = UNSET
        else:
            filter_ = RecordFilter.from_dict(_filter_)




        record_color_rule = cls(
            color=color,
            filter_=filter_,
        )

        return record_color_rule


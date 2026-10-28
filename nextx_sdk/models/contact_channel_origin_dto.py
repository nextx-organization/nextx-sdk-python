from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ContactChannelOriginDto")



@_attrs_define
class ContactChannelOriginDto:
    

    channel_type: None | str | Unset = UNSET
    channel_account_name: None | str | Unset = UNSET
    other_account_count: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        channel_type: None | str | Unset
        if isinstance(self.channel_type, Unset):
            channel_type = UNSET
        else:
            channel_type = self.channel_type

        channel_account_name: None | str | Unset
        if isinstance(self.channel_account_name, Unset):
            channel_account_name = UNSET
        else:
            channel_account_name = self.channel_account_name

        other_account_count = self.other_account_count


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if channel_type is not UNSET:
            field_dict["channelType"] = channel_type
        if channel_account_name is not UNSET:
            field_dict["channelAccountName"] = channel_account_name
        if other_account_count is not UNSET:
            field_dict["otherAccountCount"] = other_account_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_channel_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel_type = _parse_channel_type(d.pop("channelType", UNSET))


        def _parse_channel_account_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel_account_name = _parse_channel_account_name(d.pop("channelAccountName", UNSET))


        other_account_count = d.pop("otherAccountCount", UNSET)

        contact_channel_origin_dto = cls(
            channel_type=channel_type,
            channel_account_name=channel_account_name,
            other_account_count=other_account_count,
        )

        return contact_channel_origin_dto


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="PartnerRecordingLinkDto")



@_attrs_define
class PartnerRecordingLinkDto:
    

    call_id: UUID | Unset = UNSET
    url: None | str | Unset = UNSET
    expires_at: datetime.datetime | Unset = UNSET
    content_type: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        call_id: str | Unset = UNSET
        if not isinstance(self.call_id, Unset):
            call_id = str(self.call_id)

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        content_type: None | str | Unset
        if isinstance(self.content_type, Unset):
            content_type = UNSET
        else:
            content_type = self.content_type


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if call_id is not UNSET:
            field_dict["callId"] = call_id
        if url is not UNSET:
            field_dict["url"] = url
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if content_type is not UNSET:
            field_dict["contentType"] = content_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _call_id = d.pop("callId", UNSET)
        call_id: UUID | Unset
        if isinstance(_call_id,  Unset):
            call_id = UNSET
        else:
            call_id = UUID(_call_id)




        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))


        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at,  Unset):
            expires_at = UNSET
        else:
            expires_at = datetime.datetime.fromisoformat(_expires_at)




        def _parse_content_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_type = _parse_content_type(d.pop("contentType", UNSET))


        partner_recording_link_dto = cls(
            call_id=call_id,
            url=url,
            expires_at=expires_at,
            content_type=content_type,
        )

        return partner_recording_link_dto


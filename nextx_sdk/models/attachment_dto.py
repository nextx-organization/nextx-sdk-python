from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="AttachmentDto")



@_attrs_define
class AttachmentDto:
    

    id: UUID | Unset = UNSET
    file_name: None | str | Unset = UNSET
    file_size_bytes: int | Unset = UNSET
    mime_type: None | str | Unset = UNSET
    storage_key: None | str | Unset = UNSET
    download_url: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        file_size_bytes = self.file_size_bytes

        mime_type: None | str | Unset
        if isinstance(self.mime_type, Unset):
            mime_type = UNSET
        else:
            mime_type = self.mime_type

        storage_key: None | str | Unset
        if isinstance(self.storage_key, Unset):
            storage_key = UNSET
        else:
            storage_key = self.storage_key

        download_url: None | str | Unset
        if isinstance(self.download_url, Unset):
            download_url = UNSET
        else:
            download_url = self.download_url


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if file_size_bytes is not UNSET:
            field_dict["fileSizeBytes"] = file_size_bytes
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if storage_key is not UNSET:
            field_dict["storageKey"] = storage_key
        if download_url is not UNSET:
            field_dict["downloadUrl"] = download_url

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




        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("fileName", UNSET))


        file_size_bytes = d.pop("fileSizeBytes", UNSET)

        def _parse_mime_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mime_type = _parse_mime_type(d.pop("mimeType", UNSET))


        def _parse_storage_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_key = _parse_storage_key(d.pop("storageKey", UNSET))


        def _parse_download_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        download_url = _parse_download_url(d.pop("downloadUrl", UNSET))


        attachment_dto = cls(
            id=id,
            file_name=file_name,
            file_size_bytes=file_size_bytes,
            mime_type=mime_type,
            storage_key=storage_key,
            download_url=download_url,
        )

        return attachment_dto


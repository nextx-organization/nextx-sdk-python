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






T = TypeVar("T", bound="EmailTemplateListDto")



@_attrs_define
class EmailTemplateListDto:
    

    id: UUID | Unset = UNSET
    name: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    is_system: bool | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    editor_mode: None | str | Unset = UNSET
    used_in_campaigns: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        is_system = self.is_system

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        editor_mode: None | str | Unset
        if isinstance(self.editor_mode, Unset):
            editor_mode = UNSET
        else:
            editor_mode = self.editor_mode

        used_in_campaigns = self.used_in_campaigns


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if category is not UNSET:
            field_dict["category"] = category
        if is_system is not UNSET:
            field_dict["isSystem"] = is_system
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if editor_mode is not UNSET:
            field_dict["editorMode"] = editor_mode
        if used_in_campaigns is not UNSET:
            field_dict["usedInCampaigns"] = used_in_campaigns

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




        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))


        is_system = d.pop("isSystem", UNSET)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)




        def _parse_editor_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        editor_mode = _parse_editor_mode(d.pop("editorMode", UNSET))


        used_in_campaigns = d.pop("usedInCampaigns", UNSET)

        email_template_list_dto = cls(
            id=id,
            name=name,
            category=category,
            is_system=is_system,
            updated_at=updated_at,
            editor_mode=editor_mode,
            used_in_campaigns=used_in_campaigns,
        )

        return email_template_list_dto


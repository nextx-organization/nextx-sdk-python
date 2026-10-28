from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PtMemberServiceLineDto")



@_attrs_define
class PtMemberServiceLineDto:
    

    service_code: None | str | Unset = UNSET
    session_count: int | None | Unset = UNSET
    sessions_used: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        service_code: None | str | Unset
        if isinstance(self.service_code, Unset):
            service_code = UNSET
        else:
            service_code = self.service_code

        session_count: int | None | Unset
        if isinstance(self.session_count, Unset):
            session_count = UNSET
        else:
            session_count = self.session_count

        sessions_used = self.sessions_used


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if service_code is not UNSET:
            field_dict["serviceCode"] = service_code
        if session_count is not UNSET:
            field_dict["sessionCount"] = session_count
        if sessions_used is not UNSET:
            field_dict["sessionsUsed"] = sessions_used

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_service_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_code = _parse_service_code(d.pop("serviceCode", UNSET))


        def _parse_session_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        session_count = _parse_session_count(d.pop("sessionCount", UNSET))


        sessions_used = d.pop("sessionsUsed", UNSET)

        pt_member_service_line_dto = cls(
            service_code=service_code,
            session_count=session_count,
            sessions_used=sessions_used,
        )

        return pt_member_service_line_dto


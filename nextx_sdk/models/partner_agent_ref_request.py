from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="PartnerAgentRefRequest")



@_attrs_define
class PartnerAgentRefRequest:
    

    agent_id: None | Unset | UUID = UNSET
    agent_email: None | str | Unset = UNSET
    extension: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        agent_id: None | str | Unset
        if isinstance(self.agent_id, Unset):
            agent_id = UNSET
        elif isinstance(self.agent_id, UUID):
            agent_id = str(self.agent_id)
        else:
            agent_id = self.agent_id

        agent_email: None | str | Unset
        if isinstance(self.agent_email, Unset):
            agent_email = UNSET
        else:
            agent_email = self.agent_email

        extension: None | str | Unset
        if isinstance(self.extension, Unset):
            extension = UNSET
        else:
            extension = self.extension


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if agent_id is not UNSET:
            field_dict["agentId"] = agent_id
        if agent_email is not UNSET:
            field_dict["agentEmail"] = agent_email
        if extension is not UNSET:
            field_dict["extension"] = extension

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_agent_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                agent_id_type_0 = UUID(data)



                return agent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        agent_id = _parse_agent_id(d.pop("agentId", UNSET))


        def _parse_agent_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        agent_email = _parse_agent_email(d.pop("agentEmail", UNSET))


        def _parse_extension(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        extension = _parse_extension(d.pop("extension", UNSET))


        partner_agent_ref_request = cls(
            agent_id=agent_id,
            agent_email=agent_email,
            extension=extension,
        )

        return partner_agent_ref_request


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.partner_originate_request_metadata_type_0 import PartnerOriginateRequestMetadataType0





T = TypeVar("T", bound="PartnerOriginateRequest")



@_attrs_define
class PartnerOriginateRequest:
    

    agent_id: None | Unset | UUID = UNSET
    agent_email: None | str | Unset = UNSET
    extension: None | str | Unset = UNSET
    to: None | str | Unset = UNSET
    caller_id: None | str | Unset = UNSET
    contact_ref: None | str | Unset = UNSET
    metadata: None | PartnerOriginateRequestMetadataType0 | Unset = UNSET
    crm_contact_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.partner_originate_request_metadata_type_0 import PartnerOriginateRequestMetadataType0 # noqa: PLC0415
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

        to: None | str | Unset
        if isinstance(self.to, Unset):
            to = UNSET
        else:
            to = self.to

        caller_id: None | str | Unset
        if isinstance(self.caller_id, Unset):
            caller_id = UNSET
        else:
            caller_id = self.caller_id

        contact_ref: None | str | Unset
        if isinstance(self.contact_ref, Unset):
            contact_ref = UNSET
        else:
            contact_ref = self.contact_ref

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, PartnerOriginateRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        crm_contact_id: None | str | Unset
        if isinstance(self.crm_contact_id, Unset):
            crm_contact_id = UNSET
        elif isinstance(self.crm_contact_id, UUID):
            crm_contact_id = str(self.crm_contact_id)
        else:
            crm_contact_id = self.crm_contact_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if agent_id is not UNSET:
            field_dict["agentId"] = agent_id
        if agent_email is not UNSET:
            field_dict["agentEmail"] = agent_email
        if extension is not UNSET:
            field_dict["extension"] = extension
        if to is not UNSET:
            field_dict["to"] = to
        if caller_id is not UNSET:
            field_dict["callerId"] = caller_id
        if contact_ref is not UNSET:
            field_dict["contactRef"] = contact_ref
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if crm_contact_id is not UNSET:
            field_dict["crmContactId"] = crm_contact_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.partner_originate_request_metadata_type_0 import PartnerOriginateRequestMetadataType0 # noqa: PLC0415
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


        def _parse_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        to = _parse_to(d.pop("to", UNSET))


        def _parse_caller_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        caller_id = _parse_caller_id(d.pop("callerId", UNSET))


        def _parse_contact_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_ref = _parse_contact_ref(d.pop("contactRef", UNSET))


        def _parse_metadata(data: object) -> None | PartnerOriginateRequestMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = PartnerOriginateRequestMetadataType0.from_dict(data)



                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PartnerOriginateRequestMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))


        def _parse_crm_contact_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                crm_contact_id_type_0 = UUID(data)



                return crm_contact_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        crm_contact_id = _parse_crm_contact_id(d.pop("crmContactId", UNSET))


        partner_originate_request = cls(
            agent_id=agent_id,
            agent_email=agent_email,
            extension=extension,
            to=to,
            caller_id=caller_id,
            contact_ref=contact_ref,
            metadata=metadata,
            crm_contact_id=crm_contact_id,
        )

        return partner_originate_request


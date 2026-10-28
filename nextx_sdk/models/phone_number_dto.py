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






T = TypeVar("T", bound="PhoneNumberDto")



@_attrs_define
class PhoneNumberDto:
    

    id: UUID | Unset = UNSET
    inbound_sip_trunk_id: None | Unset | UUID = UNSET
    outbound_sip_trunk_id: None | Unset | UUID = UNSET
    did_number: None | str | Unset = UNSET
    direction: None | str | Unset = UNSET
    routing_target_type: None | str | Unset = UNSET
    routing_target_id: None | Unset | UUID = UNSET
    routing_target_name: None | str | Unset = UNSET
    is_active: bool | Unset = UNSET
    inbound_sip_trunk_name: None | str | Unset = UNSET
    outbound_sip_trunk_name: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    is_default_outbound_cid: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        inbound_sip_trunk_id: None | str | Unset
        if isinstance(self.inbound_sip_trunk_id, Unset):
            inbound_sip_trunk_id = UNSET
        elif isinstance(self.inbound_sip_trunk_id, UUID):
            inbound_sip_trunk_id = str(self.inbound_sip_trunk_id)
        else:
            inbound_sip_trunk_id = self.inbound_sip_trunk_id

        outbound_sip_trunk_id: None | str | Unset
        if isinstance(self.outbound_sip_trunk_id, Unset):
            outbound_sip_trunk_id = UNSET
        elif isinstance(self.outbound_sip_trunk_id, UUID):
            outbound_sip_trunk_id = str(self.outbound_sip_trunk_id)
        else:
            outbound_sip_trunk_id = self.outbound_sip_trunk_id

        did_number: None | str | Unset
        if isinstance(self.did_number, Unset):
            did_number = UNSET
        else:
            did_number = self.did_number

        direction: None | str | Unset
        if isinstance(self.direction, Unset):
            direction = UNSET
        else:
            direction = self.direction

        routing_target_type: None | str | Unset
        if isinstance(self.routing_target_type, Unset):
            routing_target_type = UNSET
        else:
            routing_target_type = self.routing_target_type

        routing_target_id: None | str | Unset
        if isinstance(self.routing_target_id, Unset):
            routing_target_id = UNSET
        elif isinstance(self.routing_target_id, UUID):
            routing_target_id = str(self.routing_target_id)
        else:
            routing_target_id = self.routing_target_id

        routing_target_name: None | str | Unset
        if isinstance(self.routing_target_name, Unset):
            routing_target_name = UNSET
        else:
            routing_target_name = self.routing_target_name

        is_active = self.is_active

        inbound_sip_trunk_name: None | str | Unset
        if isinstance(self.inbound_sip_trunk_name, Unset):
            inbound_sip_trunk_name = UNSET
        else:
            inbound_sip_trunk_name = self.inbound_sip_trunk_name

        outbound_sip_trunk_name: None | str | Unset
        if isinstance(self.outbound_sip_trunk_name, Unset):
            outbound_sip_trunk_name = UNSET
        else:
            outbound_sip_trunk_name = self.outbound_sip_trunk_name

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        is_default_outbound_cid = self.is_default_outbound_cid


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if inbound_sip_trunk_id is not UNSET:
            field_dict["inboundSipTrunkId"] = inbound_sip_trunk_id
        if outbound_sip_trunk_id is not UNSET:
            field_dict["outboundSipTrunkId"] = outbound_sip_trunk_id
        if did_number is not UNSET:
            field_dict["didNumber"] = did_number
        if direction is not UNSET:
            field_dict["direction"] = direction
        if routing_target_type is not UNSET:
            field_dict["routingTargetType"] = routing_target_type
        if routing_target_id is not UNSET:
            field_dict["routingTargetId"] = routing_target_id
        if routing_target_name is not UNSET:
            field_dict["routingTargetName"] = routing_target_name
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if inbound_sip_trunk_name is not UNSET:
            field_dict["inboundSipTrunkName"] = inbound_sip_trunk_name
        if outbound_sip_trunk_name is not UNSET:
            field_dict["outboundSipTrunkName"] = outbound_sip_trunk_name
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if is_default_outbound_cid is not UNSET:
            field_dict["isDefaultOutboundCid"] = is_default_outbound_cid

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




        def _parse_inbound_sip_trunk_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                inbound_sip_trunk_id_type_0 = UUID(data)



                return inbound_sip_trunk_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        inbound_sip_trunk_id = _parse_inbound_sip_trunk_id(d.pop("inboundSipTrunkId", UNSET))


        def _parse_outbound_sip_trunk_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                outbound_sip_trunk_id_type_0 = UUID(data)



                return outbound_sip_trunk_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        outbound_sip_trunk_id = _parse_outbound_sip_trunk_id(d.pop("outboundSipTrunkId", UNSET))


        def _parse_did_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        did_number = _parse_did_number(d.pop("didNumber", UNSET))


        def _parse_direction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        direction = _parse_direction(d.pop("direction", UNSET))


        def _parse_routing_target_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        routing_target_type = _parse_routing_target_type(d.pop("routingTargetType", UNSET))


        def _parse_routing_target_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                routing_target_id_type_0 = UUID(data)



                return routing_target_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        routing_target_id = _parse_routing_target_id(d.pop("routingTargetId", UNSET))


        def _parse_routing_target_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        routing_target_name = _parse_routing_target_name(d.pop("routingTargetName", UNSET))


        is_active = d.pop("isActive", UNSET)

        def _parse_inbound_sip_trunk_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        inbound_sip_trunk_name = _parse_inbound_sip_trunk_name(d.pop("inboundSipTrunkName", UNSET))


        def _parse_outbound_sip_trunk_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        outbound_sip_trunk_name = _parse_outbound_sip_trunk_name(d.pop("outboundSipTrunkName", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        is_default_outbound_cid = d.pop("isDefaultOutboundCid", UNSET)

        phone_number_dto = cls(
            id=id,
            inbound_sip_trunk_id=inbound_sip_trunk_id,
            outbound_sip_trunk_id=outbound_sip_trunk_id,
            did_number=did_number,
            direction=direction,
            routing_target_type=routing_target_type,
            routing_target_id=routing_target_id,
            routing_target_name=routing_target_name,
            is_active=is_active,
            inbound_sip_trunk_name=inbound_sip_trunk_name,
            outbound_sip_trunk_name=outbound_sip_trunk_name,
            created_at=created_at,
            is_default_outbound_cid=is_default_outbound_cid,
        )

        return phone_number_dto


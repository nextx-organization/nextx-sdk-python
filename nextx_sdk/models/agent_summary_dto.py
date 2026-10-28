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






T = TypeVar("T", bound="AgentSummaryDto")



@_attrs_define
class AgentSummaryDto:
    

    id: UUID | Unset = UNSET
    user_id: UUID | Unset = UNSET
    display_name: None | str | Unset = UNSET
    avatar: None | str | Unset = UNSET
    extension: None | str | Unset = UNSET
    sip_username: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    device_type: None | str | Unset = UNSET
    skill_group: None | str | Unset = UNSET
    level: int | Unset = UNSET
    is_active: bool | Unset = UNSET
    queue_ids: list[UUID] | None | Unset = UNSET
    queue_names: list[str] | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    outbound_phone_number_id: None | Unset | UUID = UNSET
    outbound_phone_number_did_number: None | str | Unset = UNSET
    agent_code: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        avatar: None | str | Unset
        if isinstance(self.avatar, Unset):
            avatar = UNSET
        else:
            avatar = self.avatar

        extension: None | str | Unset
        if isinstance(self.extension, Unset):
            extension = UNSET
        else:
            extension = self.extension

        sip_username: None | str | Unset
        if isinstance(self.sip_username, Unset):
            sip_username = UNSET
        else:
            sip_username = self.sip_username

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        device_type: None | str | Unset
        if isinstance(self.device_type, Unset):
            device_type = UNSET
        else:
            device_type = self.device_type

        skill_group: None | str | Unset
        if isinstance(self.skill_group, Unset):
            skill_group = UNSET
        else:
            skill_group = self.skill_group

        level = self.level

        is_active = self.is_active

        queue_ids: list[str] | None | Unset
        if isinstance(self.queue_ids, Unset):
            queue_ids = UNSET
        elif isinstance(self.queue_ids, list):
            queue_ids = []
            for queue_ids_type_0_item_data in self.queue_ids:
                queue_ids_type_0_item = str(queue_ids_type_0_item_data)
                queue_ids.append(queue_ids_type_0_item)


        else:
            queue_ids = self.queue_ids

        queue_names: list[str] | None | Unset
        if isinstance(self.queue_names, Unset):
            queue_names = UNSET
        elif isinstance(self.queue_names, list):
            queue_names = self.queue_names


        else:
            queue_names = self.queue_names

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        outbound_phone_number_id: None | str | Unset
        if isinstance(self.outbound_phone_number_id, Unset):
            outbound_phone_number_id = UNSET
        elif isinstance(self.outbound_phone_number_id, UUID):
            outbound_phone_number_id = str(self.outbound_phone_number_id)
        else:
            outbound_phone_number_id = self.outbound_phone_number_id

        outbound_phone_number_did_number: None | str | Unset
        if isinstance(self.outbound_phone_number_did_number, Unset):
            outbound_phone_number_did_number = UNSET
        else:
            outbound_phone_number_did_number = self.outbound_phone_number_did_number

        agent_code: None | str | Unset
        if isinstance(self.agent_code, Unset):
            agent_code = UNSET
        else:
            agent_code = self.agent_code


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if extension is not UNSET:
            field_dict["extension"] = extension
        if sip_username is not UNSET:
            field_dict["sipUsername"] = sip_username
        if status is not UNSET:
            field_dict["status"] = status
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if skill_group is not UNSET:
            field_dict["skillGroup"] = skill_group
        if level is not UNSET:
            field_dict["level"] = level
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if queue_ids is not UNSET:
            field_dict["queueIds"] = queue_ids
        if queue_names is not UNSET:
            field_dict["queueNames"] = queue_names
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if outbound_phone_number_id is not UNSET:
            field_dict["outboundPhoneNumberId"] = outbound_phone_number_id
        if outbound_phone_number_did_number is not UNSET:
            field_dict["outboundPhoneNumberDidNumber"] = outbound_phone_number_did_number
        if agent_code is not UNSET:
            field_dict["agentCode"] = agent_code

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




        _user_id = d.pop("userId", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id,  Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)




        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))


        def _parse_avatar(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar = _parse_avatar(d.pop("avatar", UNSET))


        def _parse_extension(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        extension = _parse_extension(d.pop("extension", UNSET))


        def _parse_sip_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sip_username = _parse_sip_username(d.pop("sipUsername", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_device_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_type = _parse_device_type(d.pop("deviceType", UNSET))


        def _parse_skill_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        skill_group = _parse_skill_group(d.pop("skillGroup", UNSET))


        level = d.pop("level", UNSET)

        is_active = d.pop("isActive", UNSET)

        def _parse_queue_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                queue_ids_type_0 = []
                _queue_ids_type_0 = data
                for queue_ids_type_0_item_data in (_queue_ids_type_0):
                    queue_ids_type_0_item = UUID(queue_ids_type_0_item_data)



                    queue_ids_type_0.append(queue_ids_type_0_item)

                return queue_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        queue_ids = _parse_queue_ids(d.pop("queueIds", UNSET))


        def _parse_queue_names(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                queue_names_type_0 = cast(list[str], data)

                return queue_names_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        queue_names = _parse_queue_names(d.pop("queueNames", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_outbound_phone_number_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                outbound_phone_number_id_type_0 = UUID(data)



                return outbound_phone_number_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        outbound_phone_number_id = _parse_outbound_phone_number_id(d.pop("outboundPhoneNumberId", UNSET))


        def _parse_outbound_phone_number_did_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        outbound_phone_number_did_number = _parse_outbound_phone_number_did_number(d.pop("outboundPhoneNumberDidNumber", UNSET))


        def _parse_agent_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        agent_code = _parse_agent_code(d.pop("agentCode", UNSET))


        agent_summary_dto = cls(
            id=id,
            user_id=user_id,
            display_name=display_name,
            avatar=avatar,
            extension=extension,
            sip_username=sip_username,
            status=status,
            device_type=device_type,
            skill_group=skill_group,
            level=level,
            is_active=is_active,
            queue_ids=queue_ids,
            queue_names=queue_names,
            created_at=created_at,
            outbound_phone_number_id=outbound_phone_number_id,
            outbound_phone_number_did_number=outbound_phone_number_did_number,
            agent_code=agent_code,
        )

        return agent_summary_dto


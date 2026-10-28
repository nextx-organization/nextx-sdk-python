from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="ContactChatSummaryDto")



@_attrs_define
class ContactChatSummaryDto:
    

    open_count: int | Unset = UNSET
    total_count: int | Unset = UNSET
    unread_count: int | Unset = UNSET
    last_message_at: datetime.datetime | None | Unset = UNSET
    last_message_preview: None | str | Unset = UNSET
    last_message_direction: None | str | Unset = UNSET
    last_channel_type: None | str | Unset = UNSET
    awaiting_reply_minutes: int | None | Unset = UNSET
    sla_breached: bool | Unset = UNSET
    bot_handling: bool | Unset = UNSET
    linked_order_codes: list[str] | None | Unset = UNSET
    conversation_tags: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        open_count = self.open_count

        total_count = self.total_count

        unread_count = self.unread_count

        last_message_at: None | str | Unset
        if isinstance(self.last_message_at, Unset):
            last_message_at = UNSET
        elif isinstance(self.last_message_at, datetime.datetime):
            last_message_at = self.last_message_at.isoformat()
        else:
            last_message_at = self.last_message_at

        last_message_preview: None | str | Unset
        if isinstance(self.last_message_preview, Unset):
            last_message_preview = UNSET
        else:
            last_message_preview = self.last_message_preview

        last_message_direction: None | str | Unset
        if isinstance(self.last_message_direction, Unset):
            last_message_direction = UNSET
        else:
            last_message_direction = self.last_message_direction

        last_channel_type: None | str | Unset
        if isinstance(self.last_channel_type, Unset):
            last_channel_type = UNSET
        else:
            last_channel_type = self.last_channel_type

        awaiting_reply_minutes: int | None | Unset
        if isinstance(self.awaiting_reply_minutes, Unset):
            awaiting_reply_minutes = UNSET
        else:
            awaiting_reply_minutes = self.awaiting_reply_minutes

        sla_breached = self.sla_breached

        bot_handling = self.bot_handling

        linked_order_codes: list[str] | None | Unset
        if isinstance(self.linked_order_codes, Unset):
            linked_order_codes = UNSET
        elif isinstance(self.linked_order_codes, list):
            linked_order_codes = self.linked_order_codes


        else:
            linked_order_codes = self.linked_order_codes

        conversation_tags: list[str] | None | Unset
        if isinstance(self.conversation_tags, Unset):
            conversation_tags = UNSET
        elif isinstance(self.conversation_tags, list):
            conversation_tags = self.conversation_tags


        else:
            conversation_tags = self.conversation_tags


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if open_count is not UNSET:
            field_dict["openCount"] = open_count
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count
        if unread_count is not UNSET:
            field_dict["unreadCount"] = unread_count
        if last_message_at is not UNSET:
            field_dict["lastMessageAt"] = last_message_at
        if last_message_preview is not UNSET:
            field_dict["lastMessagePreview"] = last_message_preview
        if last_message_direction is not UNSET:
            field_dict["lastMessageDirection"] = last_message_direction
        if last_channel_type is not UNSET:
            field_dict["lastChannelType"] = last_channel_type
        if awaiting_reply_minutes is not UNSET:
            field_dict["awaitingReplyMinutes"] = awaiting_reply_minutes
        if sla_breached is not UNSET:
            field_dict["slaBreached"] = sla_breached
        if bot_handling is not UNSET:
            field_dict["botHandling"] = bot_handling
        if linked_order_codes is not UNSET:
            field_dict["linkedOrderCodes"] = linked_order_codes
        if conversation_tags is not UNSET:
            field_dict["conversationTags"] = conversation_tags

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        open_count = d.pop("openCount", UNSET)

        total_count = d.pop("totalCount", UNSET)

        unread_count = d.pop("unreadCount", UNSET)

        def _parse_last_message_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_message_at_type_0 = datetime.datetime.fromisoformat(data)



                return last_message_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_message_at = _parse_last_message_at(d.pop("lastMessageAt", UNSET))


        def _parse_last_message_preview(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_message_preview = _parse_last_message_preview(d.pop("lastMessagePreview", UNSET))


        def _parse_last_message_direction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_message_direction = _parse_last_message_direction(d.pop("lastMessageDirection", UNSET))


        def _parse_last_channel_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_channel_type = _parse_last_channel_type(d.pop("lastChannelType", UNSET))


        def _parse_awaiting_reply_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        awaiting_reply_minutes = _parse_awaiting_reply_minutes(d.pop("awaitingReplyMinutes", UNSET))


        sla_breached = d.pop("slaBreached", UNSET)

        bot_handling = d.pop("botHandling", UNSET)

        def _parse_linked_order_codes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                linked_order_codes_type_0 = cast(list[str], data)

                return linked_order_codes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        linked_order_codes = _parse_linked_order_codes(d.pop("linkedOrderCodes", UNSET))


        def _parse_conversation_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                conversation_tags_type_0 = cast(list[str], data)

                return conversation_tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        conversation_tags = _parse_conversation_tags(d.pop("conversationTags", UNSET))


        contact_chat_summary_dto = cls(
            open_count=open_count,
            total_count=total_count,
            unread_count=unread_count,
            last_message_at=last_message_at,
            last_message_preview=last_message_preview,
            last_message_direction=last_message_direction,
            last_channel_type=last_channel_type,
            awaiting_reply_minutes=awaiting_reply_minutes,
            sla_breached=sla_breached,
            bot_handling=bot_handling,
            linked_order_codes=linked_order_codes,
            conversation_tags=conversation_tags,
        )

        return contact_chat_summary_dto


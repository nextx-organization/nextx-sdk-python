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

if TYPE_CHECKING:
  from ..models.attachment_dto import AttachmentDto
  from ..models.message_button_dto import MessageButtonDto
  from ..models.message_mention_dto import MessageMentionDto
  from ..models.message_reaction_dto import MessageReactionDto





T = TypeVar("T", bound="MessageDto")



@_attrs_define
class MessageDto:
    

    id: UUID | Unset = UNSET
    direction: None | str | Unset = UNSET
    sender_type: None | str | Unset = UNSET
    sender_name: None | str | Unset = UNSET
    message_type: None | str | Unset = UNSET
    content: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    attachments: list[AttachmentDto] | None | Unset = UNSET
    sent_at: datetime.datetime | None | Unset = UNSET
    failure_reason: None | str | Unset = UNSET
    is_internal: bool | Unset = UNSET
    product_snapshot: None | str | Unset = UNSET
    reactions: list[MessageReactionDto] | None | Unset = UNSET
    visibility: None | str | Unset = UNSET
    facebook_comment_id: None | str | Unset = UNSET
    facebook_parent_comment_id: None | str | Unset = UNSET
    buttons: list[MessageButtonDto] | None | Unset = UNSET
    reply_to_message_id: None | Unset | UUID = UNSET
    reply_to_snippet: None | str | Unset = UNSET
    reply_to_sender_name: None | str | Unset = UNSET
    sender_avatar_url: None | str | Unset = UNSET
    mentions: list[MessageMentionDto] | None | Unset = UNSET
    metadata: None | str | Unset = UNSET
    is_recalled: bool | Unset = UNSET
    recalled_at: datetime.datetime | None | Unset = UNSET
    comment_cluster_id: None | Unset | UUID = UNSET
    sender_external_id: None | str | Unset = UNSET
    sender_handle: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.attachment_dto import AttachmentDto # noqa: PLC0415
        from ..models.message_button_dto import MessageButtonDto # noqa: PLC0415
        from ..models.message_mention_dto import MessageMentionDto # noqa: PLC0415
        from ..models.message_reaction_dto import MessageReactionDto # noqa: PLC0415
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        direction: None | str | Unset
        if isinstance(self.direction, Unset):
            direction = UNSET
        else:
            direction = self.direction

        sender_type: None | str | Unset
        if isinstance(self.sender_type, Unset):
            sender_type = UNSET
        else:
            sender_type = self.sender_type

        sender_name: None | str | Unset
        if isinstance(self.sender_name, Unset):
            sender_name = UNSET
        else:
            sender_name = self.sender_name

        message_type: None | str | Unset
        if isinstance(self.message_type, Unset):
            message_type = UNSET
        else:
            message_type = self.message_type

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        attachments: list[dict[str, Any]] | None | Unset
        if isinstance(self.attachments, Unset):
            attachments = UNSET
        elif isinstance(self.attachments, list):
            attachments = []
            for attachments_type_0_item_data in self.attachments:
                attachments_type_0_item = attachments_type_0_item_data.to_dict()
                attachments.append(attachments_type_0_item)


        else:
            attachments = self.attachments

        sent_at: None | str | Unset
        if isinstance(self.sent_at, Unset):
            sent_at = UNSET
        elif isinstance(self.sent_at, datetime.datetime):
            sent_at = self.sent_at.isoformat()
        else:
            sent_at = self.sent_at

        failure_reason: None | str | Unset
        if isinstance(self.failure_reason, Unset):
            failure_reason = UNSET
        else:
            failure_reason = self.failure_reason

        is_internal = self.is_internal

        product_snapshot: None | str | Unset
        if isinstance(self.product_snapshot, Unset):
            product_snapshot = UNSET
        else:
            product_snapshot = self.product_snapshot

        reactions: list[dict[str, Any]] | None | Unset
        if isinstance(self.reactions, Unset):
            reactions = UNSET
        elif isinstance(self.reactions, list):
            reactions = []
            for reactions_type_0_item_data in self.reactions:
                reactions_type_0_item = reactions_type_0_item_data.to_dict()
                reactions.append(reactions_type_0_item)


        else:
            reactions = self.reactions

        visibility: None | str | Unset
        if isinstance(self.visibility, Unset):
            visibility = UNSET
        else:
            visibility = self.visibility

        facebook_comment_id: None | str | Unset
        if isinstance(self.facebook_comment_id, Unset):
            facebook_comment_id = UNSET
        else:
            facebook_comment_id = self.facebook_comment_id

        facebook_parent_comment_id: None | str | Unset
        if isinstance(self.facebook_parent_comment_id, Unset):
            facebook_parent_comment_id = UNSET
        else:
            facebook_parent_comment_id = self.facebook_parent_comment_id

        buttons: list[dict[str, Any]] | None | Unset
        if isinstance(self.buttons, Unset):
            buttons = UNSET
        elif isinstance(self.buttons, list):
            buttons = []
            for buttons_type_0_item_data in self.buttons:
                buttons_type_0_item = buttons_type_0_item_data.to_dict()
                buttons.append(buttons_type_0_item)


        else:
            buttons = self.buttons

        reply_to_message_id: None | str | Unset
        if isinstance(self.reply_to_message_id, Unset):
            reply_to_message_id = UNSET
        elif isinstance(self.reply_to_message_id, UUID):
            reply_to_message_id = str(self.reply_to_message_id)
        else:
            reply_to_message_id = self.reply_to_message_id

        reply_to_snippet: None | str | Unset
        if isinstance(self.reply_to_snippet, Unset):
            reply_to_snippet = UNSET
        else:
            reply_to_snippet = self.reply_to_snippet

        reply_to_sender_name: None | str | Unset
        if isinstance(self.reply_to_sender_name, Unset):
            reply_to_sender_name = UNSET
        else:
            reply_to_sender_name = self.reply_to_sender_name

        sender_avatar_url: None | str | Unset
        if isinstance(self.sender_avatar_url, Unset):
            sender_avatar_url = UNSET
        else:
            sender_avatar_url = self.sender_avatar_url

        mentions: list[dict[str, Any]] | None | Unset
        if isinstance(self.mentions, Unset):
            mentions = UNSET
        elif isinstance(self.mentions, list):
            mentions = []
            for mentions_type_0_item_data in self.mentions:
                mentions_type_0_item = mentions_type_0_item_data.to_dict()
                mentions.append(mentions_type_0_item)


        else:
            mentions = self.mentions

        metadata: None | str | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        else:
            metadata = self.metadata

        is_recalled = self.is_recalled

        recalled_at: None | str | Unset
        if isinstance(self.recalled_at, Unset):
            recalled_at = UNSET
        elif isinstance(self.recalled_at, datetime.datetime):
            recalled_at = self.recalled_at.isoformat()
        else:
            recalled_at = self.recalled_at

        comment_cluster_id: None | str | Unset
        if isinstance(self.comment_cluster_id, Unset):
            comment_cluster_id = UNSET
        elif isinstance(self.comment_cluster_id, UUID):
            comment_cluster_id = str(self.comment_cluster_id)
        else:
            comment_cluster_id = self.comment_cluster_id

        sender_external_id: None | str | Unset
        if isinstance(self.sender_external_id, Unset):
            sender_external_id = UNSET
        else:
            sender_external_id = self.sender_external_id

        sender_handle: None | str | Unset
        if isinstance(self.sender_handle, Unset):
            sender_handle = UNSET
        else:
            sender_handle = self.sender_handle


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if direction is not UNSET:
            field_dict["direction"] = direction
        if sender_type is not UNSET:
            field_dict["senderType"] = sender_type
        if sender_name is not UNSET:
            field_dict["senderName"] = sender_name
        if message_type is not UNSET:
            field_dict["messageType"] = message_type
        if content is not UNSET:
            field_dict["content"] = content
        if status is not UNSET:
            field_dict["status"] = status
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if sent_at is not UNSET:
            field_dict["sentAt"] = sent_at
        if failure_reason is not UNSET:
            field_dict["failureReason"] = failure_reason
        if is_internal is not UNSET:
            field_dict["isInternal"] = is_internal
        if product_snapshot is not UNSET:
            field_dict["productSnapshot"] = product_snapshot
        if reactions is not UNSET:
            field_dict["reactions"] = reactions
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if facebook_comment_id is not UNSET:
            field_dict["facebookCommentId"] = facebook_comment_id
        if facebook_parent_comment_id is not UNSET:
            field_dict["facebookParentCommentId"] = facebook_parent_comment_id
        if buttons is not UNSET:
            field_dict["buttons"] = buttons
        if reply_to_message_id is not UNSET:
            field_dict["replyToMessageId"] = reply_to_message_id
        if reply_to_snippet is not UNSET:
            field_dict["replyToSnippet"] = reply_to_snippet
        if reply_to_sender_name is not UNSET:
            field_dict["replyToSenderName"] = reply_to_sender_name
        if sender_avatar_url is not UNSET:
            field_dict["senderAvatarUrl"] = sender_avatar_url
        if mentions is not UNSET:
            field_dict["mentions"] = mentions
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if is_recalled is not UNSET:
            field_dict["isRecalled"] = is_recalled
        if recalled_at is not UNSET:
            field_dict["recalledAt"] = recalled_at
        if comment_cluster_id is not UNSET:
            field_dict["commentClusterId"] = comment_cluster_id
        if sender_external_id is not UNSET:
            field_dict["senderExternalId"] = sender_external_id
        if sender_handle is not UNSET:
            field_dict["senderHandle"] = sender_handle

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attachment_dto import AttachmentDto # noqa: PLC0415
        from ..models.message_button_dto import MessageButtonDto # noqa: PLC0415
        from ..models.message_mention_dto import MessageMentionDto # noqa: PLC0415
        from ..models.message_reaction_dto import MessageReactionDto # noqa: PLC0415
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_direction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        direction = _parse_direction(d.pop("direction", UNSET))


        def _parse_sender_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sender_type = _parse_sender_type(d.pop("senderType", UNSET))


        def _parse_sender_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sender_name = _parse_sender_name(d.pop("senderName", UNSET))


        def _parse_message_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message_type = _parse_message_type(d.pop("messageType", UNSET))


        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_attachments(data: object) -> list[AttachmentDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attachments_type_0 = []
                _attachments_type_0 = data
                for attachments_type_0_item_data in (_attachments_type_0):
                    attachments_type_0_item = AttachmentDto.from_dict(attachments_type_0_item_data)



                    attachments_type_0.append(attachments_type_0_item)

                return attachments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AttachmentDto] | None | Unset, data)

        attachments = _parse_attachments(d.pop("attachments", UNSET))


        def _parse_sent_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sent_at_type_0 = datetime.datetime.fromisoformat(data)



                return sent_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        sent_at = _parse_sent_at(d.pop("sentAt", UNSET))


        def _parse_failure_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        failure_reason = _parse_failure_reason(d.pop("failureReason", UNSET))


        is_internal = d.pop("isInternal", UNSET)

        def _parse_product_snapshot(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_snapshot = _parse_product_snapshot(d.pop("productSnapshot", UNSET))


        def _parse_reactions(data: object) -> list[MessageReactionDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                reactions_type_0 = []
                _reactions_type_0 = data
                for reactions_type_0_item_data in (_reactions_type_0):
                    reactions_type_0_item = MessageReactionDto.from_dict(reactions_type_0_item_data)



                    reactions_type_0.append(reactions_type_0_item)

                return reactions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MessageReactionDto] | None | Unset, data)

        reactions = _parse_reactions(d.pop("reactions", UNSET))


        def _parse_visibility(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        visibility = _parse_visibility(d.pop("visibility", UNSET))


        def _parse_facebook_comment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facebook_comment_id = _parse_facebook_comment_id(d.pop("facebookCommentId", UNSET))


        def _parse_facebook_parent_comment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facebook_parent_comment_id = _parse_facebook_parent_comment_id(d.pop("facebookParentCommentId", UNSET))


        def _parse_buttons(data: object) -> list[MessageButtonDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                buttons_type_0 = []
                _buttons_type_0 = data
                for buttons_type_0_item_data in (_buttons_type_0):
                    buttons_type_0_item = MessageButtonDto.from_dict(buttons_type_0_item_data)



                    buttons_type_0.append(buttons_type_0_item)

                return buttons_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MessageButtonDto] | None | Unset, data)

        buttons = _parse_buttons(d.pop("buttons", UNSET))


        def _parse_reply_to_message_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reply_to_message_id_type_0 = UUID(data)



                return reply_to_message_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        reply_to_message_id = _parse_reply_to_message_id(d.pop("replyToMessageId", UNSET))


        def _parse_reply_to_snippet(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reply_to_snippet = _parse_reply_to_snippet(d.pop("replyToSnippet", UNSET))


        def _parse_reply_to_sender_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reply_to_sender_name = _parse_reply_to_sender_name(d.pop("replyToSenderName", UNSET))


        def _parse_sender_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sender_avatar_url = _parse_sender_avatar_url(d.pop("senderAvatarUrl", UNSET))


        def _parse_mentions(data: object) -> list[MessageMentionDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                mentions_type_0 = []
                _mentions_type_0 = data
                for mentions_type_0_item_data in (_mentions_type_0):
                    mentions_type_0_item = MessageMentionDto.from_dict(mentions_type_0_item_data)



                    mentions_type_0.append(mentions_type_0_item)

                return mentions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MessageMentionDto] | None | Unset, data)

        mentions = _parse_mentions(d.pop("mentions", UNSET))


        def _parse_metadata(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))


        is_recalled = d.pop("isRecalled", UNSET)

        def _parse_recalled_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                recalled_at_type_0 = datetime.datetime.fromisoformat(data)



                return recalled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        recalled_at = _parse_recalled_at(d.pop("recalledAt", UNSET))


        def _parse_comment_cluster_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                comment_cluster_id_type_0 = UUID(data)



                return comment_cluster_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        comment_cluster_id = _parse_comment_cluster_id(d.pop("commentClusterId", UNSET))


        def _parse_sender_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sender_external_id = _parse_sender_external_id(d.pop("senderExternalId", UNSET))


        def _parse_sender_handle(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sender_handle = _parse_sender_handle(d.pop("senderHandle", UNSET))


        message_dto = cls(
            id=id,
            direction=direction,
            sender_type=sender_type,
            sender_name=sender_name,
            message_type=message_type,
            content=content,
            status=status,
            attachments=attachments,
            sent_at=sent_at,
            failure_reason=failure_reason,
            is_internal=is_internal,
            product_snapshot=product_snapshot,
            reactions=reactions,
            visibility=visibility,
            facebook_comment_id=facebook_comment_id,
            facebook_parent_comment_id=facebook_parent_comment_id,
            buttons=buttons,
            reply_to_message_id=reply_to_message_id,
            reply_to_snippet=reply_to_snippet,
            reply_to_sender_name=reply_to_sender_name,
            sender_avatar_url=sender_avatar_url,
            mentions=mentions,
            metadata=metadata,
            is_recalled=is_recalled,
            recalled_at=recalled_at,
            comment_cluster_id=comment_cluster_id,
            sender_external_id=sender_external_id,
            sender_handle=sender_handle,
        )

        return message_dto


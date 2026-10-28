from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.send_message_request_type import check_send_message_request_type
from ..models.send_message_request_type import SendMessageRequestType
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.mention_request import MentionRequest





T = TypeVar("T", bound="SendMessageRequest")



@_attrs_define
class SendMessageRequest:
    

    type_: SendMessageRequestType | Unset = UNSET
    content: None | str | Unset = UNSET
    storage_key: None | str | Unset = UNSET
    file_name: None | str | Unset = UNSET
    file_size_bytes: int | None | Unset = UNSET
    mime_type: None | str | Unset = UNSET
    client_id: None | str | Unset = UNSET
    product_snapshot: None | str | Unset = UNSET
    visibility: None | str | Unset = UNSET
    mentions: list[MentionRequest] | None | Unset = UNSET
    reply_to_message_id: None | Unset | UUID = UNSET
    comment_cluster_id: None | Unset | UUID = UNSET
    reply_to_comment_message_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mention_request import MentionRequest # noqa: PLC0415
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_


        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        storage_key: None | str | Unset
        if isinstance(self.storage_key, Unset):
            storage_key = UNSET
        else:
            storage_key = self.storage_key

        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        file_size_bytes: int | None | Unset
        if isinstance(self.file_size_bytes, Unset):
            file_size_bytes = UNSET
        else:
            file_size_bytes = self.file_size_bytes

        mime_type: None | str | Unset
        if isinstance(self.mime_type, Unset):
            mime_type = UNSET
        else:
            mime_type = self.mime_type

        client_id: None | str | Unset
        if isinstance(self.client_id, Unset):
            client_id = UNSET
        else:
            client_id = self.client_id

        product_snapshot: None | str | Unset
        if isinstance(self.product_snapshot, Unset):
            product_snapshot = UNSET
        else:
            product_snapshot = self.product_snapshot

        visibility: None | str | Unset
        if isinstance(self.visibility, Unset):
            visibility = UNSET
        else:
            visibility = self.visibility

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

        reply_to_message_id: None | str | Unset
        if isinstance(self.reply_to_message_id, Unset):
            reply_to_message_id = UNSET
        elif isinstance(self.reply_to_message_id, UUID):
            reply_to_message_id = str(self.reply_to_message_id)
        else:
            reply_to_message_id = self.reply_to_message_id

        comment_cluster_id: None | str | Unset
        if isinstance(self.comment_cluster_id, Unset):
            comment_cluster_id = UNSET
        elif isinstance(self.comment_cluster_id, UUID):
            comment_cluster_id = str(self.comment_cluster_id)
        else:
            comment_cluster_id = self.comment_cluster_id

        reply_to_comment_message_id: None | str | Unset
        if isinstance(self.reply_to_comment_message_id, Unset):
            reply_to_comment_message_id = UNSET
        elif isinstance(self.reply_to_comment_message_id, UUID):
            reply_to_comment_message_id = str(self.reply_to_comment_message_id)
        else:
            reply_to_comment_message_id = self.reply_to_comment_message_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if content is not UNSET:
            field_dict["content"] = content
        if storage_key is not UNSET:
            field_dict["storageKey"] = storage_key
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if file_size_bytes is not UNSET:
            field_dict["fileSizeBytes"] = file_size_bytes
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if product_snapshot is not UNSET:
            field_dict["productSnapshot"] = product_snapshot
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if mentions is not UNSET:
            field_dict["mentions"] = mentions
        if reply_to_message_id is not UNSET:
            field_dict["replyToMessageId"] = reply_to_message_id
        if comment_cluster_id is not UNSET:
            field_dict["commentClusterId"] = comment_cluster_id
        if reply_to_comment_message_id is not UNSET:
            field_dict["replyToCommentMessageId"] = reply_to_comment_message_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mention_request import MentionRequest # noqa: PLC0415
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: SendMessageRequestType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = check_send_message_request_type(_type_)




        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))


        def _parse_storage_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_key = _parse_storage_key(d.pop("storageKey", UNSET))


        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("fileName", UNSET))


        def _parse_file_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        file_size_bytes = _parse_file_size_bytes(d.pop("fileSizeBytes", UNSET))


        def _parse_mime_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mime_type = _parse_mime_type(d.pop("mimeType", UNSET))


        def _parse_client_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_id = _parse_client_id(d.pop("clientId", UNSET))


        def _parse_product_snapshot(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_snapshot = _parse_product_snapshot(d.pop("productSnapshot", UNSET))


        def _parse_visibility(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        visibility = _parse_visibility(d.pop("visibility", UNSET))


        def _parse_mentions(data: object) -> list[MentionRequest] | None | Unset:
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
                    mentions_type_0_item = MentionRequest.from_dict(mentions_type_0_item_data)



                    mentions_type_0.append(mentions_type_0_item)

                return mentions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MentionRequest] | None | Unset, data)

        mentions = _parse_mentions(d.pop("mentions", UNSET))


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


        def _parse_reply_to_comment_message_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reply_to_comment_message_id_type_0 = UUID(data)



                return reply_to_comment_message_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        reply_to_comment_message_id = _parse_reply_to_comment_message_id(d.pop("replyToCommentMessageId", UNSET))


        send_message_request = cls(
            type_=type_,
            content=content,
            storage_key=storage_key,
            file_name=file_name,
            file_size_bytes=file_size_bytes,
            mime_type=mime_type,
            client_id=client_id,
            product_snapshot=product_snapshot,
            visibility=visibility,
            mentions=mentions,
            reply_to_message_id=reply_to_message_id,
            comment_cluster_id=comment_cluster_id,
            reply_to_comment_message_id=reply_to_comment_message_id,
        )

        return send_message_request


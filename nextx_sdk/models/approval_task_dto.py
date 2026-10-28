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






T = TypeVar("T", bound="ApprovalTaskDto")



@_attrs_define
class ApprovalTaskDto:
    

    id: UUID | Unset = UNSET
    instance_id: UUID | Unset = UNSET
    node_id: UUID | Unset = UNSET
    approver_id: UUID | Unset = UNSET
    status: None | str | Unset = UNSET
    task_kind: None | str | Unset = UNSET
    comment: None | str | Unset = UNSET
    acted_at: datetime.datetime | None | Unset = UNSET
    origin_task_id: None | Unset | UUID = UNSET
    position: int | Unset = UNSET
    due_at: datetime.datetime | None | Unset = UNSET
    escalated_at: datetime.datetime | None | Unset = UNSET
    delegated_for_user_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        instance_id: str | Unset = UNSET
        if not isinstance(self.instance_id, Unset):
            instance_id = str(self.instance_id)

        node_id: str | Unset = UNSET
        if not isinstance(self.node_id, Unset):
            node_id = str(self.node_id)

        approver_id: str | Unset = UNSET
        if not isinstance(self.approver_id, Unset):
            approver_id = str(self.approver_id)

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        task_kind: None | str | Unset
        if isinstance(self.task_kind, Unset):
            task_kind = UNSET
        else:
            task_kind = self.task_kind

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        acted_at: None | str | Unset
        if isinstance(self.acted_at, Unset):
            acted_at = UNSET
        elif isinstance(self.acted_at, datetime.datetime):
            acted_at = self.acted_at.isoformat()
        else:
            acted_at = self.acted_at

        origin_task_id: None | str | Unset
        if isinstance(self.origin_task_id, Unset):
            origin_task_id = UNSET
        elif isinstance(self.origin_task_id, UUID):
            origin_task_id = str(self.origin_task_id)
        else:
            origin_task_id = self.origin_task_id

        position = self.position

        due_at: None | str | Unset
        if isinstance(self.due_at, Unset):
            due_at = UNSET
        elif isinstance(self.due_at, datetime.datetime):
            due_at = self.due_at.isoformat()
        else:
            due_at = self.due_at

        escalated_at: None | str | Unset
        if isinstance(self.escalated_at, Unset):
            escalated_at = UNSET
        elif isinstance(self.escalated_at, datetime.datetime):
            escalated_at = self.escalated_at.isoformat()
        else:
            escalated_at = self.escalated_at

        delegated_for_user_id: None | str | Unset
        if isinstance(self.delegated_for_user_id, Unset):
            delegated_for_user_id = UNSET
        elif isinstance(self.delegated_for_user_id, UUID):
            delegated_for_user_id = str(self.delegated_for_user_id)
        else:
            delegated_for_user_id = self.delegated_for_user_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if instance_id is not UNSET:
            field_dict["instanceId"] = instance_id
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if approver_id is not UNSET:
            field_dict["approverId"] = approver_id
        if status is not UNSET:
            field_dict["status"] = status
        if task_kind is not UNSET:
            field_dict["taskKind"] = task_kind
        if comment is not UNSET:
            field_dict["comment"] = comment
        if acted_at is not UNSET:
            field_dict["actedAt"] = acted_at
        if origin_task_id is not UNSET:
            field_dict["originTaskId"] = origin_task_id
        if position is not UNSET:
            field_dict["position"] = position
        if due_at is not UNSET:
            field_dict["dueAt"] = due_at
        if escalated_at is not UNSET:
            field_dict["escalatedAt"] = escalated_at
        if delegated_for_user_id is not UNSET:
            field_dict["delegatedForUserId"] = delegated_for_user_id

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




        _instance_id = d.pop("instanceId", UNSET)
        instance_id: UUID | Unset
        if isinstance(_instance_id,  Unset):
            instance_id = UNSET
        else:
            instance_id = UUID(_instance_id)




        _node_id = d.pop("nodeId", UNSET)
        node_id: UUID | Unset
        if isinstance(_node_id,  Unset):
            node_id = UNSET
        else:
            node_id = UUID(_node_id)




        _approver_id = d.pop("approverId", UNSET)
        approver_id: UUID | Unset
        if isinstance(_approver_id,  Unset):
            approver_id = UNSET
        else:
            approver_id = UUID(_approver_id)




        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_task_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        task_kind = _parse_task_kind(d.pop("taskKind", UNSET))


        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))


        def _parse_acted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                acted_at_type_0 = datetime.datetime.fromisoformat(data)



                return acted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        acted_at = _parse_acted_at(d.pop("actedAt", UNSET))


        def _parse_origin_task_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                origin_task_id_type_0 = UUID(data)



                return origin_task_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        origin_task_id = _parse_origin_task_id(d.pop("originTaskId", UNSET))


        position = d.pop("position", UNSET)

        def _parse_due_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_at_type_0 = datetime.datetime.fromisoformat(data)



                return due_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        due_at = _parse_due_at(d.pop("dueAt", UNSET))


        def _parse_escalated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                escalated_at_type_0 = datetime.datetime.fromisoformat(data)



                return escalated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        escalated_at = _parse_escalated_at(d.pop("escalatedAt", UNSET))


        def _parse_delegated_for_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delegated_for_user_id_type_0 = UUID(data)



                return delegated_for_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        delegated_for_user_id = _parse_delegated_for_user_id(d.pop("delegatedForUserId", UNSET))


        approval_task_dto = cls(
            id=id,
            instance_id=instance_id,
            node_id=node_id,
            approver_id=approver_id,
            status=status,
            task_kind=task_kind,
            comment=comment,
            acted_at=acted_at,
            origin_task_id=origin_task_id,
            position=position,
            due_at=due_at,
            escalated_at=escalated_at,
            delegated_for_user_id=delegated_for_user_id,
        )

        return approval_task_dto


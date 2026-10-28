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
  from ..models.failure_reason_dto import FailureReasonDto





T = TypeVar("T", bound="CallSummaryDto")



@_attrs_define
class CallSummaryDto:
    

    id: UUID | Unset = UNSET
    call_uuid: None | str | Unset = UNSET
    direction: None | str | Unset = UNSET
    caller_number: None | str | Unset = UNSET
    callee_number: None | str | Unset = UNSET
    agent_id: None | Unset | UUID = UNSET
    agent_name: None | str | Unset = UNSET
    queue_id: None | Unset | UUID = UNSET
    queue_name: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    started_at: datetime.datetime | None | Unset = UNSET
    answered_at: datetime.datetime | None | Unset = UNSET
    ended_at: datetime.datetime | None | Unset = UNSET
    wait_duration_sec: int | None | Unset = UNSET
    talk_duration_sec: int | None | Unset = UNSET
    has_recording: bool | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    csat_score: int | None | Unset = UNSET
    ticket_id: None | Unset | UUID = UNSET
    order_id: None | Unset | UUID = UNSET
    created_at: datetime.datetime | Unset = UNSET
    crm_contact_id: None | Unset | UUID = UNSET
    crm_contact_name: None | str | Unset = UNSET
    crm_contact_tier: None | str | Unset = UNSET
    open_ticket_count: int | None | Unset = UNSET
    agent_avatar: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    is_internal: bool | Unset = UNSET
    disposition: None | str | Unset = UNSET
    failure_reason: FailureReasonDto | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.failure_reason_dto import FailureReasonDto # noqa: PLC0415
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        call_uuid: None | str | Unset
        if isinstance(self.call_uuid, Unset):
            call_uuid = UNSET
        else:
            call_uuid = self.call_uuid

        direction: None | str | Unset
        if isinstance(self.direction, Unset):
            direction = UNSET
        else:
            direction = self.direction

        caller_number: None | str | Unset
        if isinstance(self.caller_number, Unset):
            caller_number = UNSET
        else:
            caller_number = self.caller_number

        callee_number: None | str | Unset
        if isinstance(self.callee_number, Unset):
            callee_number = UNSET
        else:
            callee_number = self.callee_number

        agent_id: None | str | Unset
        if isinstance(self.agent_id, Unset):
            agent_id = UNSET
        elif isinstance(self.agent_id, UUID):
            agent_id = str(self.agent_id)
        else:
            agent_id = self.agent_id

        agent_name: None | str | Unset
        if isinstance(self.agent_name, Unset):
            agent_name = UNSET
        else:
            agent_name = self.agent_name

        queue_id: None | str | Unset
        if isinstance(self.queue_id, Unset):
            queue_id = UNSET
        elif isinstance(self.queue_id, UUID):
            queue_id = str(self.queue_id)
        else:
            queue_id = self.queue_id

        queue_name: None | str | Unset
        if isinstance(self.queue_name, Unset):
            queue_name = UNSET
        else:
            queue_name = self.queue_name

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        answered_at: None | str | Unset
        if isinstance(self.answered_at, Unset):
            answered_at = UNSET
        elif isinstance(self.answered_at, datetime.datetime):
            answered_at = self.answered_at.isoformat()
        else:
            answered_at = self.answered_at

        ended_at: None | str | Unset
        if isinstance(self.ended_at, Unset):
            ended_at = UNSET
        elif isinstance(self.ended_at, datetime.datetime):
            ended_at = self.ended_at.isoformat()
        else:
            ended_at = self.ended_at

        wait_duration_sec: int | None | Unset
        if isinstance(self.wait_duration_sec, Unset):
            wait_duration_sec = UNSET
        else:
            wait_duration_sec = self.wait_duration_sec

        talk_duration_sec: int | None | Unset
        if isinstance(self.talk_duration_sec, Unset):
            talk_duration_sec = UNSET
        else:
            talk_duration_sec = self.talk_duration_sec

        has_recording = self.has_recording

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags


        else:
            tags = self.tags

        csat_score: int | None | Unset
        if isinstance(self.csat_score, Unset):
            csat_score = UNSET
        else:
            csat_score = self.csat_score

        ticket_id: None | str | Unset
        if isinstance(self.ticket_id, Unset):
            ticket_id = UNSET
        elif isinstance(self.ticket_id, UUID):
            ticket_id = str(self.ticket_id)
        else:
            ticket_id = self.ticket_id

        order_id: None | str | Unset
        if isinstance(self.order_id, Unset):
            order_id = UNSET
        elif isinstance(self.order_id, UUID):
            order_id = str(self.order_id)
        else:
            order_id = self.order_id

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        crm_contact_id: None | str | Unset
        if isinstance(self.crm_contact_id, Unset):
            crm_contact_id = UNSET
        elif isinstance(self.crm_contact_id, UUID):
            crm_contact_id = str(self.crm_contact_id)
        else:
            crm_contact_id = self.crm_contact_id

        crm_contact_name: None | str | Unset
        if isinstance(self.crm_contact_name, Unset):
            crm_contact_name = UNSET
        else:
            crm_contact_name = self.crm_contact_name

        crm_contact_tier: None | str | Unset
        if isinstance(self.crm_contact_tier, Unset):
            crm_contact_tier = UNSET
        else:
            crm_contact_tier = self.crm_contact_tier

        open_ticket_count: int | None | Unset
        if isinstance(self.open_ticket_count, Unset):
            open_ticket_count = UNSET
        else:
            open_ticket_count = self.open_ticket_count

        agent_avatar: None | str | Unset
        if isinstance(self.agent_avatar, Unset):
            agent_avatar = UNSET
        else:
            agent_avatar = self.agent_avatar

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        is_internal = self.is_internal

        disposition: None | str | Unset
        if isinstance(self.disposition, Unset):
            disposition = UNSET
        else:
            disposition = self.disposition

        failure_reason: dict[str, Any] | Unset = UNSET
        if not isinstance(self.failure_reason, Unset):
            failure_reason = self.failure_reason.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if call_uuid is not UNSET:
            field_dict["callUuid"] = call_uuid
        if direction is not UNSET:
            field_dict["direction"] = direction
        if caller_number is not UNSET:
            field_dict["callerNumber"] = caller_number
        if callee_number is not UNSET:
            field_dict["calleeNumber"] = callee_number
        if agent_id is not UNSET:
            field_dict["agentId"] = agent_id
        if agent_name is not UNSET:
            field_dict["agentName"] = agent_name
        if queue_id is not UNSET:
            field_dict["queueId"] = queue_id
        if queue_name is not UNSET:
            field_dict["queueName"] = queue_name
        if status is not UNSET:
            field_dict["status"] = status
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if answered_at is not UNSET:
            field_dict["answeredAt"] = answered_at
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at
        if wait_duration_sec is not UNSET:
            field_dict["waitDurationSec"] = wait_duration_sec
        if talk_duration_sec is not UNSET:
            field_dict["talkDurationSec"] = talk_duration_sec
        if has_recording is not UNSET:
            field_dict["hasRecording"] = has_recording
        if tags is not UNSET:
            field_dict["tags"] = tags
        if csat_score is not UNSET:
            field_dict["csatScore"] = csat_score
        if ticket_id is not UNSET:
            field_dict["ticketId"] = ticket_id
        if order_id is not UNSET:
            field_dict["orderId"] = order_id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if crm_contact_id is not UNSET:
            field_dict["crmContactId"] = crm_contact_id
        if crm_contact_name is not UNSET:
            field_dict["crmContactName"] = crm_contact_name
        if crm_contact_tier is not UNSET:
            field_dict["crmContactTier"] = crm_contact_tier
        if open_ticket_count is not UNSET:
            field_dict["openTicketCount"] = open_ticket_count
        if agent_avatar is not UNSET:
            field_dict["agentAvatar"] = agent_avatar
        if notes is not UNSET:
            field_dict["notes"] = notes
        if is_internal is not UNSET:
            field_dict["isInternal"] = is_internal
        if disposition is not UNSET:
            field_dict["disposition"] = disposition
        if failure_reason is not UNSET:
            field_dict["failureReason"] = failure_reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.failure_reason_dto import FailureReasonDto # noqa: PLC0415
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_call_uuid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        call_uuid = _parse_call_uuid(d.pop("callUuid", UNSET))


        def _parse_direction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        direction = _parse_direction(d.pop("direction", UNSET))


        def _parse_caller_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        caller_number = _parse_caller_number(d.pop("callerNumber", UNSET))


        def _parse_callee_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        callee_number = _parse_callee_number(d.pop("calleeNumber", UNSET))


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


        def _parse_agent_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        agent_name = _parse_agent_name(d.pop("agentName", UNSET))


        def _parse_queue_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                queue_id_type_0 = UUID(data)



                return queue_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        queue_id = _parse_queue_id(d.pop("queueId", UNSET))


        def _parse_queue_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        queue_name = _parse_queue_name(d.pop("queueName", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_started_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = datetime.datetime.fromisoformat(data)



                return started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        started_at = _parse_started_at(d.pop("startedAt", UNSET))


        def _parse_answered_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                answered_at_type_0 = datetime.datetime.fromisoformat(data)



                return answered_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        answered_at = _parse_answered_at(d.pop("answeredAt", UNSET))


        def _parse_ended_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ended_at_type_0 = datetime.datetime.fromisoformat(data)



                return ended_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        ended_at = _parse_ended_at(d.pop("endedAt", UNSET))


        def _parse_wait_duration_sec(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        wait_duration_sec = _parse_wait_duration_sec(d.pop("waitDurationSec", UNSET))


        def _parse_talk_duration_sec(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        talk_duration_sec = _parse_talk_duration_sec(d.pop("talkDurationSec", UNSET))


        has_recording = d.pop("hasRecording", UNSET)

        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))


        def _parse_csat_score(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        csat_score = _parse_csat_score(d.pop("csatScore", UNSET))


        def _parse_ticket_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ticket_id_type_0 = UUID(data)



                return ticket_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        ticket_id = _parse_ticket_id(d.pop("ticketId", UNSET))


        def _parse_order_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                order_id_type_0 = UUID(data)



                return order_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        order_id = _parse_order_id(d.pop("orderId", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




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


        def _parse_crm_contact_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        crm_contact_name = _parse_crm_contact_name(d.pop("crmContactName", UNSET))


        def _parse_crm_contact_tier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        crm_contact_tier = _parse_crm_contact_tier(d.pop("crmContactTier", UNSET))


        def _parse_open_ticket_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        open_ticket_count = _parse_open_ticket_count(d.pop("openTicketCount", UNSET))


        def _parse_agent_avatar(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        agent_avatar = _parse_agent_avatar(d.pop("agentAvatar", UNSET))


        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


        is_internal = d.pop("isInternal", UNSET)

        def _parse_disposition(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        disposition = _parse_disposition(d.pop("disposition", UNSET))


        _failure_reason = d.pop("failureReason", UNSET)
        failure_reason: FailureReasonDto | Unset
        if isinstance(_failure_reason,  Unset):
            failure_reason = UNSET
        else:
            failure_reason = FailureReasonDto.from_dict(_failure_reason)




        call_summary_dto = cls(
            id=id,
            call_uuid=call_uuid,
            direction=direction,
            caller_number=caller_number,
            callee_number=callee_number,
            agent_id=agent_id,
            agent_name=agent_name,
            queue_id=queue_id,
            queue_name=queue_name,
            status=status,
            started_at=started_at,
            answered_at=answered_at,
            ended_at=ended_at,
            wait_duration_sec=wait_duration_sec,
            talk_duration_sec=talk_duration_sec,
            has_recording=has_recording,
            tags=tags,
            csat_score=csat_score,
            ticket_id=ticket_id,
            order_id=order_id,
            created_at=created_at,
            crm_contact_id=crm_contact_id,
            crm_contact_name=crm_contact_name,
            crm_contact_tier=crm_contact_tier,
            open_ticket_count=open_ticket_count,
            agent_avatar=agent_avatar,
            notes=notes,
            is_internal=is_internal,
            disposition=disposition,
            failure_reason=failure_reason,
        )

        return call_summary_dto


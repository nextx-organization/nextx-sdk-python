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
  from ..models.partner_agent_dto import PartnerAgentDto





T = TypeVar("T", bound="PartnerCallDto")



@_attrs_define
class PartnerCallDto:
    

    call_id: UUID | Unset = UNSET
    status: None | str | Unset = UNSET
    direction: None | str | Unset = UNSET
    from_: None | str | Unset = UNSET
    to: None | str | Unset = UNSET
    agent: PartnerAgentDto | Unset = UNSET
    queue_id: None | Unset | UUID = UNSET
    queue_name: None | str | Unset = UNSET
    started_at: datetime.datetime | None | Unset = UNSET
    answered_at: datetime.datetime | None | Unset = UNSET
    ended_at: datetime.datetime | None | Unset = UNSET
    duration_sec: int | None | Unset = UNSET
    talk_sec: int | None | Unset = UNSET
    wait_sec: int | None | Unset = UNSET
    hangup_cause: int | None | Unset = UNSET
    hangup_cause_name: None | str | Unset = UNSET
    contact_ref: None | str | Unset = UNSET
    metadata: Any | Unset = UNSET
    crm_contact_id: None | Unset | UUID = UNSET
    has_recording: bool | Unset = UNSET
    has_summary: bool | Unset = UNSET
    summary: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.partner_agent_dto import PartnerAgentDto # noqa: PLC0415
        call_id: str | Unset = UNSET
        if not isinstance(self.call_id, Unset):
            call_id = str(self.call_id)

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        direction: None | str | Unset
        if isinstance(self.direction, Unset):
            direction = UNSET
        else:
            direction = self.direction

        from_: None | str | Unset
        if isinstance(self.from_, Unset):
            from_ = UNSET
        else:
            from_ = self.from_

        to: None | str | Unset
        if isinstance(self.to, Unset):
            to = UNSET
        else:
            to = self.to

        agent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.agent, Unset):
            agent = self.agent.to_dict()

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

        duration_sec: int | None | Unset
        if isinstance(self.duration_sec, Unset):
            duration_sec = UNSET
        else:
            duration_sec = self.duration_sec

        talk_sec: int | None | Unset
        if isinstance(self.talk_sec, Unset):
            talk_sec = UNSET
        else:
            talk_sec = self.talk_sec

        wait_sec: int | None | Unset
        if isinstance(self.wait_sec, Unset):
            wait_sec = UNSET
        else:
            wait_sec = self.wait_sec

        hangup_cause: int | None | Unset
        if isinstance(self.hangup_cause, Unset):
            hangup_cause = UNSET
        else:
            hangup_cause = self.hangup_cause

        hangup_cause_name: None | str | Unset
        if isinstance(self.hangup_cause_name, Unset):
            hangup_cause_name = UNSET
        else:
            hangup_cause_name = self.hangup_cause_name

        contact_ref: None | str | Unset
        if isinstance(self.contact_ref, Unset):
            contact_ref = UNSET
        else:
            contact_ref = self.contact_ref

        metadata = self.metadata

        crm_contact_id: None | str | Unset
        if isinstance(self.crm_contact_id, Unset):
            crm_contact_id = UNSET
        elif isinstance(self.crm_contact_id, UUID):
            crm_contact_id = str(self.crm_contact_id)
        else:
            crm_contact_id = self.crm_contact_id

        has_recording = self.has_recording

        has_summary = self.has_summary

        summary: None | str | Unset
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if call_id is not UNSET:
            field_dict["callId"] = call_id
        if status is not UNSET:
            field_dict["status"] = status
        if direction is not UNSET:
            field_dict["direction"] = direction
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if agent is not UNSET:
            field_dict["agent"] = agent
        if queue_id is not UNSET:
            field_dict["queueId"] = queue_id
        if queue_name is not UNSET:
            field_dict["queueName"] = queue_name
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if answered_at is not UNSET:
            field_dict["answeredAt"] = answered_at
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at
        if duration_sec is not UNSET:
            field_dict["durationSec"] = duration_sec
        if talk_sec is not UNSET:
            field_dict["talkSec"] = talk_sec
        if wait_sec is not UNSET:
            field_dict["waitSec"] = wait_sec
        if hangup_cause is not UNSET:
            field_dict["hangupCause"] = hangup_cause
        if hangup_cause_name is not UNSET:
            field_dict["hangupCauseName"] = hangup_cause_name
        if contact_ref is not UNSET:
            field_dict["contactRef"] = contact_ref
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if crm_contact_id is not UNSET:
            field_dict["crmContactId"] = crm_contact_id
        if has_recording is not UNSET:
            field_dict["hasRecording"] = has_recording
        if has_summary is not UNSET:
            field_dict["hasSummary"] = has_summary
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.partner_agent_dto import PartnerAgentDto # noqa: PLC0415
        d = dict(src_dict)
        _call_id = d.pop("callId", UNSET)
        call_id: UUID | Unset
        if isinstance(_call_id,  Unset):
            call_id = UNSET
        else:
            call_id = UUID(_call_id)




        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_direction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        direction = _parse_direction(d.pop("direction", UNSET))


        def _parse_from_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_ = _parse_from_(d.pop("from", UNSET))


        def _parse_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        to = _parse_to(d.pop("to", UNSET))


        _agent = d.pop("agent", UNSET)
        agent: PartnerAgentDto | Unset
        if isinstance(_agent,  Unset):
            agent = UNSET
        else:
            agent = PartnerAgentDto.from_dict(_agent)




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


        def _parse_duration_sec(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_sec = _parse_duration_sec(d.pop("durationSec", UNSET))


        def _parse_talk_sec(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        talk_sec = _parse_talk_sec(d.pop("talkSec", UNSET))


        def _parse_wait_sec(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        wait_sec = _parse_wait_sec(d.pop("waitSec", UNSET))


        def _parse_hangup_cause(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        hangup_cause = _parse_hangup_cause(d.pop("hangupCause", UNSET))


        def _parse_hangup_cause_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hangup_cause_name = _parse_hangup_cause_name(d.pop("hangupCauseName", UNSET))


        def _parse_contact_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_ref = _parse_contact_ref(d.pop("contactRef", UNSET))


        metadata = d.pop("metadata", UNSET)

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


        has_recording = d.pop("hasRecording", UNSET)

        has_summary = d.pop("hasSummary", UNSET)

        def _parse_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary = _parse_summary(d.pop("summary", UNSET))


        partner_call_dto = cls(
            call_id=call_id,
            status=status,
            direction=direction,
            from_=from_,
            to=to,
            agent=agent,
            queue_id=queue_id,
            queue_name=queue_name,
            started_at=started_at,
            answered_at=answered_at,
            ended_at=ended_at,
            duration_sec=duration_sec,
            talk_sec=talk_sec,
            wait_sec=wait_sec,
            hangup_cause=hangup_cause,
            hangup_cause_name=hangup_cause_name,
            contact_ref=contact_ref,
            metadata=metadata,
            crm_contact_id=crm_contact_id,
            has_recording=has_recording,
            has_summary=has_summary,
            summary=summary,
        )

        return partner_call_dto


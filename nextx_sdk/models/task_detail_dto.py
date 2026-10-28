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






T = TypeVar("T", bound="TaskDetailDto")



@_attrs_define
class TaskDetailDto:
    

    id: UUID | Unset = UNSET
    code: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    priority: None | str | Unset = UNSET
    start_date: datetime.date | None | Unset = UNSET
    due_date: datetime.date | None | Unset = UNSET
    assignee_id: None | Unset | UUID = UNSET
    assignee_name: None | str | Unset = UNSET
    contact_id: None | Unset | UUID = UNSET
    contact_name: None | str | Unset = UNSET
    contact_code: None | str | Unset = UNSET
    opportunity_id: None | Unset | UUID = UNSET
    opportunity_name: None | str | Unset = UNSET
    opportunity_code: None | str | Unset = UNSET
    ticket_id: None | Unset | UUID = UNSET
    ticket_subject: None | str | Unset = UNSET
    parent_task_id: None | Unset | UUID = UNSET
    parent_task_title: None | str | Unset = UNSET
    parent_task_code: None | str | Unset = UNSET
    progress: int | Unset = UNSET
    custom_fields: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    remind_at: datetime.datetime | None | Unset = UNSET
    reminder_sent_at: datetime.datetime | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        priority: None | str | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.date):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        due_date: None | str | Unset
        if isinstance(self.due_date, Unset):
            due_date = UNSET
        elif isinstance(self.due_date, datetime.date):
            due_date = self.due_date.isoformat()
        else:
            due_date = self.due_date

        assignee_id: None | str | Unset
        if isinstance(self.assignee_id, Unset):
            assignee_id = UNSET
        elif isinstance(self.assignee_id, UUID):
            assignee_id = str(self.assignee_id)
        else:
            assignee_id = self.assignee_id

        assignee_name: None | str | Unset
        if isinstance(self.assignee_name, Unset):
            assignee_name = UNSET
        else:
            assignee_name = self.assignee_name

        contact_id: None | str | Unset
        if isinstance(self.contact_id, Unset):
            contact_id = UNSET
        elif isinstance(self.contact_id, UUID):
            contact_id = str(self.contact_id)
        else:
            contact_id = self.contact_id

        contact_name: None | str | Unset
        if isinstance(self.contact_name, Unset):
            contact_name = UNSET
        else:
            contact_name = self.contact_name

        contact_code: None | str | Unset
        if isinstance(self.contact_code, Unset):
            contact_code = UNSET
        else:
            contact_code = self.contact_code

        opportunity_id: None | str | Unset
        if isinstance(self.opportunity_id, Unset):
            opportunity_id = UNSET
        elif isinstance(self.opportunity_id, UUID):
            opportunity_id = str(self.opportunity_id)
        else:
            opportunity_id = self.opportunity_id

        opportunity_name: None | str | Unset
        if isinstance(self.opportunity_name, Unset):
            opportunity_name = UNSET
        else:
            opportunity_name = self.opportunity_name

        opportunity_code: None | str | Unset
        if isinstance(self.opportunity_code, Unset):
            opportunity_code = UNSET
        else:
            opportunity_code = self.opportunity_code

        ticket_id: None | str | Unset
        if isinstance(self.ticket_id, Unset):
            ticket_id = UNSET
        elif isinstance(self.ticket_id, UUID):
            ticket_id = str(self.ticket_id)
        else:
            ticket_id = self.ticket_id

        ticket_subject: None | str | Unset
        if isinstance(self.ticket_subject, Unset):
            ticket_subject = UNSET
        else:
            ticket_subject = self.ticket_subject

        parent_task_id: None | str | Unset
        if isinstance(self.parent_task_id, Unset):
            parent_task_id = UNSET
        elif isinstance(self.parent_task_id, UUID):
            parent_task_id = str(self.parent_task_id)
        else:
            parent_task_id = self.parent_task_id

        parent_task_title: None | str | Unset
        if isinstance(self.parent_task_title, Unset):
            parent_task_title = UNSET
        else:
            parent_task_title = self.parent_task_title

        parent_task_code: None | str | Unset
        if isinstance(self.parent_task_code, Unset):
            parent_task_code = UNSET
        else:
            parent_task_code = self.parent_task_code

        progress = self.progress

        custom_fields: None | str | Unset
        if isinstance(self.custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = self.custom_fields

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        remind_at: None | str | Unset
        if isinstance(self.remind_at, Unset):
            remind_at = UNSET
        elif isinstance(self.remind_at, datetime.datetime):
            remind_at = self.remind_at.isoformat()
        else:
            remind_at = self.remind_at

        reminder_sent_at: None | str | Unset
        if isinstance(self.reminder_sent_at, Unset):
            reminder_sent_at = UNSET
        elif isinstance(self.reminder_sent_at, datetime.datetime):
            reminder_sent_at = self.reminder_sent_at.isoformat()
        else:
            reminder_sent_at = self.reminder_sent_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if code is not UNSET:
            field_dict["code"] = code
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status
        if priority is not UNSET:
            field_dict["priority"] = priority
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if assignee_id is not UNSET:
            field_dict["assigneeId"] = assignee_id
        if assignee_name is not UNSET:
            field_dict["assigneeName"] = assignee_name
        if contact_id is not UNSET:
            field_dict["contactId"] = contact_id
        if contact_name is not UNSET:
            field_dict["contactName"] = contact_name
        if contact_code is not UNSET:
            field_dict["contactCode"] = contact_code
        if opportunity_id is not UNSET:
            field_dict["opportunityId"] = opportunity_id
        if opportunity_name is not UNSET:
            field_dict["opportunityName"] = opportunity_name
        if opportunity_code is not UNSET:
            field_dict["opportunityCode"] = opportunity_code
        if ticket_id is not UNSET:
            field_dict["ticketId"] = ticket_id
        if ticket_subject is not UNSET:
            field_dict["ticketSubject"] = ticket_subject
        if parent_task_id is not UNSET:
            field_dict["parentTaskId"] = parent_task_id
        if parent_task_title is not UNSET:
            field_dict["parentTaskTitle"] = parent_task_title
        if parent_task_code is not UNSET:
            field_dict["parentTaskCode"] = parent_task_code
        if progress is not UNSET:
            field_dict["progress"] = progress
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if remind_at is not UNSET:
            field_dict["remindAt"] = remind_at
        if reminder_sent_at is not UNSET:
            field_dict["reminderSentAt"] = reminder_sent_at

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




        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_priority(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))


        def _parse_start_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = datetime.date.fromisoformat(data)



                return start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        start_date = _parse_start_date(d.pop("startDate", UNSET))


        def _parse_due_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_date_type_0 = datetime.date.fromisoformat(data)



                return due_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        due_date = _parse_due_date(d.pop("dueDate", UNSET))


        def _parse_assignee_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                assignee_id_type_0 = UUID(data)



                return assignee_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        assignee_id = _parse_assignee_id(d.pop("assigneeId", UNSET))


        def _parse_assignee_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assignee_name = _parse_assignee_name(d.pop("assigneeName", UNSET))


        def _parse_contact_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                contact_id_type_0 = UUID(data)



                return contact_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        contact_id = _parse_contact_id(d.pop("contactId", UNSET))


        def _parse_contact_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_name = _parse_contact_name(d.pop("contactName", UNSET))


        def _parse_contact_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_code = _parse_contact_code(d.pop("contactCode", UNSET))


        def _parse_opportunity_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                opportunity_id_type_0 = UUID(data)



                return opportunity_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        opportunity_id = _parse_opportunity_id(d.pop("opportunityId", UNSET))


        def _parse_opportunity_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opportunity_name = _parse_opportunity_name(d.pop("opportunityName", UNSET))


        def _parse_opportunity_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opportunity_code = _parse_opportunity_code(d.pop("opportunityCode", UNSET))


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


        def _parse_ticket_subject(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ticket_subject = _parse_ticket_subject(d.pop("ticketSubject", UNSET))


        def _parse_parent_task_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_task_id_type_0 = UUID(data)



                return parent_task_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_task_id = _parse_parent_task_id(d.pop("parentTaskId", UNSET))


        def _parse_parent_task_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_task_title = _parse_parent_task_title(d.pop("parentTaskTitle", UNSET))


        def _parse_parent_task_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_task_code = _parse_parent_task_code(d.pop("parentTaskCode", UNSET))


        progress = d.pop("progress", UNSET)

        def _parse_custom_fields(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_fields = _parse_custom_fields(d.pop("customFields", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)




        def _parse_remind_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                remind_at_type_0 = datetime.datetime.fromisoformat(data)



                return remind_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        remind_at = _parse_remind_at(d.pop("remindAt", UNSET))


        def _parse_reminder_sent_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reminder_sent_at_type_0 = datetime.datetime.fromisoformat(data)



                return reminder_sent_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        reminder_sent_at = _parse_reminder_sent_at(d.pop("reminderSentAt", UNSET))


        task_detail_dto = cls(
            id=id,
            code=code,
            title=title,
            description=description,
            status=status,
            priority=priority,
            start_date=start_date,
            due_date=due_date,
            assignee_id=assignee_id,
            assignee_name=assignee_name,
            contact_id=contact_id,
            contact_name=contact_name,
            contact_code=contact_code,
            opportunity_id=opportunity_id,
            opportunity_name=opportunity_name,
            opportunity_code=opportunity_code,
            ticket_id=ticket_id,
            ticket_subject=ticket_subject,
            parent_task_id=parent_task_id,
            parent_task_title=parent_task_title,
            parent_task_code=parent_task_code,
            progress=progress,
            custom_fields=custom_fields,
            created_at=created_at,
            updated_at=updated_at,
            remind_at=remind_at,
            reminder_sent_at=reminder_sent_at,
        )

        return task_detail_dto


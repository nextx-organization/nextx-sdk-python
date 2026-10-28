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
  from ..models.create_task_request_custom_fields_type_0 import CreateTaskRequestCustomFieldsType0





T = TypeVar("T", bound="CreateTaskRequest")



@_attrs_define
class CreateTaskRequest:
    

    title: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    priority: None | str | Unset = UNSET
    start_date: datetime.date | None | Unset = UNSET
    due_date: datetime.date | None | Unset = UNSET
    assignee_id: None | Unset | UUID = UNSET
    contact_id: None | Unset | UUID = UNSET
    opportunity_id: None | Unset | UUID = UNSET
    ticket_id: None | Unset | UUID = UNSET
    parent_task_id: None | Unset | UUID = UNSET
    custom_fields: CreateTaskRequestCustomFieldsType0 | None | Unset = UNSET
    remind_at: datetime.datetime | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_task_request_custom_fields_type_0 import CreateTaskRequestCustomFieldsType0 # noqa: PLC0415
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

        contact_id: None | str | Unset
        if isinstance(self.contact_id, Unset):
            contact_id = UNSET
        elif isinstance(self.contact_id, UUID):
            contact_id = str(self.contact_id)
        else:
            contact_id = self.contact_id

        opportunity_id: None | str | Unset
        if isinstance(self.opportunity_id, Unset):
            opportunity_id = UNSET
        elif isinstance(self.opportunity_id, UUID):
            opportunity_id = str(self.opportunity_id)
        else:
            opportunity_id = self.opportunity_id

        ticket_id: None | str | Unset
        if isinstance(self.ticket_id, Unset):
            ticket_id = UNSET
        elif isinstance(self.ticket_id, UUID):
            ticket_id = str(self.ticket_id)
        else:
            ticket_id = self.ticket_id

        parent_task_id: None | str | Unset
        if isinstance(self.parent_task_id, Unset):
            parent_task_id = UNSET
        elif isinstance(self.parent_task_id, UUID):
            parent_task_id = str(self.parent_task_id)
        else:
            parent_task_id = self.parent_task_id

        custom_fields: dict[str, Any] | None | Unset
        if isinstance(self.custom_fields, Unset):
            custom_fields = UNSET
        elif isinstance(self.custom_fields, CreateTaskRequestCustomFieldsType0):
            custom_fields = self.custom_fields.to_dict()
        else:
            custom_fields = self.custom_fields

        remind_at: None | str | Unset
        if isinstance(self.remind_at, Unset):
            remind_at = UNSET
        elif isinstance(self.remind_at, datetime.datetime):
            remind_at = self.remind_at.isoformat()
        else:
            remind_at = self.remind_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
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
        if contact_id is not UNSET:
            field_dict["contactId"] = contact_id
        if opportunity_id is not UNSET:
            field_dict["opportunityId"] = opportunity_id
        if ticket_id is not UNSET:
            field_dict["ticketId"] = ticket_id
        if parent_task_id is not UNSET:
            field_dict["parentTaskId"] = parent_task_id
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if remind_at is not UNSET:
            field_dict["remindAt"] = remind_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_task_request_custom_fields_type_0 import CreateTaskRequestCustomFieldsType0 # noqa: PLC0415
        d = dict(src_dict)
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


        def _parse_custom_fields(data: object) -> CreateTaskRequestCustomFieldsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_fields_type_0 = CreateTaskRequestCustomFieldsType0.from_dict(data)



                return custom_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateTaskRequestCustomFieldsType0 | None | Unset, data)

        custom_fields = _parse_custom_fields(d.pop("customFields", UNSET))


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


        create_task_request = cls(
            title=title,
            description=description,
            status=status,
            priority=priority,
            start_date=start_date,
            due_date=due_date,
            assignee_id=assignee_id,
            contact_id=contact_id,
            opportunity_id=opportunity_id,
            ticket_id=ticket_id,
            parent_task_id=parent_task_id,
            custom_fields=custom_fields,
            remind_at=remind_at,
        )

        return create_task_request


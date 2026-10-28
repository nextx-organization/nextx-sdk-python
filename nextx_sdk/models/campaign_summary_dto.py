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






T = TypeVar("T", bound="CampaignSummaryDto")



@_attrs_define
class CampaignSummaryDto:
    

    id: UUID | Unset = UNSET
    name: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    dialer_mode: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    caller_id: None | str | Unset = UNSET
    concurrent_calls: int | Unset = UNSET
    total_contacts: int | Unset = UNSET
    called_contacts: int | Unset = UNSET
    completed_contacts: int | Unset = UNSET
    pending_contacts: int | Unset = UNSET
    progress_percent: float | Unset = UNSET
    start_date: datetime.date | None | Unset = UNSET
    end_date: datetime.date | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        dialer_mode: None | str | Unset
        if isinstance(self.dialer_mode, Unset):
            dialer_mode = UNSET
        else:
            dialer_mode = self.dialer_mode

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        caller_id: None | str | Unset
        if isinstance(self.caller_id, Unset):
            caller_id = UNSET
        else:
            caller_id = self.caller_id

        concurrent_calls = self.concurrent_calls

        total_contacts = self.total_contacts

        called_contacts = self.called_contacts

        completed_contacts = self.completed_contacts

        pending_contacts = self.pending_contacts

        progress_percent = self.progress_percent

        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.date):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.date):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if dialer_mode is not UNSET:
            field_dict["dialerMode"] = dialer_mode
        if status is not UNSET:
            field_dict["status"] = status
        if caller_id is not UNSET:
            field_dict["callerId"] = caller_id
        if concurrent_calls is not UNSET:
            field_dict["concurrentCalls"] = concurrent_calls
        if total_contacts is not UNSET:
            field_dict["totalContacts"] = total_contacts
        if called_contacts is not UNSET:
            field_dict["calledContacts"] = called_contacts
        if completed_contacts is not UNSET:
            field_dict["completedContacts"] = completed_contacts
        if pending_contacts is not UNSET:
            field_dict["pendingContacts"] = pending_contacts
        if progress_percent is not UNSET:
            field_dict["progressPercent"] = progress_percent
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

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




        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))


        def _parse_dialer_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dialer_mode = _parse_dialer_mode(d.pop("dialerMode", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_caller_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        caller_id = _parse_caller_id(d.pop("callerId", UNSET))


        concurrent_calls = d.pop("concurrentCalls", UNSET)

        total_contacts = d.pop("totalContacts", UNSET)

        called_contacts = d.pop("calledContacts", UNSET)

        completed_contacts = d.pop("completedContacts", UNSET)

        pending_contacts = d.pop("pendingContacts", UNSET)

        progress_percent = d.pop("progressPercent", UNSET)

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


        def _parse_end_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = datetime.date.fromisoformat(data)



                return end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        end_date = _parse_end_date(d.pop("endDate", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        campaign_summary_dto = cls(
            id=id,
            name=name,
            type_=type_,
            dialer_mode=dialer_mode,
            status=status,
            caller_id=caller_id,
            concurrent_calls=concurrent_calls,
            total_contacts=total_contacts,
            called_contacts=called_contacts,
            completed_contacts=completed_contacts,
            pending_contacts=pending_contacts,
            progress_percent=progress_percent,
            start_date=start_date,
            end_date=end_date,
            created_at=created_at,
        )

        return campaign_summary_dto


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






T = TypeVar("T", bound="OpportunityChangeDto")



@_attrs_define
class OpportunityChangeDto:
    

    id: UUID | Unset = UNSET
    code: None | str | Unset = UNSET
    contact_id: None | Unset | UUID = UNSET
    pipeline_id: UUID | Unset = UNSET
    pipeline_stage_id: UUID | Unset = UNSET
    estimated_value: float | None | Unset = UNSET
    probability: int | None | Unset = UNSET
    expected_close_date: datetime.date | Unset = UNSET
    assignee_id: UUID | Unset = UNSET
    status: None | str | Unset = UNSET
    won_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    is_deleted: bool | Unset = UNSET
    deleted_at: datetime.datetime | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        contact_id: None | str | Unset
        if isinstance(self.contact_id, Unset):
            contact_id = UNSET
        elif isinstance(self.contact_id, UUID):
            contact_id = str(self.contact_id)
        else:
            contact_id = self.contact_id

        pipeline_id: str | Unset = UNSET
        if not isinstance(self.pipeline_id, Unset):
            pipeline_id = str(self.pipeline_id)

        pipeline_stage_id: str | Unset = UNSET
        if not isinstance(self.pipeline_stage_id, Unset):
            pipeline_stage_id = str(self.pipeline_stage_id)

        estimated_value: float | None | Unset
        if isinstance(self.estimated_value, Unset):
            estimated_value = UNSET
        else:
            estimated_value = self.estimated_value

        probability: int | None | Unset
        if isinstance(self.probability, Unset):
            probability = UNSET
        else:
            probability = self.probability

        expected_close_date: str | Unset = UNSET
        if not isinstance(self.expected_close_date, Unset):
            expected_close_date = self.expected_close_date.isoformat()

        assignee_id: str | Unset = UNSET
        if not isinstance(self.assignee_id, Unset):
            assignee_id = str(self.assignee_id)

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        won_at: None | str | Unset
        if isinstance(self.won_at, Unset):
            won_at = UNSET
        elif isinstance(self.won_at, datetime.datetime):
            won_at = self.won_at.isoformat()
        else:
            won_at = self.won_at

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        is_deleted = self.is_deleted

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        elif isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if code is not UNSET:
            field_dict["code"] = code
        if contact_id is not UNSET:
            field_dict["contactId"] = contact_id
        if pipeline_id is not UNSET:
            field_dict["pipelineId"] = pipeline_id
        if pipeline_stage_id is not UNSET:
            field_dict["pipelineStageId"] = pipeline_stage_id
        if estimated_value is not UNSET:
            field_dict["estimatedValue"] = estimated_value
        if probability is not UNSET:
            field_dict["probability"] = probability
        if expected_close_date is not UNSET:
            field_dict["expectedCloseDate"] = expected_close_date
        if assignee_id is not UNSET:
            field_dict["assigneeId"] = assignee_id
        if status is not UNSET:
            field_dict["status"] = status
        if won_at is not UNSET:
            field_dict["wonAt"] = won_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at

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


        _pipeline_id = d.pop("pipelineId", UNSET)
        pipeline_id: UUID | Unset
        if isinstance(_pipeline_id,  Unset):
            pipeline_id = UNSET
        else:
            pipeline_id = UUID(_pipeline_id)




        _pipeline_stage_id = d.pop("pipelineStageId", UNSET)
        pipeline_stage_id: UUID | Unset
        if isinstance(_pipeline_stage_id,  Unset):
            pipeline_stage_id = UNSET
        else:
            pipeline_stage_id = UUID(_pipeline_stage_id)




        def _parse_estimated_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        estimated_value = _parse_estimated_value(d.pop("estimatedValue", UNSET))


        def _parse_probability(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        probability = _parse_probability(d.pop("probability", UNSET))


        _expected_close_date = d.pop("expectedCloseDate", UNSET)
        expected_close_date: datetime.date | Unset
        if isinstance(_expected_close_date,  Unset):
            expected_close_date = UNSET
        else:
            expected_close_date = datetime.date.fromisoformat(_expected_close_date)




        _assignee_id = d.pop("assigneeId", UNSET)
        assignee_id: UUID | Unset
        if isinstance(_assignee_id,  Unset):
            assignee_id = UNSET
        else:
            assignee_id = UUID(_assignee_id)




        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_won_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                won_at_type_0 = datetime.datetime.fromisoformat(data)



                return won_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        won_at = _parse_won_at(d.pop("wonAt", UNSET))


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




        is_deleted = d.pop("isDeleted", UNSET)

        def _parse_deleted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_at_type_0 = datetime.datetime.fromisoformat(data)



                return deleted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        opportunity_change_dto = cls(
            id=id,
            code=code,
            contact_id=contact_id,
            pipeline_id=pipeline_id,
            pipeline_stage_id=pipeline_stage_id,
            estimated_value=estimated_value,
            probability=probability,
            expected_close_date=expected_close_date,
            assignee_id=assignee_id,
            status=status,
            won_at=won_at,
            created_at=created_at,
            updated_at=updated_at,
            is_deleted=is_deleted,
            deleted_at=deleted_at,
        )

        return opportunity_change_dto


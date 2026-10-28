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
  from ..models.opportunity_detail_dto_custom_fields_type_0 import OpportunityDetailDtoCustomFieldsType0





T = TypeVar("T", bound="OpportunityDetailDto")



@_attrs_define
class OpportunityDetailDto:
    

    id: UUID | Unset = UNSET
    code: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    contact_id: None | Unset | UUID = UNSET
    contact_name: None | str | Unset = UNSET
    lead_id: None | Unset | UUID = UNSET
    lead_name: None | str | Unset = UNSET
    pipeline_stage_id: UUID | Unset = UNSET
    pipeline_stage_name: None | str | Unset = UNSET
    pipeline_stage_color: None | str | Unset = UNSET
    estimated_value: float | None | Unset = UNSET
    probability: int | None | Unset = UNSET
    expected_close_date: datetime.date | Unset = UNSET
    assignee_id: UUID | Unset = UNSET
    assignee_name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    custom_fields: None | OpportunityDetailDtoCustomFieldsType0 | Unset = UNSET
    status: None | str | Unset = UNSET
    won_reason: None | str | Unset = UNSET
    lost_reason: None | str | Unset = UNSET
    lost_to_competitor: None | str | Unset = UNSET
    actual_value: float | None | Unset = UNSET
    actual_close_date: datetime.date | None | Unset = UNSET
    won_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    reopen_count: int | Unset = UNSET
    last_reopen_reason: None | str | Unset = UNSET
    reopened_at: datetime.datetime | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.opportunity_detail_dto_custom_fields_type_0 import OpportunityDetailDtoCustomFieldsType0 # noqa: PLC0415
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

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

        lead_id: None | str | Unset
        if isinstance(self.lead_id, Unset):
            lead_id = UNSET
        elif isinstance(self.lead_id, UUID):
            lead_id = str(self.lead_id)
        else:
            lead_id = self.lead_id

        lead_name: None | str | Unset
        if isinstance(self.lead_name, Unset):
            lead_name = UNSET
        else:
            lead_name = self.lead_name

        pipeline_stage_id: str | Unset = UNSET
        if not isinstance(self.pipeline_stage_id, Unset):
            pipeline_stage_id = str(self.pipeline_stage_id)

        pipeline_stage_name: None | str | Unset
        if isinstance(self.pipeline_stage_name, Unset):
            pipeline_stage_name = UNSET
        else:
            pipeline_stage_name = self.pipeline_stage_name

        pipeline_stage_color: None | str | Unset
        if isinstance(self.pipeline_stage_color, Unset):
            pipeline_stage_color = UNSET
        else:
            pipeline_stage_color = self.pipeline_stage_color

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

        assignee_name: None | str | Unset
        if isinstance(self.assignee_name, Unset):
            assignee_name = UNSET
        else:
            assignee_name = self.assignee_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        custom_fields: dict[str, Any] | None | Unset
        if isinstance(self.custom_fields, Unset):
            custom_fields = UNSET
        elif isinstance(self.custom_fields, OpportunityDetailDtoCustomFieldsType0):
            custom_fields = self.custom_fields.to_dict()
        else:
            custom_fields = self.custom_fields

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        won_reason: None | str | Unset
        if isinstance(self.won_reason, Unset):
            won_reason = UNSET
        else:
            won_reason = self.won_reason

        lost_reason: None | str | Unset
        if isinstance(self.lost_reason, Unset):
            lost_reason = UNSET
        else:
            lost_reason = self.lost_reason

        lost_to_competitor: None | str | Unset
        if isinstance(self.lost_to_competitor, Unset):
            lost_to_competitor = UNSET
        else:
            lost_to_competitor = self.lost_to_competitor

        actual_value: float | None | Unset
        if isinstance(self.actual_value, Unset):
            actual_value = UNSET
        else:
            actual_value = self.actual_value

        actual_close_date: None | str | Unset
        if isinstance(self.actual_close_date, Unset):
            actual_close_date = UNSET
        elif isinstance(self.actual_close_date, datetime.date):
            actual_close_date = self.actual_close_date.isoformat()
        else:
            actual_close_date = self.actual_close_date

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

        reopen_count = self.reopen_count

        last_reopen_reason: None | str | Unset
        if isinstance(self.last_reopen_reason, Unset):
            last_reopen_reason = UNSET
        else:
            last_reopen_reason = self.last_reopen_reason

        reopened_at: None | str | Unset
        if isinstance(self.reopened_at, Unset):
            reopened_at = UNSET
        elif isinstance(self.reopened_at, datetime.datetime):
            reopened_at = self.reopened_at.isoformat()
        else:
            reopened_at = self.reopened_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name
        if contact_id is not UNSET:
            field_dict["contactId"] = contact_id
        if contact_name is not UNSET:
            field_dict["contactName"] = contact_name
        if lead_id is not UNSET:
            field_dict["leadId"] = lead_id
        if lead_name is not UNSET:
            field_dict["leadName"] = lead_name
        if pipeline_stage_id is not UNSET:
            field_dict["pipelineStageId"] = pipeline_stage_id
        if pipeline_stage_name is not UNSET:
            field_dict["pipelineStageName"] = pipeline_stage_name
        if pipeline_stage_color is not UNSET:
            field_dict["pipelineStageColor"] = pipeline_stage_color
        if estimated_value is not UNSET:
            field_dict["estimatedValue"] = estimated_value
        if probability is not UNSET:
            field_dict["probability"] = probability
        if expected_close_date is not UNSET:
            field_dict["expectedCloseDate"] = expected_close_date
        if assignee_id is not UNSET:
            field_dict["assigneeId"] = assignee_id
        if assignee_name is not UNSET:
            field_dict["assigneeName"] = assignee_name
        if description is not UNSET:
            field_dict["description"] = description
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if status is not UNSET:
            field_dict["status"] = status
        if won_reason is not UNSET:
            field_dict["wonReason"] = won_reason
        if lost_reason is not UNSET:
            field_dict["lostReason"] = lost_reason
        if lost_to_competitor is not UNSET:
            field_dict["lostToCompetitor"] = lost_to_competitor
        if actual_value is not UNSET:
            field_dict["actualValue"] = actual_value
        if actual_close_date is not UNSET:
            field_dict["actualCloseDate"] = actual_close_date
        if won_at is not UNSET:
            field_dict["wonAt"] = won_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if reopen_count is not UNSET:
            field_dict["reopenCount"] = reopen_count
        if last_reopen_reason is not UNSET:
            field_dict["lastReopenReason"] = last_reopen_reason
        if reopened_at is not UNSET:
            field_dict["reopenedAt"] = reopened_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.opportunity_detail_dto_custom_fields_type_0 import OpportunityDetailDtoCustomFieldsType0 # noqa: PLC0415
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


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


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


        def _parse_lead_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                lead_id_type_0 = UUID(data)



                return lead_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        lead_id = _parse_lead_id(d.pop("leadId", UNSET))


        def _parse_lead_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lead_name = _parse_lead_name(d.pop("leadName", UNSET))


        _pipeline_stage_id = d.pop("pipelineStageId", UNSET)
        pipeline_stage_id: UUID | Unset
        if isinstance(_pipeline_stage_id,  Unset):
            pipeline_stage_id = UNSET
        else:
            pipeline_stage_id = UUID(_pipeline_stage_id)




        def _parse_pipeline_stage_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pipeline_stage_name = _parse_pipeline_stage_name(d.pop("pipelineStageName", UNSET))


        def _parse_pipeline_stage_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pipeline_stage_color = _parse_pipeline_stage_color(d.pop("pipelineStageColor", UNSET))


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




        def _parse_assignee_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assignee_name = _parse_assignee_name(d.pop("assigneeName", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_custom_fields(data: object) -> None | OpportunityDetailDtoCustomFieldsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_fields_type_0 = OpportunityDetailDtoCustomFieldsType0.from_dict(data)



                return custom_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OpportunityDetailDtoCustomFieldsType0 | Unset, data)

        custom_fields = _parse_custom_fields(d.pop("customFields", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_won_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        won_reason = _parse_won_reason(d.pop("wonReason", UNSET))


        def _parse_lost_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lost_reason = _parse_lost_reason(d.pop("lostReason", UNSET))


        def _parse_lost_to_competitor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lost_to_competitor = _parse_lost_to_competitor(d.pop("lostToCompetitor", UNSET))


        def _parse_actual_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        actual_value = _parse_actual_value(d.pop("actualValue", UNSET))


        def _parse_actual_close_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                actual_close_date_type_0 = datetime.date.fromisoformat(data)



                return actual_close_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        actual_close_date = _parse_actual_close_date(d.pop("actualCloseDate", UNSET))


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




        reopen_count = d.pop("reopenCount", UNSET)

        def _parse_last_reopen_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_reopen_reason = _parse_last_reopen_reason(d.pop("lastReopenReason", UNSET))


        def _parse_reopened_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reopened_at_type_0 = datetime.datetime.fromisoformat(data)



                return reopened_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        reopened_at = _parse_reopened_at(d.pop("reopenedAt", UNSET))


        opportunity_detail_dto = cls(
            id=id,
            code=code,
            name=name,
            contact_id=contact_id,
            contact_name=contact_name,
            lead_id=lead_id,
            lead_name=lead_name,
            pipeline_stage_id=pipeline_stage_id,
            pipeline_stage_name=pipeline_stage_name,
            pipeline_stage_color=pipeline_stage_color,
            estimated_value=estimated_value,
            probability=probability,
            expected_close_date=expected_close_date,
            assignee_id=assignee_id,
            assignee_name=assignee_name,
            description=description,
            custom_fields=custom_fields,
            status=status,
            won_reason=won_reason,
            lost_reason=lost_reason,
            lost_to_competitor=lost_to_competitor,
            actual_value=actual_value,
            actual_close_date=actual_close_date,
            won_at=won_at,
            created_at=created_at,
            updated_at=updated_at,
            reopen_count=reopen_count,
            last_reopen_reason=last_reopen_reason,
            reopened_at=reopened_at,
        )

        return opportunity_detail_dto


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
  from ..models.opportunity_tag_dto import OpportunityTagDto





T = TypeVar("T", bound="OpportunitySummaryDto")



@_attrs_define
class OpportunitySummaryDto:
    

    id: UUID | Unset = UNSET
    code: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    contact_id: None | Unset | UUID = UNSET
    contact_name: None | str | Unset = UNSET
    contact_company_name: None | str | Unset = UNSET
    pipeline_stage_id: UUID | Unset = UNSET
    pipeline_stage_name: None | str | Unset = UNSET
    pipeline_stage_color: None | str | Unset = UNSET
    estimated_value: float | None | Unset = UNSET
    probability: int | None | Unset = UNSET
    expected_close_date: datetime.date | Unset = UNSET
    assignee_id: UUID | Unset = UNSET
    assignee_name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    won_reason: None | str | Unset = UNSET
    lost_reason: None | str | Unset = UNSET
    lost_to_competitor: None | str | Unset = UNSET
    won_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    is_overdue: bool | Unset = UNSET
    days_overdue: int | None | Unset = UNSET
    quotation_count: int | Unset = UNSET
    contract_count: int | Unset = UNSET
    latest_comment_text: None | str | Unset = UNSET
    latest_comment_at: datetime.datetime | None | Unset = UNSET
    reopen_count: int | Unset = UNSET
    contact_phone: None | str | Unset = UNSET
    campaign_name: None | str | Unset = UNSET
    next_call_at: datetime.datetime | None | Unset = UNSET
    call_count: int | Unset = UNSET
    last_disposition: None | str | Unset = UNSET
    last_called_at: datetime.datetime | None | Unset = UNSET
    tags: list[OpportunityTagDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.opportunity_tag_dto import OpportunityTagDto # noqa: PLC0415
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

        contact_company_name: None | str | Unset
        if isinstance(self.contact_company_name, Unset):
            contact_company_name = UNSET
        else:
            contact_company_name = self.contact_company_name

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

        is_overdue = self.is_overdue

        days_overdue: int | None | Unset
        if isinstance(self.days_overdue, Unset):
            days_overdue = UNSET
        else:
            days_overdue = self.days_overdue

        quotation_count = self.quotation_count

        contract_count = self.contract_count

        latest_comment_text: None | str | Unset
        if isinstance(self.latest_comment_text, Unset):
            latest_comment_text = UNSET
        else:
            latest_comment_text = self.latest_comment_text

        latest_comment_at: None | str | Unset
        if isinstance(self.latest_comment_at, Unset):
            latest_comment_at = UNSET
        elif isinstance(self.latest_comment_at, datetime.datetime):
            latest_comment_at = self.latest_comment_at.isoformat()
        else:
            latest_comment_at = self.latest_comment_at

        reopen_count = self.reopen_count

        contact_phone: None | str | Unset
        if isinstance(self.contact_phone, Unset):
            contact_phone = UNSET
        else:
            contact_phone = self.contact_phone

        campaign_name: None | str | Unset
        if isinstance(self.campaign_name, Unset):
            campaign_name = UNSET
        else:
            campaign_name = self.campaign_name

        next_call_at: None | str | Unset
        if isinstance(self.next_call_at, Unset):
            next_call_at = UNSET
        elif isinstance(self.next_call_at, datetime.datetime):
            next_call_at = self.next_call_at.isoformat()
        else:
            next_call_at = self.next_call_at

        call_count = self.call_count

        last_disposition: None | str | Unset
        if isinstance(self.last_disposition, Unset):
            last_disposition = UNSET
        else:
            last_disposition = self.last_disposition

        last_called_at: None | str | Unset
        if isinstance(self.last_called_at, Unset):
            last_called_at = UNSET
        elif isinstance(self.last_called_at, datetime.datetime):
            last_called_at = self.last_called_at.isoformat()
        else:
            last_called_at = self.last_called_at

        tags: list[dict[str, Any]] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = []
            for tags_type_0_item_data in self.tags:
                tags_type_0_item = tags_type_0_item_data.to_dict()
                tags.append(tags_type_0_item)


        else:
            tags = self.tags


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
        if contact_company_name is not UNSET:
            field_dict["contactCompanyName"] = contact_company_name
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
        if status is not UNSET:
            field_dict["status"] = status
        if won_reason is not UNSET:
            field_dict["wonReason"] = won_reason
        if lost_reason is not UNSET:
            field_dict["lostReason"] = lost_reason
        if lost_to_competitor is not UNSET:
            field_dict["lostToCompetitor"] = lost_to_competitor
        if won_at is not UNSET:
            field_dict["wonAt"] = won_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if is_overdue is not UNSET:
            field_dict["isOverdue"] = is_overdue
        if days_overdue is not UNSET:
            field_dict["daysOverdue"] = days_overdue
        if quotation_count is not UNSET:
            field_dict["quotationCount"] = quotation_count
        if contract_count is not UNSET:
            field_dict["contractCount"] = contract_count
        if latest_comment_text is not UNSET:
            field_dict["latestCommentText"] = latest_comment_text
        if latest_comment_at is not UNSET:
            field_dict["latestCommentAt"] = latest_comment_at
        if reopen_count is not UNSET:
            field_dict["reopenCount"] = reopen_count
        if contact_phone is not UNSET:
            field_dict["contactPhone"] = contact_phone
        if campaign_name is not UNSET:
            field_dict["campaignName"] = campaign_name
        if next_call_at is not UNSET:
            field_dict["nextCallAt"] = next_call_at
        if call_count is not UNSET:
            field_dict["callCount"] = call_count
        if last_disposition is not UNSET:
            field_dict["lastDisposition"] = last_disposition
        if last_called_at is not UNSET:
            field_dict["lastCalledAt"] = last_called_at
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.opportunity_tag_dto import OpportunityTagDto # noqa: PLC0415
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


        def _parse_contact_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_company_name = _parse_contact_company_name(d.pop("contactCompanyName", UNSET))


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




        is_overdue = d.pop("isOverdue", UNSET)

        def _parse_days_overdue(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        days_overdue = _parse_days_overdue(d.pop("daysOverdue", UNSET))


        quotation_count = d.pop("quotationCount", UNSET)

        contract_count = d.pop("contractCount", UNSET)

        def _parse_latest_comment_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_comment_text = _parse_latest_comment_text(d.pop("latestCommentText", UNSET))


        def _parse_latest_comment_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                latest_comment_at_type_0 = datetime.datetime.fromisoformat(data)



                return latest_comment_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        latest_comment_at = _parse_latest_comment_at(d.pop("latestCommentAt", UNSET))


        reopen_count = d.pop("reopenCount", UNSET)

        def _parse_contact_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_phone = _parse_contact_phone(d.pop("contactPhone", UNSET))


        def _parse_campaign_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        campaign_name = _parse_campaign_name(d.pop("campaignName", UNSET))


        def _parse_next_call_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_call_at_type_0 = datetime.datetime.fromisoformat(data)



                return next_call_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_call_at = _parse_next_call_at(d.pop("nextCallAt", UNSET))


        call_count = d.pop("callCount", UNSET)

        def _parse_last_disposition(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_disposition = _parse_last_disposition(d.pop("lastDisposition", UNSET))


        def _parse_last_called_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_called_at_type_0 = datetime.datetime.fromisoformat(data)



                return last_called_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_called_at = _parse_last_called_at(d.pop("lastCalledAt", UNSET))


        def _parse_tags(data: object) -> list[OpportunityTagDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = []
                _tags_type_0 = data
                for tags_type_0_item_data in (_tags_type_0):
                    tags_type_0_item = OpportunityTagDto.from_dict(tags_type_0_item_data)



                    tags_type_0.append(tags_type_0_item)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OpportunityTagDto] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))


        opportunity_summary_dto = cls(
            id=id,
            code=code,
            name=name,
            contact_id=contact_id,
            contact_name=contact_name,
            contact_company_name=contact_company_name,
            pipeline_stage_id=pipeline_stage_id,
            pipeline_stage_name=pipeline_stage_name,
            pipeline_stage_color=pipeline_stage_color,
            estimated_value=estimated_value,
            probability=probability,
            expected_close_date=expected_close_date,
            assignee_id=assignee_id,
            assignee_name=assignee_name,
            description=description,
            status=status,
            won_reason=won_reason,
            lost_reason=lost_reason,
            lost_to_competitor=lost_to_competitor,
            won_at=won_at,
            created_at=created_at,
            is_overdue=is_overdue,
            days_overdue=days_overdue,
            quotation_count=quotation_count,
            contract_count=contract_count,
            latest_comment_text=latest_comment_text,
            latest_comment_at=latest_comment_at,
            reopen_count=reopen_count,
            contact_phone=contact_phone,
            campaign_name=campaign_name,
            next_call_at=next_call_at,
            call_count=call_count,
            last_disposition=last_disposition,
            last_called_at=last_called_at,
            tags=tags,
        )

        return opportunity_summary_dto


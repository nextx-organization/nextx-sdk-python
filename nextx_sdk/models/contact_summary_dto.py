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
  from ..models.contact_channel_origin_dto import ContactChannelOriginDto
  from ..models.contact_chat_summary_dto import ContactChatSummaryDto
  from ..models.contact_summary_dto_custom_fields_type_0 import ContactSummaryDtoCustomFieldsType0
  from ..models.tag_dto import TagDto





T = TypeVar("T", bound="ContactSummaryDto")



@_attrs_define
class ContactSummaryDto:
    

    id: UUID | Unset = UNSET
    code: None | str | Unset = UNSET
    contact_type: None | str | Unset = UNSET
    full_name: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    job_title: None | str | Unset = UNSET
    company_name: None | str | Unset = UNSET
    avatar_url: None | str | Unset = UNSET
    tier: None | str | Unset = UNSET
    has_customer_profile: bool | Unset = UNSET
    tags: list[TagDto] | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    lifecycle_stage: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    ward: None | str | Unset = UNSET
    assignee_name: None | str | Unset = UNSET
    assignee_id: None | Unset | UUID = UNSET
    pipeline_stage_name: None | str | Unset = UNSET
    pipeline_stage_color: None | str | Unset = UNSET
    order_count: int | Unset = UNSET
    deal_count: int | Unset = UNSET
    top_deal_value: float | None | Unset = UNSET
    top_deal_stage: None | str | Unset = UNSET
    top_deal_stage_color: None | str | Unset = UNSET
    top_deal_close_date: datetime.date | None | Unset = UNSET
    top_deal_id: None | Unset | UUID = UNSET
    province_code: None | str | Unset = UNSET
    customer_status: None | str | Unset = UNSET
    group_name: None | str | Unset = UNSET
    last_activity_at: datetime.datetime | None | Unset = UNSET
    group_icon: None | str | Unset = UNSET
    group_color: None | str | Unset = UNSET
    status_label: None | str | Unset = UNSET
    status_icon: None | str | Unset = UNSET
    status_color: None | str | Unset = UNSET
    custom_fields: ContactSummaryDtoCustomFieldsType0 | None | Unset = UNSET
    source_id: None | Unset | UUID = UNSET
    assigned_at: datetime.datetime | None | Unset = UNSET
    lead_score: int | Unset = UNSET
    lead_tier: None | str | Unset = UNSET
    latest_comment_text: None | str | Unset = UNSET
    latest_comment_at: datetime.datetime | None | Unset = UNSET
    notes: None | str | Unset = UNSET
    source_name: None | str | Unset = UNSET
    phone2: None | str | Unset = UNSET
    phone3: None | str | Unset = UNSET
    dob: datetime.date | None | Unset = UNSET
    channel_origin: ContactChannelOriginDto | Unset = UNSET
    chat_summary: ContactChatSummaryDto | Unset = UNSET
    next_activity_at: datetime.datetime | None | Unset = UNSET
    next_activity_kind: None | str | Unset = UNSET
    next_activity_title: None | str | Unset = UNSET
    contact_status_id: None | Unset | UUID = UNSET
    branch_id: None | Unset | UUID = UNSET
    branch_name: None | str | Unset = UNSET
    sla_stage: int | Unset = UNSET
    sla_contacted_at: datetime.datetime | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.contact_channel_origin_dto import ContactChannelOriginDto # noqa: PLC0415
        from ..models.contact_chat_summary_dto import ContactChatSummaryDto # noqa: PLC0415
        from ..models.contact_summary_dto_custom_fields_type_0 import ContactSummaryDtoCustomFieldsType0 # noqa: PLC0415
        from ..models.tag_dto import TagDto # noqa: PLC0415
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        contact_type: None | str | Unset
        if isinstance(self.contact_type, Unset):
            contact_type = UNSET
        else:
            contact_type = self.contact_type

        full_name: None | str | Unset
        if isinstance(self.full_name, Unset):
            full_name = UNSET
        else:
            full_name = self.full_name

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        job_title: None | str | Unset
        if isinstance(self.job_title, Unset):
            job_title = UNSET
        else:
            job_title = self.job_title

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        tier: None | str | Unset
        if isinstance(self.tier, Unset):
            tier = UNSET
        else:
            tier = self.tier

        has_customer_profile = self.has_customer_profile

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

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        lifecycle_stage: None | str | Unset
        if isinstance(self.lifecycle_stage, Unset):
            lifecycle_stage = UNSET
        else:
            lifecycle_stage = self.lifecycle_stage

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        ward: None | str | Unset
        if isinstance(self.ward, Unset):
            ward = UNSET
        else:
            ward = self.ward

        assignee_name: None | str | Unset
        if isinstance(self.assignee_name, Unset):
            assignee_name = UNSET
        else:
            assignee_name = self.assignee_name

        assignee_id: None | str | Unset
        if isinstance(self.assignee_id, Unset):
            assignee_id = UNSET
        elif isinstance(self.assignee_id, UUID):
            assignee_id = str(self.assignee_id)
        else:
            assignee_id = self.assignee_id

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

        order_count = self.order_count

        deal_count = self.deal_count

        top_deal_value: float | None | Unset
        if isinstance(self.top_deal_value, Unset):
            top_deal_value = UNSET
        else:
            top_deal_value = self.top_deal_value

        top_deal_stage: None | str | Unset
        if isinstance(self.top_deal_stage, Unset):
            top_deal_stage = UNSET
        else:
            top_deal_stage = self.top_deal_stage

        top_deal_stage_color: None | str | Unset
        if isinstance(self.top_deal_stage_color, Unset):
            top_deal_stage_color = UNSET
        else:
            top_deal_stage_color = self.top_deal_stage_color

        top_deal_close_date: None | str | Unset
        if isinstance(self.top_deal_close_date, Unset):
            top_deal_close_date = UNSET
        elif isinstance(self.top_deal_close_date, datetime.date):
            top_deal_close_date = self.top_deal_close_date.isoformat()
        else:
            top_deal_close_date = self.top_deal_close_date

        top_deal_id: None | str | Unset
        if isinstance(self.top_deal_id, Unset):
            top_deal_id = UNSET
        elif isinstance(self.top_deal_id, UUID):
            top_deal_id = str(self.top_deal_id)
        else:
            top_deal_id = self.top_deal_id

        province_code: None | str | Unset
        if isinstance(self.province_code, Unset):
            province_code = UNSET
        else:
            province_code = self.province_code

        customer_status: None | str | Unset
        if isinstance(self.customer_status, Unset):
            customer_status = UNSET
        else:
            customer_status = self.customer_status

        group_name: None | str | Unset
        if isinstance(self.group_name, Unset):
            group_name = UNSET
        else:
            group_name = self.group_name

        last_activity_at: None | str | Unset
        if isinstance(self.last_activity_at, Unset):
            last_activity_at = UNSET
        elif isinstance(self.last_activity_at, datetime.datetime):
            last_activity_at = self.last_activity_at.isoformat()
        else:
            last_activity_at = self.last_activity_at

        group_icon: None | str | Unset
        if isinstance(self.group_icon, Unset):
            group_icon = UNSET
        else:
            group_icon = self.group_icon

        group_color: None | str | Unset
        if isinstance(self.group_color, Unset):
            group_color = UNSET
        else:
            group_color = self.group_color

        status_label: None | str | Unset
        if isinstance(self.status_label, Unset):
            status_label = UNSET
        else:
            status_label = self.status_label

        status_icon: None | str | Unset
        if isinstance(self.status_icon, Unset):
            status_icon = UNSET
        else:
            status_icon = self.status_icon

        status_color: None | str | Unset
        if isinstance(self.status_color, Unset):
            status_color = UNSET
        else:
            status_color = self.status_color

        custom_fields: dict[str, Any] | None | Unset
        if isinstance(self.custom_fields, Unset):
            custom_fields = UNSET
        elif isinstance(self.custom_fields, ContactSummaryDtoCustomFieldsType0):
            custom_fields = self.custom_fields.to_dict()
        else:
            custom_fields = self.custom_fields

        source_id: None | str | Unset
        if isinstance(self.source_id, Unset):
            source_id = UNSET
        elif isinstance(self.source_id, UUID):
            source_id = str(self.source_id)
        else:
            source_id = self.source_id

        assigned_at: None | str | Unset
        if isinstance(self.assigned_at, Unset):
            assigned_at = UNSET
        elif isinstance(self.assigned_at, datetime.datetime):
            assigned_at = self.assigned_at.isoformat()
        else:
            assigned_at = self.assigned_at

        lead_score = self.lead_score

        lead_tier: None | str | Unset
        if isinstance(self.lead_tier, Unset):
            lead_tier = UNSET
        else:
            lead_tier = self.lead_tier

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

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        source_name: None | str | Unset
        if isinstance(self.source_name, Unset):
            source_name = UNSET
        else:
            source_name = self.source_name

        phone2: None | str | Unset
        if isinstance(self.phone2, Unset):
            phone2 = UNSET
        else:
            phone2 = self.phone2

        phone3: None | str | Unset
        if isinstance(self.phone3, Unset):
            phone3 = UNSET
        else:
            phone3 = self.phone3

        dob: None | str | Unset
        if isinstance(self.dob, Unset):
            dob = UNSET
        elif isinstance(self.dob, datetime.date):
            dob = self.dob.isoformat()
        else:
            dob = self.dob

        channel_origin: dict[str, Any] | Unset = UNSET
        if not isinstance(self.channel_origin, Unset):
            channel_origin = self.channel_origin.to_dict()

        chat_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.chat_summary, Unset):
            chat_summary = self.chat_summary.to_dict()

        next_activity_at: None | str | Unset
        if isinstance(self.next_activity_at, Unset):
            next_activity_at = UNSET
        elif isinstance(self.next_activity_at, datetime.datetime):
            next_activity_at = self.next_activity_at.isoformat()
        else:
            next_activity_at = self.next_activity_at

        next_activity_kind: None | str | Unset
        if isinstance(self.next_activity_kind, Unset):
            next_activity_kind = UNSET
        else:
            next_activity_kind = self.next_activity_kind

        next_activity_title: None | str | Unset
        if isinstance(self.next_activity_title, Unset):
            next_activity_title = UNSET
        else:
            next_activity_title = self.next_activity_title

        contact_status_id: None | str | Unset
        if isinstance(self.contact_status_id, Unset):
            contact_status_id = UNSET
        elif isinstance(self.contact_status_id, UUID):
            contact_status_id = str(self.contact_status_id)
        else:
            contact_status_id = self.contact_status_id

        branch_id: None | str | Unset
        if isinstance(self.branch_id, Unset):
            branch_id = UNSET
        elif isinstance(self.branch_id, UUID):
            branch_id = str(self.branch_id)
        else:
            branch_id = self.branch_id

        branch_name: None | str | Unset
        if isinstance(self.branch_name, Unset):
            branch_name = UNSET
        else:
            branch_name = self.branch_name

        sla_stage = self.sla_stage

        sla_contacted_at: None | str | Unset
        if isinstance(self.sla_contacted_at, Unset):
            sla_contacted_at = UNSET
        elif isinstance(self.sla_contacted_at, datetime.datetime):
            sla_contacted_at = self.sla_contacted_at.isoformat()
        else:
            sla_contacted_at = self.sla_contacted_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if code is not UNSET:
            field_dict["code"] = code
        if contact_type is not UNSET:
            field_dict["contactType"] = contact_type
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if job_title is not UNSET:
            field_dict["jobTitle"] = job_title
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if tier is not UNSET:
            field_dict["tier"] = tier
        if has_customer_profile is not UNSET:
            field_dict["hasCustomerProfile"] = has_customer_profile
        if tags is not UNSET:
            field_dict["tags"] = tags
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if lifecycle_stage is not UNSET:
            field_dict["lifecycleStage"] = lifecycle_stage
        if address is not UNSET:
            field_dict["address"] = address
        if city is not UNSET:
            field_dict["city"] = city
        if ward is not UNSET:
            field_dict["ward"] = ward
        if assignee_name is not UNSET:
            field_dict["assigneeName"] = assignee_name
        if assignee_id is not UNSET:
            field_dict["assigneeId"] = assignee_id
        if pipeline_stage_name is not UNSET:
            field_dict["pipelineStageName"] = pipeline_stage_name
        if pipeline_stage_color is not UNSET:
            field_dict["pipelineStageColor"] = pipeline_stage_color
        if order_count is not UNSET:
            field_dict["orderCount"] = order_count
        if deal_count is not UNSET:
            field_dict["dealCount"] = deal_count
        if top_deal_value is not UNSET:
            field_dict["topDealValue"] = top_deal_value
        if top_deal_stage is not UNSET:
            field_dict["topDealStage"] = top_deal_stage
        if top_deal_stage_color is not UNSET:
            field_dict["topDealStageColor"] = top_deal_stage_color
        if top_deal_close_date is not UNSET:
            field_dict["topDealCloseDate"] = top_deal_close_date
        if top_deal_id is not UNSET:
            field_dict["topDealId"] = top_deal_id
        if province_code is not UNSET:
            field_dict["provinceCode"] = province_code
        if customer_status is not UNSET:
            field_dict["customerStatus"] = customer_status
        if group_name is not UNSET:
            field_dict["groupName"] = group_name
        if last_activity_at is not UNSET:
            field_dict["lastActivityAt"] = last_activity_at
        if group_icon is not UNSET:
            field_dict["groupIcon"] = group_icon
        if group_color is not UNSET:
            field_dict["groupColor"] = group_color
        if status_label is not UNSET:
            field_dict["statusLabel"] = status_label
        if status_icon is not UNSET:
            field_dict["statusIcon"] = status_icon
        if status_color is not UNSET:
            field_dict["statusColor"] = status_color
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if source_id is not UNSET:
            field_dict["sourceId"] = source_id
        if assigned_at is not UNSET:
            field_dict["assignedAt"] = assigned_at
        if lead_score is not UNSET:
            field_dict["leadScore"] = lead_score
        if lead_tier is not UNSET:
            field_dict["leadTier"] = lead_tier
        if latest_comment_text is not UNSET:
            field_dict["latestCommentText"] = latest_comment_text
        if latest_comment_at is not UNSET:
            field_dict["latestCommentAt"] = latest_comment_at
        if notes is not UNSET:
            field_dict["notes"] = notes
        if source_name is not UNSET:
            field_dict["sourceName"] = source_name
        if phone2 is not UNSET:
            field_dict["phone2"] = phone2
        if phone3 is not UNSET:
            field_dict["phone3"] = phone3
        if dob is not UNSET:
            field_dict["dob"] = dob
        if channel_origin is not UNSET:
            field_dict["channelOrigin"] = channel_origin
        if chat_summary is not UNSET:
            field_dict["chatSummary"] = chat_summary
        if next_activity_at is not UNSET:
            field_dict["nextActivityAt"] = next_activity_at
        if next_activity_kind is not UNSET:
            field_dict["nextActivityKind"] = next_activity_kind
        if next_activity_title is not UNSET:
            field_dict["nextActivityTitle"] = next_activity_title
        if contact_status_id is not UNSET:
            field_dict["contactStatusId"] = contact_status_id
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id
        if branch_name is not UNSET:
            field_dict["branchName"] = branch_name
        if sla_stage is not UNSET:
            field_dict["slaStage"] = sla_stage
        if sla_contacted_at is not UNSET:
            field_dict["slaContactedAt"] = sla_contacted_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_channel_origin_dto import ContactChannelOriginDto # noqa: PLC0415
        from ..models.contact_chat_summary_dto import ContactChatSummaryDto # noqa: PLC0415
        from ..models.contact_summary_dto_custom_fields_type_0 import ContactSummaryDtoCustomFieldsType0 # noqa: PLC0415
        from ..models.tag_dto import TagDto # noqa: PLC0415
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


        def _parse_contact_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_type = _parse_contact_type(d.pop("contactType", UNSET))


        def _parse_full_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        full_name = _parse_full_name(d.pop("fullName", UNSET))


        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))


        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))


        def _parse_job_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_title = _parse_job_title(d.pop("jobTitle", UNSET))


        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("companyName", UNSET))


        def _parse_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url = _parse_avatar_url(d.pop("avatarUrl", UNSET))


        def _parse_tier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tier = _parse_tier(d.pop("tier", UNSET))


        has_customer_profile = d.pop("hasCustomerProfile", UNSET)

        def _parse_tags(data: object) -> list[TagDto] | None | Unset:
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
                    tags_type_0_item = TagDto.from_dict(tags_type_0_item_data)



                    tags_type_0.append(tags_type_0_item)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TagDto] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_lifecycle_stage(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lifecycle_stage = _parse_lifecycle_stage(d.pop("lifecycleStage", UNSET))


        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))


        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))


        def _parse_ward(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ward = _parse_ward(d.pop("ward", UNSET))


        def _parse_assignee_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assignee_name = _parse_assignee_name(d.pop("assigneeName", UNSET))


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


        order_count = d.pop("orderCount", UNSET)

        deal_count = d.pop("dealCount", UNSET)

        def _parse_top_deal_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        top_deal_value = _parse_top_deal_value(d.pop("topDealValue", UNSET))


        def _parse_top_deal_stage(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        top_deal_stage = _parse_top_deal_stage(d.pop("topDealStage", UNSET))


        def _parse_top_deal_stage_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        top_deal_stage_color = _parse_top_deal_stage_color(d.pop("topDealStageColor", UNSET))


        def _parse_top_deal_close_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                top_deal_close_date_type_0 = datetime.date.fromisoformat(data)



                return top_deal_close_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        top_deal_close_date = _parse_top_deal_close_date(d.pop("topDealCloseDate", UNSET))


        def _parse_top_deal_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                top_deal_id_type_0 = UUID(data)



                return top_deal_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        top_deal_id = _parse_top_deal_id(d.pop("topDealId", UNSET))


        def _parse_province_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        province_code = _parse_province_code(d.pop("provinceCode", UNSET))


        def _parse_customer_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_status = _parse_customer_status(d.pop("customerStatus", UNSET))


        def _parse_group_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_name = _parse_group_name(d.pop("groupName", UNSET))


        def _parse_last_activity_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_activity_at_type_0 = datetime.datetime.fromisoformat(data)



                return last_activity_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_activity_at = _parse_last_activity_at(d.pop("lastActivityAt", UNSET))


        def _parse_group_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_icon = _parse_group_icon(d.pop("groupIcon", UNSET))


        def _parse_group_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_color = _parse_group_color(d.pop("groupColor", UNSET))


        def _parse_status_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_label = _parse_status_label(d.pop("statusLabel", UNSET))


        def _parse_status_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_icon = _parse_status_icon(d.pop("statusIcon", UNSET))


        def _parse_status_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_color = _parse_status_color(d.pop("statusColor", UNSET))


        def _parse_custom_fields(data: object) -> ContactSummaryDtoCustomFieldsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_fields_type_0 = ContactSummaryDtoCustomFieldsType0.from_dict(data)



                return custom_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ContactSummaryDtoCustomFieldsType0 | None | Unset, data)

        custom_fields = _parse_custom_fields(d.pop("customFields", UNSET))


        def _parse_source_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_id_type_0 = UUID(data)



                return source_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        source_id = _parse_source_id(d.pop("sourceId", UNSET))


        def _parse_assigned_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                assigned_at_type_0 = datetime.datetime.fromisoformat(data)



                return assigned_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        assigned_at = _parse_assigned_at(d.pop("assignedAt", UNSET))


        lead_score = d.pop("leadScore", UNSET)

        def _parse_lead_tier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lead_tier = _parse_lead_tier(d.pop("leadTier", UNSET))


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


        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


        def _parse_source_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_name = _parse_source_name(d.pop("sourceName", UNSET))


        def _parse_phone2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone2 = _parse_phone2(d.pop("phone2", UNSET))


        def _parse_phone3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone3 = _parse_phone3(d.pop("phone3", UNSET))


        def _parse_dob(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dob_type_0 = datetime.date.fromisoformat(data)



                return dob_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        dob = _parse_dob(d.pop("dob", UNSET))


        _channel_origin = d.pop("channelOrigin", UNSET)
        channel_origin: ContactChannelOriginDto | Unset
        if isinstance(_channel_origin,  Unset):
            channel_origin = UNSET
        else:
            channel_origin = ContactChannelOriginDto.from_dict(_channel_origin)




        _chat_summary = d.pop("chatSummary", UNSET)
        chat_summary: ContactChatSummaryDto | Unset
        if isinstance(_chat_summary,  Unset):
            chat_summary = UNSET
        else:
            chat_summary = ContactChatSummaryDto.from_dict(_chat_summary)




        def _parse_next_activity_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_activity_at_type_0 = datetime.datetime.fromisoformat(data)



                return next_activity_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_activity_at = _parse_next_activity_at(d.pop("nextActivityAt", UNSET))


        def _parse_next_activity_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_activity_kind = _parse_next_activity_kind(d.pop("nextActivityKind", UNSET))


        def _parse_next_activity_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_activity_title = _parse_next_activity_title(d.pop("nextActivityTitle", UNSET))


        def _parse_contact_status_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                contact_status_id_type_0 = UUID(data)



                return contact_status_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        contact_status_id = _parse_contact_status_id(d.pop("contactStatusId", UNSET))


        def _parse_branch_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                branch_id_type_0 = UUID(data)



                return branch_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        branch_id = _parse_branch_id(d.pop("branchId", UNSET))


        def _parse_branch_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch_name = _parse_branch_name(d.pop("branchName", UNSET))


        sla_stage = d.pop("slaStage", UNSET)

        def _parse_sla_contacted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sla_contacted_at_type_0 = datetime.datetime.fromisoformat(data)



                return sla_contacted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        sla_contacted_at = _parse_sla_contacted_at(d.pop("slaContactedAt", UNSET))


        contact_summary_dto = cls(
            id=id,
            code=code,
            contact_type=contact_type,
            full_name=full_name,
            email=email,
            phone=phone,
            job_title=job_title,
            company_name=company_name,
            avatar_url=avatar_url,
            tier=tier,
            has_customer_profile=has_customer_profile,
            tags=tags,
            created_at=created_at,
            lifecycle_stage=lifecycle_stage,
            address=address,
            city=city,
            ward=ward,
            assignee_name=assignee_name,
            assignee_id=assignee_id,
            pipeline_stage_name=pipeline_stage_name,
            pipeline_stage_color=pipeline_stage_color,
            order_count=order_count,
            deal_count=deal_count,
            top_deal_value=top_deal_value,
            top_deal_stage=top_deal_stage,
            top_deal_stage_color=top_deal_stage_color,
            top_deal_close_date=top_deal_close_date,
            top_deal_id=top_deal_id,
            province_code=province_code,
            customer_status=customer_status,
            group_name=group_name,
            last_activity_at=last_activity_at,
            group_icon=group_icon,
            group_color=group_color,
            status_label=status_label,
            status_icon=status_icon,
            status_color=status_color,
            custom_fields=custom_fields,
            source_id=source_id,
            assigned_at=assigned_at,
            lead_score=lead_score,
            lead_tier=lead_tier,
            latest_comment_text=latest_comment_text,
            latest_comment_at=latest_comment_at,
            notes=notes,
            source_name=source_name,
            phone2=phone2,
            phone3=phone3,
            dob=dob,
            channel_origin=channel_origin,
            chat_summary=chat_summary,
            next_activity_at=next_activity_at,
            next_activity_kind=next_activity_kind,
            next_activity_title=next_activity_title,
            contact_status_id=contact_status_id,
            branch_id=branch_id,
            branch_name=branch_name,
            sla_stage=sla_stage,
            sla_contacted_at=sla_contacted_at,
        )

        return contact_summary_dto


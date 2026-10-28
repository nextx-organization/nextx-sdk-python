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
  from ..models.audience_filter_dto import AudienceFilterDto
  from ..models.email_campaign_dto_merge_tags_type_0 import EmailCampaignDtoMergeTagsType0
  from ..models.sender_profile_summary_dto import SenderProfileSummaryDto





T = TypeVar("T", bound="EmailCampaignDto")



@_attrs_define
class EmailCampaignDto:
    

    id: UUID | Unset = UNSET
    name: None | str | Unset = UNSET
    subject: None | str | Unset = UNSET
    preview_text: None | str | Unset = UNSET
    sender_profile: SenderProfileSummaryDto | Unset = UNSET
    template_id: None | Unset | UUID = UNSET
    audience_filter: AudienceFilterDto | Unset = UNSET
    ab_test_enabled: bool | Unset = UNSET
    ab_subject_variant: None | str | Unset = UNSET
    ab_split_pct: int | None | Unset = UNSET
    status: None | str | Unset = UNSET
    recipient_count: int | None | Unset = UNSET
    scheduled_at: datetime.datetime | None | Unset = UNSET
    sent_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    merge_tags: EmailCampaignDtoMergeTagsType0 | None | Unset = UNSET
    optimize_send_time: bool | Unset = UNSET
    sent: int | Unset = UNSET
    delivered: int | Unset = UNSET
    opens_unique: int | Unset = UNSET
    clicks_unique: int | Unset = UNSET
    exclude_recent_days: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.audience_filter_dto import AudienceFilterDto # noqa: PLC0415
        from ..models.email_campaign_dto_merge_tags_type_0 import EmailCampaignDtoMergeTagsType0 # noqa: PLC0415
        from ..models.sender_profile_summary_dto import SenderProfileSummaryDto # noqa: PLC0415
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        subject: None | str | Unset
        if isinstance(self.subject, Unset):
            subject = UNSET
        else:
            subject = self.subject

        preview_text: None | str | Unset
        if isinstance(self.preview_text, Unset):
            preview_text = UNSET
        else:
            preview_text = self.preview_text

        sender_profile: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sender_profile, Unset):
            sender_profile = self.sender_profile.to_dict()

        template_id: None | str | Unset
        if isinstance(self.template_id, Unset):
            template_id = UNSET
        elif isinstance(self.template_id, UUID):
            template_id = str(self.template_id)
        else:
            template_id = self.template_id

        audience_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.audience_filter, Unset):
            audience_filter = self.audience_filter.to_dict()

        ab_test_enabled = self.ab_test_enabled

        ab_subject_variant: None | str | Unset
        if isinstance(self.ab_subject_variant, Unset):
            ab_subject_variant = UNSET
        else:
            ab_subject_variant = self.ab_subject_variant

        ab_split_pct: int | None | Unset
        if isinstance(self.ab_split_pct, Unset):
            ab_split_pct = UNSET
        else:
            ab_split_pct = self.ab_split_pct

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        recipient_count: int | None | Unset
        if isinstance(self.recipient_count, Unset):
            recipient_count = UNSET
        else:
            recipient_count = self.recipient_count

        scheduled_at: None | str | Unset
        if isinstance(self.scheduled_at, Unset):
            scheduled_at = UNSET
        elif isinstance(self.scheduled_at, datetime.datetime):
            scheduled_at = self.scheduled_at.isoformat()
        else:
            scheduled_at = self.scheduled_at

        sent_at: None | str | Unset
        if isinstance(self.sent_at, Unset):
            sent_at = UNSET
        elif isinstance(self.sent_at, datetime.datetime):
            sent_at = self.sent_at.isoformat()
        else:
            sent_at = self.sent_at

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        merge_tags: dict[str, Any] | None | Unset
        if isinstance(self.merge_tags, Unset):
            merge_tags = UNSET
        elif isinstance(self.merge_tags, EmailCampaignDtoMergeTagsType0):
            merge_tags = self.merge_tags.to_dict()
        else:
            merge_tags = self.merge_tags

        optimize_send_time = self.optimize_send_time

        sent = self.sent

        delivered = self.delivered

        opens_unique = self.opens_unique

        clicks_unique = self.clicks_unique

        exclude_recent_days: int | None | Unset
        if isinstance(self.exclude_recent_days, Unset):
            exclude_recent_days = UNSET
        else:
            exclude_recent_days = self.exclude_recent_days


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if subject is not UNSET:
            field_dict["subject"] = subject
        if preview_text is not UNSET:
            field_dict["previewText"] = preview_text
        if sender_profile is not UNSET:
            field_dict["senderProfile"] = sender_profile
        if template_id is not UNSET:
            field_dict["templateId"] = template_id
        if audience_filter is not UNSET:
            field_dict["audienceFilter"] = audience_filter
        if ab_test_enabled is not UNSET:
            field_dict["abTestEnabled"] = ab_test_enabled
        if ab_subject_variant is not UNSET:
            field_dict["abSubjectVariant"] = ab_subject_variant
        if ab_split_pct is not UNSET:
            field_dict["abSplitPct"] = ab_split_pct
        if status is not UNSET:
            field_dict["status"] = status
        if recipient_count is not UNSET:
            field_dict["recipientCount"] = recipient_count
        if scheduled_at is not UNSET:
            field_dict["scheduledAt"] = scheduled_at
        if sent_at is not UNSET:
            field_dict["sentAt"] = sent_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if merge_tags is not UNSET:
            field_dict["mergeTags"] = merge_tags
        if optimize_send_time is not UNSET:
            field_dict["optimizeSendTime"] = optimize_send_time
        if sent is not UNSET:
            field_dict["sent"] = sent
        if delivered is not UNSET:
            field_dict["delivered"] = delivered
        if opens_unique is not UNSET:
            field_dict["opensUnique"] = opens_unique
        if clicks_unique is not UNSET:
            field_dict["clicksUnique"] = clicks_unique
        if exclude_recent_days is not UNSET:
            field_dict["excludeRecentDays"] = exclude_recent_days

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audience_filter_dto import AudienceFilterDto # noqa: PLC0415
        from ..models.email_campaign_dto_merge_tags_type_0 import EmailCampaignDtoMergeTagsType0 # noqa: PLC0415
        from ..models.sender_profile_summary_dto import SenderProfileSummaryDto # noqa: PLC0415
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


        def _parse_subject(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subject = _parse_subject(d.pop("subject", UNSET))


        def _parse_preview_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preview_text = _parse_preview_text(d.pop("previewText", UNSET))


        _sender_profile = d.pop("senderProfile", UNSET)
        sender_profile: SenderProfileSummaryDto | Unset
        if isinstance(_sender_profile,  Unset):
            sender_profile = UNSET
        else:
            sender_profile = SenderProfileSummaryDto.from_dict(_sender_profile)




        def _parse_template_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                template_id_type_0 = UUID(data)



                return template_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        template_id = _parse_template_id(d.pop("templateId", UNSET))


        _audience_filter = d.pop("audienceFilter", UNSET)
        audience_filter: AudienceFilterDto | Unset
        if isinstance(_audience_filter,  Unset):
            audience_filter = UNSET
        else:
            audience_filter = AudienceFilterDto.from_dict(_audience_filter)




        ab_test_enabled = d.pop("abTestEnabled", UNSET)

        def _parse_ab_subject_variant(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ab_subject_variant = _parse_ab_subject_variant(d.pop("abSubjectVariant", UNSET))


        def _parse_ab_split_pct(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ab_split_pct = _parse_ab_split_pct(d.pop("abSplitPct", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_recipient_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        recipient_count = _parse_recipient_count(d.pop("recipientCount", UNSET))


        def _parse_scheduled_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scheduled_at_type_0 = datetime.datetime.fromisoformat(data)



                return scheduled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        scheduled_at = _parse_scheduled_at(d.pop("scheduledAt", UNSET))


        def _parse_sent_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sent_at_type_0 = datetime.datetime.fromisoformat(data)



                return sent_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        sent_at = _parse_sent_at(d.pop("sentAt", UNSET))


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




        def _parse_merge_tags(data: object) -> EmailCampaignDtoMergeTagsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                merge_tags_type_0 = EmailCampaignDtoMergeTagsType0.from_dict(data)



                return merge_tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EmailCampaignDtoMergeTagsType0 | None | Unset, data)

        merge_tags = _parse_merge_tags(d.pop("mergeTags", UNSET))


        optimize_send_time = d.pop("optimizeSendTime", UNSET)

        sent = d.pop("sent", UNSET)

        delivered = d.pop("delivered", UNSET)

        opens_unique = d.pop("opensUnique", UNSET)

        clicks_unique = d.pop("clicksUnique", UNSET)

        def _parse_exclude_recent_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        exclude_recent_days = _parse_exclude_recent_days(d.pop("excludeRecentDays", UNSET))


        email_campaign_dto = cls(
            id=id,
            name=name,
            subject=subject,
            preview_text=preview_text,
            sender_profile=sender_profile,
            template_id=template_id,
            audience_filter=audience_filter,
            ab_test_enabled=ab_test_enabled,
            ab_subject_variant=ab_subject_variant,
            ab_split_pct=ab_split_pct,
            status=status,
            recipient_count=recipient_count,
            scheduled_at=scheduled_at,
            sent_at=sent_at,
            created_at=created_at,
            updated_at=updated_at,
            merge_tags=merge_tags,
            optimize_send_time=optimize_send_time,
            sent=sent,
            delivered=delivered,
            opens_unique=opens_unique,
            clicks_unique=clicks_unique,
            exclude_recent_days=exclude_recent_days,
        )

        return email_campaign_dto


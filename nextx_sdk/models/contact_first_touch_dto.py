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






T = TypeVar("T", bound="ContactFirstTouchDto")



@_attrs_define
class ContactFirstTouchDto:
    

    intake_event_id: UUID | Unset = UNSET
    received_at: datetime.datetime | None | Unset = UNSET
    door_type: None | str | Unset = UNSET
    door_name: None | str | Unset = UNSET
    source_id: None | Unset | UUID = UNSET
    source_raw: None | str | Unset = UNSET
    utm_source: None | str | Unset = UNSET
    utm_medium: None | str | Unset = UNSET
    utm_campaign: None | str | Unset = UNSET
    landing_url: None | str | Unset = UNSET
    referral_raw: None | str | Unset = UNSET
    referral_match: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        intake_event_id: str | Unset = UNSET
        if not isinstance(self.intake_event_id, Unset):
            intake_event_id = str(self.intake_event_id)

        received_at: None | str | Unset
        if isinstance(self.received_at, Unset):
            received_at = UNSET
        elif isinstance(self.received_at, datetime.datetime):
            received_at = self.received_at.isoformat()
        else:
            received_at = self.received_at

        door_type: None | str | Unset
        if isinstance(self.door_type, Unset):
            door_type = UNSET
        else:
            door_type = self.door_type

        door_name: None | str | Unset
        if isinstance(self.door_name, Unset):
            door_name = UNSET
        else:
            door_name = self.door_name

        source_id: None | str | Unset
        if isinstance(self.source_id, Unset):
            source_id = UNSET
        elif isinstance(self.source_id, UUID):
            source_id = str(self.source_id)
        else:
            source_id = self.source_id

        source_raw: None | str | Unset
        if isinstance(self.source_raw, Unset):
            source_raw = UNSET
        else:
            source_raw = self.source_raw

        utm_source: None | str | Unset
        if isinstance(self.utm_source, Unset):
            utm_source = UNSET
        else:
            utm_source = self.utm_source

        utm_medium: None | str | Unset
        if isinstance(self.utm_medium, Unset):
            utm_medium = UNSET
        else:
            utm_medium = self.utm_medium

        utm_campaign: None | str | Unset
        if isinstance(self.utm_campaign, Unset):
            utm_campaign = UNSET
        else:
            utm_campaign = self.utm_campaign

        landing_url: None | str | Unset
        if isinstance(self.landing_url, Unset):
            landing_url = UNSET
        else:
            landing_url = self.landing_url

        referral_raw: None | str | Unset
        if isinstance(self.referral_raw, Unset):
            referral_raw = UNSET
        else:
            referral_raw = self.referral_raw

        referral_match: None | str | Unset
        if isinstance(self.referral_match, Unset):
            referral_match = UNSET
        else:
            referral_match = self.referral_match


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if intake_event_id is not UNSET:
            field_dict["intakeEventId"] = intake_event_id
        if received_at is not UNSET:
            field_dict["receivedAt"] = received_at
        if door_type is not UNSET:
            field_dict["doorType"] = door_type
        if door_name is not UNSET:
            field_dict["doorName"] = door_name
        if source_id is not UNSET:
            field_dict["sourceId"] = source_id
        if source_raw is not UNSET:
            field_dict["sourceRaw"] = source_raw
        if utm_source is not UNSET:
            field_dict["utmSource"] = utm_source
        if utm_medium is not UNSET:
            field_dict["utmMedium"] = utm_medium
        if utm_campaign is not UNSET:
            field_dict["utmCampaign"] = utm_campaign
        if landing_url is not UNSET:
            field_dict["landingUrl"] = landing_url
        if referral_raw is not UNSET:
            field_dict["referralRaw"] = referral_raw
        if referral_match is not UNSET:
            field_dict["referralMatch"] = referral_match

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _intake_event_id = d.pop("intakeEventId", UNSET)
        intake_event_id: UUID | Unset
        if isinstance(_intake_event_id,  Unset):
            intake_event_id = UNSET
        else:
            intake_event_id = UUID(_intake_event_id)




        def _parse_received_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                received_at_type_0 = datetime.datetime.fromisoformat(data)



                return received_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        received_at = _parse_received_at(d.pop("receivedAt", UNSET))


        def _parse_door_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        door_type = _parse_door_type(d.pop("doorType", UNSET))


        def _parse_door_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        door_name = _parse_door_name(d.pop("doorName", UNSET))


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


        def _parse_source_raw(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_raw = _parse_source_raw(d.pop("sourceRaw", UNSET))


        def _parse_utm_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        utm_source = _parse_utm_source(d.pop("utmSource", UNSET))


        def _parse_utm_medium(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        utm_medium = _parse_utm_medium(d.pop("utmMedium", UNSET))


        def _parse_utm_campaign(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        utm_campaign = _parse_utm_campaign(d.pop("utmCampaign", UNSET))


        def _parse_landing_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        landing_url = _parse_landing_url(d.pop("landingUrl", UNSET))


        def _parse_referral_raw(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        referral_raw = _parse_referral_raw(d.pop("referralRaw", UNSET))


        def _parse_referral_match(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        referral_match = _parse_referral_match(d.pop("referralMatch", UNSET))


        contact_first_touch_dto = cls(
            intake_event_id=intake_event_id,
            received_at=received_at,
            door_type=door_type,
            door_name=door_name,
            source_id=source_id,
            source_raw=source_raw,
            utm_source=utm_source,
            utm_medium=utm_medium,
            utm_campaign=utm_campaign,
            landing_url=landing_url,
            referral_raw=referral_raw,
            referral_match=referral_match,
        )

        return contact_first_touch_dto


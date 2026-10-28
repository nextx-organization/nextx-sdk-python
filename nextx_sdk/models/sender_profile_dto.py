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






T = TypeVar("T", bound="SenderProfileDto")



@_attrs_define
class SenderProfileDto:
    

    id: UUID | Unset = UNSET
    from_name: None | str | Unset = UNSET
    from_email: None | str | Unset = UNSET
    reply_to: None | str | Unset = UNSET
    is_default: bool | Unset = UNSET
    is_verified: bool | Unset = UNSET
    verified_at: datetime.datetime | None | Unset = UNSET
    dkim_status: None | str | Unset = UNSET
    spf_status: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    brevo_sender_id: int | None | Unset = UNSET
    domain: None | str | Unset = UNSET
    is_freemail_domain: bool | Unset = UNSET
    dkim_record: None | str | Unset = UNSET
    dkim_record_host: None | str | Unset = UNSET
    spf_record: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        from_name: None | str | Unset
        if isinstance(self.from_name, Unset):
            from_name = UNSET
        else:
            from_name = self.from_name

        from_email: None | str | Unset
        if isinstance(self.from_email, Unset):
            from_email = UNSET
        else:
            from_email = self.from_email

        reply_to: None | str | Unset
        if isinstance(self.reply_to, Unset):
            reply_to = UNSET
        else:
            reply_to = self.reply_to

        is_default = self.is_default

        is_verified = self.is_verified

        verified_at: None | str | Unset
        if isinstance(self.verified_at, Unset):
            verified_at = UNSET
        elif isinstance(self.verified_at, datetime.datetime):
            verified_at = self.verified_at.isoformat()
        else:
            verified_at = self.verified_at

        dkim_status: None | str | Unset
        if isinstance(self.dkim_status, Unset):
            dkim_status = UNSET
        else:
            dkim_status = self.dkim_status

        spf_status: None | str | Unset
        if isinstance(self.spf_status, Unset):
            spf_status = UNSET
        else:
            spf_status = self.spf_status

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        brevo_sender_id: int | None | Unset
        if isinstance(self.brevo_sender_id, Unset):
            brevo_sender_id = UNSET
        else:
            brevo_sender_id = self.brevo_sender_id

        domain: None | str | Unset
        if isinstance(self.domain, Unset):
            domain = UNSET
        else:
            domain = self.domain

        is_freemail_domain = self.is_freemail_domain

        dkim_record: None | str | Unset
        if isinstance(self.dkim_record, Unset):
            dkim_record = UNSET
        else:
            dkim_record = self.dkim_record

        dkim_record_host: None | str | Unset
        if isinstance(self.dkim_record_host, Unset):
            dkim_record_host = UNSET
        else:
            dkim_record_host = self.dkim_record_host

        spf_record: None | str | Unset
        if isinstance(self.spf_record, Unset):
            spf_record = UNSET
        else:
            spf_record = self.spf_record


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if from_name is not UNSET:
            field_dict["fromName"] = from_name
        if from_email is not UNSET:
            field_dict["fromEmail"] = from_email
        if reply_to is not UNSET:
            field_dict["replyTo"] = reply_to
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if is_verified is not UNSET:
            field_dict["isVerified"] = is_verified
        if verified_at is not UNSET:
            field_dict["verifiedAt"] = verified_at
        if dkim_status is not UNSET:
            field_dict["dkimStatus"] = dkim_status
        if spf_status is not UNSET:
            field_dict["spfStatus"] = spf_status
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if brevo_sender_id is not UNSET:
            field_dict["brevoSenderId"] = brevo_sender_id
        if domain is not UNSET:
            field_dict["domain"] = domain
        if is_freemail_domain is not UNSET:
            field_dict["isFreemailDomain"] = is_freemail_domain
        if dkim_record is not UNSET:
            field_dict["dkimRecord"] = dkim_record
        if dkim_record_host is not UNSET:
            field_dict["dkimRecordHost"] = dkim_record_host
        if spf_record is not UNSET:
            field_dict["spfRecord"] = spf_record

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




        def _parse_from_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_name = _parse_from_name(d.pop("fromName", UNSET))


        def _parse_from_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_email = _parse_from_email(d.pop("fromEmail", UNSET))


        def _parse_reply_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reply_to = _parse_reply_to(d.pop("replyTo", UNSET))


        is_default = d.pop("isDefault", UNSET)

        is_verified = d.pop("isVerified", UNSET)

        def _parse_verified_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                verified_at_type_0 = datetime.datetime.fromisoformat(data)



                return verified_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        verified_at = _parse_verified_at(d.pop("verifiedAt", UNSET))


        def _parse_dkim_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dkim_status = _parse_dkim_status(d.pop("dkimStatus", UNSET))


        def _parse_spf_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        spf_status = _parse_spf_status(d.pop("spfStatus", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_brevo_sender_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        brevo_sender_id = _parse_brevo_sender_id(d.pop("brevoSenderId", UNSET))


        def _parse_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domain = _parse_domain(d.pop("domain", UNSET))


        is_freemail_domain = d.pop("isFreemailDomain", UNSET)

        def _parse_dkim_record(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dkim_record = _parse_dkim_record(d.pop("dkimRecord", UNSET))


        def _parse_dkim_record_host(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dkim_record_host = _parse_dkim_record_host(d.pop("dkimRecordHost", UNSET))


        def _parse_spf_record(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        spf_record = _parse_spf_record(d.pop("spfRecord", UNSET))


        sender_profile_dto = cls(
            id=id,
            from_name=from_name,
            from_email=from_email,
            reply_to=reply_to,
            is_default=is_default,
            is_verified=is_verified,
            verified_at=verified_at,
            dkim_status=dkim_status,
            spf_status=spf_status,
            created_at=created_at,
            brevo_sender_id=brevo_sender_id,
            domain=domain,
            is_freemail_domain=is_freemail_domain,
            dkim_record=dkim_record,
            dkim_record_host=dkim_record_host,
            spf_record=spf_record,
        )

        return sender_profile_dto


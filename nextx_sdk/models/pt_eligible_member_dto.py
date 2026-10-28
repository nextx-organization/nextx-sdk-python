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
  from ..models.pt_member_service_line_dto import PtMemberServiceLineDto





T = TypeVar("T", bound="PtEligibleMemberDto")



@_attrs_define
class PtEligibleMemberDto:
    

    gym_profile_id: UUID | Unset = UNSET
    member_code: None | str | Unset = UNSET
    full_name: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    subscription_id: UUID | Unset = UNSET
    contract_code: None | str | Unset = UNSET
    package_name: None | str | Unset = UNSET
    sessions_total: int | None | Unset = UNSET
    sessions_used: int | Unset = UNSET
    sessions_remaining: int | Unset = UNSET
    service_lines: list[PtMemberServiceLineDto] | None | Unset = UNSET
    avatar_url: None | str | Unset = UNSET
    expire_date: datetime.date | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.pt_member_service_line_dto import PtMemberServiceLineDto # noqa: PLC0415
        gym_profile_id: str | Unset = UNSET
        if not isinstance(self.gym_profile_id, Unset):
            gym_profile_id = str(self.gym_profile_id)

        member_code: None | str | Unset
        if isinstance(self.member_code, Unset):
            member_code = UNSET
        else:
            member_code = self.member_code

        full_name: None | str | Unset
        if isinstance(self.full_name, Unset):
            full_name = UNSET
        else:
            full_name = self.full_name

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        subscription_id: str | Unset = UNSET
        if not isinstance(self.subscription_id, Unset):
            subscription_id = str(self.subscription_id)

        contract_code: None | str | Unset
        if isinstance(self.contract_code, Unset):
            contract_code = UNSET
        else:
            contract_code = self.contract_code

        package_name: None | str | Unset
        if isinstance(self.package_name, Unset):
            package_name = UNSET
        else:
            package_name = self.package_name

        sessions_total: int | None | Unset
        if isinstance(self.sessions_total, Unset):
            sessions_total = UNSET
        else:
            sessions_total = self.sessions_total

        sessions_used = self.sessions_used

        sessions_remaining = self.sessions_remaining

        service_lines: list[dict[str, Any]] | None | Unset
        if isinstance(self.service_lines, Unset):
            service_lines = UNSET
        elif isinstance(self.service_lines, list):
            service_lines = []
            for service_lines_type_0_item_data in self.service_lines:
                service_lines_type_0_item = service_lines_type_0_item_data.to_dict()
                service_lines.append(service_lines_type_0_item)


        else:
            service_lines = self.service_lines

        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        expire_date: None | str | Unset
        if isinstance(self.expire_date, Unset):
            expire_date = UNSET
        elif isinstance(self.expire_date, datetime.date):
            expire_date = self.expire_date.isoformat()
        else:
            expire_date = self.expire_date


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if gym_profile_id is not UNSET:
            field_dict["gymProfileId"] = gym_profile_id
        if member_code is not UNSET:
            field_dict["memberCode"] = member_code
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if contract_code is not UNSET:
            field_dict["contractCode"] = contract_code
        if package_name is not UNSET:
            field_dict["packageName"] = package_name
        if sessions_total is not UNSET:
            field_dict["sessionsTotal"] = sessions_total
        if sessions_used is not UNSET:
            field_dict["sessionsUsed"] = sessions_used
        if sessions_remaining is not UNSET:
            field_dict["sessionsRemaining"] = sessions_remaining
        if service_lines is not UNSET:
            field_dict["serviceLines"] = service_lines
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if expire_date is not UNSET:
            field_dict["expireDate"] = expire_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pt_member_service_line_dto import PtMemberServiceLineDto # noqa: PLC0415
        d = dict(src_dict)
        _gym_profile_id = d.pop("gymProfileId", UNSET)
        gym_profile_id: UUID | Unset
        if isinstance(_gym_profile_id,  Unset):
            gym_profile_id = UNSET
        else:
            gym_profile_id = UUID(_gym_profile_id)




        def _parse_member_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_code = _parse_member_code(d.pop("memberCode", UNSET))


        def _parse_full_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        full_name = _parse_full_name(d.pop("fullName", UNSET))


        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))


        _subscription_id = d.pop("subscriptionId", UNSET)
        subscription_id: UUID | Unset
        if isinstance(_subscription_id,  Unset):
            subscription_id = UNSET
        else:
            subscription_id = UUID(_subscription_id)




        def _parse_contract_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contract_code = _parse_contract_code(d.pop("contractCode", UNSET))


        def _parse_package_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        package_name = _parse_package_name(d.pop("packageName", UNSET))


        def _parse_sessions_total(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sessions_total = _parse_sessions_total(d.pop("sessionsTotal", UNSET))


        sessions_used = d.pop("sessionsUsed", UNSET)

        sessions_remaining = d.pop("sessionsRemaining", UNSET)

        def _parse_service_lines(data: object) -> list[PtMemberServiceLineDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                service_lines_type_0 = []
                _service_lines_type_0 = data
                for service_lines_type_0_item_data in (_service_lines_type_0):
                    service_lines_type_0_item = PtMemberServiceLineDto.from_dict(service_lines_type_0_item_data)



                    service_lines_type_0.append(service_lines_type_0_item)

                return service_lines_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PtMemberServiceLineDto] | None | Unset, data)

        service_lines = _parse_service_lines(d.pop("serviceLines", UNSET))


        def _parse_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url = _parse_avatar_url(d.pop("avatarUrl", UNSET))


        def _parse_expire_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expire_date_type_0 = datetime.date.fromisoformat(data)



                return expire_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        expire_date = _parse_expire_date(d.pop("expireDate", UNSET))


        pt_eligible_member_dto = cls(
            gym_profile_id=gym_profile_id,
            member_code=member_code,
            full_name=full_name,
            phone=phone,
            subscription_id=subscription_id,
            contract_code=contract_code,
            package_name=package_name,
            sessions_total=sessions_total,
            sessions_used=sessions_used,
            sessions_remaining=sessions_remaining,
            service_lines=service_lines,
            avatar_url=avatar_url,
            expire_date=expire_date,
        )

        return pt_eligible_member_dto


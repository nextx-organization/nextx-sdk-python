from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.bookable_class_subscription_dto import BookableClassSubscriptionDto





T = TypeVar("T", bound="BookableClassMemberDto")



@_attrs_define
class BookableClassMemberDto:
    

    gym_profile_id: UUID | Unset = UNSET
    member_code: None | str | Unset = UNSET
    full_name: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    avatar_url: None | str | Unset = UNSET
    subscriptions: list[BookableClassSubscriptionDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.bookable_class_subscription_dto import BookableClassSubscriptionDto # noqa: PLC0415
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

        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        subscriptions: list[dict[str, Any]] | None | Unset
        if isinstance(self.subscriptions, Unset):
            subscriptions = UNSET
        elif isinstance(self.subscriptions, list):
            subscriptions = []
            for subscriptions_type_0_item_data in self.subscriptions:
                subscriptions_type_0_item = subscriptions_type_0_item_data.to_dict()
                subscriptions.append(subscriptions_type_0_item)


        else:
            subscriptions = self.subscriptions


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
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bookable_class_subscription_dto import BookableClassSubscriptionDto # noqa: PLC0415
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


        def _parse_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url = _parse_avatar_url(d.pop("avatarUrl", UNSET))


        def _parse_subscriptions(data: object) -> list[BookableClassSubscriptionDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                subscriptions_type_0 = []
                _subscriptions_type_0 = data
                for subscriptions_type_0_item_data in (_subscriptions_type_0):
                    subscriptions_type_0_item = BookableClassSubscriptionDto.from_dict(subscriptions_type_0_item_data)



                    subscriptions_type_0.append(subscriptions_type_0_item)

                return subscriptions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BookableClassSubscriptionDto] | None | Unset, data)

        subscriptions = _parse_subscriptions(d.pop("subscriptions", UNSET))


        bookable_class_member_dto = cls(
            gym_profile_id=gym_profile_id,
            member_code=member_code,
            full_name=full_name,
            phone=phone,
            avatar_url=avatar_url,
            subscriptions=subscriptions,
        )

        return bookable_class_member_dto


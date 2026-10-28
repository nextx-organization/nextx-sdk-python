from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OrderListOutletInfoDto")



@_attrs_define
class OrderListOutletInfoDto:
    

    code: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    owner_name: None | str | Unset = UNSET
    owner_phone: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    channel_code: None | str | Unset = UNSET
    tier: None | str | Unset = UNSET
    rep_names: None | str | Unset = UNSET
    route_names: None | str | Unset = UNSET
    tax_code: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
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

        owner_name: None | str | Unset
        if isinstance(self.owner_name, Unset):
            owner_name = UNSET
        else:
            owner_name = self.owner_name

        owner_phone: None | str | Unset
        if isinstance(self.owner_phone, Unset):
            owner_phone = UNSET
        else:
            owner_phone = self.owner_phone

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        channel_code: None | str | Unset
        if isinstance(self.channel_code, Unset):
            channel_code = UNSET
        else:
            channel_code = self.channel_code

        tier: None | str | Unset
        if isinstance(self.tier, Unset):
            tier = UNSET
        else:
            tier = self.tier

        rep_names: None | str | Unset
        if isinstance(self.rep_names, Unset):
            rep_names = UNSET
        else:
            rep_names = self.rep_names

        route_names: None | str | Unset
        if isinstance(self.route_names, Unset):
            route_names = UNSET
        else:
            route_names = self.route_names

        tax_code: None | str | Unset
        if isinstance(self.tax_code, Unset):
            tax_code = UNSET
        else:
            tax_code = self.tax_code


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name
        if owner_name is not UNSET:
            field_dict["ownerName"] = owner_name
        if owner_phone is not UNSET:
            field_dict["ownerPhone"] = owner_phone
        if address is not UNSET:
            field_dict["address"] = address
        if channel_code is not UNSET:
            field_dict["channelCode"] = channel_code
        if tier is not UNSET:
            field_dict["tier"] = tier
        if rep_names is not UNSET:
            field_dict["repNames"] = rep_names
        if route_names is not UNSET:
            field_dict["routeNames"] = route_names
        if tax_code is not UNSET:
            field_dict["taxCode"] = tax_code

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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


        def _parse_owner_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_name = _parse_owner_name(d.pop("ownerName", UNSET))


        def _parse_owner_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_phone = _parse_owner_phone(d.pop("ownerPhone", UNSET))


        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))


        def _parse_channel_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel_code = _parse_channel_code(d.pop("channelCode", UNSET))


        def _parse_tier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tier = _parse_tier(d.pop("tier", UNSET))


        def _parse_rep_names(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rep_names = _parse_rep_names(d.pop("repNames", UNSET))


        def _parse_route_names(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        route_names = _parse_route_names(d.pop("routeNames", UNSET))


        def _parse_tax_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tax_code = _parse_tax_code(d.pop("taxCode", UNSET))


        order_list_outlet_info_dto = cls(
            code=code,
            name=name,
            owner_name=owner_name,
            owner_phone=owner_phone,
            address=address,
            channel_code=channel_code,
            tier=tier,
            rep_names=rep_names,
            route_names=route_names,
            tax_code=tax_code,
        )

        return order_list_outlet_info_dto


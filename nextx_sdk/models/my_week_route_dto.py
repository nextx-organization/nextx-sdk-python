from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="MyWeekRouteDto")



@_attrs_define
class MyWeekRouteDto:
    

    route_id: UUID | Unset = UNSET
    route_code: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    stop_count: int | Unset = UNSET
    role_type: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        route_id: str | Unset = UNSET
        if not isinstance(self.route_id, Unset):
            route_id = str(self.route_id)

        route_code: None | str | Unset
        if isinstance(self.route_code, Unset):
            route_code = UNSET
        else:
            route_code = self.route_code

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        stop_count = self.stop_count

        role_type: None | str | Unset
        if isinstance(self.role_type, Unset):
            role_type = UNSET
        else:
            role_type = self.role_type


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if route_id is not UNSET:
            field_dict["routeId"] = route_id
        if route_code is not UNSET:
            field_dict["routeCode"] = route_code
        if name is not UNSET:
            field_dict["name"] = name
        if stop_count is not UNSET:
            field_dict["stopCount"] = stop_count
        if role_type is not UNSET:
            field_dict["roleType"] = role_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _route_id = d.pop("routeId", UNSET)
        route_id: UUID | Unset
        if isinstance(_route_id,  Unset):
            route_id = UNSET
        else:
            route_id = UUID(_route_id)




        def _parse_route_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        route_code = _parse_route_code(d.pop("routeCode", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        stop_count = d.pop("stopCount", UNSET)

        def _parse_role_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role_type = _parse_role_type(d.pop("roleType", UNSET))


        my_week_route_dto = cls(
            route_id=route_id,
            route_code=route_code,
            name=name,
            stop_count=stop_count,
            role_type=role_type,
        )

        return my_week_route_dto


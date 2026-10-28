from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OutletAssignedRepDto")



@_attrs_define
class OutletAssignedRepDto:
    

    employee_id: UUID | Unset = UNSET
    employee_code: None | str | Unset = UNSET
    employee_name: None | str | Unset = UNSET
    role_type: None | str | Unset = UNSET
    route_codes: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        employee_id: str | Unset = UNSET
        if not isinstance(self.employee_id, Unset):
            employee_id = str(self.employee_id)

        employee_code: None | str | Unset
        if isinstance(self.employee_code, Unset):
            employee_code = UNSET
        else:
            employee_code = self.employee_code

        employee_name: None | str | Unset
        if isinstance(self.employee_name, Unset):
            employee_name = UNSET
        else:
            employee_name = self.employee_name

        role_type: None | str | Unset
        if isinstance(self.role_type, Unset):
            role_type = UNSET
        else:
            role_type = self.role_type

        route_codes: list[str] | None | Unset
        if isinstance(self.route_codes, Unset):
            route_codes = UNSET
        elif isinstance(self.route_codes, list):
            route_codes = self.route_codes


        else:
            route_codes = self.route_codes


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if employee_id is not UNSET:
            field_dict["employeeId"] = employee_id
        if employee_code is not UNSET:
            field_dict["employeeCode"] = employee_code
        if employee_name is not UNSET:
            field_dict["employeeName"] = employee_name
        if role_type is not UNSET:
            field_dict["roleType"] = role_type
        if route_codes is not UNSET:
            field_dict["routeCodes"] = route_codes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _employee_id = d.pop("employeeId", UNSET)
        employee_id: UUID | Unset
        if isinstance(_employee_id,  Unset):
            employee_id = UNSET
        else:
            employee_id = UUID(_employee_id)




        def _parse_employee_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        employee_code = _parse_employee_code(d.pop("employeeCode", UNSET))


        def _parse_employee_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        employee_name = _parse_employee_name(d.pop("employeeName", UNSET))


        def _parse_role_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role_type = _parse_role_type(d.pop("roleType", UNSET))


        def _parse_route_codes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                route_codes_type_0 = cast(list[str], data)

                return route_codes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        route_codes = _parse_route_codes(d.pop("routeCodes", UNSET))


        outlet_assigned_rep_dto = cls(
            employee_id=employee_id,
            employee_code=employee_code,
            employee_name=employee_name,
            role_type=role_type,
            route_codes=route_codes,
        )

        return outlet_assigned_rep_dto


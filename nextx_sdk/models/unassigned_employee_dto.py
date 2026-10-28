from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="UnassignedEmployeeDto")



@_attrs_define
class UnassignedEmployeeDto:
    

    employee_id: UUID | Unset = UNSET
    employee_code: None | str | Unset = UNSET
    full_name: None | str | Unset = UNSET
    role_type: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        employee_id: str | Unset = UNSET
        if not isinstance(self.employee_id, Unset):
            employee_id = str(self.employee_id)

        employee_code: None | str | Unset
        if isinstance(self.employee_code, Unset):
            employee_code = UNSET
        else:
            employee_code = self.employee_code

        full_name: None | str | Unset
        if isinstance(self.full_name, Unset):
            full_name = UNSET
        else:
            full_name = self.full_name

        role_type: None | str | Unset
        if isinstance(self.role_type, Unset):
            role_type = UNSET
        else:
            role_type = self.role_type


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if employee_id is not UNSET:
            field_dict["employeeId"] = employee_id
        if employee_code is not UNSET:
            field_dict["employeeCode"] = employee_code
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if role_type is not UNSET:
            field_dict["roleType"] = role_type

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


        def _parse_full_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        full_name = _parse_full_name(d.pop("fullName", UNSET))


        def _parse_role_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role_type = _parse_role_type(d.pop("roleType", UNSET))


        unassigned_employee_dto = cls(
            employee_id=employee_id,
            employee_code=employee_code,
            full_name=full_name,
            role_type=role_type,
        )

        return unassigned_employee_dto


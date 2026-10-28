from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OrderListCustomerInfoDto")



@_attrs_define
class OrderListCustomerInfoDto:
    

    group_name: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    company_name: None | str | Unset = UNSET
    tax_code: None | str | Unset = UNSET
    net_debt: float | Unset = UNSET
    owner_name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        group_name: None | str | Unset
        if isinstance(self.group_name, Unset):
            group_name = UNSET
        else:
            group_name = self.group_name

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        tax_code: None | str | Unset
        if isinstance(self.tax_code, Unset):
            tax_code = UNSET
        else:
            tax_code = self.tax_code

        net_debt = self.net_debt

        owner_name: None | str | Unset
        if isinstance(self.owner_name, Unset):
            owner_name = UNSET
        else:
            owner_name = self.owner_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if group_name is not UNSET:
            field_dict["groupName"] = group_name
        if email is not UNSET:
            field_dict["email"] = email
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if tax_code is not UNSET:
            field_dict["taxCode"] = tax_code
        if net_debt is not UNSET:
            field_dict["netDebt"] = net_debt
        if owner_name is not UNSET:
            field_dict["ownerName"] = owner_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_group_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_name = _parse_group_name(d.pop("groupName", UNSET))


        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))


        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("companyName", UNSET))


        def _parse_tax_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tax_code = _parse_tax_code(d.pop("taxCode", UNSET))


        net_debt = d.pop("netDebt", UNSET)

        def _parse_owner_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_name = _parse_owner_name(d.pop("ownerName", UNSET))


        order_list_customer_info_dto = cls(
            group_name=group_name,
            email=email,
            company_name=company_name,
            tax_code=tax_code,
            net_debt=net_debt,
            owner_name=owner_name,
        )

        return order_list_customer_info_dto


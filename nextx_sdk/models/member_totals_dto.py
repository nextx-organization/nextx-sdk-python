from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MemberTotalsDto")



@_attrs_define
class MemberTotalsDto:
    

    total: int | Unset = UNSET
    joined_today: int | Unset = UNSET
    active: int | Unset = UNSET
    expiring_soon: int | Unset = UNSET
    no_contract: int | Unset = UNSET
    total_sales: float | None | Unset = UNSET
    total_paid: float | None | Unset = UNSET
    total_debt: float | None | Unset = UNSET
    can_view_total: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        total = self.total

        joined_today = self.joined_today

        active = self.active

        expiring_soon = self.expiring_soon

        no_contract = self.no_contract

        total_sales: float | None | Unset
        if isinstance(self.total_sales, Unset):
            total_sales = UNSET
        else:
            total_sales = self.total_sales

        total_paid: float | None | Unset
        if isinstance(self.total_paid, Unset):
            total_paid = UNSET
        else:
            total_paid = self.total_paid

        total_debt: float | None | Unset
        if isinstance(self.total_debt, Unset):
            total_debt = UNSET
        else:
            total_debt = self.total_debt

        can_view_total = self.can_view_total


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if total is not UNSET:
            field_dict["total"] = total
        if joined_today is not UNSET:
            field_dict["joinedToday"] = joined_today
        if active is not UNSET:
            field_dict["active"] = active
        if expiring_soon is not UNSET:
            field_dict["expiringSoon"] = expiring_soon
        if no_contract is not UNSET:
            field_dict["noContract"] = no_contract
        if total_sales is not UNSET:
            field_dict["totalSales"] = total_sales
        if total_paid is not UNSET:
            field_dict["totalPaid"] = total_paid
        if total_debt is not UNSET:
            field_dict["totalDebt"] = total_debt
        if can_view_total is not UNSET:
            field_dict["canViewTotal"] = can_view_total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total", UNSET)

        joined_today = d.pop("joinedToday", UNSET)

        active = d.pop("active", UNSET)

        expiring_soon = d.pop("expiringSoon", UNSET)

        no_contract = d.pop("noContract", UNSET)

        def _parse_total_sales(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_sales = _parse_total_sales(d.pop("totalSales", UNSET))


        def _parse_total_paid(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_paid = _parse_total_paid(d.pop("totalPaid", UNSET))


        def _parse_total_debt(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_debt = _parse_total_debt(d.pop("totalDebt", UNSET))


        can_view_total = d.pop("canViewTotal", UNSET)

        member_totals_dto = cls(
            total=total,
            joined_today=joined_today,
            active=active,
            expiring_soon=expiring_soon,
            no_contract=no_contract,
            total_sales=total_sales,
            total_paid=total_paid,
            total_debt=total_debt,
            can_view_total=can_view_total,
        )

        return member_totals_dto


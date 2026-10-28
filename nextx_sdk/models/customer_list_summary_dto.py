from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CustomerListSummaryDto")



@_attrs_define
class CustomerListSummaryDto:
    

    total_debt: float | Unset = UNSET
    total_revenue: float | Unset = UNSET
    total_purchase: float | Unset = UNSET
    total_debt_limit: float | Unset = UNSET
    total_orders: int | Unset = UNSET
    total_points: int | Unset = UNSET
    total_advance: float | Unset = UNSET
    net_debt: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        total_debt = self.total_debt

        total_revenue = self.total_revenue

        total_purchase = self.total_purchase

        total_debt_limit = self.total_debt_limit

        total_orders = self.total_orders

        total_points = self.total_points

        total_advance = self.total_advance

        net_debt = self.net_debt


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if total_debt is not UNSET:
            field_dict["totalDebt"] = total_debt
        if total_revenue is not UNSET:
            field_dict["totalRevenue"] = total_revenue
        if total_purchase is not UNSET:
            field_dict["totalPurchase"] = total_purchase
        if total_debt_limit is not UNSET:
            field_dict["totalDebtLimit"] = total_debt_limit
        if total_orders is not UNSET:
            field_dict["totalOrders"] = total_orders
        if total_points is not UNSET:
            field_dict["totalPoints"] = total_points
        if total_advance is not UNSET:
            field_dict["totalAdvance"] = total_advance
        if net_debt is not UNSET:
            field_dict["netDebt"] = net_debt

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_debt = d.pop("totalDebt", UNSET)

        total_revenue = d.pop("totalRevenue", UNSET)

        total_purchase = d.pop("totalPurchase", UNSET)

        total_debt_limit = d.pop("totalDebtLimit", UNSET)

        total_orders = d.pop("totalOrders", UNSET)

        total_points = d.pop("totalPoints", UNSET)

        total_advance = d.pop("totalAdvance", UNSET)

        net_debt = d.pop("netDebt", UNSET)

        customer_list_summary_dto = cls(
            total_debt=total_debt,
            total_revenue=total_revenue,
            total_purchase=total_purchase,
            total_debt_limit=total_debt_limit,
            total_orders=total_orders,
            total_points=total_points,
            total_advance=total_advance,
            net_debt=net_debt,
        )

        return customer_list_summary_dto


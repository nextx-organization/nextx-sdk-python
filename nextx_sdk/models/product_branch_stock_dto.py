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






T = TypeVar("T", bound="ProductBranchStockDto")



@_attrs_define
class ProductBranchStockDto:
    

    branch_id: UUID | Unset = UNSET
    branch_name: None | str | Unset = UNSET
    on_hand: float | Unset = UNSET
    reserved: float | Unset = UNSET
    available: float | Unset = UNSET
    sold: float | Unset = UNSET
    incoming: float | Unset = UNSET
    days_until_stockout: int | None | Unset = UNSET
    estimated_stockout_date: datetime.datetime | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        branch_id: str | Unset = UNSET
        if not isinstance(self.branch_id, Unset):
            branch_id = str(self.branch_id)

        branch_name: None | str | Unset
        if isinstance(self.branch_name, Unset):
            branch_name = UNSET
        else:
            branch_name = self.branch_name

        on_hand = self.on_hand

        reserved = self.reserved

        available = self.available

        sold = self.sold

        incoming = self.incoming

        days_until_stockout: int | None | Unset
        if isinstance(self.days_until_stockout, Unset):
            days_until_stockout = UNSET
        else:
            days_until_stockout = self.days_until_stockout

        estimated_stockout_date: None | str | Unset
        if isinstance(self.estimated_stockout_date, Unset):
            estimated_stockout_date = UNSET
        elif isinstance(self.estimated_stockout_date, datetime.datetime):
            estimated_stockout_date = self.estimated_stockout_date.isoformat()
        else:
            estimated_stockout_date = self.estimated_stockout_date


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id
        if branch_name is not UNSET:
            field_dict["branchName"] = branch_name
        if on_hand is not UNSET:
            field_dict["onHand"] = on_hand
        if reserved is not UNSET:
            field_dict["reserved"] = reserved
        if available is not UNSET:
            field_dict["available"] = available
        if sold is not UNSET:
            field_dict["sold"] = sold
        if incoming is not UNSET:
            field_dict["incoming"] = incoming
        if days_until_stockout is not UNSET:
            field_dict["daysUntilStockout"] = days_until_stockout
        if estimated_stockout_date is not UNSET:
            field_dict["estimatedStockoutDate"] = estimated_stockout_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _branch_id = d.pop("branchId", UNSET)
        branch_id: UUID | Unset
        if isinstance(_branch_id,  Unset):
            branch_id = UNSET
        else:
            branch_id = UUID(_branch_id)




        def _parse_branch_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch_name = _parse_branch_name(d.pop("branchName", UNSET))


        on_hand = d.pop("onHand", UNSET)

        reserved = d.pop("reserved", UNSET)

        available = d.pop("available", UNSET)

        sold = d.pop("sold", UNSET)

        incoming = d.pop("incoming", UNSET)

        def _parse_days_until_stockout(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        days_until_stockout = _parse_days_until_stockout(d.pop("daysUntilStockout", UNSET))


        def _parse_estimated_stockout_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                estimated_stockout_date_type_0 = datetime.datetime.fromisoformat(data)



                return estimated_stockout_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        estimated_stockout_date = _parse_estimated_stockout_date(d.pop("estimatedStockoutDate", UNSET))


        product_branch_stock_dto = cls(
            branch_id=branch_id,
            branch_name=branch_name,
            on_hand=on_hand,
            reserved=reserved,
            available=available,
            sold=sold,
            incoming=incoming,
            days_until_stockout=days_until_stockout,
            estimated_stockout_date=estimated_stockout_date,
        )

        return product_branch_stock_dto


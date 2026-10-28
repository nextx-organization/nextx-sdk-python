from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.sales_order_dto import SalesOrderDto
  from ..models.sales_order_totals_dto import SalesOrderTotalsDto





T = TypeVar("T", bound="SalesOrderPagedDto")



@_attrs_define
class SalesOrderPagedDto:
    

    items: list[SalesOrderDto] | None | Unset = UNSET
    total_count: int | Unset = UNSET
    page: int | Unset = UNSET
    page_size: int | Unset = UNSET
    totals: SalesOrderTotalsDto | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.sales_order_dto import SalesOrderDto # noqa: PLC0415
        from ..models.sales_order_totals_dto import SalesOrderTotalsDto # noqa: PLC0415
        items: list[dict[str, Any]] | None | Unset
        if isinstance(self.items, Unset):
            items = UNSET
        elif isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)


        else:
            items = self.items

        total_count = self.total_count

        page = self.page

        page_size = self.page_size

        totals: dict[str, Any] | Unset = UNSET
        if not isinstance(self.totals, Unset):
            totals = self.totals.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if items is not UNSET:
            field_dict["items"] = items
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count
        if page is not UNSET:
            field_dict["page"] = page
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if totals is not UNSET:
            field_dict["totals"] = totals

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sales_order_dto import SalesOrderDto # noqa: PLC0415
        from ..models.sales_order_totals_dto import SalesOrderTotalsDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_items(data: object) -> list[SalesOrderDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in (_items_type_0):
                    items_type_0_item = SalesOrderDto.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SalesOrderDto] | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))


        total_count = d.pop("totalCount", UNSET)

        page = d.pop("page", UNSET)

        page_size = d.pop("pageSize", UNSET)

        _totals = d.pop("totals", UNSET)
        totals: SalesOrderTotalsDto | Unset
        if isinstance(_totals,  Unset):
            totals = UNSET
        else:
            totals = SalesOrderTotalsDto.from_dict(_totals)




        sales_order_paged_dto = cls(
            items=items,
            total_count=total_count,
            page=page,
            page_size=page_size,
            totals=totals,
        )

        return sales_order_paged_dto


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.order_change_dto import OrderChangeDto





T = TypeVar("T", bound="OrderChangesResult")



@_attrs_define
class OrderChangesResult:
    

    items: list[OrderChangeDto] | None | Unset = UNSET
    next_cursor: None | str | Unset = UNSET
    has_more: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.order_change_dto import OrderChangeDto # noqa: PLC0415
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

        next_cursor: None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        has_more = self.has_more


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if items is not UNSET:
            field_dict["items"] = items
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor
        if has_more is not UNSET:
            field_dict["hasMore"] = has_more

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.order_change_dto import OrderChangeDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_items(data: object) -> list[OrderChangeDto] | None | Unset:
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
                    items_type_0_item = OrderChangeDto.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OrderChangeDto] | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))


        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))


        has_more = d.pop("hasMore", UNSET)

        order_changes_result = cls(
            items=items,
            next_cursor=next_cursor,
            has_more=has_more,
        )

        return order_changes_result


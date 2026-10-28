from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.stale_opportunity_item_dto import StaleOpportunityItemDto





T = TypeVar("T", bound="StaleOpportunitiesDto")



@_attrs_define
class StaleOpportunitiesDto:
    

    total_count: int | Unset = UNSET
    total_estimated_value: float | Unset = UNSET
    oldest_expected_close_date: datetime.date | None | Unset = UNSET
    items: list[StaleOpportunityItemDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.stale_opportunity_item_dto import StaleOpportunityItemDto # noqa: PLC0415
        total_count = self.total_count

        total_estimated_value = self.total_estimated_value

        oldest_expected_close_date: None | str | Unset
        if isinstance(self.oldest_expected_close_date, Unset):
            oldest_expected_close_date = UNSET
        elif isinstance(self.oldest_expected_close_date, datetime.date):
            oldest_expected_close_date = self.oldest_expected_close_date.isoformat()
        else:
            oldest_expected_close_date = self.oldest_expected_close_date

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


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count
        if total_estimated_value is not UNSET:
            field_dict["totalEstimatedValue"] = total_estimated_value
        if oldest_expected_close_date is not UNSET:
            field_dict["oldestExpectedCloseDate"] = oldest_expected_close_date
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stale_opportunity_item_dto import StaleOpportunityItemDto # noqa: PLC0415
        d = dict(src_dict)
        total_count = d.pop("totalCount", UNSET)

        total_estimated_value = d.pop("totalEstimatedValue", UNSET)

        def _parse_oldest_expected_close_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                oldest_expected_close_date_type_0 = datetime.date.fromisoformat(data)



                return oldest_expected_close_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        oldest_expected_close_date = _parse_oldest_expected_close_date(d.pop("oldestExpectedCloseDate", UNSET))


        def _parse_items(data: object) -> list[StaleOpportunityItemDto] | None | Unset:
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
                    items_type_0_item = StaleOpportunityItemDto.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[StaleOpportunityItemDto] | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))


        stale_opportunities_dto = cls(
            total_count=total_count,
            total_estimated_value=total_estimated_value,
            oldest_expected_close_date=oldest_expected_close_date,
            items=items,
        )

        return stale_opportunities_dto


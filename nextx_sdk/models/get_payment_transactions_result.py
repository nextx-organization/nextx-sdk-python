from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.payment_transaction_dto import PaymentTransactionDto





T = TypeVar("T", bound="GetPaymentTransactionsResult")



@_attrs_define
class GetPaymentTransactionsResult:
    

    items: list[PaymentTransactionDto] | None | Unset = UNSET
    page_number: int | Unset = UNSET
    page_size: int | Unset = UNSET
    total_pages: int | Unset = UNSET
    total_records: int | Unset = UNSET
    total_amount: int | Unset = UNSET
    total_net_amount: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.payment_transaction_dto import PaymentTransactionDto # noqa: PLC0415
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

        page_number = self.page_number

        page_size = self.page_size

        total_pages = self.total_pages

        total_records = self.total_records

        total_amount = self.total_amount

        total_net_amount = self.total_net_amount


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if items is not UNSET:
            field_dict["items"] = items
        if page_number is not UNSET:
            field_dict["pageNumber"] = page_number
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if total_pages is not UNSET:
            field_dict["totalPages"] = total_pages
        if total_records is not UNSET:
            field_dict["totalRecords"] = total_records
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if total_net_amount is not UNSET:
            field_dict["totalNetAmount"] = total_net_amount

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payment_transaction_dto import PaymentTransactionDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_items(data: object) -> list[PaymentTransactionDto] | None | Unset:
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
                    items_type_0_item = PaymentTransactionDto.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PaymentTransactionDto] | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))


        page_number = d.pop("pageNumber", UNSET)

        page_size = d.pop("pageSize", UNSET)

        total_pages = d.pop("totalPages", UNSET)

        total_records = d.pop("totalRecords", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        total_net_amount = d.pop("totalNetAmount", UNSET)

        get_payment_transactions_result = cls(
            items=items,
            page_number=page_number,
            page_size=page_size,
            total_pages=total_pages,
            total_records=total_records,
            total_amount=total_amount,
            total_net_amount=total_net_amount,
        )

        return get_payment_transactions_result


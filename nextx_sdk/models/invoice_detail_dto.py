from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.invoice_dto import InvoiceDto
  from ..models.invoice_item_dto import InvoiceItemDto





T = TypeVar("T", bound="InvoiceDetailDto")



@_attrs_define
class InvoiceDetailDto:
    

    invoice: InvoiceDto | Unset = UNSET
    items: list[InvoiceItemDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.invoice_dto import InvoiceDto # noqa: PLC0415
        from ..models.invoice_item_dto import InvoiceItemDto # noqa: PLC0415
        invoice: dict[str, Any] | Unset = UNSET
        if not isinstance(self.invoice, Unset):
            invoice = self.invoice.to_dict()

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
        if invoice is not UNSET:
            field_dict["invoice"] = invoice
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invoice_dto import InvoiceDto # noqa: PLC0415
        from ..models.invoice_item_dto import InvoiceItemDto # noqa: PLC0415
        d = dict(src_dict)
        _invoice = d.pop("invoice", UNSET)
        invoice: InvoiceDto | Unset
        if isinstance(_invoice,  Unset):
            invoice = UNSET
        else:
            invoice = InvoiceDto.from_dict(_invoice)




        def _parse_items(data: object) -> list[InvoiceItemDto] | None | Unset:
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
                    items_type_0_item = InvoiceItemDto.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[InvoiceItemDto] | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))


        invoice_detail_dto = cls(
            invoice=invoice,
            items=items,
        )

        return invoice_detail_dto


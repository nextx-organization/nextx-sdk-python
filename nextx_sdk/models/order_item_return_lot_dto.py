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






T = TypeVar("T", bound="OrderItemReturnLotDto")



@_attrs_define
class OrderItemReturnLotDto:
    

    lot_id: UUID | Unset = UNSET
    lot_number: None | str | Unset = UNSET
    expiry_date: datetime.date | None | Unset = UNSET
    quantity: float | Unset = UNSET
    returned_quantity: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        lot_id: str | Unset = UNSET
        if not isinstance(self.lot_id, Unset):
            lot_id = str(self.lot_id)

        lot_number: None | str | Unset
        if isinstance(self.lot_number, Unset):
            lot_number = UNSET
        else:
            lot_number = self.lot_number

        expiry_date: None | str | Unset
        if isinstance(self.expiry_date, Unset):
            expiry_date = UNSET
        elif isinstance(self.expiry_date, datetime.date):
            expiry_date = self.expiry_date.isoformat()
        else:
            expiry_date = self.expiry_date

        quantity = self.quantity

        returned_quantity = self.returned_quantity


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if lot_id is not UNSET:
            field_dict["lotId"] = lot_id
        if lot_number is not UNSET:
            field_dict["lotNumber"] = lot_number
        if expiry_date is not UNSET:
            field_dict["expiryDate"] = expiry_date
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if returned_quantity is not UNSET:
            field_dict["returnedQuantity"] = returned_quantity

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _lot_id = d.pop("lotId", UNSET)
        lot_id: UUID | Unset
        if isinstance(_lot_id,  Unset):
            lot_id = UNSET
        else:
            lot_id = UUID(_lot_id)




        def _parse_lot_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lot_number = _parse_lot_number(d.pop("lotNumber", UNSET))


        def _parse_expiry_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiry_date_type_0 = datetime.date.fromisoformat(data)



                return expiry_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        expiry_date = _parse_expiry_date(d.pop("expiryDate", UNSET))


        quantity = d.pop("quantity", UNSET)

        returned_quantity = d.pop("returnedQuantity", UNSET)

        order_item_return_lot_dto = cls(
            lot_id=lot_id,
            lot_number=lot_number,
            expiry_date=expiry_date,
            quantity=quantity,
            returned_quantity=returned_quantity,
        )

        return order_item_return_lot_dto


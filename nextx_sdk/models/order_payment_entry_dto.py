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






T = TypeVar("T", bound="OrderPaymentEntryDto")



@_attrs_define
class OrderPaymentEntryDto:
    

    receipt_id: UUID | Unset = UNSET
    receipt_code: None | str | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    payment_method: None | str | Unset = UNSET
    amount: float | Unset = UNSET
    bank_account_id: None | Unset | UUID = UNSET
    bank_account_label: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        receipt_id: str | Unset = UNSET
        if not isinstance(self.receipt_id, Unset):
            receipt_id = str(self.receipt_id)

        receipt_code: None | str | Unset
        if isinstance(self.receipt_code, Unset):
            receipt_code = UNSET
        else:
            receipt_code = self.receipt_code

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        payment_method: None | str | Unset
        if isinstance(self.payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = self.payment_method

        amount = self.amount

        bank_account_id: None | str | Unset
        if isinstance(self.bank_account_id, Unset):
            bank_account_id = UNSET
        elif isinstance(self.bank_account_id, UUID):
            bank_account_id = str(self.bank_account_id)
        else:
            bank_account_id = self.bank_account_id

        bank_account_label: None | str | Unset
        if isinstance(self.bank_account_label, Unset):
            bank_account_label = UNSET
        else:
            bank_account_label = self.bank_account_label


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if receipt_id is not UNSET:
            field_dict["receiptId"] = receipt_id
        if receipt_code is not UNSET:
            field_dict["receiptCode"] = receipt_code
        if date is not UNSET:
            field_dict["date"] = date
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method
        if amount is not UNSET:
            field_dict["amount"] = amount
        if bank_account_id is not UNSET:
            field_dict["bankAccountId"] = bank_account_id
        if bank_account_label is not UNSET:
            field_dict["bankAccountLabel"] = bank_account_label

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _receipt_id = d.pop("receiptId", UNSET)
        receipt_id: UUID | Unset
        if isinstance(_receipt_id,  Unset):
            receipt_id = UNSET
        else:
            receipt_id = UUID(_receipt_id)




        def _parse_receipt_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        receipt_code = _parse_receipt_code(d.pop("receiptCode", UNSET))


        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date,  Unset):
            date = UNSET
        else:
            date = datetime.datetime.fromisoformat(_date)




        def _parse_payment_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_method = _parse_payment_method(d.pop("paymentMethod", UNSET))


        amount = d.pop("amount", UNSET)

        def _parse_bank_account_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                bank_account_id_type_0 = UUID(data)



                return bank_account_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        bank_account_id = _parse_bank_account_id(d.pop("bankAccountId", UNSET))


        def _parse_bank_account_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bank_account_label = _parse_bank_account_label(d.pop("bankAccountLabel", UNSET))


        order_payment_entry_dto = cls(
            receipt_id=receipt_id,
            receipt_code=receipt_code,
            date=date,
            payment_method=payment_method,
            amount=amount,
            bank_account_id=bank_account_id,
            bank_account_label=bank_account_label,
        )

        return order_payment_entry_dto


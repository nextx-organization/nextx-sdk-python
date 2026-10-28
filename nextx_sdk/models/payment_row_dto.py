from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PaymentRowDto")



@_attrs_define
class PaymentRowDto:
    

    method: None | str | Unset = UNSET
    amount: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        method: None | str | Unset
        if isinstance(self.method, Unset):
            method = UNSET
        else:
            method = self.method

        amount = self.amount


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if method is not UNSET:
            field_dict["method"] = method
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        method = _parse_method(d.pop("method", UNSET))


        amount = d.pop("amount", UNSET)

        payment_row_dto = cls(
            method=method,
            amount=amount,
        )

        return payment_row_dto


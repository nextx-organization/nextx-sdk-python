from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ProviderBreakdownDto")



@_attrs_define
class ProviderBreakdownDto:
    

    provider_code: None | str | Unset = UNSET
    transaction_count: int | Unset = UNSET
    total_amount: int | Unset = UNSET
    success_rate: float | Unset = UNSET
    avg_fee_rate: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        provider_code: None | str | Unset
        if isinstance(self.provider_code, Unset):
            provider_code = UNSET
        else:
            provider_code = self.provider_code

        transaction_count = self.transaction_count

        total_amount = self.total_amount

        success_rate = self.success_rate

        avg_fee_rate = self.avg_fee_rate


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if provider_code is not UNSET:
            field_dict["providerCode"] = provider_code
        if transaction_count is not UNSET:
            field_dict["transactionCount"] = transaction_count
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if success_rate is not UNSET:
            field_dict["successRate"] = success_rate
        if avg_fee_rate is not UNSET:
            field_dict["avgFeeRate"] = avg_fee_rate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_provider_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_code = _parse_provider_code(d.pop("providerCode", UNSET))


        transaction_count = d.pop("transactionCount", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        success_rate = d.pop("successRate", UNSET)

        avg_fee_rate = d.pop("avgFeeRate", UNSET)

        provider_breakdown_dto = cls(
            provider_code=provider_code,
            transaction_count=transaction_count,
            total_amount=total_amount,
            success_rate=success_rate,
            avg_fee_rate=avg_fee_rate,
        )

        return provider_breakdown_dto


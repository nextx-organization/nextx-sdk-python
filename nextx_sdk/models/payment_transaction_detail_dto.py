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






T = TypeVar("T", bound="PaymentTransactionDetailDto")



@_attrs_define
class PaymentTransactionDetailDto:
    

    transaction_id: UUID | Unset = UNSET
    intent_id: UUID | Unset = UNSET
    provider_code: None | str | Unset = UNSET
    provider_transaction_id: None | str | Unset = UNSET
    reference_type: None | str | Unset = UNSET
    reference_id: UUID | Unset = UNSET
    payer_type: None | str | Unset = UNSET
    payer_id: UUID | Unset = UNSET
    amount: int | Unset = UNSET
    net_amount: int | Unset = UNSET
    currency: None | str | Unset = UNSET
    paid_at: datetime.datetime | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        transaction_id: str | Unset = UNSET
        if not isinstance(self.transaction_id, Unset):
            transaction_id = str(self.transaction_id)

        intent_id: str | Unset = UNSET
        if not isinstance(self.intent_id, Unset):
            intent_id = str(self.intent_id)

        provider_code: None | str | Unset
        if isinstance(self.provider_code, Unset):
            provider_code = UNSET
        else:
            provider_code = self.provider_code

        provider_transaction_id: None | str | Unset
        if isinstance(self.provider_transaction_id, Unset):
            provider_transaction_id = UNSET
        else:
            provider_transaction_id = self.provider_transaction_id

        reference_type: None | str | Unset
        if isinstance(self.reference_type, Unset):
            reference_type = UNSET
        else:
            reference_type = self.reference_type

        reference_id: str | Unset = UNSET
        if not isinstance(self.reference_id, Unset):
            reference_id = str(self.reference_id)

        payer_type: None | str | Unset
        if isinstance(self.payer_type, Unset):
            payer_type = UNSET
        else:
            payer_type = self.payer_type

        payer_id: str | Unset = UNSET
        if not isinstance(self.payer_id, Unset):
            payer_id = str(self.payer_id)

        amount = self.amount

        net_amount = self.net_amount

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        paid_at: str | Unset = UNSET
        if not isinstance(self.paid_at, Unset):
            paid_at = self.paid_at.isoformat()

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id
        if intent_id is not UNSET:
            field_dict["intentId"] = intent_id
        if provider_code is not UNSET:
            field_dict["providerCode"] = provider_code
        if provider_transaction_id is not UNSET:
            field_dict["providerTransactionId"] = provider_transaction_id
        if reference_type is not UNSET:
            field_dict["referenceType"] = reference_type
        if reference_id is not UNSET:
            field_dict["referenceId"] = reference_id
        if payer_type is not UNSET:
            field_dict["payerType"] = payer_type
        if payer_id is not UNSET:
            field_dict["payerId"] = payer_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if net_amount is not UNSET:
            field_dict["netAmount"] = net_amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if paid_at is not UNSET:
            field_dict["paidAt"] = paid_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _transaction_id = d.pop("transactionId", UNSET)
        transaction_id: UUID | Unset
        if isinstance(_transaction_id,  Unset):
            transaction_id = UNSET
        else:
            transaction_id = UUID(_transaction_id)




        _intent_id = d.pop("intentId", UNSET)
        intent_id: UUID | Unset
        if isinstance(_intent_id,  Unset):
            intent_id = UNSET
        else:
            intent_id = UUID(_intent_id)




        def _parse_provider_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_code = _parse_provider_code(d.pop("providerCode", UNSET))


        def _parse_provider_transaction_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_transaction_id = _parse_provider_transaction_id(d.pop("providerTransactionId", UNSET))


        def _parse_reference_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reference_type = _parse_reference_type(d.pop("referenceType", UNSET))


        _reference_id = d.pop("referenceId", UNSET)
        reference_id: UUID | Unset
        if isinstance(_reference_id,  Unset):
            reference_id = UNSET
        else:
            reference_id = UUID(_reference_id)




        def _parse_payer_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payer_type = _parse_payer_type(d.pop("payerType", UNSET))


        _payer_id = d.pop("payerId", UNSET)
        payer_id: UUID | Unset
        if isinstance(_payer_id,  Unset):
            payer_id = UNSET
        else:
            payer_id = UUID(_payer_id)




        amount = d.pop("amount", UNSET)

        net_amount = d.pop("netAmount", UNSET)

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        _paid_at = d.pop("paidAt", UNSET)
        paid_at: datetime.datetime | Unset
        if isinstance(_paid_at,  Unset):
            paid_at = UNSET
        else:
            paid_at = datetime.datetime.fromisoformat(_paid_at)




        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        payment_transaction_detail_dto = cls(
            transaction_id=transaction_id,
            intent_id=intent_id,
            provider_code=provider_code,
            provider_transaction_id=provider_transaction_id,
            reference_type=reference_type,
            reference_id=reference_id,
            payer_type=payer_type,
            payer_id=payer_id,
            amount=amount,
            net_amount=net_amount,
            currency=currency,
            paid_at=paid_at,
            created_at=created_at,
        )

        return payment_transaction_detail_dto


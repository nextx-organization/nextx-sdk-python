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






T = TypeVar("T", bound="PaymentIntentDto")



@_attrs_define
class PaymentIntentDto:
    

    intent_id: UUID | Unset = UNSET
    status: None | str | Unset = UNSET
    provider_code: None | str | Unset = UNSET
    payment_url: None | str | Unset = UNSET
    qr_code_data: None | str | Unset = UNSET
    amount: int | Unset = UNSET
    currency: None | str | Unset = UNSET
    reference_type: None | str | Unset = UNSET
    reference_id: UUID | Unset = UNSET
    payer_type: None | str | Unset = UNSET
    payer_id: UUID | Unset = UNSET
    description: None | str | Unset = UNSET
    expires_at: datetime.datetime | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET
    transaction_id: None | Unset | UUID = UNSET
    created_at: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        intent_id: str | Unset = UNSET
        if not isinstance(self.intent_id, Unset):
            intent_id = str(self.intent_id)

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        provider_code: None | str | Unset
        if isinstance(self.provider_code, Unset):
            provider_code = UNSET
        else:
            provider_code = self.provider_code

        payment_url: None | str | Unset
        if isinstance(self.payment_url, Unset):
            payment_url = UNSET
        else:
            payment_url = self.payment_url

        qr_code_data: None | str | Unset
        if isinstance(self.qr_code_data, Unset):
            qr_code_data = UNSET
        else:
            qr_code_data = self.qr_code_data

        amount = self.amount

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

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

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        transaction_id: None | str | Unset
        if isinstance(self.transaction_id, Unset):
            transaction_id = UNSET
        elif isinstance(self.transaction_id, UUID):
            transaction_id = str(self.transaction_id)
        else:
            transaction_id = self.transaction_id

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if intent_id is not UNSET:
            field_dict["intentId"] = intent_id
        if status is not UNSET:
            field_dict["status"] = status
        if provider_code is not UNSET:
            field_dict["providerCode"] = provider_code
        if payment_url is not UNSET:
            field_dict["paymentUrl"] = payment_url
        if qr_code_data is not UNSET:
            field_dict["qrCodeData"] = qr_code_data
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if reference_type is not UNSET:
            field_dict["referenceType"] = reference_type
        if reference_id is not UNSET:
            field_dict["referenceId"] = reference_id
        if payer_type is not UNSET:
            field_dict["payerType"] = payer_type
        if payer_id is not UNSET:
            field_dict["payerId"] = payer_id
        if description is not UNSET:
            field_dict["description"] = description
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _intent_id = d.pop("intentId", UNSET)
        intent_id: UUID | Unset
        if isinstance(_intent_id,  Unset):
            intent_id = UNSET
        else:
            intent_id = UUID(_intent_id)




        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_provider_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_code = _parse_provider_code(d.pop("providerCode", UNSET))


        def _parse_payment_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_url = _parse_payment_url(d.pop("paymentUrl", UNSET))


        def _parse_qr_code_data(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        qr_code_data = _parse_qr_code_data(d.pop("qrCodeData", UNSET))


        amount = d.pop("amount", UNSET)

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


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




        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at,  Unset):
            expires_at = UNSET
        else:
            expires_at = datetime.datetime.fromisoformat(_expires_at)




        def _parse_completed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = datetime.datetime.fromisoformat(data)



                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        completed_at = _parse_completed_at(d.pop("completedAt", UNSET))


        def _parse_transaction_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                transaction_id_type_0 = UUID(data)



                return transaction_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        transaction_id = _parse_transaction_id(d.pop("transactionId", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        payment_intent_dto = cls(
            intent_id=intent_id,
            status=status,
            provider_code=provider_code,
            payment_url=payment_url,
            qr_code_data=qr_code_data,
            amount=amount,
            currency=currency,
            reference_type=reference_type,
            reference_id=reference_id,
            payer_type=payer_type,
            payer_id=payer_id,
            description=description,
            expires_at=expires_at,
            completed_at=completed_at,
            transaction_id=transaction_id,
            created_at=created_at,
        )

        return payment_intent_dto


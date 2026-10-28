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






T = TypeVar("T", bound="PaymentTransactionDto")



@_attrs_define
class PaymentTransactionDto:
    

    id: UUID | Unset = UNSET
    intent_id: UUID | Unset = UNSET
    provider_code: None | str | Unset = UNSET
    reference_type: None | str | Unset = UNSET
    reference_id: None | Unset | UUID = UNSET
    amount: int | Unset = UNSET
    net_amount: int | Unset = UNSET
    currency: None | str | Unset = UNSET
    provider_transaction_id: None | str | Unset = UNSET
    paid_at: datetime.datetime | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    provider_approval_code: None | str | Unset = UNSET
    payment_instrument: None | str | Unset = UNSET
    payment_instrument_detail: None | str | Unset = UNSET
    refunded_amount: int | Unset = UNSET
    refund_count: int | Unset = UNSET
    latest_refund_status: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        intent_id: str | Unset = UNSET
        if not isinstance(self.intent_id, Unset):
            intent_id = str(self.intent_id)

        provider_code: None | str | Unset
        if isinstance(self.provider_code, Unset):
            provider_code = UNSET
        else:
            provider_code = self.provider_code

        reference_type: None | str | Unset
        if isinstance(self.reference_type, Unset):
            reference_type = UNSET
        else:
            reference_type = self.reference_type

        reference_id: None | str | Unset
        if isinstance(self.reference_id, Unset):
            reference_id = UNSET
        elif isinstance(self.reference_id, UUID):
            reference_id = str(self.reference_id)
        else:
            reference_id = self.reference_id

        amount = self.amount

        net_amount = self.net_amount

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        provider_transaction_id: None | str | Unset
        if isinstance(self.provider_transaction_id, Unset):
            provider_transaction_id = UNSET
        else:
            provider_transaction_id = self.provider_transaction_id

        paid_at: str | Unset = UNSET
        if not isinstance(self.paid_at, Unset):
            paid_at = self.paid_at.isoformat()

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        provider_approval_code: None | str | Unset
        if isinstance(self.provider_approval_code, Unset):
            provider_approval_code = UNSET
        else:
            provider_approval_code = self.provider_approval_code

        payment_instrument: None | str | Unset
        if isinstance(self.payment_instrument, Unset):
            payment_instrument = UNSET
        else:
            payment_instrument = self.payment_instrument

        payment_instrument_detail: None | str | Unset
        if isinstance(self.payment_instrument_detail, Unset):
            payment_instrument_detail = UNSET
        else:
            payment_instrument_detail = self.payment_instrument_detail

        refunded_amount = self.refunded_amount

        refund_count = self.refund_count

        latest_refund_status: None | str | Unset
        if isinstance(self.latest_refund_status, Unset):
            latest_refund_status = UNSET
        else:
            latest_refund_status = self.latest_refund_status


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if intent_id is not UNSET:
            field_dict["intentId"] = intent_id
        if provider_code is not UNSET:
            field_dict["providerCode"] = provider_code
        if reference_type is not UNSET:
            field_dict["referenceType"] = reference_type
        if reference_id is not UNSET:
            field_dict["referenceId"] = reference_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if net_amount is not UNSET:
            field_dict["netAmount"] = net_amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if provider_transaction_id is not UNSET:
            field_dict["providerTransactionId"] = provider_transaction_id
        if paid_at is not UNSET:
            field_dict["paidAt"] = paid_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if provider_approval_code is not UNSET:
            field_dict["providerApprovalCode"] = provider_approval_code
        if payment_instrument is not UNSET:
            field_dict["paymentInstrument"] = payment_instrument
        if payment_instrument_detail is not UNSET:
            field_dict["paymentInstrumentDetail"] = payment_instrument_detail
        if refunded_amount is not UNSET:
            field_dict["refundedAmount"] = refunded_amount
        if refund_count is not UNSET:
            field_dict["refundCount"] = refund_count
        if latest_refund_status is not UNSET:
            field_dict["latestRefundStatus"] = latest_refund_status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




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


        def _parse_reference_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reference_type = _parse_reference_type(d.pop("referenceType", UNSET))


        def _parse_reference_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reference_id_type_0 = UUID(data)



                return reference_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        reference_id = _parse_reference_id(d.pop("referenceId", UNSET))


        amount = d.pop("amount", UNSET)

        net_amount = d.pop("netAmount", UNSET)

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        def _parse_provider_transaction_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_transaction_id = _parse_provider_transaction_id(d.pop("providerTransactionId", UNSET))


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




        def _parse_provider_approval_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_approval_code = _parse_provider_approval_code(d.pop("providerApprovalCode", UNSET))


        def _parse_payment_instrument(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_instrument = _parse_payment_instrument(d.pop("paymentInstrument", UNSET))


        def _parse_payment_instrument_detail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_instrument_detail = _parse_payment_instrument_detail(d.pop("paymentInstrumentDetail", UNSET))


        refunded_amount = d.pop("refundedAmount", UNSET)

        refund_count = d.pop("refundCount", UNSET)

        def _parse_latest_refund_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_refund_status = _parse_latest_refund_status(d.pop("latestRefundStatus", UNSET))


        payment_transaction_dto = cls(
            id=id,
            intent_id=intent_id,
            provider_code=provider_code,
            reference_type=reference_type,
            reference_id=reference_id,
            amount=amount,
            net_amount=net_amount,
            currency=currency,
            provider_transaction_id=provider_transaction_id,
            paid_at=paid_at,
            created_at=created_at,
            provider_approval_code=provider_approval_code,
            payment_instrument=payment_instrument,
            payment_instrument_detail=payment_instrument_detail,
            refunded_amount=refunded_amount,
            refund_count=refund_count,
            latest_refund_status=latest_refund_status,
        )

        return payment_transaction_dto


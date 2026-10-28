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






T = TypeVar("T", bound="PaymentRefundDto")



@_attrs_define
class PaymentRefundDto:
    

    refund_id: UUID | Unset = UNSET
    transaction_id: UUID | Unset = UNSET
    amount: int | Unset = UNSET
    currency: None | str | Unset = UNSET
    refund_method: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    reason: None | str | Unset = UNSET
    requested_by: UUID | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    approved_by: None | Unset | UUID = UNSET
    approved_at: datetime.datetime | None | Unset = UNSET
    rejected_by: None | Unset | UUID = UNSET
    rejected_at: datetime.datetime | None | Unset = UNSET
    rejection_reason: None | str | Unset = UNSET
    processed_at: datetime.datetime | None | Unset = UNSET
    provider_refund_id: None | str | Unset = UNSET
    bank_transaction_ref: None | str | Unset = UNSET
    provider_code: None | str | Unset = UNSET
    transaction_amount: int | None | Unset = UNSET
    reference_type: None | str | Unset = UNSET
    reference_id: None | Unset | UUID = UNSET
    provider_transaction_id: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        refund_id: str | Unset = UNSET
        if not isinstance(self.refund_id, Unset):
            refund_id = str(self.refund_id)

        transaction_id: str | Unset = UNSET
        if not isinstance(self.transaction_id, Unset):
            transaction_id = str(self.transaction_id)

        amount = self.amount

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        refund_method: None | str | Unset
        if isinstance(self.refund_method, Unset):
            refund_method = UNSET
        else:
            refund_method = self.refund_method

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        requested_by: str | Unset = UNSET
        if not isinstance(self.requested_by, Unset):
            requested_by = str(self.requested_by)

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        approved_by: None | str | Unset
        if isinstance(self.approved_by, Unset):
            approved_by = UNSET
        elif isinstance(self.approved_by, UUID):
            approved_by = str(self.approved_by)
        else:
            approved_by = self.approved_by

        approved_at: None | str | Unset
        if isinstance(self.approved_at, Unset):
            approved_at = UNSET
        elif isinstance(self.approved_at, datetime.datetime):
            approved_at = self.approved_at.isoformat()
        else:
            approved_at = self.approved_at

        rejected_by: None | str | Unset
        if isinstance(self.rejected_by, Unset):
            rejected_by = UNSET
        elif isinstance(self.rejected_by, UUID):
            rejected_by = str(self.rejected_by)
        else:
            rejected_by = self.rejected_by

        rejected_at: None | str | Unset
        if isinstance(self.rejected_at, Unset):
            rejected_at = UNSET
        elif isinstance(self.rejected_at, datetime.datetime):
            rejected_at = self.rejected_at.isoformat()
        else:
            rejected_at = self.rejected_at

        rejection_reason: None | str | Unset
        if isinstance(self.rejection_reason, Unset):
            rejection_reason = UNSET
        else:
            rejection_reason = self.rejection_reason

        processed_at: None | str | Unset
        if isinstance(self.processed_at, Unset):
            processed_at = UNSET
        elif isinstance(self.processed_at, datetime.datetime):
            processed_at = self.processed_at.isoformat()
        else:
            processed_at = self.processed_at

        provider_refund_id: None | str | Unset
        if isinstance(self.provider_refund_id, Unset):
            provider_refund_id = UNSET
        else:
            provider_refund_id = self.provider_refund_id

        bank_transaction_ref: None | str | Unset
        if isinstance(self.bank_transaction_ref, Unset):
            bank_transaction_ref = UNSET
        else:
            bank_transaction_ref = self.bank_transaction_ref

        provider_code: None | str | Unset
        if isinstance(self.provider_code, Unset):
            provider_code = UNSET
        else:
            provider_code = self.provider_code

        transaction_amount: int | None | Unset
        if isinstance(self.transaction_amount, Unset):
            transaction_amount = UNSET
        else:
            transaction_amount = self.transaction_amount

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

        provider_transaction_id: None | str | Unset
        if isinstance(self.provider_transaction_id, Unset):
            provider_transaction_id = UNSET
        else:
            provider_transaction_id = self.provider_transaction_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if refund_id is not UNSET:
            field_dict["refundId"] = refund_id
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if refund_method is not UNSET:
            field_dict["refundMethod"] = refund_method
        if status is not UNSET:
            field_dict["status"] = status
        if reason is not UNSET:
            field_dict["reason"] = reason
        if requested_by is not UNSET:
            field_dict["requestedBy"] = requested_by
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if approved_by is not UNSET:
            field_dict["approvedBy"] = approved_by
        if approved_at is not UNSET:
            field_dict["approvedAt"] = approved_at
        if rejected_by is not UNSET:
            field_dict["rejectedBy"] = rejected_by
        if rejected_at is not UNSET:
            field_dict["rejectedAt"] = rejected_at
        if rejection_reason is not UNSET:
            field_dict["rejectionReason"] = rejection_reason
        if processed_at is not UNSET:
            field_dict["processedAt"] = processed_at
        if provider_refund_id is not UNSET:
            field_dict["providerRefundId"] = provider_refund_id
        if bank_transaction_ref is not UNSET:
            field_dict["bankTransactionRef"] = bank_transaction_ref
        if provider_code is not UNSET:
            field_dict["providerCode"] = provider_code
        if transaction_amount is not UNSET:
            field_dict["transactionAmount"] = transaction_amount
        if reference_type is not UNSET:
            field_dict["referenceType"] = reference_type
        if reference_id is not UNSET:
            field_dict["referenceId"] = reference_id
        if provider_transaction_id is not UNSET:
            field_dict["providerTransactionId"] = provider_transaction_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _refund_id = d.pop("refundId", UNSET)
        refund_id: UUID | Unset
        if isinstance(_refund_id,  Unset):
            refund_id = UNSET
        else:
            refund_id = UUID(_refund_id)




        _transaction_id = d.pop("transactionId", UNSET)
        transaction_id: UUID | Unset
        if isinstance(_transaction_id,  Unset):
            transaction_id = UNSET
        else:
            transaction_id = UUID(_transaction_id)




        amount = d.pop("amount", UNSET)

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        def _parse_refund_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        refund_method = _parse_refund_method(d.pop("refundMethod", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))


        _requested_by = d.pop("requestedBy", UNSET)
        requested_by: UUID | Unset
        if isinstance(_requested_by,  Unset):
            requested_by = UNSET
        else:
            requested_by = UUID(_requested_by)




        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_approved_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_by_type_0 = UUID(data)



                return approved_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        approved_by = _parse_approved_by(d.pop("approvedBy", UNSET))


        def _parse_approved_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_at_type_0 = datetime.datetime.fromisoformat(data)



                return approved_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        approved_at = _parse_approved_at(d.pop("approvedAt", UNSET))


        def _parse_rejected_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rejected_by_type_0 = UUID(data)



                return rejected_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        rejected_by = _parse_rejected_by(d.pop("rejectedBy", UNSET))


        def _parse_rejected_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rejected_at_type_0 = datetime.datetime.fromisoformat(data)



                return rejected_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        rejected_at = _parse_rejected_at(d.pop("rejectedAt", UNSET))


        def _parse_rejection_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rejection_reason = _parse_rejection_reason(d.pop("rejectionReason", UNSET))


        def _parse_processed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                processed_at_type_0 = datetime.datetime.fromisoformat(data)



                return processed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        processed_at = _parse_processed_at(d.pop("processedAt", UNSET))


        def _parse_provider_refund_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_refund_id = _parse_provider_refund_id(d.pop("providerRefundId", UNSET))


        def _parse_bank_transaction_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bank_transaction_ref = _parse_bank_transaction_ref(d.pop("bankTransactionRef", UNSET))


        def _parse_provider_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_code = _parse_provider_code(d.pop("providerCode", UNSET))


        def _parse_transaction_amount(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        transaction_amount = _parse_transaction_amount(d.pop("transactionAmount", UNSET))


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


        def _parse_provider_transaction_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_transaction_id = _parse_provider_transaction_id(d.pop("providerTransactionId", UNSET))


        payment_refund_dto = cls(
            refund_id=refund_id,
            transaction_id=transaction_id,
            amount=amount,
            currency=currency,
            refund_method=refund_method,
            status=status,
            reason=reason,
            requested_by=requested_by,
            created_at=created_at,
            approved_by=approved_by,
            approved_at=approved_at,
            rejected_by=rejected_by,
            rejected_at=rejected_at,
            rejection_reason=rejection_reason,
            processed_at=processed_at,
            provider_refund_id=provider_refund_id,
            bank_transaction_ref=bank_transaction_ref,
            provider_code=provider_code,
            transaction_amount=transaction_amount,
            reference_type=reference_type,
            reference_id=reference_id,
            provider_transaction_id=provider_transaction_id,
        )

        return payment_refund_dto


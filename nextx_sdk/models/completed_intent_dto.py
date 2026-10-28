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

if TYPE_CHECKING:
  from ..models.completed_intent_dto_metadata_type_0 import CompletedIntentDtoMetadataType0





T = TypeVar("T", bound="CompletedIntentDto")



@_attrs_define
class CompletedIntentDto:
    

    payment_intent_id: UUID | Unset = UNSET
    workspace_id: UUID | Unset = UNSET
    payer_type: None | str | Unset = UNSET
    payer_id: UUID | Unset = UNSET
    reference_type: None | str | Unset = UNSET
    reference_id: UUID | Unset = UNSET
    amount: int | Unset = UNSET
    net_amount: int | Unset = UNSET
    currency: None | str | Unset = UNSET
    provider_code: None | str | Unset = UNSET
    provider_transaction_id: None | str | Unset = UNSET
    paid_at: datetime.datetime | Unset = UNSET
    db_transaction_id: UUID | Unset = UNSET
    provider_approval_code: None | str | Unset = UNSET
    payment_instrument: None | str | Unset = UNSET
    payment_instrument_detail: None | str | Unset = UNSET
    metadata: CompletedIntentDtoMetadataType0 | None | Unset = UNSET
    recurring_contract_no: None | str | Unset = UNSET
    recurring_period_num: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.completed_intent_dto_metadata_type_0 import CompletedIntentDtoMetadataType0 # noqa: PLC0415
        payment_intent_id: str | Unset = UNSET
        if not isinstance(self.payment_intent_id, Unset):
            payment_intent_id = str(self.payment_intent_id)

        workspace_id: str | Unset = UNSET
        if not isinstance(self.workspace_id, Unset):
            workspace_id = str(self.workspace_id)

        payer_type: None | str | Unset
        if isinstance(self.payer_type, Unset):
            payer_type = UNSET
        else:
            payer_type = self.payer_type

        payer_id: str | Unset = UNSET
        if not isinstance(self.payer_id, Unset):
            payer_id = str(self.payer_id)

        reference_type: None | str | Unset
        if isinstance(self.reference_type, Unset):
            reference_type = UNSET
        else:
            reference_type = self.reference_type

        reference_id: str | Unset = UNSET
        if not isinstance(self.reference_id, Unset):
            reference_id = str(self.reference_id)

        amount = self.amount

        net_amount = self.net_amount

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

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

        paid_at: str | Unset = UNSET
        if not isinstance(self.paid_at, Unset):
            paid_at = self.paid_at.isoformat()

        db_transaction_id: str | Unset = UNSET
        if not isinstance(self.db_transaction_id, Unset):
            db_transaction_id = str(self.db_transaction_id)

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

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, CompletedIntentDtoMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        recurring_contract_no: None | str | Unset
        if isinstance(self.recurring_contract_no, Unset):
            recurring_contract_no = UNSET
        else:
            recurring_contract_no = self.recurring_contract_no

        recurring_period_num: int | None | Unset
        if isinstance(self.recurring_period_num, Unset):
            recurring_period_num = UNSET
        else:
            recurring_period_num = self.recurring_period_num


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if payment_intent_id is not UNSET:
            field_dict["paymentIntentId"] = payment_intent_id
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id
        if payer_type is not UNSET:
            field_dict["payerType"] = payer_type
        if payer_id is not UNSET:
            field_dict["payerId"] = payer_id
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
        if provider_code is not UNSET:
            field_dict["providerCode"] = provider_code
        if provider_transaction_id is not UNSET:
            field_dict["providerTransactionId"] = provider_transaction_id
        if paid_at is not UNSET:
            field_dict["paidAt"] = paid_at
        if db_transaction_id is not UNSET:
            field_dict["dbTransactionId"] = db_transaction_id
        if provider_approval_code is not UNSET:
            field_dict["providerApprovalCode"] = provider_approval_code
        if payment_instrument is not UNSET:
            field_dict["paymentInstrument"] = payment_instrument
        if payment_instrument_detail is not UNSET:
            field_dict["paymentInstrumentDetail"] = payment_instrument_detail
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if recurring_contract_no is not UNSET:
            field_dict["recurringContractNo"] = recurring_contract_no
        if recurring_period_num is not UNSET:
            field_dict["recurringPeriodNum"] = recurring_period_num

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.completed_intent_dto_metadata_type_0 import CompletedIntentDtoMetadataType0 # noqa: PLC0415
        d = dict(src_dict)
        _payment_intent_id = d.pop("paymentIntentId", UNSET)
        payment_intent_id: UUID | Unset
        if isinstance(_payment_intent_id,  Unset):
            payment_intent_id = UNSET
        else:
            payment_intent_id = UUID(_payment_intent_id)




        _workspace_id = d.pop("workspaceId", UNSET)
        workspace_id: UUID | Unset
        if isinstance(_workspace_id,  Unset):
            workspace_id = UNSET
        else:
            workspace_id = UUID(_workspace_id)




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




        amount = d.pop("amount", UNSET)

        net_amount = d.pop("netAmount", UNSET)

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


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


        _paid_at = d.pop("paidAt", UNSET)
        paid_at: datetime.datetime | Unset
        if isinstance(_paid_at,  Unset):
            paid_at = UNSET
        else:
            paid_at = datetime.datetime.fromisoformat(_paid_at)




        _db_transaction_id = d.pop("dbTransactionId", UNSET)
        db_transaction_id: UUID | Unset
        if isinstance(_db_transaction_id,  Unset):
            db_transaction_id = UNSET
        else:
            db_transaction_id = UUID(_db_transaction_id)




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


        def _parse_metadata(data: object) -> CompletedIntentDtoMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = CompletedIntentDtoMetadataType0.from_dict(data)



                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompletedIntentDtoMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))


        def _parse_recurring_contract_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recurring_contract_no = _parse_recurring_contract_no(d.pop("recurringContractNo", UNSET))


        def _parse_recurring_period_num(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        recurring_period_num = _parse_recurring_period_num(d.pop("recurringPeriodNum", UNSET))


        completed_intent_dto = cls(
            payment_intent_id=payment_intent_id,
            workspace_id=workspace_id,
            payer_type=payer_type,
            payer_id=payer_id,
            reference_type=reference_type,
            reference_id=reference_id,
            amount=amount,
            net_amount=net_amount,
            currency=currency,
            provider_code=provider_code,
            provider_transaction_id=provider_transaction_id,
            paid_at=paid_at,
            db_transaction_id=db_transaction_id,
            provider_approval_code=provider_approval_code,
            payment_instrument=payment_instrument,
            payment_instrument_detail=payment_instrument_detail,
            metadata=metadata,
            recurring_contract_no=recurring_contract_no,
            recurring_period_num=recurring_period_num,
        )

        return completed_intent_dto


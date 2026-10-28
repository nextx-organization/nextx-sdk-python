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






T = TypeVar("T", bound="PaymentSubscriptionDto")



@_attrs_define
class PaymentSubscriptionDto:
    

    subscription_id: UUID | Unset = UNSET
    reference_type: None | str | Unset = UNSET
    reference_id: UUID | Unset = UNSET
    payer_type: None | str | Unset = UNSET
    payer_id: UUID | Unset = UNSET
    provider_code: None | str | Unset = UNSET
    amount: int | Unset = UNSET
    currency: None | str | Unset = UNSET
    billing_period: None | str | Unset = UNSET
    renewal_model: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    current_period_start: datetime.datetime | Unset = UNSET
    current_period_end: datetime.datetime | Unset = UNSET
    next_billing_date: datetime.datetime | Unset = UNSET
    reminder_days_before: int | Unset = UNSET
    grace_period_days: int | Unset = UNSET
    reminder_sent_at: datetime.datetime | None | Unset = UNSET
    suspended_at: datetime.datetime | None | Unset = UNSET
    cancelled_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        subscription_id: str | Unset = UNSET
        if not isinstance(self.subscription_id, Unset):
            subscription_id = str(self.subscription_id)

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

        provider_code: None | str | Unset
        if isinstance(self.provider_code, Unset):
            provider_code = UNSET
        else:
            provider_code = self.provider_code

        amount = self.amount

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        billing_period: None | str | Unset
        if isinstance(self.billing_period, Unset):
            billing_period = UNSET
        else:
            billing_period = self.billing_period

        renewal_model: None | str | Unset
        if isinstance(self.renewal_model, Unset):
            renewal_model = UNSET
        else:
            renewal_model = self.renewal_model

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        current_period_start: str | Unset = UNSET
        if not isinstance(self.current_period_start, Unset):
            current_period_start = self.current_period_start.isoformat()

        current_period_end: str | Unset = UNSET
        if not isinstance(self.current_period_end, Unset):
            current_period_end = self.current_period_end.isoformat()

        next_billing_date: str | Unset = UNSET
        if not isinstance(self.next_billing_date, Unset):
            next_billing_date = self.next_billing_date.isoformat()

        reminder_days_before = self.reminder_days_before

        grace_period_days = self.grace_period_days

        reminder_sent_at: None | str | Unset
        if isinstance(self.reminder_sent_at, Unset):
            reminder_sent_at = UNSET
        elif isinstance(self.reminder_sent_at, datetime.datetime):
            reminder_sent_at = self.reminder_sent_at.isoformat()
        else:
            reminder_sent_at = self.reminder_sent_at

        suspended_at: None | str | Unset
        if isinstance(self.suspended_at, Unset):
            suspended_at = UNSET
        elif isinstance(self.suspended_at, datetime.datetime):
            suspended_at = self.suspended_at.isoformat()
        else:
            suspended_at = self.suspended_at

        cancelled_at: None | str | Unset
        if isinstance(self.cancelled_at, Unset):
            cancelled_at = UNSET
        elif isinstance(self.cancelled_at, datetime.datetime):
            cancelled_at = self.cancelled_at.isoformat()
        else:
            cancelled_at = self.cancelled_at

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if reference_type is not UNSET:
            field_dict["referenceType"] = reference_type
        if reference_id is not UNSET:
            field_dict["referenceId"] = reference_id
        if payer_type is not UNSET:
            field_dict["payerType"] = payer_type
        if payer_id is not UNSET:
            field_dict["payerId"] = payer_id
        if provider_code is not UNSET:
            field_dict["providerCode"] = provider_code
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if billing_period is not UNSET:
            field_dict["billingPeriod"] = billing_period
        if renewal_model is not UNSET:
            field_dict["renewalModel"] = renewal_model
        if status is not UNSET:
            field_dict["status"] = status
        if current_period_start is not UNSET:
            field_dict["currentPeriodStart"] = current_period_start
        if current_period_end is not UNSET:
            field_dict["currentPeriodEnd"] = current_period_end
        if next_billing_date is not UNSET:
            field_dict["nextBillingDate"] = next_billing_date
        if reminder_days_before is not UNSET:
            field_dict["reminderDaysBefore"] = reminder_days_before
        if grace_period_days is not UNSET:
            field_dict["gracePeriodDays"] = grace_period_days
        if reminder_sent_at is not UNSET:
            field_dict["reminderSentAt"] = reminder_sent_at
        if suspended_at is not UNSET:
            field_dict["suspendedAt"] = suspended_at
        if cancelled_at is not UNSET:
            field_dict["cancelledAt"] = cancelled_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _subscription_id = d.pop("subscriptionId", UNSET)
        subscription_id: UUID | Unset
        if isinstance(_subscription_id,  Unset):
            subscription_id = UNSET
        else:
            subscription_id = UUID(_subscription_id)




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




        def _parse_provider_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_code = _parse_provider_code(d.pop("providerCode", UNSET))


        amount = d.pop("amount", UNSET)

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        def _parse_billing_period(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        billing_period = _parse_billing_period(d.pop("billingPeriod", UNSET))


        def _parse_renewal_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        renewal_model = _parse_renewal_model(d.pop("renewalModel", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        _current_period_start = d.pop("currentPeriodStart", UNSET)
        current_period_start: datetime.datetime | Unset
        if isinstance(_current_period_start,  Unset):
            current_period_start = UNSET
        else:
            current_period_start = datetime.datetime.fromisoformat(_current_period_start)




        _current_period_end = d.pop("currentPeriodEnd", UNSET)
        current_period_end: datetime.datetime | Unset
        if isinstance(_current_period_end,  Unset):
            current_period_end = UNSET
        else:
            current_period_end = datetime.datetime.fromisoformat(_current_period_end)




        _next_billing_date = d.pop("nextBillingDate", UNSET)
        next_billing_date: datetime.datetime | Unset
        if isinstance(_next_billing_date,  Unset):
            next_billing_date = UNSET
        else:
            next_billing_date = datetime.datetime.fromisoformat(_next_billing_date)




        reminder_days_before = d.pop("reminderDaysBefore", UNSET)

        grace_period_days = d.pop("gracePeriodDays", UNSET)

        def _parse_reminder_sent_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reminder_sent_at_type_0 = datetime.datetime.fromisoformat(data)



                return reminder_sent_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        reminder_sent_at = _parse_reminder_sent_at(d.pop("reminderSentAt", UNSET))


        def _parse_suspended_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                suspended_at_type_0 = datetime.datetime.fromisoformat(data)



                return suspended_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        suspended_at = _parse_suspended_at(d.pop("suspendedAt", UNSET))


        def _parse_cancelled_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cancelled_at_type_0 = datetime.datetime.fromisoformat(data)



                return cancelled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        cancelled_at = _parse_cancelled_at(d.pop("cancelledAt", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        payment_subscription_dto = cls(
            subscription_id=subscription_id,
            reference_type=reference_type,
            reference_id=reference_id,
            payer_type=payer_type,
            payer_id=payer_id,
            provider_code=provider_code,
            amount=amount,
            currency=currency,
            billing_period=billing_period,
            renewal_model=renewal_model,
            status=status,
            current_period_start=current_period_start,
            current_period_end=current_period_end,
            next_billing_date=next_billing_date,
            reminder_days_before=reminder_days_before,
            grace_period_days=grace_period_days,
            reminder_sent_at=reminder_sent_at,
            suspended_at=suspended_at,
            cancelled_at=cancelled_at,
            created_at=created_at,
        )

        return payment_subscription_dto


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.provider_breakdown_dto import ProviderBreakdownDto
  from ..models.reference_type_breakdown_dto import ReferenceTypeBreakdownDto





T = TypeVar("T", bound="PaymentOverviewDto")



@_attrs_define
class PaymentOverviewDto:
    

    from_: datetime.date | Unset = UNSET
    to: datetime.date | Unset = UNSET
    total_transactions: int | Unset = UNSET
    total_amount: int | Unset = UNSET
    total_net_amount: int | Unset = UNSET
    total_fees: int | Unset = UNSET
    total_refunds: int | Unset = UNSET
    active_subscriptions: int | Unset = UNSET
    pending_refunds: int | Unset = UNSET
    by_provider: list[ProviderBreakdownDto] | None | Unset = UNSET
    by_reference_type: list[ReferenceTypeBreakdownDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.provider_breakdown_dto import ProviderBreakdownDto # noqa: PLC0415
        from ..models.reference_type_breakdown_dto import ReferenceTypeBreakdownDto # noqa: PLC0415
        from_: str | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        to: str | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat()

        total_transactions = self.total_transactions

        total_amount = self.total_amount

        total_net_amount = self.total_net_amount

        total_fees = self.total_fees

        total_refunds = self.total_refunds

        active_subscriptions = self.active_subscriptions

        pending_refunds = self.pending_refunds

        by_provider: list[dict[str, Any]] | None | Unset
        if isinstance(self.by_provider, Unset):
            by_provider = UNSET
        elif isinstance(self.by_provider, list):
            by_provider = []
            for by_provider_type_0_item_data in self.by_provider:
                by_provider_type_0_item = by_provider_type_0_item_data.to_dict()
                by_provider.append(by_provider_type_0_item)


        else:
            by_provider = self.by_provider

        by_reference_type: list[dict[str, Any]] | None | Unset
        if isinstance(self.by_reference_type, Unset):
            by_reference_type = UNSET
        elif isinstance(self.by_reference_type, list):
            by_reference_type = []
            for by_reference_type_type_0_item_data in self.by_reference_type:
                by_reference_type_type_0_item = by_reference_type_type_0_item_data.to_dict()
                by_reference_type.append(by_reference_type_type_0_item)


        else:
            by_reference_type = self.by_reference_type


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if total_transactions is not UNSET:
            field_dict["totalTransactions"] = total_transactions
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if total_net_amount is not UNSET:
            field_dict["totalNetAmount"] = total_net_amount
        if total_fees is not UNSET:
            field_dict["totalFees"] = total_fees
        if total_refunds is not UNSET:
            field_dict["totalRefunds"] = total_refunds
        if active_subscriptions is not UNSET:
            field_dict["activeSubscriptions"] = active_subscriptions
        if pending_refunds is not UNSET:
            field_dict["pendingRefunds"] = pending_refunds
        if by_provider is not UNSET:
            field_dict["byProvider"] = by_provider
        if by_reference_type is not UNSET:
            field_dict["byReferenceType"] = by_reference_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_breakdown_dto import ProviderBreakdownDto # noqa: PLC0415
        from ..models.reference_type_breakdown_dto import ReferenceTypeBreakdownDto # noqa: PLC0415
        d = dict(src_dict)
        _from_ = d.pop("from", UNSET)
        from_: datetime.date | Unset
        if isinstance(_from_,  Unset):
            from_ = UNSET
        else:
            from_ = datetime.date.fromisoformat(_from_)




        _to = d.pop("to", UNSET)
        to: datetime.date | Unset
        if isinstance(_to,  Unset):
            to = UNSET
        else:
            to = datetime.date.fromisoformat(_to)




        total_transactions = d.pop("totalTransactions", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        total_net_amount = d.pop("totalNetAmount", UNSET)

        total_fees = d.pop("totalFees", UNSET)

        total_refunds = d.pop("totalRefunds", UNSET)

        active_subscriptions = d.pop("activeSubscriptions", UNSET)

        pending_refunds = d.pop("pendingRefunds", UNSET)

        def _parse_by_provider(data: object) -> list[ProviderBreakdownDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                by_provider_type_0 = []
                _by_provider_type_0 = data
                for by_provider_type_0_item_data in (_by_provider_type_0):
                    by_provider_type_0_item = ProviderBreakdownDto.from_dict(by_provider_type_0_item_data)



                    by_provider_type_0.append(by_provider_type_0_item)

                return by_provider_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProviderBreakdownDto] | None | Unset, data)

        by_provider = _parse_by_provider(d.pop("byProvider", UNSET))


        def _parse_by_reference_type(data: object) -> list[ReferenceTypeBreakdownDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                by_reference_type_type_0 = []
                _by_reference_type_type_0 = data
                for by_reference_type_type_0_item_data in (_by_reference_type_type_0):
                    by_reference_type_type_0_item = ReferenceTypeBreakdownDto.from_dict(by_reference_type_type_0_item_data)



                    by_reference_type_type_0.append(by_reference_type_type_0_item)

                return by_reference_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ReferenceTypeBreakdownDto] | None | Unset, data)

        by_reference_type = _parse_by_reference_type(d.pop("byReferenceType", UNSET))


        payment_overview_dto = cls(
            from_=from_,
            to=to,
            total_transactions=total_transactions,
            total_amount=total_amount,
            total_net_amount=total_net_amount,
            total_fees=total_fees,
            total_refunds=total_refunds,
            active_subscriptions=active_subscriptions,
            pending_refunds=pending_refunds,
            by_provider=by_provider,
            by_reference_type=by_reference_type,
        )

        return payment_overview_dto


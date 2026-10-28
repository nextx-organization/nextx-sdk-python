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






T = TypeVar("T", bound="OrderReturnSummaryDto")



@_attrs_define
class OrderReturnSummaryDto:
    

    id: UUID | Unset = UNSET
    return_code: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    return_type: None | str | Unset = UNSET
    refund_amount: float | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    exchange_new_order_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        return_code: None | str | Unset
        if isinstance(self.return_code, Unset):
            return_code = UNSET
        else:
            return_code = self.return_code

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        return_type: None | str | Unset
        if isinstance(self.return_type, Unset):
            return_type = UNSET
        else:
            return_type = self.return_type

        refund_amount = self.refund_amount

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        exchange_new_order_id: None | str | Unset
        if isinstance(self.exchange_new_order_id, Unset):
            exchange_new_order_id = UNSET
        elif isinstance(self.exchange_new_order_id, UUID):
            exchange_new_order_id = str(self.exchange_new_order_id)
        else:
            exchange_new_order_id = self.exchange_new_order_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if return_code is not UNSET:
            field_dict["returnCode"] = return_code
        if status is not UNSET:
            field_dict["status"] = status
        if return_type is not UNSET:
            field_dict["returnType"] = return_type
        if refund_amount is not UNSET:
            field_dict["refundAmount"] = refund_amount
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if exchange_new_order_id is not UNSET:
            field_dict["exchangeNewOrderId"] = exchange_new_order_id

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




        def _parse_return_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        return_code = _parse_return_code(d.pop("returnCode", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_return_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        return_type = _parse_return_type(d.pop("returnType", UNSET))


        refund_amount = d.pop("refundAmount", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_exchange_new_order_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                exchange_new_order_id_type_0 = UUID(data)



                return exchange_new_order_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        exchange_new_order_id = _parse_exchange_new_order_id(d.pop("exchangeNewOrderId", UNSET))


        order_return_summary_dto = cls(
            id=id,
            return_code=return_code,
            status=status,
            return_type=return_type,
            refund_amount=refund_amount,
            created_at=created_at,
            exchange_new_order_id=exchange_new_order_id,
        )

        return order_return_summary_dto


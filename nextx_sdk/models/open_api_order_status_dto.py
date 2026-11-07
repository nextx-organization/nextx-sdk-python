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
  from ..models.open_api_order_shipment_dto import OpenApiOrderShipmentDto





T = TypeVar("T", bound="OpenApiOrderStatusDto")



@_attrs_define
class OpenApiOrderStatusDto:
    

    order_id: UUID | Unset = UNSET
    order_code: None | str | Unset = UNSET
    external_order_id: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    total: float | Unset = UNSET
    paid_amount: float | Unset = UNSET
    debt_amount: float | Unset = UNSET
    payment_status: None | str | Unset = UNSET
    delivery_status: None | str | Unset = UNSET
    delivered_at: datetime.datetime | None | Unset = UNSET
    shipment: OpenApiOrderShipmentDto | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    idempotent_replay: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.open_api_order_shipment_dto import OpenApiOrderShipmentDto # noqa: PLC0415
        order_id: str | Unset = UNSET
        if not isinstance(self.order_id, Unset):
            order_id = str(self.order_id)

        order_code: None | str | Unset
        if isinstance(self.order_code, Unset):
            order_code = UNSET
        else:
            order_code = self.order_code

        external_order_id: None | str | Unset
        if isinstance(self.external_order_id, Unset):
            external_order_id = UNSET
        else:
            external_order_id = self.external_order_id

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        total = self.total

        paid_amount = self.paid_amount

        debt_amount = self.debt_amount

        payment_status: None | str | Unset
        if isinstance(self.payment_status, Unset):
            payment_status = UNSET
        else:
            payment_status = self.payment_status

        delivery_status: None | str | Unset
        if isinstance(self.delivery_status, Unset):
            delivery_status = UNSET
        else:
            delivery_status = self.delivery_status

        delivered_at: None | str | Unset
        if isinstance(self.delivered_at, Unset):
            delivered_at = UNSET
        elif isinstance(self.delivered_at, datetime.datetime):
            delivered_at = self.delivered_at.isoformat()
        else:
            delivered_at = self.delivered_at

        shipment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shipment, Unset):
            shipment = self.shipment.to_dict()

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        idempotent_replay = self.idempotent_replay


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if order_id is not UNSET:
            field_dict["orderId"] = order_id
        if order_code is not UNSET:
            field_dict["orderCode"] = order_code
        if external_order_id is not UNSET:
            field_dict["externalOrderId"] = external_order_id
        if status is not UNSET:
            field_dict["status"] = status
        if total is not UNSET:
            field_dict["total"] = total
        if paid_amount is not UNSET:
            field_dict["paidAmount"] = paid_amount
        if debt_amount is not UNSET:
            field_dict["debtAmount"] = debt_amount
        if payment_status is not UNSET:
            field_dict["paymentStatus"] = payment_status
        if delivery_status is not UNSET:
            field_dict["deliveryStatus"] = delivery_status
        if delivered_at is not UNSET:
            field_dict["deliveredAt"] = delivered_at
        if shipment is not UNSET:
            field_dict["shipment"] = shipment
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if idempotent_replay is not UNSET:
            field_dict["idempotentReplay"] = idempotent_replay

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_api_order_shipment_dto import OpenApiOrderShipmentDto # noqa: PLC0415
        d = dict(src_dict)
        _order_id = d.pop("orderId", UNSET)
        order_id: UUID | Unset
        if isinstance(_order_id,  Unset):
            order_id = UNSET
        else:
            order_id = UUID(_order_id)




        def _parse_order_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        order_code = _parse_order_code(d.pop("orderCode", UNSET))


        def _parse_external_order_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_order_id = _parse_external_order_id(d.pop("externalOrderId", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        total = d.pop("total", UNSET)

        paid_amount = d.pop("paidAmount", UNSET)

        debt_amount = d.pop("debtAmount", UNSET)

        def _parse_payment_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_status = _parse_payment_status(d.pop("paymentStatus", UNSET))


        def _parse_delivery_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        delivery_status = _parse_delivery_status(d.pop("deliveryStatus", UNSET))


        def _parse_delivered_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delivered_at_type_0 = datetime.datetime.fromisoformat(data)



                return delivered_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        delivered_at = _parse_delivered_at(d.pop("deliveredAt", UNSET))


        _shipment = d.pop("shipment", UNSET)
        shipment: OpenApiOrderShipmentDto | Unset
        if isinstance(_shipment,  Unset):
            shipment = UNSET
        else:
            shipment = OpenApiOrderShipmentDto.from_dict(_shipment)




        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)



                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))


        idempotent_replay = d.pop("idempotentReplay", UNSET)

        open_api_order_status_dto = cls(
            order_id=order_id,
            order_code=order_code,
            external_order_id=external_order_id,
            status=status,
            total=total,
            paid_amount=paid_amount,
            debt_amount=debt_amount,
            payment_status=payment_status,
            delivery_status=delivery_status,
            delivered_at=delivered_at,
            shipment=shipment,
            created_at=created_at,
            updated_at=updated_at,
            idempotent_replay=idempotent_replay,
        )

        return open_api_order_status_dto


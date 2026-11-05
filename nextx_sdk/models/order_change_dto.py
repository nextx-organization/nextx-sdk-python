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






T = TypeVar("T", bound="OrderChangeDto")



@_attrs_define
class OrderChangeDto:
    

    id: UUID | Unset = UNSET
    code: None | str | Unset = UNSET
    order_type: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    crm_contact_id: None | Unset | UUID = UNSET
    branch_id: UUID | Unset = UNSET
    subtotal: float | Unset = UNSET
    discount_amount: float | Unset = UNSET
    tax_amount: float | Unset = UNSET
    shipping_fee: float | Unset = UNSET
    total: float | Unset = UNSET
    paid_amount: float | Unset = UNSET
    channel_code: None | str | Unset = UNSET
    order_date: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    confirmed_at: datetime.datetime | None | Unset = UNSET
    cancelled_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    is_deleted: bool | Unset = UNSET
    deleted_at: datetime.datetime | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        order_type: None | str | Unset
        if isinstance(self.order_type, Unset):
            order_type = UNSET
        else:
            order_type = self.order_type

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        crm_contact_id: None | str | Unset
        if isinstance(self.crm_contact_id, Unset):
            crm_contact_id = UNSET
        elif isinstance(self.crm_contact_id, UUID):
            crm_contact_id = str(self.crm_contact_id)
        else:
            crm_contact_id = self.crm_contact_id

        branch_id: str | Unset = UNSET
        if not isinstance(self.branch_id, Unset):
            branch_id = str(self.branch_id)

        subtotal = self.subtotal

        discount_amount = self.discount_amount

        tax_amount = self.tax_amount

        shipping_fee = self.shipping_fee

        total = self.total

        paid_amount = self.paid_amount

        channel_code: None | str | Unset
        if isinstance(self.channel_code, Unset):
            channel_code = UNSET
        else:
            channel_code = self.channel_code

        order_date: None | str | Unset
        if isinstance(self.order_date, Unset):
            order_date = UNSET
        elif isinstance(self.order_date, datetime.datetime):
            order_date = self.order_date.isoformat()
        else:
            order_date = self.order_date

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        confirmed_at: None | str | Unset
        if isinstance(self.confirmed_at, Unset):
            confirmed_at = UNSET
        elif isinstance(self.confirmed_at, datetime.datetime):
            confirmed_at = self.confirmed_at.isoformat()
        else:
            confirmed_at = self.confirmed_at

        cancelled_at: None | str | Unset
        if isinstance(self.cancelled_at, Unset):
            cancelled_at = UNSET
        elif isinstance(self.cancelled_at, datetime.datetime):
            cancelled_at = self.cancelled_at.isoformat()
        else:
            cancelled_at = self.cancelled_at

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        is_deleted = self.is_deleted

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        elif isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if code is not UNSET:
            field_dict["code"] = code
        if order_type is not UNSET:
            field_dict["orderType"] = order_type
        if status is not UNSET:
            field_dict["status"] = status
        if crm_contact_id is not UNSET:
            field_dict["crmContactId"] = crm_contact_id
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id
        if subtotal is not UNSET:
            field_dict["subtotal"] = subtotal
        if discount_amount is not UNSET:
            field_dict["discountAmount"] = discount_amount
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if shipping_fee is not UNSET:
            field_dict["shippingFee"] = shipping_fee
        if total is not UNSET:
            field_dict["total"] = total
        if paid_amount is not UNSET:
            field_dict["paidAmount"] = paid_amount
        if channel_code is not UNSET:
            field_dict["channelCode"] = channel_code
        if order_date is not UNSET:
            field_dict["orderDate"] = order_date
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if confirmed_at is not UNSET:
            field_dict["confirmedAt"] = confirmed_at
        if cancelled_at is not UNSET:
            field_dict["cancelledAt"] = cancelled_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at

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




        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        def _parse_order_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        order_type = _parse_order_type(d.pop("orderType", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_crm_contact_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                crm_contact_id_type_0 = UUID(data)



                return crm_contact_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        crm_contact_id = _parse_crm_contact_id(d.pop("crmContactId", UNSET))


        _branch_id = d.pop("branchId", UNSET)
        branch_id: UUID | Unset
        if isinstance(_branch_id,  Unset):
            branch_id = UNSET
        else:
            branch_id = UUID(_branch_id)




        subtotal = d.pop("subtotal", UNSET)

        discount_amount = d.pop("discountAmount", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        shipping_fee = d.pop("shippingFee", UNSET)

        total = d.pop("total", UNSET)

        paid_amount = d.pop("paidAmount", UNSET)

        def _parse_channel_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel_code = _parse_channel_code(d.pop("channelCode", UNSET))


        def _parse_order_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                order_date_type_0 = datetime.datetime.fromisoformat(data)



                return order_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        order_date = _parse_order_date(d.pop("orderDate", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_confirmed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                confirmed_at_type_0 = datetime.datetime.fromisoformat(data)



                return confirmed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        confirmed_at = _parse_confirmed_at(d.pop("confirmedAt", UNSET))


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


        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)




        is_deleted = d.pop("isDeleted", UNSET)

        def _parse_deleted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_at_type_0 = datetime.datetime.fromisoformat(data)



                return deleted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        order_change_dto = cls(
            id=id,
            code=code,
            order_type=order_type,
            status=status,
            crm_contact_id=crm_contact_id,
            branch_id=branch_id,
            subtotal=subtotal,
            discount_amount=discount_amount,
            tax_amount=tax_amount,
            shipping_fee=shipping_fee,
            total=total,
            paid_amount=paid_amount,
            channel_code=channel_code,
            order_date=order_date,
            created_at=created_at,
            confirmed_at=confirmed_at,
            cancelled_at=cancelled_at,
            updated_at=updated_at,
            is_deleted=is_deleted,
            deleted_at=deleted_at,
        )

        return order_change_dto


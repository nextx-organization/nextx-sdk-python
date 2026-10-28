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
  from ..models.sales_order_payment_dto import SalesOrderPaymentDto





T = TypeVar("T", bound="SalesOrderDto")



@_attrs_define
class SalesOrderDto:
    

    id: UUID | Unset = UNSET
    order_code: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    total_amount: float | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    payment_method: None | str | Unset = UNSET
    payment_status: None | str | Unset = UNSET
    branch_id: None | Unset | UUID = UNSET
    branch_name: None | str | Unset = UNSET
    assigned_to: None | Unset | UUID = UNSET
    assigned_to_name: None | str | Unset = UNSET
    crm_contact_id: None | Unset | UUID = UNSET
    contact_name: None | str | Unset = UNSET
    order_type: None | str | Unset = UNSET
    outlet_id: None | Unset | UUID = UNSET
    outlet_name: None | str | Unset = UNSET
    deposit_amount: float | Unset = UNSET
    expected_delivery_date: datetime.datetime | None | Unset = UNSET
    paid_amount: float | None | Unset = UNSET
    debt_amount: float | None | Unset = UNSET
    item_count: int | None | Unset = UNSET
    subtotal: float | Unset = UNSET
    discount_amount: float | Unset = UNSET
    tax_amount: float | Unset = UNSET
    shipping_fee: float | Unset = UNSET
    total_quantity: float | Unset = UNSET
    customer_code: None | str | Unset = UNSET
    delivery_employee_id: None | Unset | UUID = UNSET
    delivery_employee_name: None | str | Unset = UNSET
    delivery_id: None | Unset | UUID = UNSET
    delivery_status: None | str | Unset = UNSET
    delivered_at: datetime.datetime | None | Unset = UNSET
    last_payment_date: datetime.datetime | None | Unset = UNSET
    payments: list[SalesOrderPaymentDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.sales_order_payment_dto import SalesOrderPaymentDto # noqa: PLC0415
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        order_code: None | str | Unset
        if isinstance(self.order_code, Unset):
            order_code = UNSET
        else:
            order_code = self.order_code

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        total_amount = self.total_amount

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        payment_method: None | str | Unset
        if isinstance(self.payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = self.payment_method

        payment_status: None | str | Unset
        if isinstance(self.payment_status, Unset):
            payment_status = UNSET
        else:
            payment_status = self.payment_status

        branch_id: None | str | Unset
        if isinstance(self.branch_id, Unset):
            branch_id = UNSET
        elif isinstance(self.branch_id, UUID):
            branch_id = str(self.branch_id)
        else:
            branch_id = self.branch_id

        branch_name: None | str | Unset
        if isinstance(self.branch_name, Unset):
            branch_name = UNSET
        else:
            branch_name = self.branch_name

        assigned_to: None | str | Unset
        if isinstance(self.assigned_to, Unset):
            assigned_to = UNSET
        elif isinstance(self.assigned_to, UUID):
            assigned_to = str(self.assigned_to)
        else:
            assigned_to = self.assigned_to

        assigned_to_name: None | str | Unset
        if isinstance(self.assigned_to_name, Unset):
            assigned_to_name = UNSET
        else:
            assigned_to_name = self.assigned_to_name

        crm_contact_id: None | str | Unset
        if isinstance(self.crm_contact_id, Unset):
            crm_contact_id = UNSET
        elif isinstance(self.crm_contact_id, UUID):
            crm_contact_id = str(self.crm_contact_id)
        else:
            crm_contact_id = self.crm_contact_id

        contact_name: None | str | Unset
        if isinstance(self.contact_name, Unset):
            contact_name = UNSET
        else:
            contact_name = self.contact_name

        order_type: None | str | Unset
        if isinstance(self.order_type, Unset):
            order_type = UNSET
        else:
            order_type = self.order_type

        outlet_id: None | str | Unset
        if isinstance(self.outlet_id, Unset):
            outlet_id = UNSET
        elif isinstance(self.outlet_id, UUID):
            outlet_id = str(self.outlet_id)
        else:
            outlet_id = self.outlet_id

        outlet_name: None | str | Unset
        if isinstance(self.outlet_name, Unset):
            outlet_name = UNSET
        else:
            outlet_name = self.outlet_name

        deposit_amount = self.deposit_amount

        expected_delivery_date: None | str | Unset
        if isinstance(self.expected_delivery_date, Unset):
            expected_delivery_date = UNSET
        elif isinstance(self.expected_delivery_date, datetime.datetime):
            expected_delivery_date = self.expected_delivery_date.isoformat()
        else:
            expected_delivery_date = self.expected_delivery_date

        paid_amount: float | None | Unset
        if isinstance(self.paid_amount, Unset):
            paid_amount = UNSET
        else:
            paid_amount = self.paid_amount

        debt_amount: float | None | Unset
        if isinstance(self.debt_amount, Unset):
            debt_amount = UNSET
        else:
            debt_amount = self.debt_amount

        item_count: int | None | Unset
        if isinstance(self.item_count, Unset):
            item_count = UNSET
        else:
            item_count = self.item_count

        subtotal = self.subtotal

        discount_amount = self.discount_amount

        tax_amount = self.tax_amount

        shipping_fee = self.shipping_fee

        total_quantity = self.total_quantity

        customer_code: None | str | Unset
        if isinstance(self.customer_code, Unset):
            customer_code = UNSET
        else:
            customer_code = self.customer_code

        delivery_employee_id: None | str | Unset
        if isinstance(self.delivery_employee_id, Unset):
            delivery_employee_id = UNSET
        elif isinstance(self.delivery_employee_id, UUID):
            delivery_employee_id = str(self.delivery_employee_id)
        else:
            delivery_employee_id = self.delivery_employee_id

        delivery_employee_name: None | str | Unset
        if isinstance(self.delivery_employee_name, Unset):
            delivery_employee_name = UNSET
        else:
            delivery_employee_name = self.delivery_employee_name

        delivery_id: None | str | Unset
        if isinstance(self.delivery_id, Unset):
            delivery_id = UNSET
        elif isinstance(self.delivery_id, UUID):
            delivery_id = str(self.delivery_id)
        else:
            delivery_id = self.delivery_id

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

        last_payment_date: None | str | Unset
        if isinstance(self.last_payment_date, Unset):
            last_payment_date = UNSET
        elif isinstance(self.last_payment_date, datetime.datetime):
            last_payment_date = self.last_payment_date.isoformat()
        else:
            last_payment_date = self.last_payment_date

        payments: list[dict[str, Any]] | None | Unset
        if isinstance(self.payments, Unset):
            payments = UNSET
        elif isinstance(self.payments, list):
            payments = []
            for payments_type_0_item_data in self.payments:
                payments_type_0_item = payments_type_0_item_data.to_dict()
                payments.append(payments_type_0_item)


        else:
            payments = self.payments


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if order_code is not UNSET:
            field_dict["orderCode"] = order_code
        if status is not UNSET:
            field_dict["status"] = status
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method
        if payment_status is not UNSET:
            field_dict["paymentStatus"] = payment_status
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id
        if branch_name is not UNSET:
            field_dict["branchName"] = branch_name
        if assigned_to is not UNSET:
            field_dict["assignedTo"] = assigned_to
        if assigned_to_name is not UNSET:
            field_dict["assignedToName"] = assigned_to_name
        if crm_contact_id is not UNSET:
            field_dict["crmContactId"] = crm_contact_id
        if contact_name is not UNSET:
            field_dict["contactName"] = contact_name
        if order_type is not UNSET:
            field_dict["orderType"] = order_type
        if outlet_id is not UNSET:
            field_dict["outletId"] = outlet_id
        if outlet_name is not UNSET:
            field_dict["outletName"] = outlet_name
        if deposit_amount is not UNSET:
            field_dict["depositAmount"] = deposit_amount
        if expected_delivery_date is not UNSET:
            field_dict["expectedDeliveryDate"] = expected_delivery_date
        if paid_amount is not UNSET:
            field_dict["paidAmount"] = paid_amount
        if debt_amount is not UNSET:
            field_dict["debtAmount"] = debt_amount
        if item_count is not UNSET:
            field_dict["itemCount"] = item_count
        if subtotal is not UNSET:
            field_dict["subtotal"] = subtotal
        if discount_amount is not UNSET:
            field_dict["discountAmount"] = discount_amount
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if shipping_fee is not UNSET:
            field_dict["shippingFee"] = shipping_fee
        if total_quantity is not UNSET:
            field_dict["totalQuantity"] = total_quantity
        if customer_code is not UNSET:
            field_dict["customerCode"] = customer_code
        if delivery_employee_id is not UNSET:
            field_dict["deliveryEmployeeId"] = delivery_employee_id
        if delivery_employee_name is not UNSET:
            field_dict["deliveryEmployeeName"] = delivery_employee_name
        if delivery_id is not UNSET:
            field_dict["deliveryId"] = delivery_id
        if delivery_status is not UNSET:
            field_dict["deliveryStatus"] = delivery_status
        if delivered_at is not UNSET:
            field_dict["deliveredAt"] = delivered_at
        if last_payment_date is not UNSET:
            field_dict["lastPaymentDate"] = last_payment_date
        if payments is not UNSET:
            field_dict["payments"] = payments

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sales_order_payment_dto import SalesOrderPaymentDto # noqa: PLC0415
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_order_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        order_code = _parse_order_code(d.pop("orderCode", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        total_amount = d.pop("totalAmount", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_payment_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_method = _parse_payment_method(d.pop("paymentMethod", UNSET))


        def _parse_payment_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_status = _parse_payment_status(d.pop("paymentStatus", UNSET))


        def _parse_branch_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                branch_id_type_0 = UUID(data)



                return branch_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        branch_id = _parse_branch_id(d.pop("branchId", UNSET))


        def _parse_branch_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch_name = _parse_branch_name(d.pop("branchName", UNSET))


        def _parse_assigned_to(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                assigned_to_type_0 = UUID(data)



                return assigned_to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        assigned_to = _parse_assigned_to(d.pop("assignedTo", UNSET))


        def _parse_assigned_to_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assigned_to_name = _parse_assigned_to_name(d.pop("assignedToName", UNSET))


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


        def _parse_contact_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_name = _parse_contact_name(d.pop("contactName", UNSET))


        def _parse_order_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        order_type = _parse_order_type(d.pop("orderType", UNSET))


        def _parse_outlet_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                outlet_id_type_0 = UUID(data)



                return outlet_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        outlet_id = _parse_outlet_id(d.pop("outletId", UNSET))


        def _parse_outlet_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        outlet_name = _parse_outlet_name(d.pop("outletName", UNSET))


        deposit_amount = d.pop("depositAmount", UNSET)

        def _parse_expected_delivery_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expected_delivery_date_type_0 = datetime.datetime.fromisoformat(data)



                return expected_delivery_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expected_delivery_date = _parse_expected_delivery_date(d.pop("expectedDeliveryDate", UNSET))


        def _parse_paid_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        paid_amount = _parse_paid_amount(d.pop("paidAmount", UNSET))


        def _parse_debt_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        debt_amount = _parse_debt_amount(d.pop("debtAmount", UNSET))


        def _parse_item_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        item_count = _parse_item_count(d.pop("itemCount", UNSET))


        subtotal = d.pop("subtotal", UNSET)

        discount_amount = d.pop("discountAmount", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        shipping_fee = d.pop("shippingFee", UNSET)

        total_quantity = d.pop("totalQuantity", UNSET)

        def _parse_customer_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_code = _parse_customer_code(d.pop("customerCode", UNSET))


        def _parse_delivery_employee_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delivery_employee_id_type_0 = UUID(data)



                return delivery_employee_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        delivery_employee_id = _parse_delivery_employee_id(d.pop("deliveryEmployeeId", UNSET))


        def _parse_delivery_employee_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        delivery_employee_name = _parse_delivery_employee_name(d.pop("deliveryEmployeeName", UNSET))


        def _parse_delivery_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delivery_id_type_0 = UUID(data)



                return delivery_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        delivery_id = _parse_delivery_id(d.pop("deliveryId", UNSET))


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


        def _parse_last_payment_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_payment_date_type_0 = datetime.datetime.fromisoformat(data)



                return last_payment_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_payment_date = _parse_last_payment_date(d.pop("lastPaymentDate", UNSET))


        def _parse_payments(data: object) -> list[SalesOrderPaymentDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                payments_type_0 = []
                _payments_type_0 = data
                for payments_type_0_item_data in (_payments_type_0):
                    payments_type_0_item = SalesOrderPaymentDto.from_dict(payments_type_0_item_data)



                    payments_type_0.append(payments_type_0_item)

                return payments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SalesOrderPaymentDto] | None | Unset, data)

        payments = _parse_payments(d.pop("payments", UNSET))


        sales_order_dto = cls(
            id=id,
            order_code=order_code,
            status=status,
            total_amount=total_amount,
            created_at=created_at,
            payment_method=payment_method,
            payment_status=payment_status,
            branch_id=branch_id,
            branch_name=branch_name,
            assigned_to=assigned_to,
            assigned_to_name=assigned_to_name,
            crm_contact_id=crm_contact_id,
            contact_name=contact_name,
            order_type=order_type,
            outlet_id=outlet_id,
            outlet_name=outlet_name,
            deposit_amount=deposit_amount,
            expected_delivery_date=expected_delivery_date,
            paid_amount=paid_amount,
            debt_amount=debt_amount,
            item_count=item_count,
            subtotal=subtotal,
            discount_amount=discount_amount,
            tax_amount=tax_amount,
            shipping_fee=shipping_fee,
            total_quantity=total_quantity,
            customer_code=customer_code,
            delivery_employee_id=delivery_employee_id,
            delivery_employee_name=delivery_employee_name,
            delivery_id=delivery_id,
            delivery_status=delivery_status,
            delivered_at=delivered_at,
            last_payment_date=last_payment_date,
            payments=payments,
        )

        return sales_order_dto


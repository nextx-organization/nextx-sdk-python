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
  from ..models.order_assignee_dto import OrderAssigneeDto
  from ..models.order_list_customer_info_dto import OrderListCustomerInfoDto
  from ..models.order_list_outlet_info_dto import OrderListOutletInfoDto
  from ..models.order_payment_entry_dto import OrderPaymentEntryDto
  from ..models.payment_row_dto import PaymentRowDto
  from ..models.user_ref_dto import UserRefDto





T = TypeVar("T", bound="OrderListDto")



@_attrs_define
class OrderListDto:
    

    id: UUID | Unset = UNSET
    code: None | str | Unset = UNSET
    order_type: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    sales_customer_id: UUID | Unset = UNSET
    contact_name: None | str | Unset = UNSET
    contact_phone: None | str | Unset = UNSET
    customer_code: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    branch_id: UUID | Unset = UNSET
    branch_name: None | str | Unset = UNSET
    subtotal: float | Unset = UNSET
    discount_amount: float | Unset = UNSET
    tax_amount: float | Unset = UNSET
    shipping_fee: float | Unset = UNSET
    total: float | Unset = UNSET
    paid_amount: float | Unset = UNSET
    debt_amount: float | Unset = UNSET
    debt_status: None | str | Unset = UNSET
    payment_method: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    notes: None | str | Unset = UNSET
    vat_mode: None | str | Unset = UNSET
    confirmed_at: datetime.datetime | None | Unset = UNSET
    cancelled_at: datetime.datetime | None | Unset = UNSET
    cancel_reason: None | str | Unset = UNSET
    item_count: int | Unset = UNSET
    assigned_to: UserRefDto | Unset = UNSET
    assignees: list[OrderAssigneeDto] | None | Unset = UNSET
    unit_code: None | str | Unset = UNSET
    unit_name: None | str | Unset = UNSET
    payment_breakdown: list[PaymentRowDto] | None | Unset = UNSET
    return_status: None | str | Unset = UNSET
    has_open_return: bool | Unset = UNSET
    channel_code: None | str | Unset = UNSET
    order_date: datetime.datetime | None | Unset = UNSET
    e_invoice_status: None | str | Unset = UNSET
    e_invoice_number: None | str | Unset = UNSET
    vat_exported_at: datetime.datetime | None | Unset = UNSET
    outlet_id: None | Unset | UUID = UNSET
    delivery_employee: UserRefDto | Unset = UNSET
    expected_delivery_date: datetime.datetime | None | Unset = UNSET
    deposit_amount: float | Unset = UNSET
    delivery_status: None | str | Unset = UNSET
    internal_notes: None | str | Unset = UNSET
    delivered_at: datetime.datetime | None | Unset = UNSET
    last_payment_date: datetime.datetime | None | Unset = UNSET
    payments: list[OrderPaymentEntryDto] | None | Unset = UNSET
    delivery_address: None | str | Unset = UNSET
    delivery_name: None | str | Unset = UNSET
    delivery_phone: None | str | Unset = UNSET
    customer_info: OrderListCustomerInfoDto | Unset = UNSET
    outlet_info: OrderListOutletInfoDto | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.order_assignee_dto import OrderAssigneeDto # noqa: PLC0415
        from ..models.order_list_customer_info_dto import OrderListCustomerInfoDto # noqa: PLC0415
        from ..models.order_list_outlet_info_dto import OrderListOutletInfoDto # noqa: PLC0415
        from ..models.order_payment_entry_dto import OrderPaymentEntryDto # noqa: PLC0415
        from ..models.payment_row_dto import PaymentRowDto # noqa: PLC0415
        from ..models.user_ref_dto import UserRefDto # noqa: PLC0415
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

        sales_customer_id: str | Unset = UNSET
        if not isinstance(self.sales_customer_id, Unset):
            sales_customer_id = str(self.sales_customer_id)

        contact_name: None | str | Unset
        if isinstance(self.contact_name, Unset):
            contact_name = UNSET
        else:
            contact_name = self.contact_name

        contact_phone: None | str | Unset
        if isinstance(self.contact_phone, Unset):
            contact_phone = UNSET
        else:
            contact_phone = self.contact_phone

        customer_code: None | str | Unset
        if isinstance(self.customer_code, Unset):
            customer_code = UNSET
        else:
            customer_code = self.customer_code

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        branch_id: str | Unset = UNSET
        if not isinstance(self.branch_id, Unset):
            branch_id = str(self.branch_id)

        branch_name: None | str | Unset
        if isinstance(self.branch_name, Unset):
            branch_name = UNSET
        else:
            branch_name = self.branch_name

        subtotal = self.subtotal

        discount_amount = self.discount_amount

        tax_amount = self.tax_amount

        shipping_fee = self.shipping_fee

        total = self.total

        paid_amount = self.paid_amount

        debt_amount = self.debt_amount

        debt_status: None | str | Unset
        if isinstance(self.debt_status, Unset):
            debt_status = UNSET
        else:
            debt_status = self.debt_status

        payment_method: None | str | Unset
        if isinstance(self.payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = self.payment_method

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        vat_mode: None | str | Unset
        if isinstance(self.vat_mode, Unset):
            vat_mode = UNSET
        else:
            vat_mode = self.vat_mode

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

        cancel_reason: None | str | Unset
        if isinstance(self.cancel_reason, Unset):
            cancel_reason = UNSET
        else:
            cancel_reason = self.cancel_reason

        item_count = self.item_count

        assigned_to: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assigned_to, Unset):
            assigned_to = self.assigned_to.to_dict()

        assignees: list[dict[str, Any]] | None | Unset
        if isinstance(self.assignees, Unset):
            assignees = UNSET
        elif isinstance(self.assignees, list):
            assignees = []
            for assignees_type_0_item_data in self.assignees:
                assignees_type_0_item = assignees_type_0_item_data.to_dict()
                assignees.append(assignees_type_0_item)


        else:
            assignees = self.assignees

        unit_code: None | str | Unset
        if isinstance(self.unit_code, Unset):
            unit_code = UNSET
        else:
            unit_code = self.unit_code

        unit_name: None | str | Unset
        if isinstance(self.unit_name, Unset):
            unit_name = UNSET
        else:
            unit_name = self.unit_name

        payment_breakdown: list[dict[str, Any]] | None | Unset
        if isinstance(self.payment_breakdown, Unset):
            payment_breakdown = UNSET
        elif isinstance(self.payment_breakdown, list):
            payment_breakdown = []
            for payment_breakdown_type_0_item_data in self.payment_breakdown:
                payment_breakdown_type_0_item = payment_breakdown_type_0_item_data.to_dict()
                payment_breakdown.append(payment_breakdown_type_0_item)


        else:
            payment_breakdown = self.payment_breakdown

        return_status: None | str | Unset
        if isinstance(self.return_status, Unset):
            return_status = UNSET
        else:
            return_status = self.return_status

        has_open_return = self.has_open_return

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

        e_invoice_status: None | str | Unset
        if isinstance(self.e_invoice_status, Unset):
            e_invoice_status = UNSET
        else:
            e_invoice_status = self.e_invoice_status

        e_invoice_number: None | str | Unset
        if isinstance(self.e_invoice_number, Unset):
            e_invoice_number = UNSET
        else:
            e_invoice_number = self.e_invoice_number

        vat_exported_at: None | str | Unset
        if isinstance(self.vat_exported_at, Unset):
            vat_exported_at = UNSET
        elif isinstance(self.vat_exported_at, datetime.datetime):
            vat_exported_at = self.vat_exported_at.isoformat()
        else:
            vat_exported_at = self.vat_exported_at

        outlet_id: None | str | Unset
        if isinstance(self.outlet_id, Unset):
            outlet_id = UNSET
        elif isinstance(self.outlet_id, UUID):
            outlet_id = str(self.outlet_id)
        else:
            outlet_id = self.outlet_id

        delivery_employee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delivery_employee, Unset):
            delivery_employee = self.delivery_employee.to_dict()

        expected_delivery_date: None | str | Unset
        if isinstance(self.expected_delivery_date, Unset):
            expected_delivery_date = UNSET
        elif isinstance(self.expected_delivery_date, datetime.datetime):
            expected_delivery_date = self.expected_delivery_date.isoformat()
        else:
            expected_delivery_date = self.expected_delivery_date

        deposit_amount = self.deposit_amount

        delivery_status: None | str | Unset
        if isinstance(self.delivery_status, Unset):
            delivery_status = UNSET
        else:
            delivery_status = self.delivery_status

        internal_notes: None | str | Unset
        if isinstance(self.internal_notes, Unset):
            internal_notes = UNSET
        else:
            internal_notes = self.internal_notes

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

        delivery_address: None | str | Unset
        if isinstance(self.delivery_address, Unset):
            delivery_address = UNSET
        else:
            delivery_address = self.delivery_address

        delivery_name: None | str | Unset
        if isinstance(self.delivery_name, Unset):
            delivery_name = UNSET
        else:
            delivery_name = self.delivery_name

        delivery_phone: None | str | Unset
        if isinstance(self.delivery_phone, Unset):
            delivery_phone = UNSET
        else:
            delivery_phone = self.delivery_phone

        customer_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.customer_info, Unset):
            customer_info = self.customer_info.to_dict()

        outlet_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.outlet_info, Unset):
            outlet_info = self.outlet_info.to_dict()


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
        if sales_customer_id is not UNSET:
            field_dict["salesCustomerId"] = sales_customer_id
        if contact_name is not UNSET:
            field_dict["contactName"] = contact_name
        if contact_phone is not UNSET:
            field_dict["contactPhone"] = contact_phone
        if customer_code is not UNSET:
            field_dict["customerCode"] = customer_code
        if address is not UNSET:
            field_dict["address"] = address
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id
        if branch_name is not UNSET:
            field_dict["branchName"] = branch_name
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
        if debt_amount is not UNSET:
            field_dict["debtAmount"] = debt_amount
        if debt_status is not UNSET:
            field_dict["debtStatus"] = debt_status
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if notes is not UNSET:
            field_dict["notes"] = notes
        if vat_mode is not UNSET:
            field_dict["vatMode"] = vat_mode
        if confirmed_at is not UNSET:
            field_dict["confirmedAt"] = confirmed_at
        if cancelled_at is not UNSET:
            field_dict["cancelledAt"] = cancelled_at
        if cancel_reason is not UNSET:
            field_dict["cancelReason"] = cancel_reason
        if item_count is not UNSET:
            field_dict["itemCount"] = item_count
        if assigned_to is not UNSET:
            field_dict["assignedTo"] = assigned_to
        if assignees is not UNSET:
            field_dict["assignees"] = assignees
        if unit_code is not UNSET:
            field_dict["unitCode"] = unit_code
        if unit_name is not UNSET:
            field_dict["unitName"] = unit_name
        if payment_breakdown is not UNSET:
            field_dict["paymentBreakdown"] = payment_breakdown
        if return_status is not UNSET:
            field_dict["returnStatus"] = return_status
        if has_open_return is not UNSET:
            field_dict["hasOpenReturn"] = has_open_return
        if channel_code is not UNSET:
            field_dict["channelCode"] = channel_code
        if order_date is not UNSET:
            field_dict["orderDate"] = order_date
        if e_invoice_status is not UNSET:
            field_dict["eInvoiceStatus"] = e_invoice_status
        if e_invoice_number is not UNSET:
            field_dict["eInvoiceNumber"] = e_invoice_number
        if vat_exported_at is not UNSET:
            field_dict["vatExportedAt"] = vat_exported_at
        if outlet_id is not UNSET:
            field_dict["outletId"] = outlet_id
        if delivery_employee is not UNSET:
            field_dict["deliveryEmployee"] = delivery_employee
        if expected_delivery_date is not UNSET:
            field_dict["expectedDeliveryDate"] = expected_delivery_date
        if deposit_amount is not UNSET:
            field_dict["depositAmount"] = deposit_amount
        if delivery_status is not UNSET:
            field_dict["deliveryStatus"] = delivery_status
        if internal_notes is not UNSET:
            field_dict["internalNotes"] = internal_notes
        if delivered_at is not UNSET:
            field_dict["deliveredAt"] = delivered_at
        if last_payment_date is not UNSET:
            field_dict["lastPaymentDate"] = last_payment_date
        if payments is not UNSET:
            field_dict["payments"] = payments
        if delivery_address is not UNSET:
            field_dict["deliveryAddress"] = delivery_address
        if delivery_name is not UNSET:
            field_dict["deliveryName"] = delivery_name
        if delivery_phone is not UNSET:
            field_dict["deliveryPhone"] = delivery_phone
        if customer_info is not UNSET:
            field_dict["customerInfo"] = customer_info
        if outlet_info is not UNSET:
            field_dict["outletInfo"] = outlet_info

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.order_assignee_dto import OrderAssigneeDto # noqa: PLC0415
        from ..models.order_list_customer_info_dto import OrderListCustomerInfoDto # noqa: PLC0415
        from ..models.order_list_outlet_info_dto import OrderListOutletInfoDto # noqa: PLC0415
        from ..models.order_payment_entry_dto import OrderPaymentEntryDto # noqa: PLC0415
        from ..models.payment_row_dto import PaymentRowDto # noqa: PLC0415
        from ..models.user_ref_dto import UserRefDto # noqa: PLC0415
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


        _sales_customer_id = d.pop("salesCustomerId", UNSET)
        sales_customer_id: UUID | Unset
        if isinstance(_sales_customer_id,  Unset):
            sales_customer_id = UNSET
        else:
            sales_customer_id = UUID(_sales_customer_id)




        def _parse_contact_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_name = _parse_contact_name(d.pop("contactName", UNSET))


        def _parse_contact_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_phone = _parse_contact_phone(d.pop("contactPhone", UNSET))


        def _parse_customer_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_code = _parse_customer_code(d.pop("customerCode", UNSET))


        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))


        _branch_id = d.pop("branchId", UNSET)
        branch_id: UUID | Unset
        if isinstance(_branch_id,  Unset):
            branch_id = UNSET
        else:
            branch_id = UUID(_branch_id)




        def _parse_branch_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch_name = _parse_branch_name(d.pop("branchName", UNSET))


        subtotal = d.pop("subtotal", UNSET)

        discount_amount = d.pop("discountAmount", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        shipping_fee = d.pop("shippingFee", UNSET)

        total = d.pop("total", UNSET)

        paid_amount = d.pop("paidAmount", UNSET)

        debt_amount = d.pop("debtAmount", UNSET)

        def _parse_debt_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        debt_status = _parse_debt_status(d.pop("debtStatus", UNSET))


        def _parse_payment_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_method = _parse_payment_method(d.pop("paymentMethod", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


        def _parse_vat_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vat_mode = _parse_vat_mode(d.pop("vatMode", UNSET))


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


        def _parse_cancel_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cancel_reason = _parse_cancel_reason(d.pop("cancelReason", UNSET))


        item_count = d.pop("itemCount", UNSET)

        _assigned_to = d.pop("assignedTo", UNSET)
        assigned_to: UserRefDto | Unset
        if isinstance(_assigned_to,  Unset):
            assigned_to = UNSET
        else:
            assigned_to = UserRefDto.from_dict(_assigned_to)




        def _parse_assignees(data: object) -> list[OrderAssigneeDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assignees_type_0 = []
                _assignees_type_0 = data
                for assignees_type_0_item_data in (_assignees_type_0):
                    assignees_type_0_item = OrderAssigneeDto.from_dict(assignees_type_0_item_data)



                    assignees_type_0.append(assignees_type_0_item)

                return assignees_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OrderAssigneeDto] | None | Unset, data)

        assignees = _parse_assignees(d.pop("assignees", UNSET))


        def _parse_unit_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit_code = _parse_unit_code(d.pop("unitCode", UNSET))


        def _parse_unit_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit_name = _parse_unit_name(d.pop("unitName", UNSET))


        def _parse_payment_breakdown(data: object) -> list[PaymentRowDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                payment_breakdown_type_0 = []
                _payment_breakdown_type_0 = data
                for payment_breakdown_type_0_item_data in (_payment_breakdown_type_0):
                    payment_breakdown_type_0_item = PaymentRowDto.from_dict(payment_breakdown_type_0_item_data)



                    payment_breakdown_type_0.append(payment_breakdown_type_0_item)

                return payment_breakdown_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PaymentRowDto] | None | Unset, data)

        payment_breakdown = _parse_payment_breakdown(d.pop("paymentBreakdown", UNSET))


        def _parse_return_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        return_status = _parse_return_status(d.pop("returnStatus", UNSET))


        has_open_return = d.pop("hasOpenReturn", UNSET)

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


        def _parse_e_invoice_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        e_invoice_status = _parse_e_invoice_status(d.pop("eInvoiceStatus", UNSET))


        def _parse_e_invoice_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        e_invoice_number = _parse_e_invoice_number(d.pop("eInvoiceNumber", UNSET))


        def _parse_vat_exported_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                vat_exported_at_type_0 = datetime.datetime.fromisoformat(data)



                return vat_exported_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        vat_exported_at = _parse_vat_exported_at(d.pop("vatExportedAt", UNSET))


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


        _delivery_employee = d.pop("deliveryEmployee", UNSET)
        delivery_employee: UserRefDto | Unset
        if isinstance(_delivery_employee,  Unset):
            delivery_employee = UNSET
        else:
            delivery_employee = UserRefDto.from_dict(_delivery_employee)




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


        deposit_amount = d.pop("depositAmount", UNSET)

        def _parse_delivery_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        delivery_status = _parse_delivery_status(d.pop("deliveryStatus", UNSET))


        def _parse_internal_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        internal_notes = _parse_internal_notes(d.pop("internalNotes", UNSET))


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


        def _parse_payments(data: object) -> list[OrderPaymentEntryDto] | None | Unset:
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
                    payments_type_0_item = OrderPaymentEntryDto.from_dict(payments_type_0_item_data)



                    payments_type_0.append(payments_type_0_item)

                return payments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OrderPaymentEntryDto] | None | Unset, data)

        payments = _parse_payments(d.pop("payments", UNSET))


        def _parse_delivery_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        delivery_address = _parse_delivery_address(d.pop("deliveryAddress", UNSET))


        def _parse_delivery_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        delivery_name = _parse_delivery_name(d.pop("deliveryName", UNSET))


        def _parse_delivery_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        delivery_phone = _parse_delivery_phone(d.pop("deliveryPhone", UNSET))


        _customer_info = d.pop("customerInfo", UNSET)
        customer_info: OrderListCustomerInfoDto | Unset
        if isinstance(_customer_info,  Unset):
            customer_info = UNSET
        else:
            customer_info = OrderListCustomerInfoDto.from_dict(_customer_info)




        _outlet_info = d.pop("outletInfo", UNSET)
        outlet_info: OrderListOutletInfoDto | Unset
        if isinstance(_outlet_info,  Unset):
            outlet_info = UNSET
        else:
            outlet_info = OrderListOutletInfoDto.from_dict(_outlet_info)




        order_list_dto = cls(
            id=id,
            code=code,
            order_type=order_type,
            status=status,
            sales_customer_id=sales_customer_id,
            contact_name=contact_name,
            contact_phone=contact_phone,
            customer_code=customer_code,
            address=address,
            branch_id=branch_id,
            branch_name=branch_name,
            subtotal=subtotal,
            discount_amount=discount_amount,
            tax_amount=tax_amount,
            shipping_fee=shipping_fee,
            total=total,
            paid_amount=paid_amount,
            debt_amount=debt_amount,
            debt_status=debt_status,
            payment_method=payment_method,
            created_at=created_at,
            notes=notes,
            vat_mode=vat_mode,
            confirmed_at=confirmed_at,
            cancelled_at=cancelled_at,
            cancel_reason=cancel_reason,
            item_count=item_count,
            assigned_to=assigned_to,
            assignees=assignees,
            unit_code=unit_code,
            unit_name=unit_name,
            payment_breakdown=payment_breakdown,
            return_status=return_status,
            has_open_return=has_open_return,
            channel_code=channel_code,
            order_date=order_date,
            e_invoice_status=e_invoice_status,
            e_invoice_number=e_invoice_number,
            vat_exported_at=vat_exported_at,
            outlet_id=outlet_id,
            delivery_employee=delivery_employee,
            expected_delivery_date=expected_delivery_date,
            deposit_amount=deposit_amount,
            delivery_status=delivery_status,
            internal_notes=internal_notes,
            delivered_at=delivered_at,
            last_payment_date=last_payment_date,
            payments=payments,
            delivery_address=delivery_address,
            delivery_name=delivery_name,
            delivery_phone=delivery_phone,
            customer_info=customer_info,
            outlet_info=outlet_info,
        )

        return order_list_dto


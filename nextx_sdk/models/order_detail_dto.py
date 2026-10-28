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
  from ..models.delivery_address_dto import DeliveryAddressDto
  from ..models.order_assignee_dto import OrderAssigneeDto
  from ..models.order_detail_dto_custom_fields_type_0 import OrderDetailDtoCustomFieldsType0
  from ..models.order_discount_dto import OrderDiscountDto
  from ..models.order_item_dto import OrderItemDto
  from ..models.order_return_summary_dto import OrderReturnSummaryDto
  from ..models.order_shipping_plan_dto import OrderShippingPlanDto
  from ..models.order_vat_dto import OrderVatDto
  from ..models.payment_row_dto import PaymentRowDto
  from ..models.pre_order_child_order_dto import PreOrderChildOrderDto
  from ..models.user_ref_dto import UserRefDto





T = TypeVar("T", bound="OrderDetailDto")



@_attrs_define
class OrderDetailDto:
    

    id: UUID | Unset = UNSET
    code: None | str | Unset = UNSET
    order_type: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    sales_customer_id: UUID | Unset = UNSET
    contact_name: None | str | Unset = UNSET
    contact_phone: None | str | Unset = UNSET
    branch_id: UUID | Unset = UNSET
    branch_name: None | str | Unset = UNSET
    subtotal: float | Unset = UNSET
    shipping_fee: float | Unset = UNSET
    total: float | Unset = UNSET
    paid_amount: float | Unset = UNSET
    debt_amount: float | Unset = UNSET
    payment_method: None | str | Unset = UNSET
    cash_account_id: None | Unset | UUID = UNSET
    shipment_id: None | Unset | UUID = UNSET
    notes: None | str | Unset = UNSET
    items: list[OrderItemDto] | None | Unset = UNSET
    confirmed_at: datetime.datetime | None | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET
    cancelled_at: datetime.datetime | None | Unset = UNSET
    cancel_reason: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    assigned_to: UserRefDto | Unset = UNSET
    assignees: list[OrderAssigneeDto] | None | Unset = UNSET
    created_by: UserRefDto | Unset = UNSET
    discount: OrderDiscountDto | Unset = UNSET
    vat: OrderVatDto | Unset = UNSET
    payment_status: None | str | Unset = UNSET
    coupon_code: None | str | Unset = UNSET
    delivery: DeliveryAddressDto | Unset = UNSET
    cod_amount: float | None | Unset = UNSET
    channel_code: None | str | Unset = UNSET
    external_order_id: None | str | Unset = UNSET
    order_date: datetime.datetime | None | Unset = UNSET
    source_order_ids: list[UUID] | None | Unset = UNSET
    converted_at: datetime.datetime | None | Unset = UNSET
    returns: list[OrderReturnSummaryDto] | None | Unset = UNSET
    points_used: int | Unset = UNSET
    points_discount: float | Unset = UNSET
    voucher_codes: list[str] | None | Unset = UNSET
    deposit_amount: float | Unset = UNSET
    deposit_payment_method: None | str | Unset = UNSET
    deposit_deducted: float | Unset = UNSET
    expected_delivery_date: datetime.datetime | None | Unset = UNSET
    promotion_id: None | Unset | UUID = UNSET
    payment_breakdown: list[PaymentRowDto] | None | Unset = UNSET
    bank_account_id: None | Unset | UUID = UNSET
    customer_code: None | str | Unset = UNSET
    customer_address: None | str | Unset = UNSET
    customer_tax_code: None | str | Unset = UNSET
    price_list_id_override: None | Unset | UUID = UNSET
    source_pre_order_id: None | Unset | UUID = UNSET
    source_pre_order_code: None | str | Unset = UNSET
    customer_current_debt: float | Unset = UNSET
    custom_fields: None | OrderDetailDtoCustomFieldsType0 | Unset = UNSET
    approved_at: datetime.datetime | None | Unset = UNSET
    approved_by: None | Unset | UUID = UNSET
    child_orders: list[PreOrderChildOrderDto] | None | Unset = UNSET
    internal_notes: None | str | Unset = UNSET
    other_charges: float | Unset = UNSET
    outlet_id: None | Unset | UUID = UNSET
    delivery_employee: UserRefDto | Unset = UNSET
    delivered_at: datetime.datetime | None | Unset = UNSET
    idempotent_replay: bool | Unset = UNSET
    shipping_plan: OrderShippingPlanDto | Unset = UNSET
    discount_amount: float | Unset = UNSET
    tax_amount: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.delivery_address_dto import DeliveryAddressDto # noqa: PLC0415
        from ..models.order_assignee_dto import OrderAssigneeDto # noqa: PLC0415
        from ..models.order_detail_dto_custom_fields_type_0 import OrderDetailDtoCustomFieldsType0 # noqa: PLC0415
        from ..models.order_discount_dto import OrderDiscountDto # noqa: PLC0415
        from ..models.order_item_dto import OrderItemDto # noqa: PLC0415
        from ..models.order_return_summary_dto import OrderReturnSummaryDto # noqa: PLC0415
        from ..models.order_shipping_plan_dto import OrderShippingPlanDto # noqa: PLC0415
        from ..models.order_vat_dto import OrderVatDto # noqa: PLC0415
        from ..models.payment_row_dto import PaymentRowDto # noqa: PLC0415
        from ..models.pre_order_child_order_dto import PreOrderChildOrderDto # noqa: PLC0415
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

        branch_id: str | Unset = UNSET
        if not isinstance(self.branch_id, Unset):
            branch_id = str(self.branch_id)

        branch_name: None | str | Unset
        if isinstance(self.branch_name, Unset):
            branch_name = UNSET
        else:
            branch_name = self.branch_name

        subtotal = self.subtotal

        shipping_fee = self.shipping_fee

        total = self.total

        paid_amount = self.paid_amount

        debt_amount = self.debt_amount

        payment_method: None | str | Unset
        if isinstance(self.payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = self.payment_method

        cash_account_id: None | str | Unset
        if isinstance(self.cash_account_id, Unset):
            cash_account_id = UNSET
        elif isinstance(self.cash_account_id, UUID):
            cash_account_id = str(self.cash_account_id)
        else:
            cash_account_id = self.cash_account_id

        shipment_id: None | str | Unset
        if isinstance(self.shipment_id, Unset):
            shipment_id = UNSET
        elif isinstance(self.shipment_id, UUID):
            shipment_id = str(self.shipment_id)
        else:
            shipment_id = self.shipment_id

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        items: list[dict[str, Any]] | None | Unset
        if isinstance(self.items, Unset):
            items = UNSET
        elif isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)


        else:
            items = self.items

        confirmed_at: None | str | Unset
        if isinstance(self.confirmed_at, Unset):
            confirmed_at = UNSET
        elif isinstance(self.confirmed_at, datetime.datetime):
            confirmed_at = self.confirmed_at.isoformat()
        else:
            confirmed_at = self.confirmed_at

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

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

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

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

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        discount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.discount, Unset):
            discount = self.discount.to_dict()

        vat: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vat, Unset):
            vat = self.vat.to_dict()

        payment_status: None | str | Unset
        if isinstance(self.payment_status, Unset):
            payment_status = UNSET
        else:
            payment_status = self.payment_status

        coupon_code: None | str | Unset
        if isinstance(self.coupon_code, Unset):
            coupon_code = UNSET
        else:
            coupon_code = self.coupon_code

        delivery: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delivery, Unset):
            delivery = self.delivery.to_dict()

        cod_amount: float | None | Unset
        if isinstance(self.cod_amount, Unset):
            cod_amount = UNSET
        else:
            cod_amount = self.cod_amount

        channel_code: None | str | Unset
        if isinstance(self.channel_code, Unset):
            channel_code = UNSET
        else:
            channel_code = self.channel_code

        external_order_id: None | str | Unset
        if isinstance(self.external_order_id, Unset):
            external_order_id = UNSET
        else:
            external_order_id = self.external_order_id

        order_date: None | str | Unset
        if isinstance(self.order_date, Unset):
            order_date = UNSET
        elif isinstance(self.order_date, datetime.datetime):
            order_date = self.order_date.isoformat()
        else:
            order_date = self.order_date

        source_order_ids: list[str] | None | Unset
        if isinstance(self.source_order_ids, Unset):
            source_order_ids = UNSET
        elif isinstance(self.source_order_ids, list):
            source_order_ids = []
            for source_order_ids_type_0_item_data in self.source_order_ids:
                source_order_ids_type_0_item = str(source_order_ids_type_0_item_data)
                source_order_ids.append(source_order_ids_type_0_item)


        else:
            source_order_ids = self.source_order_ids

        converted_at: None | str | Unset
        if isinstance(self.converted_at, Unset):
            converted_at = UNSET
        elif isinstance(self.converted_at, datetime.datetime):
            converted_at = self.converted_at.isoformat()
        else:
            converted_at = self.converted_at

        returns: list[dict[str, Any]] | None | Unset
        if isinstance(self.returns, Unset):
            returns = UNSET
        elif isinstance(self.returns, list):
            returns = []
            for returns_type_0_item_data in self.returns:
                returns_type_0_item = returns_type_0_item_data.to_dict()
                returns.append(returns_type_0_item)


        else:
            returns = self.returns

        points_used = self.points_used

        points_discount = self.points_discount

        voucher_codes: list[str] | None | Unset
        if isinstance(self.voucher_codes, Unset):
            voucher_codes = UNSET
        elif isinstance(self.voucher_codes, list):
            voucher_codes = self.voucher_codes


        else:
            voucher_codes = self.voucher_codes

        deposit_amount = self.deposit_amount

        deposit_payment_method: None | str | Unset
        if isinstance(self.deposit_payment_method, Unset):
            deposit_payment_method = UNSET
        else:
            deposit_payment_method = self.deposit_payment_method

        deposit_deducted = self.deposit_deducted

        expected_delivery_date: None | str | Unset
        if isinstance(self.expected_delivery_date, Unset):
            expected_delivery_date = UNSET
        elif isinstance(self.expected_delivery_date, datetime.datetime):
            expected_delivery_date = self.expected_delivery_date.isoformat()
        else:
            expected_delivery_date = self.expected_delivery_date

        promotion_id: None | str | Unset
        if isinstance(self.promotion_id, Unset):
            promotion_id = UNSET
        elif isinstance(self.promotion_id, UUID):
            promotion_id = str(self.promotion_id)
        else:
            promotion_id = self.promotion_id

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

        bank_account_id: None | str | Unset
        if isinstance(self.bank_account_id, Unset):
            bank_account_id = UNSET
        elif isinstance(self.bank_account_id, UUID):
            bank_account_id = str(self.bank_account_id)
        else:
            bank_account_id = self.bank_account_id

        customer_code: None | str | Unset
        if isinstance(self.customer_code, Unset):
            customer_code = UNSET
        else:
            customer_code = self.customer_code

        customer_address: None | str | Unset
        if isinstance(self.customer_address, Unset):
            customer_address = UNSET
        else:
            customer_address = self.customer_address

        customer_tax_code: None | str | Unset
        if isinstance(self.customer_tax_code, Unset):
            customer_tax_code = UNSET
        else:
            customer_tax_code = self.customer_tax_code

        price_list_id_override: None | str | Unset
        if isinstance(self.price_list_id_override, Unset):
            price_list_id_override = UNSET
        elif isinstance(self.price_list_id_override, UUID):
            price_list_id_override = str(self.price_list_id_override)
        else:
            price_list_id_override = self.price_list_id_override

        source_pre_order_id: None | str | Unset
        if isinstance(self.source_pre_order_id, Unset):
            source_pre_order_id = UNSET
        elif isinstance(self.source_pre_order_id, UUID):
            source_pre_order_id = str(self.source_pre_order_id)
        else:
            source_pre_order_id = self.source_pre_order_id

        source_pre_order_code: None | str | Unset
        if isinstance(self.source_pre_order_code, Unset):
            source_pre_order_code = UNSET
        else:
            source_pre_order_code = self.source_pre_order_code

        customer_current_debt = self.customer_current_debt

        custom_fields: dict[str, Any] | None | Unset
        if isinstance(self.custom_fields, Unset):
            custom_fields = UNSET
        elif isinstance(self.custom_fields, OrderDetailDtoCustomFieldsType0):
            custom_fields = self.custom_fields.to_dict()
        else:
            custom_fields = self.custom_fields

        approved_at: None | str | Unset
        if isinstance(self.approved_at, Unset):
            approved_at = UNSET
        elif isinstance(self.approved_at, datetime.datetime):
            approved_at = self.approved_at.isoformat()
        else:
            approved_at = self.approved_at

        approved_by: None | str | Unset
        if isinstance(self.approved_by, Unset):
            approved_by = UNSET
        elif isinstance(self.approved_by, UUID):
            approved_by = str(self.approved_by)
        else:
            approved_by = self.approved_by

        child_orders: list[dict[str, Any]] | None | Unset
        if isinstance(self.child_orders, Unset):
            child_orders = UNSET
        elif isinstance(self.child_orders, list):
            child_orders = []
            for child_orders_type_0_item_data in self.child_orders:
                child_orders_type_0_item = child_orders_type_0_item_data.to_dict()
                child_orders.append(child_orders_type_0_item)


        else:
            child_orders = self.child_orders

        internal_notes: None | str | Unset
        if isinstance(self.internal_notes, Unset):
            internal_notes = UNSET
        else:
            internal_notes = self.internal_notes

        other_charges = self.other_charges

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

        delivered_at: None | str | Unset
        if isinstance(self.delivered_at, Unset):
            delivered_at = UNSET
        elif isinstance(self.delivered_at, datetime.datetime):
            delivered_at = self.delivered_at.isoformat()
        else:
            delivered_at = self.delivered_at

        idempotent_replay = self.idempotent_replay

        shipping_plan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shipping_plan, Unset):
            shipping_plan = self.shipping_plan.to_dict()

        discount_amount = self.discount_amount

        tax_amount = self.tax_amount


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
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id
        if branch_name is not UNSET:
            field_dict["branchName"] = branch_name
        if subtotal is not UNSET:
            field_dict["subtotal"] = subtotal
        if shipping_fee is not UNSET:
            field_dict["shippingFee"] = shipping_fee
        if total is not UNSET:
            field_dict["total"] = total
        if paid_amount is not UNSET:
            field_dict["paidAmount"] = paid_amount
        if debt_amount is not UNSET:
            field_dict["debtAmount"] = debt_amount
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method
        if cash_account_id is not UNSET:
            field_dict["cashAccountId"] = cash_account_id
        if shipment_id is not UNSET:
            field_dict["shipmentId"] = shipment_id
        if notes is not UNSET:
            field_dict["notes"] = notes
        if items is not UNSET:
            field_dict["items"] = items
        if confirmed_at is not UNSET:
            field_dict["confirmedAt"] = confirmed_at
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if cancelled_at is not UNSET:
            field_dict["cancelledAt"] = cancelled_at
        if cancel_reason is not UNSET:
            field_dict["cancelReason"] = cancel_reason
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if assigned_to is not UNSET:
            field_dict["assignedTo"] = assigned_to
        if assignees is not UNSET:
            field_dict["assignees"] = assignees
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if discount is not UNSET:
            field_dict["discount"] = discount
        if vat is not UNSET:
            field_dict["vat"] = vat
        if payment_status is not UNSET:
            field_dict["paymentStatus"] = payment_status
        if coupon_code is not UNSET:
            field_dict["couponCode"] = coupon_code
        if delivery is not UNSET:
            field_dict["delivery"] = delivery
        if cod_amount is not UNSET:
            field_dict["codAmount"] = cod_amount
        if channel_code is not UNSET:
            field_dict["channelCode"] = channel_code
        if external_order_id is not UNSET:
            field_dict["externalOrderId"] = external_order_id
        if order_date is not UNSET:
            field_dict["orderDate"] = order_date
        if source_order_ids is not UNSET:
            field_dict["sourceOrderIds"] = source_order_ids
        if converted_at is not UNSET:
            field_dict["convertedAt"] = converted_at
        if returns is not UNSET:
            field_dict["returns"] = returns
        if points_used is not UNSET:
            field_dict["pointsUsed"] = points_used
        if points_discount is not UNSET:
            field_dict["pointsDiscount"] = points_discount
        if voucher_codes is not UNSET:
            field_dict["voucherCodes"] = voucher_codes
        if deposit_amount is not UNSET:
            field_dict["depositAmount"] = deposit_amount
        if deposit_payment_method is not UNSET:
            field_dict["depositPaymentMethod"] = deposit_payment_method
        if deposit_deducted is not UNSET:
            field_dict["depositDeducted"] = deposit_deducted
        if expected_delivery_date is not UNSET:
            field_dict["expectedDeliveryDate"] = expected_delivery_date
        if promotion_id is not UNSET:
            field_dict["promotionId"] = promotion_id
        if payment_breakdown is not UNSET:
            field_dict["paymentBreakdown"] = payment_breakdown
        if bank_account_id is not UNSET:
            field_dict["bankAccountId"] = bank_account_id
        if customer_code is not UNSET:
            field_dict["customerCode"] = customer_code
        if customer_address is not UNSET:
            field_dict["customerAddress"] = customer_address
        if customer_tax_code is not UNSET:
            field_dict["customerTaxCode"] = customer_tax_code
        if price_list_id_override is not UNSET:
            field_dict["priceListIdOverride"] = price_list_id_override
        if source_pre_order_id is not UNSET:
            field_dict["sourcePreOrderId"] = source_pre_order_id
        if source_pre_order_code is not UNSET:
            field_dict["sourcePreOrderCode"] = source_pre_order_code
        if customer_current_debt is not UNSET:
            field_dict["customerCurrentDebt"] = customer_current_debt
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if approved_at is not UNSET:
            field_dict["approvedAt"] = approved_at
        if approved_by is not UNSET:
            field_dict["approvedBy"] = approved_by
        if child_orders is not UNSET:
            field_dict["childOrders"] = child_orders
        if internal_notes is not UNSET:
            field_dict["internalNotes"] = internal_notes
        if other_charges is not UNSET:
            field_dict["otherCharges"] = other_charges
        if outlet_id is not UNSET:
            field_dict["outletId"] = outlet_id
        if delivery_employee is not UNSET:
            field_dict["deliveryEmployee"] = delivery_employee
        if delivered_at is not UNSET:
            field_dict["deliveredAt"] = delivered_at
        if idempotent_replay is not UNSET:
            field_dict["idempotentReplay"] = idempotent_replay
        if shipping_plan is not UNSET:
            field_dict["shippingPlan"] = shipping_plan
        if discount_amount is not UNSET:
            field_dict["discountAmount"] = discount_amount
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delivery_address_dto import DeliveryAddressDto # noqa: PLC0415
        from ..models.order_assignee_dto import OrderAssigneeDto # noqa: PLC0415
        from ..models.order_detail_dto_custom_fields_type_0 import OrderDetailDtoCustomFieldsType0 # noqa: PLC0415
        from ..models.order_discount_dto import OrderDiscountDto # noqa: PLC0415
        from ..models.order_item_dto import OrderItemDto # noqa: PLC0415
        from ..models.order_return_summary_dto import OrderReturnSummaryDto # noqa: PLC0415
        from ..models.order_shipping_plan_dto import OrderShippingPlanDto # noqa: PLC0415
        from ..models.order_vat_dto import OrderVatDto # noqa: PLC0415
        from ..models.payment_row_dto import PaymentRowDto # noqa: PLC0415
        from ..models.pre_order_child_order_dto import PreOrderChildOrderDto # noqa: PLC0415
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

        shipping_fee = d.pop("shippingFee", UNSET)

        total = d.pop("total", UNSET)

        paid_amount = d.pop("paidAmount", UNSET)

        debt_amount = d.pop("debtAmount", UNSET)

        def _parse_payment_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_method = _parse_payment_method(d.pop("paymentMethod", UNSET))


        def _parse_cash_account_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cash_account_id_type_0 = UUID(data)



                return cash_account_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        cash_account_id = _parse_cash_account_id(d.pop("cashAccountId", UNSET))


        def _parse_shipment_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shipment_id_type_0 = UUID(data)



                return shipment_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        shipment_id = _parse_shipment_id(d.pop("shipmentId", UNSET))


        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


        def _parse_items(data: object) -> list[OrderItemDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in (_items_type_0):
                    items_type_0_item = OrderItemDto.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OrderItemDto] | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))


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


        def _parse_completed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = datetime.datetime.fromisoformat(data)



                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        completed_at = _parse_completed_at(d.pop("completedAt", UNSET))


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


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)




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


        _created_by = d.pop("createdBy", UNSET)
        created_by: UserRefDto | Unset
        if isinstance(_created_by,  Unset):
            created_by = UNSET
        else:
            created_by = UserRefDto.from_dict(_created_by)




        _discount = d.pop("discount", UNSET)
        discount: OrderDiscountDto | Unset
        if isinstance(_discount,  Unset):
            discount = UNSET
        else:
            discount = OrderDiscountDto.from_dict(_discount)




        _vat = d.pop("vat", UNSET)
        vat: OrderVatDto | Unset
        if isinstance(_vat,  Unset):
            vat = UNSET
        else:
            vat = OrderVatDto.from_dict(_vat)




        def _parse_payment_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_status = _parse_payment_status(d.pop("paymentStatus", UNSET))


        def _parse_coupon_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        coupon_code = _parse_coupon_code(d.pop("couponCode", UNSET))


        _delivery = d.pop("delivery", UNSET)
        delivery: DeliveryAddressDto | Unset
        if isinstance(_delivery,  Unset):
            delivery = UNSET
        else:
            delivery = DeliveryAddressDto.from_dict(_delivery)




        def _parse_cod_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cod_amount = _parse_cod_amount(d.pop("codAmount", UNSET))


        def _parse_channel_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel_code = _parse_channel_code(d.pop("channelCode", UNSET))


        def _parse_external_order_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_order_id = _parse_external_order_id(d.pop("externalOrderId", UNSET))


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


        def _parse_source_order_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                source_order_ids_type_0 = []
                _source_order_ids_type_0 = data
                for source_order_ids_type_0_item_data in (_source_order_ids_type_0):
                    source_order_ids_type_0_item = UUID(source_order_ids_type_0_item_data)



                    source_order_ids_type_0.append(source_order_ids_type_0_item)

                return source_order_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        source_order_ids = _parse_source_order_ids(d.pop("sourceOrderIds", UNSET))


        def _parse_converted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                converted_at_type_0 = datetime.datetime.fromisoformat(data)



                return converted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        converted_at = _parse_converted_at(d.pop("convertedAt", UNSET))


        def _parse_returns(data: object) -> list[OrderReturnSummaryDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                returns_type_0 = []
                _returns_type_0 = data
                for returns_type_0_item_data in (_returns_type_0):
                    returns_type_0_item = OrderReturnSummaryDto.from_dict(returns_type_0_item_data)



                    returns_type_0.append(returns_type_0_item)

                return returns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OrderReturnSummaryDto] | None | Unset, data)

        returns = _parse_returns(d.pop("returns", UNSET))


        points_used = d.pop("pointsUsed", UNSET)

        points_discount = d.pop("pointsDiscount", UNSET)

        def _parse_voucher_codes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                voucher_codes_type_0 = cast(list[str], data)

                return voucher_codes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        voucher_codes = _parse_voucher_codes(d.pop("voucherCodes", UNSET))


        deposit_amount = d.pop("depositAmount", UNSET)

        def _parse_deposit_payment_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deposit_payment_method = _parse_deposit_payment_method(d.pop("depositPaymentMethod", UNSET))


        deposit_deducted = d.pop("depositDeducted", UNSET)

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


        def _parse_promotion_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                promotion_id_type_0 = UUID(data)



                return promotion_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        promotion_id = _parse_promotion_id(d.pop("promotionId", UNSET))


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


        def _parse_bank_account_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                bank_account_id_type_0 = UUID(data)



                return bank_account_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        bank_account_id = _parse_bank_account_id(d.pop("bankAccountId", UNSET))


        def _parse_customer_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_code = _parse_customer_code(d.pop("customerCode", UNSET))


        def _parse_customer_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_address = _parse_customer_address(d.pop("customerAddress", UNSET))


        def _parse_customer_tax_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_tax_code = _parse_customer_tax_code(d.pop("customerTaxCode", UNSET))


        def _parse_price_list_id_override(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                price_list_id_override_type_0 = UUID(data)



                return price_list_id_override_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        price_list_id_override = _parse_price_list_id_override(d.pop("priceListIdOverride", UNSET))


        def _parse_source_pre_order_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_pre_order_id_type_0 = UUID(data)



                return source_pre_order_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        source_pre_order_id = _parse_source_pre_order_id(d.pop("sourcePreOrderId", UNSET))


        def _parse_source_pre_order_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_pre_order_code = _parse_source_pre_order_code(d.pop("sourcePreOrderCode", UNSET))


        customer_current_debt = d.pop("customerCurrentDebt", UNSET)

        def _parse_custom_fields(data: object) -> None | OrderDetailDtoCustomFieldsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_fields_type_0 = OrderDetailDtoCustomFieldsType0.from_dict(data)



                return custom_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OrderDetailDtoCustomFieldsType0 | Unset, data)

        custom_fields = _parse_custom_fields(d.pop("customFields", UNSET))


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


        def _parse_child_orders(data: object) -> list[PreOrderChildOrderDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                child_orders_type_0 = []
                _child_orders_type_0 = data
                for child_orders_type_0_item_data in (_child_orders_type_0):
                    child_orders_type_0_item = PreOrderChildOrderDto.from_dict(child_orders_type_0_item_data)



                    child_orders_type_0.append(child_orders_type_0_item)

                return child_orders_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PreOrderChildOrderDto] | None | Unset, data)

        child_orders = _parse_child_orders(d.pop("childOrders", UNSET))


        def _parse_internal_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        internal_notes = _parse_internal_notes(d.pop("internalNotes", UNSET))


        other_charges = d.pop("otherCharges", UNSET)

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


        idempotent_replay = d.pop("idempotentReplay", UNSET)

        _shipping_plan = d.pop("shippingPlan", UNSET)
        shipping_plan: OrderShippingPlanDto | Unset
        if isinstance(_shipping_plan,  Unset):
            shipping_plan = UNSET
        else:
            shipping_plan = OrderShippingPlanDto.from_dict(_shipping_plan)




        discount_amount = d.pop("discountAmount", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        order_detail_dto = cls(
            id=id,
            code=code,
            order_type=order_type,
            status=status,
            sales_customer_id=sales_customer_id,
            contact_name=contact_name,
            contact_phone=contact_phone,
            branch_id=branch_id,
            branch_name=branch_name,
            subtotal=subtotal,
            shipping_fee=shipping_fee,
            total=total,
            paid_amount=paid_amount,
            debt_amount=debt_amount,
            payment_method=payment_method,
            cash_account_id=cash_account_id,
            shipment_id=shipment_id,
            notes=notes,
            items=items,
            confirmed_at=confirmed_at,
            completed_at=completed_at,
            cancelled_at=cancelled_at,
            cancel_reason=cancel_reason,
            created_at=created_at,
            updated_at=updated_at,
            assigned_to=assigned_to,
            assignees=assignees,
            created_by=created_by,
            discount=discount,
            vat=vat,
            payment_status=payment_status,
            coupon_code=coupon_code,
            delivery=delivery,
            cod_amount=cod_amount,
            channel_code=channel_code,
            external_order_id=external_order_id,
            order_date=order_date,
            source_order_ids=source_order_ids,
            converted_at=converted_at,
            returns=returns,
            points_used=points_used,
            points_discount=points_discount,
            voucher_codes=voucher_codes,
            deposit_amount=deposit_amount,
            deposit_payment_method=deposit_payment_method,
            deposit_deducted=deposit_deducted,
            expected_delivery_date=expected_delivery_date,
            promotion_id=promotion_id,
            payment_breakdown=payment_breakdown,
            bank_account_id=bank_account_id,
            customer_code=customer_code,
            customer_address=customer_address,
            customer_tax_code=customer_tax_code,
            price_list_id_override=price_list_id_override,
            source_pre_order_id=source_pre_order_id,
            source_pre_order_code=source_pre_order_code,
            customer_current_debt=customer_current_debt,
            custom_fields=custom_fields,
            approved_at=approved_at,
            approved_by=approved_by,
            child_orders=child_orders,
            internal_notes=internal_notes,
            other_charges=other_charges,
            outlet_id=outlet_id,
            delivery_employee=delivery_employee,
            delivered_at=delivered_at,
            idempotent_replay=idempotent_replay,
            shipping_plan=shipping_plan,
            discount_amount=discount_amount,
            tax_amount=tax_amount,
        )

        return order_detail_dto


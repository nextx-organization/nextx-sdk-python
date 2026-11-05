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
  from ..models.order_return_refund_payment_row_dto import OrderReturnRefundPaymentRowDto
  from ..models.user_ref_dto import UserRefDto





T = TypeVar("T", bound="OrderReturnListDto")



@_attrs_define
class OrderReturnListDto:
    

    id: UUID | Unset = UNSET
    return_code: None | str | Unset = UNSET
    order_id: UUID | Unset = UNSET
    status: None | str | Unset = UNSET
    reason: None | str | Unset = UNSET
    return_type: None | str | Unset = UNSET
    refund_amount: float | Unset = UNSET
    refund_method: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    is_full_return: bool | Unset = UNSET
    notes: None | str | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET
    branch_id: None | Unset | UUID = UNSET
    grand_total: float | Unset = UNSET
    refund_percent: float | Unset = UNSET
    created_by_name: None | str | Unset = UNSET
    contact_name: None | str | Unset = UNSET
    contact_phone: None | str | Unset = UNSET
    refund_payment_rows: list[OrderReturnRefundPaymentRowDto] | None | Unset = UNSET
    settlement_amount: float | Unset = UNSET
    settlement_direction: None | str | Unset = UNSET
    settled_amount: float | Unset = UNSET
    settled_payment_rows: list[OrderReturnRefundPaymentRowDto] | None | Unset = UNSET
    exchange_new_order_id: None | Unset | UUID = UNSET
    exchange_grand_total: float | Unset = UNSET
    price_diff: float | Unset = UNSET
    return_date: datetime.datetime | None | Unset = UNSET
    crm_contact_id: None | Unset | UUID = UNSET
    outlet_id: None | Unset | UUID = UNSET
    max_cash_refund: float | Unset = UNSET
    force_full_cash_refund: bool | Unset = UNSET
    refund_bank_account_id: None | Unset | UUID = UNSET
    refund_bank_account_label: None | str | Unset = UNSET
    branch_name: None | str | Unset = UNSET
    delivery_address: None | str | Unset = UNSET
    assigned_to_name: None | str | Unset = UNSET
    assignees: list[OrderAssigneeDto] | None | Unset = UNSET
    receiving_branch_ids: list[UUID] | None | Unset = UNSET
    receiving_branch_names: list[str] | None | Unset = UNSET
    delivery_employee: UserRefDto | Unset = UNSET
    delivered_at: datetime.datetime | None | Unset = UNSET
    customer_code: None | str | Unset = UNSET
    customer_info: OrderListCustomerInfoDto | Unset = UNSET
    outlet_info: OrderListOutletInfoDto | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.order_assignee_dto import OrderAssigneeDto # noqa: PLC0415
        from ..models.order_list_customer_info_dto import OrderListCustomerInfoDto # noqa: PLC0415
        from ..models.order_list_outlet_info_dto import OrderListOutletInfoDto # noqa: PLC0415
        from ..models.order_return_refund_payment_row_dto import OrderReturnRefundPaymentRowDto # noqa: PLC0415
        from ..models.user_ref_dto import UserRefDto # noqa: PLC0415
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        return_code: None | str | Unset
        if isinstance(self.return_code, Unset):
            return_code = UNSET
        else:
            return_code = self.return_code

        order_id: str | Unset = UNSET
        if not isinstance(self.order_id, Unset):
            order_id = str(self.order_id)

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

        return_type: None | str | Unset
        if isinstance(self.return_type, Unset):
            return_type = UNSET
        else:
            return_type = self.return_type

        refund_amount = self.refund_amount

        refund_method: None | str | Unset
        if isinstance(self.refund_method, Unset):
            refund_method = UNSET
        else:
            refund_method = self.refund_method

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        is_full_return = self.is_full_return

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        branch_id: None | str | Unset
        if isinstance(self.branch_id, Unset):
            branch_id = UNSET
        elif isinstance(self.branch_id, UUID):
            branch_id = str(self.branch_id)
        else:
            branch_id = self.branch_id

        grand_total = self.grand_total

        refund_percent = self.refund_percent

        created_by_name: None | str | Unset
        if isinstance(self.created_by_name, Unset):
            created_by_name = UNSET
        else:
            created_by_name = self.created_by_name

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

        refund_payment_rows: list[dict[str, Any]] | None | Unset
        if isinstance(self.refund_payment_rows, Unset):
            refund_payment_rows = UNSET
        elif isinstance(self.refund_payment_rows, list):
            refund_payment_rows = []
            for refund_payment_rows_type_0_item_data in self.refund_payment_rows:
                refund_payment_rows_type_0_item = refund_payment_rows_type_0_item_data.to_dict()
                refund_payment_rows.append(refund_payment_rows_type_0_item)


        else:
            refund_payment_rows = self.refund_payment_rows

        settlement_amount = self.settlement_amount

        settlement_direction: None | str | Unset
        if isinstance(self.settlement_direction, Unset):
            settlement_direction = UNSET
        else:
            settlement_direction = self.settlement_direction

        settled_amount = self.settled_amount

        settled_payment_rows: list[dict[str, Any]] | None | Unset
        if isinstance(self.settled_payment_rows, Unset):
            settled_payment_rows = UNSET
        elif isinstance(self.settled_payment_rows, list):
            settled_payment_rows = []
            for settled_payment_rows_type_0_item_data in self.settled_payment_rows:
                settled_payment_rows_type_0_item = settled_payment_rows_type_0_item_data.to_dict()
                settled_payment_rows.append(settled_payment_rows_type_0_item)


        else:
            settled_payment_rows = self.settled_payment_rows

        exchange_new_order_id: None | str | Unset
        if isinstance(self.exchange_new_order_id, Unset):
            exchange_new_order_id = UNSET
        elif isinstance(self.exchange_new_order_id, UUID):
            exchange_new_order_id = str(self.exchange_new_order_id)
        else:
            exchange_new_order_id = self.exchange_new_order_id

        exchange_grand_total = self.exchange_grand_total

        price_diff = self.price_diff

        return_date: None | str | Unset
        if isinstance(self.return_date, Unset):
            return_date = UNSET
        elif isinstance(self.return_date, datetime.datetime):
            return_date = self.return_date.isoformat()
        else:
            return_date = self.return_date

        crm_contact_id: None | str | Unset
        if isinstance(self.crm_contact_id, Unset):
            crm_contact_id = UNSET
        elif isinstance(self.crm_contact_id, UUID):
            crm_contact_id = str(self.crm_contact_id)
        else:
            crm_contact_id = self.crm_contact_id

        outlet_id: None | str | Unset
        if isinstance(self.outlet_id, Unset):
            outlet_id = UNSET
        elif isinstance(self.outlet_id, UUID):
            outlet_id = str(self.outlet_id)
        else:
            outlet_id = self.outlet_id

        max_cash_refund = self.max_cash_refund

        force_full_cash_refund = self.force_full_cash_refund

        refund_bank_account_id: None | str | Unset
        if isinstance(self.refund_bank_account_id, Unset):
            refund_bank_account_id = UNSET
        elif isinstance(self.refund_bank_account_id, UUID):
            refund_bank_account_id = str(self.refund_bank_account_id)
        else:
            refund_bank_account_id = self.refund_bank_account_id

        refund_bank_account_label: None | str | Unset
        if isinstance(self.refund_bank_account_label, Unset):
            refund_bank_account_label = UNSET
        else:
            refund_bank_account_label = self.refund_bank_account_label

        branch_name: None | str | Unset
        if isinstance(self.branch_name, Unset):
            branch_name = UNSET
        else:
            branch_name = self.branch_name

        delivery_address: None | str | Unset
        if isinstance(self.delivery_address, Unset):
            delivery_address = UNSET
        else:
            delivery_address = self.delivery_address

        assigned_to_name: None | str | Unset
        if isinstance(self.assigned_to_name, Unset):
            assigned_to_name = UNSET
        else:
            assigned_to_name = self.assigned_to_name

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

        receiving_branch_ids: list[str] | None | Unset
        if isinstance(self.receiving_branch_ids, Unset):
            receiving_branch_ids = UNSET
        elif isinstance(self.receiving_branch_ids, list):
            receiving_branch_ids = []
            for receiving_branch_ids_type_0_item_data in self.receiving_branch_ids:
                receiving_branch_ids_type_0_item = str(receiving_branch_ids_type_0_item_data)
                receiving_branch_ids.append(receiving_branch_ids_type_0_item)


        else:
            receiving_branch_ids = self.receiving_branch_ids

        receiving_branch_names: list[str] | None | Unset
        if isinstance(self.receiving_branch_names, Unset):
            receiving_branch_names = UNSET
        elif isinstance(self.receiving_branch_names, list):
            receiving_branch_names = self.receiving_branch_names


        else:
            receiving_branch_names = self.receiving_branch_names

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

        customer_code: None | str | Unset
        if isinstance(self.customer_code, Unset):
            customer_code = UNSET
        else:
            customer_code = self.customer_code

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
        if return_code is not UNSET:
            field_dict["returnCode"] = return_code
        if order_id is not UNSET:
            field_dict["orderId"] = order_id
        if status is not UNSET:
            field_dict["status"] = status
        if reason is not UNSET:
            field_dict["reason"] = reason
        if return_type is not UNSET:
            field_dict["returnType"] = return_type
        if refund_amount is not UNSET:
            field_dict["refundAmount"] = refund_amount
        if refund_method is not UNSET:
            field_dict["refundMethod"] = refund_method
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if is_full_return is not UNSET:
            field_dict["isFullReturn"] = is_full_return
        if notes is not UNSET:
            field_dict["notes"] = notes
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id
        if grand_total is not UNSET:
            field_dict["grandTotal"] = grand_total
        if refund_percent is not UNSET:
            field_dict["refundPercent"] = refund_percent
        if created_by_name is not UNSET:
            field_dict["createdByName"] = created_by_name
        if contact_name is not UNSET:
            field_dict["contactName"] = contact_name
        if contact_phone is not UNSET:
            field_dict["contactPhone"] = contact_phone
        if refund_payment_rows is not UNSET:
            field_dict["refundPaymentRows"] = refund_payment_rows
        if settlement_amount is not UNSET:
            field_dict["settlementAmount"] = settlement_amount
        if settlement_direction is not UNSET:
            field_dict["settlementDirection"] = settlement_direction
        if settled_amount is not UNSET:
            field_dict["settledAmount"] = settled_amount
        if settled_payment_rows is not UNSET:
            field_dict["settledPaymentRows"] = settled_payment_rows
        if exchange_new_order_id is not UNSET:
            field_dict["exchangeNewOrderId"] = exchange_new_order_id
        if exchange_grand_total is not UNSET:
            field_dict["exchangeGrandTotal"] = exchange_grand_total
        if price_diff is not UNSET:
            field_dict["priceDiff"] = price_diff
        if return_date is not UNSET:
            field_dict["returnDate"] = return_date
        if crm_contact_id is not UNSET:
            field_dict["crmContactId"] = crm_contact_id
        if outlet_id is not UNSET:
            field_dict["outletId"] = outlet_id
        if max_cash_refund is not UNSET:
            field_dict["maxCashRefund"] = max_cash_refund
        if force_full_cash_refund is not UNSET:
            field_dict["forceFullCashRefund"] = force_full_cash_refund
        if refund_bank_account_id is not UNSET:
            field_dict["refundBankAccountId"] = refund_bank_account_id
        if refund_bank_account_label is not UNSET:
            field_dict["refundBankAccountLabel"] = refund_bank_account_label
        if branch_name is not UNSET:
            field_dict["branchName"] = branch_name
        if delivery_address is not UNSET:
            field_dict["deliveryAddress"] = delivery_address
        if assigned_to_name is not UNSET:
            field_dict["assignedToName"] = assigned_to_name
        if assignees is not UNSET:
            field_dict["assignees"] = assignees
        if receiving_branch_ids is not UNSET:
            field_dict["receivingBranchIds"] = receiving_branch_ids
        if receiving_branch_names is not UNSET:
            field_dict["receivingBranchNames"] = receiving_branch_names
        if delivery_employee is not UNSET:
            field_dict["deliveryEmployee"] = delivery_employee
        if delivered_at is not UNSET:
            field_dict["deliveredAt"] = delivered_at
        if customer_code is not UNSET:
            field_dict["customerCode"] = customer_code
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
        from ..models.order_return_refund_payment_row_dto import OrderReturnRefundPaymentRowDto # noqa: PLC0415
        from ..models.user_ref_dto import UserRefDto # noqa: PLC0415
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


        _order_id = d.pop("orderId", UNSET)
        order_id: UUID | Unset
        if isinstance(_order_id,  Unset):
            order_id = UNSET
        else:
            order_id = UUID(_order_id)




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


        def _parse_return_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        return_type = _parse_return_type(d.pop("returnType", UNSET))


        refund_amount = d.pop("refundAmount", UNSET)

        def _parse_refund_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        refund_method = _parse_refund_method(d.pop("refundMethod", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        is_full_return = d.pop("isFullReturn", UNSET)

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


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


        grand_total = d.pop("grandTotal", UNSET)

        refund_percent = d.pop("refundPercent", UNSET)

        def _parse_created_by_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by_name = _parse_created_by_name(d.pop("createdByName", UNSET))


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


        def _parse_refund_payment_rows(data: object) -> list[OrderReturnRefundPaymentRowDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                refund_payment_rows_type_0 = []
                _refund_payment_rows_type_0 = data
                for refund_payment_rows_type_0_item_data in (_refund_payment_rows_type_0):
                    refund_payment_rows_type_0_item = OrderReturnRefundPaymentRowDto.from_dict(refund_payment_rows_type_0_item_data)



                    refund_payment_rows_type_0.append(refund_payment_rows_type_0_item)

                return refund_payment_rows_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OrderReturnRefundPaymentRowDto] | None | Unset, data)

        refund_payment_rows = _parse_refund_payment_rows(d.pop("refundPaymentRows", UNSET))


        settlement_amount = d.pop("settlementAmount", UNSET)

        def _parse_settlement_direction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        settlement_direction = _parse_settlement_direction(d.pop("settlementDirection", UNSET))


        settled_amount = d.pop("settledAmount", UNSET)

        def _parse_settled_payment_rows(data: object) -> list[OrderReturnRefundPaymentRowDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                settled_payment_rows_type_0 = []
                _settled_payment_rows_type_0 = data
                for settled_payment_rows_type_0_item_data in (_settled_payment_rows_type_0):
                    settled_payment_rows_type_0_item = OrderReturnRefundPaymentRowDto.from_dict(settled_payment_rows_type_0_item_data)



                    settled_payment_rows_type_0.append(settled_payment_rows_type_0_item)

                return settled_payment_rows_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OrderReturnRefundPaymentRowDto] | None | Unset, data)

        settled_payment_rows = _parse_settled_payment_rows(d.pop("settledPaymentRows", UNSET))


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


        exchange_grand_total = d.pop("exchangeGrandTotal", UNSET)

        price_diff = d.pop("priceDiff", UNSET)

        def _parse_return_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                return_date_type_0 = datetime.datetime.fromisoformat(data)



                return return_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        return_date = _parse_return_date(d.pop("returnDate", UNSET))


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


        max_cash_refund = d.pop("maxCashRefund", UNSET)

        force_full_cash_refund = d.pop("forceFullCashRefund", UNSET)

        def _parse_refund_bank_account_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                refund_bank_account_id_type_0 = UUID(data)



                return refund_bank_account_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        refund_bank_account_id = _parse_refund_bank_account_id(d.pop("refundBankAccountId", UNSET))


        def _parse_refund_bank_account_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        refund_bank_account_label = _parse_refund_bank_account_label(d.pop("refundBankAccountLabel", UNSET))


        def _parse_branch_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch_name = _parse_branch_name(d.pop("branchName", UNSET))


        def _parse_delivery_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        delivery_address = _parse_delivery_address(d.pop("deliveryAddress", UNSET))


        def _parse_assigned_to_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assigned_to_name = _parse_assigned_to_name(d.pop("assignedToName", UNSET))


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


        def _parse_receiving_branch_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                receiving_branch_ids_type_0 = []
                _receiving_branch_ids_type_0 = data
                for receiving_branch_ids_type_0_item_data in (_receiving_branch_ids_type_0):
                    receiving_branch_ids_type_0_item = UUID(receiving_branch_ids_type_0_item_data)



                    receiving_branch_ids_type_0.append(receiving_branch_ids_type_0_item)

                return receiving_branch_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        receiving_branch_ids = _parse_receiving_branch_ids(d.pop("receivingBranchIds", UNSET))


        def _parse_receiving_branch_names(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                receiving_branch_names_type_0 = cast(list[str], data)

                return receiving_branch_names_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        receiving_branch_names = _parse_receiving_branch_names(d.pop("receivingBranchNames", UNSET))


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


        def _parse_customer_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_code = _parse_customer_code(d.pop("customerCode", UNSET))


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




        order_return_list_dto = cls(
            id=id,
            return_code=return_code,
            order_id=order_id,
            status=status,
            reason=reason,
            return_type=return_type,
            refund_amount=refund_amount,
            refund_method=refund_method,
            created_at=created_at,
            is_full_return=is_full_return,
            notes=notes,
            completed_at=completed_at,
            branch_id=branch_id,
            grand_total=grand_total,
            refund_percent=refund_percent,
            created_by_name=created_by_name,
            contact_name=contact_name,
            contact_phone=contact_phone,
            refund_payment_rows=refund_payment_rows,
            settlement_amount=settlement_amount,
            settlement_direction=settlement_direction,
            settled_amount=settled_amount,
            settled_payment_rows=settled_payment_rows,
            exchange_new_order_id=exchange_new_order_id,
            exchange_grand_total=exchange_grand_total,
            price_diff=price_diff,
            return_date=return_date,
            crm_contact_id=crm_contact_id,
            outlet_id=outlet_id,
            max_cash_refund=max_cash_refund,
            force_full_cash_refund=force_full_cash_refund,
            refund_bank_account_id=refund_bank_account_id,
            refund_bank_account_label=refund_bank_account_label,
            branch_name=branch_name,
            delivery_address=delivery_address,
            assigned_to_name=assigned_to_name,
            assignees=assignees,
            receiving_branch_ids=receiving_branch_ids,
            receiving_branch_names=receiving_branch_names,
            delivery_employee=delivery_employee,
            delivered_at=delivered_at,
            customer_code=customer_code,
            customer_info=customer_info,
            outlet_info=outlet_info,
        )

        return order_return_list_dto


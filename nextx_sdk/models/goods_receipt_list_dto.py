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
  from ..models.payment_row_dto import PaymentRowDto
  from ..models.supplier_list_info_dto import SupplierListInfoDto





T = TypeVar("T", bound="GoodsReceiptListDto")



@_attrs_define
class GoodsReceiptListDto:
    

    id: UUID | Unset = UNSET
    code: None | str | Unset = UNSET
    branch_id: UUID | Unset = UNSET
    branch_name: None | str | Unset = UNSET
    supplier_id: None | Unset | UUID = UNSET
    supplier_name: None | str | Unset = UNSET
    purchase_order_id: None | Unset | UUID = UNSET
    receipt_date: datetime.date | Unset = UNSET
    status: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    total_amount: float | Unset = UNSET
    discount_amount: float | Unset = UNSET
    shipping_fee: float | Unset = UNSET
    tax_amount: float | Unset = UNSET
    grand_total: float | Unset = UNSET
    line_count: int | Unset = UNSET
    total_quantity: int | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    created_by_name: None | str | Unset = UNSET
    paid_amount: float | Unset = UNSET
    payment_status: None | str | Unset = UNSET
    payment_due_date: datetime.date | None | Unset = UNSET
    payment_method: None | str | Unset = UNSET
    deduct_from_po: float | Unset = UNSET
    payment_breakdown: list[PaymentRowDto] | None | Unset = UNSET
    has_returnable_lines: bool | Unset = UNSET
    return_status: None | str | Unset = UNSET
    import_cost_total: float | Unset = UNSET
    notes: None | str | Unset = UNSET
    posted_at: datetime.datetime | None | Unset = UNSET
    supplier_info: SupplierListInfoDto | Unset = UNSET
    payment_bank_label: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.payment_row_dto import PaymentRowDto # noqa: PLC0415
        from ..models.supplier_list_info_dto import SupplierListInfoDto # noqa: PLC0415
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        branch_id: str | Unset = UNSET
        if not isinstance(self.branch_id, Unset):
            branch_id = str(self.branch_id)

        branch_name: None | str | Unset
        if isinstance(self.branch_name, Unset):
            branch_name = UNSET
        else:
            branch_name = self.branch_name

        supplier_id: None | str | Unset
        if isinstance(self.supplier_id, Unset):
            supplier_id = UNSET
        elif isinstance(self.supplier_id, UUID):
            supplier_id = str(self.supplier_id)
        else:
            supplier_id = self.supplier_id

        supplier_name: None | str | Unset
        if isinstance(self.supplier_name, Unset):
            supplier_name = UNSET
        else:
            supplier_name = self.supplier_name

        purchase_order_id: None | str | Unset
        if isinstance(self.purchase_order_id, Unset):
            purchase_order_id = UNSET
        elif isinstance(self.purchase_order_id, UUID):
            purchase_order_id = str(self.purchase_order_id)
        else:
            purchase_order_id = self.purchase_order_id

        receipt_date: str | Unset = UNSET
        if not isinstance(self.receipt_date, Unset):
            receipt_date = self.receipt_date.isoformat()

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        total_amount = self.total_amount

        discount_amount = self.discount_amount

        shipping_fee = self.shipping_fee

        tax_amount = self.tax_amount

        grand_total = self.grand_total

        line_count = self.line_count

        total_quantity = self.total_quantity

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by_name: None | str | Unset
        if isinstance(self.created_by_name, Unset):
            created_by_name = UNSET
        else:
            created_by_name = self.created_by_name

        paid_amount = self.paid_amount

        payment_status: None | str | Unset
        if isinstance(self.payment_status, Unset):
            payment_status = UNSET
        else:
            payment_status = self.payment_status

        payment_due_date: None | str | Unset
        if isinstance(self.payment_due_date, Unset):
            payment_due_date = UNSET
        elif isinstance(self.payment_due_date, datetime.date):
            payment_due_date = self.payment_due_date.isoformat()
        else:
            payment_due_date = self.payment_due_date

        payment_method: None | str | Unset
        if isinstance(self.payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = self.payment_method

        deduct_from_po = self.deduct_from_po

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

        has_returnable_lines = self.has_returnable_lines

        return_status: None | str | Unset
        if isinstance(self.return_status, Unset):
            return_status = UNSET
        else:
            return_status = self.return_status

        import_cost_total = self.import_cost_total

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        posted_at: None | str | Unset
        if isinstance(self.posted_at, Unset):
            posted_at = UNSET
        elif isinstance(self.posted_at, datetime.datetime):
            posted_at = self.posted_at.isoformat()
        else:
            posted_at = self.posted_at

        supplier_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.supplier_info, Unset):
            supplier_info = self.supplier_info.to_dict()

        payment_bank_label: None | str | Unset
        if isinstance(self.payment_bank_label, Unset):
            payment_bank_label = UNSET
        else:
            payment_bank_label = self.payment_bank_label


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if code is not UNSET:
            field_dict["code"] = code
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id
        if branch_name is not UNSET:
            field_dict["branchName"] = branch_name
        if supplier_id is not UNSET:
            field_dict["supplierId"] = supplier_id
        if supplier_name is not UNSET:
            field_dict["supplierName"] = supplier_name
        if purchase_order_id is not UNSET:
            field_dict["purchaseOrderId"] = purchase_order_id
        if receipt_date is not UNSET:
            field_dict["receiptDate"] = receipt_date
        if status is not UNSET:
            field_dict["status"] = status
        if source is not UNSET:
            field_dict["source"] = source
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if discount_amount is not UNSET:
            field_dict["discountAmount"] = discount_amount
        if shipping_fee is not UNSET:
            field_dict["shippingFee"] = shipping_fee
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if grand_total is not UNSET:
            field_dict["grandTotal"] = grand_total
        if line_count is not UNSET:
            field_dict["lineCount"] = line_count
        if total_quantity is not UNSET:
            field_dict["totalQuantity"] = total_quantity
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by_name is not UNSET:
            field_dict["createdByName"] = created_by_name
        if paid_amount is not UNSET:
            field_dict["paidAmount"] = paid_amount
        if payment_status is not UNSET:
            field_dict["paymentStatus"] = payment_status
        if payment_due_date is not UNSET:
            field_dict["paymentDueDate"] = payment_due_date
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method
        if deduct_from_po is not UNSET:
            field_dict["deductFromPo"] = deduct_from_po
        if payment_breakdown is not UNSET:
            field_dict["paymentBreakdown"] = payment_breakdown
        if has_returnable_lines is not UNSET:
            field_dict["hasReturnableLines"] = has_returnable_lines
        if return_status is not UNSET:
            field_dict["returnStatus"] = return_status
        if import_cost_total is not UNSET:
            field_dict["importCostTotal"] = import_cost_total
        if notes is not UNSET:
            field_dict["notes"] = notes
        if posted_at is not UNSET:
            field_dict["postedAt"] = posted_at
        if supplier_info is not UNSET:
            field_dict["supplierInfo"] = supplier_info
        if payment_bank_label is not UNSET:
            field_dict["paymentBankLabel"] = payment_bank_label

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payment_row_dto import PaymentRowDto # noqa: PLC0415
        from ..models.supplier_list_info_dto import SupplierListInfoDto # noqa: PLC0415
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


        def _parse_supplier_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                supplier_id_type_0 = UUID(data)



                return supplier_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        supplier_id = _parse_supplier_id(d.pop("supplierId", UNSET))


        def _parse_supplier_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        supplier_name = _parse_supplier_name(d.pop("supplierName", UNSET))


        def _parse_purchase_order_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                purchase_order_id_type_0 = UUID(data)



                return purchase_order_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        purchase_order_id = _parse_purchase_order_id(d.pop("purchaseOrderId", UNSET))


        _receipt_date = d.pop("receiptDate", UNSET)
        receipt_date: datetime.date | Unset
        if isinstance(_receipt_date,  Unset):
            receipt_date = UNSET
        else:
            receipt_date = datetime.date.fromisoformat(_receipt_date)




        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))


        total_amount = d.pop("totalAmount", UNSET)

        discount_amount = d.pop("discountAmount", UNSET)

        shipping_fee = d.pop("shippingFee", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        grand_total = d.pop("grandTotal", UNSET)

        line_count = d.pop("lineCount", UNSET)

        total_quantity = d.pop("totalQuantity", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_created_by_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by_name = _parse_created_by_name(d.pop("createdByName", UNSET))


        paid_amount = d.pop("paidAmount", UNSET)

        def _parse_payment_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_status = _parse_payment_status(d.pop("paymentStatus", UNSET))


        def _parse_payment_due_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                payment_due_date_type_0 = datetime.date.fromisoformat(data)



                return payment_due_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        payment_due_date = _parse_payment_due_date(d.pop("paymentDueDate", UNSET))


        def _parse_payment_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_method = _parse_payment_method(d.pop("paymentMethod", UNSET))


        deduct_from_po = d.pop("deductFromPo", UNSET)

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


        has_returnable_lines = d.pop("hasReturnableLines", UNSET)

        def _parse_return_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        return_status = _parse_return_status(d.pop("returnStatus", UNSET))


        import_cost_total = d.pop("importCostTotal", UNSET)

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


        def _parse_posted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                posted_at_type_0 = datetime.datetime.fromisoformat(data)



                return posted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        posted_at = _parse_posted_at(d.pop("postedAt", UNSET))


        _supplier_info = d.pop("supplierInfo", UNSET)
        supplier_info: SupplierListInfoDto | Unset
        if isinstance(_supplier_info,  Unset):
            supplier_info = UNSET
        else:
            supplier_info = SupplierListInfoDto.from_dict(_supplier_info)




        def _parse_payment_bank_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_bank_label = _parse_payment_bank_label(d.pop("paymentBankLabel", UNSET))


        goods_receipt_list_dto = cls(
            id=id,
            code=code,
            branch_id=branch_id,
            branch_name=branch_name,
            supplier_id=supplier_id,
            supplier_name=supplier_name,
            purchase_order_id=purchase_order_id,
            receipt_date=receipt_date,
            status=status,
            source=source,
            total_amount=total_amount,
            discount_amount=discount_amount,
            shipping_fee=shipping_fee,
            tax_amount=tax_amount,
            grand_total=grand_total,
            line_count=line_count,
            total_quantity=total_quantity,
            created_at=created_at,
            created_by_name=created_by_name,
            paid_amount=paid_amount,
            payment_status=payment_status,
            payment_due_date=payment_due_date,
            payment_method=payment_method,
            deduct_from_po=deduct_from_po,
            payment_breakdown=payment_breakdown,
            has_returnable_lines=has_returnable_lines,
            return_status=return_status,
            import_cost_total=import_cost_total,
            notes=notes,
            posted_at=posted_at,
            supplier_info=supplier_info,
            payment_bank_label=payment_bank_label,
        )

        return goods_receipt_list_dto


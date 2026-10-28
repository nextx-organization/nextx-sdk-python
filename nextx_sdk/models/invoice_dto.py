from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.invoice_dto_invoice_context import check_invoice_dto_invoice_context
from ..models.invoice_dto_invoice_context import InvoiceDtoInvoiceContext
from ..models.invoice_dto_provider_code import check_invoice_dto_provider_code
from ..models.invoice_dto_provider_code import InvoiceDtoProviderCode
from ..models.invoice_dto_status import check_invoice_dto_status
from ..models.invoice_dto_status import InvoiceDtoStatus
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="InvoiceDto")



@_attrs_define
class InvoiceDto:
    

    id: UUID | Unset = UNSET
    workspace_id: UUID | Unset = UNSET
    invoice_context: InvoiceDtoInvoiceContext | Unset = UNSET
    provider_code: InvoiceDtoProviderCode | Unset = UNSET
    series_id: None | Unset | UUID = UNSET
    invoice_number: None | str | Unset = UNSET
    invoice_series_code: None | str | Unset = UNSET
    cqt_code: None | str | Unset = UNSET
    status: InvoiceDtoStatus | Unset = UNSET
    reference_type: None | str | Unset = UNSET
    reference_id: UUID | Unset = UNSET
    reference_code: None | str | Unset = UNSET
    invoice_date: datetime.date | Unset = UNSET
    tax_period: None | str | Unset = UNSET
    buyer_name: None | str | Unset = UNSET
    buyer_tax_code: None | str | Unset = UNSET
    buyer_address: None | str | Unset = UNSET
    buyer_phone: None | str | Unset = UNSET
    buyer_email: None | str | Unset = UNSET
    buyer_id_no: None | str | Unset = UNSET
    buyer_id_type: None | str | Unset = UNSET
    subtotal: float | Unset = UNSET
    vat_rate: float | Unset = UNSET
    vat_amount: float | Unset = UNSET
    total: float | Unset = UNSET
    currency: None | str | Unset = UNSET
    payment_method_label: None | str | Unset = UNSET
    error_message: None | str | Unset = UNSET
    cancel_reason: None | str | Unset = UNSET
    issued_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    branch_id: None | Unset | UUID = UNSET
    buyer_contact_name: None | str | Unset = UNSET
    sent_at: datetime.datetime | None | Unset = UNSET
    invoice_date_manual: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        workspace_id: str | Unset = UNSET
        if not isinstance(self.workspace_id, Unset):
            workspace_id = str(self.workspace_id)

        invoice_context: str | Unset = UNSET
        if not isinstance(self.invoice_context, Unset):
            invoice_context = self.invoice_context


        provider_code: str | Unset = UNSET
        if not isinstance(self.provider_code, Unset):
            provider_code = self.provider_code


        series_id: None | str | Unset
        if isinstance(self.series_id, Unset):
            series_id = UNSET
        elif isinstance(self.series_id, UUID):
            series_id = str(self.series_id)
        else:
            series_id = self.series_id

        invoice_number: None | str | Unset
        if isinstance(self.invoice_number, Unset):
            invoice_number = UNSET
        else:
            invoice_number = self.invoice_number

        invoice_series_code: None | str | Unset
        if isinstance(self.invoice_series_code, Unset):
            invoice_series_code = UNSET
        else:
            invoice_series_code = self.invoice_series_code

        cqt_code: None | str | Unset
        if isinstance(self.cqt_code, Unset):
            cqt_code = UNSET
        else:
            cqt_code = self.cqt_code

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status


        reference_type: None | str | Unset
        if isinstance(self.reference_type, Unset):
            reference_type = UNSET
        else:
            reference_type = self.reference_type

        reference_id: str | Unset = UNSET
        if not isinstance(self.reference_id, Unset):
            reference_id = str(self.reference_id)

        reference_code: None | str | Unset
        if isinstance(self.reference_code, Unset):
            reference_code = UNSET
        else:
            reference_code = self.reference_code

        invoice_date: str | Unset = UNSET
        if not isinstance(self.invoice_date, Unset):
            invoice_date = self.invoice_date.isoformat()

        tax_period: None | str | Unset
        if isinstance(self.tax_period, Unset):
            tax_period = UNSET
        else:
            tax_period = self.tax_period

        buyer_name: None | str | Unset
        if isinstance(self.buyer_name, Unset):
            buyer_name = UNSET
        else:
            buyer_name = self.buyer_name

        buyer_tax_code: None | str | Unset
        if isinstance(self.buyer_tax_code, Unset):
            buyer_tax_code = UNSET
        else:
            buyer_tax_code = self.buyer_tax_code

        buyer_address: None | str | Unset
        if isinstance(self.buyer_address, Unset):
            buyer_address = UNSET
        else:
            buyer_address = self.buyer_address

        buyer_phone: None | str | Unset
        if isinstance(self.buyer_phone, Unset):
            buyer_phone = UNSET
        else:
            buyer_phone = self.buyer_phone

        buyer_email: None | str | Unset
        if isinstance(self.buyer_email, Unset):
            buyer_email = UNSET
        else:
            buyer_email = self.buyer_email

        buyer_id_no: None | str | Unset
        if isinstance(self.buyer_id_no, Unset):
            buyer_id_no = UNSET
        else:
            buyer_id_no = self.buyer_id_no

        buyer_id_type: None | str | Unset
        if isinstance(self.buyer_id_type, Unset):
            buyer_id_type = UNSET
        else:
            buyer_id_type = self.buyer_id_type

        subtotal = self.subtotal

        vat_rate = self.vat_rate

        vat_amount = self.vat_amount

        total = self.total

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        payment_method_label: None | str | Unset
        if isinstance(self.payment_method_label, Unset):
            payment_method_label = UNSET
        else:
            payment_method_label = self.payment_method_label

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        cancel_reason: None | str | Unset
        if isinstance(self.cancel_reason, Unset):
            cancel_reason = UNSET
        else:
            cancel_reason = self.cancel_reason

        issued_at: None | str | Unset
        if isinstance(self.issued_at, Unset):
            issued_at = UNSET
        elif isinstance(self.issued_at, datetime.datetime):
            issued_at = self.issued_at.isoformat()
        else:
            issued_at = self.issued_at

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        branch_id: None | str | Unset
        if isinstance(self.branch_id, Unset):
            branch_id = UNSET
        elif isinstance(self.branch_id, UUID):
            branch_id = str(self.branch_id)
        else:
            branch_id = self.branch_id

        buyer_contact_name: None | str | Unset
        if isinstance(self.buyer_contact_name, Unset):
            buyer_contact_name = UNSET
        else:
            buyer_contact_name = self.buyer_contact_name

        sent_at: None | str | Unset
        if isinstance(self.sent_at, Unset):
            sent_at = UNSET
        elif isinstance(self.sent_at, datetime.datetime):
            sent_at = self.sent_at.isoformat()
        else:
            sent_at = self.sent_at

        invoice_date_manual = self.invoice_date_manual


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id
        if invoice_context is not UNSET:
            field_dict["invoiceContext"] = invoice_context
        if provider_code is not UNSET:
            field_dict["providerCode"] = provider_code
        if series_id is not UNSET:
            field_dict["seriesId"] = series_id
        if invoice_number is not UNSET:
            field_dict["invoiceNumber"] = invoice_number
        if invoice_series_code is not UNSET:
            field_dict["invoiceSeriesCode"] = invoice_series_code
        if cqt_code is not UNSET:
            field_dict["cqtCode"] = cqt_code
        if status is not UNSET:
            field_dict["status"] = status
        if reference_type is not UNSET:
            field_dict["referenceType"] = reference_type
        if reference_id is not UNSET:
            field_dict["referenceId"] = reference_id
        if reference_code is not UNSET:
            field_dict["referenceCode"] = reference_code
        if invoice_date is not UNSET:
            field_dict["invoiceDate"] = invoice_date
        if tax_period is not UNSET:
            field_dict["taxPeriod"] = tax_period
        if buyer_name is not UNSET:
            field_dict["buyerName"] = buyer_name
        if buyer_tax_code is not UNSET:
            field_dict["buyerTaxCode"] = buyer_tax_code
        if buyer_address is not UNSET:
            field_dict["buyerAddress"] = buyer_address
        if buyer_phone is not UNSET:
            field_dict["buyerPhone"] = buyer_phone
        if buyer_email is not UNSET:
            field_dict["buyerEmail"] = buyer_email
        if buyer_id_no is not UNSET:
            field_dict["buyerIdNo"] = buyer_id_no
        if buyer_id_type is not UNSET:
            field_dict["buyerIdType"] = buyer_id_type
        if subtotal is not UNSET:
            field_dict["subtotal"] = subtotal
        if vat_rate is not UNSET:
            field_dict["vatRate"] = vat_rate
        if vat_amount is not UNSET:
            field_dict["vatAmount"] = vat_amount
        if total is not UNSET:
            field_dict["total"] = total
        if currency is not UNSET:
            field_dict["currency"] = currency
        if payment_method_label is not UNSET:
            field_dict["paymentMethodLabel"] = payment_method_label
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if cancel_reason is not UNSET:
            field_dict["cancelReason"] = cancel_reason
        if issued_at is not UNSET:
            field_dict["issuedAt"] = issued_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id
        if buyer_contact_name is not UNSET:
            field_dict["buyerContactName"] = buyer_contact_name
        if sent_at is not UNSET:
            field_dict["sentAt"] = sent_at
        if invoice_date_manual is not UNSET:
            field_dict["invoiceDateManual"] = invoice_date_manual

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




        _workspace_id = d.pop("workspaceId", UNSET)
        workspace_id: UUID | Unset
        if isinstance(_workspace_id,  Unset):
            workspace_id = UNSET
        else:
            workspace_id = UUID(_workspace_id)




        _invoice_context = d.pop("invoiceContext", UNSET)
        invoice_context: InvoiceDtoInvoiceContext | Unset
        if isinstance(_invoice_context,  Unset):
            invoice_context = UNSET
        else:
            invoice_context = check_invoice_dto_invoice_context(_invoice_context)




        _provider_code = d.pop("providerCode", UNSET)
        provider_code: InvoiceDtoProviderCode | Unset
        if isinstance(_provider_code,  Unset):
            provider_code = UNSET
        else:
            provider_code = check_invoice_dto_provider_code(_provider_code)




        def _parse_series_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                series_id_type_0 = UUID(data)



                return series_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        series_id = _parse_series_id(d.pop("seriesId", UNSET))


        def _parse_invoice_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        invoice_number = _parse_invoice_number(d.pop("invoiceNumber", UNSET))


        def _parse_invoice_series_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        invoice_series_code = _parse_invoice_series_code(d.pop("invoiceSeriesCode", UNSET))


        def _parse_cqt_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cqt_code = _parse_cqt_code(d.pop("cqtCode", UNSET))


        _status = d.pop("status", UNSET)
        status: InvoiceDtoStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = check_invoice_dto_status(_status)




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




        def _parse_reference_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reference_code = _parse_reference_code(d.pop("referenceCode", UNSET))


        _invoice_date = d.pop("invoiceDate", UNSET)
        invoice_date: datetime.date | Unset
        if isinstance(_invoice_date,  Unset):
            invoice_date = UNSET
        else:
            invoice_date = datetime.date.fromisoformat(_invoice_date)




        def _parse_tax_period(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tax_period = _parse_tax_period(d.pop("taxPeriod", UNSET))


        def _parse_buyer_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        buyer_name = _parse_buyer_name(d.pop("buyerName", UNSET))


        def _parse_buyer_tax_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        buyer_tax_code = _parse_buyer_tax_code(d.pop("buyerTaxCode", UNSET))


        def _parse_buyer_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        buyer_address = _parse_buyer_address(d.pop("buyerAddress", UNSET))


        def _parse_buyer_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        buyer_phone = _parse_buyer_phone(d.pop("buyerPhone", UNSET))


        def _parse_buyer_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        buyer_email = _parse_buyer_email(d.pop("buyerEmail", UNSET))


        def _parse_buyer_id_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        buyer_id_no = _parse_buyer_id_no(d.pop("buyerIdNo", UNSET))


        def _parse_buyer_id_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        buyer_id_type = _parse_buyer_id_type(d.pop("buyerIdType", UNSET))


        subtotal = d.pop("subtotal", UNSET)

        vat_rate = d.pop("vatRate", UNSET)

        vat_amount = d.pop("vatAmount", UNSET)

        total = d.pop("total", UNSET)

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        def _parse_payment_method_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_method_label = _parse_payment_method_label(d.pop("paymentMethodLabel", UNSET))


        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("errorMessage", UNSET))


        def _parse_cancel_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cancel_reason = _parse_cancel_reason(d.pop("cancelReason", UNSET))


        def _parse_issued_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                issued_at_type_0 = datetime.datetime.fromisoformat(data)



                return issued_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        issued_at = _parse_issued_at(d.pop("issuedAt", UNSET))


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


        def _parse_buyer_contact_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        buyer_contact_name = _parse_buyer_contact_name(d.pop("buyerContactName", UNSET))


        def _parse_sent_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sent_at_type_0 = datetime.datetime.fromisoformat(data)



                return sent_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        sent_at = _parse_sent_at(d.pop("sentAt", UNSET))


        invoice_date_manual = d.pop("invoiceDateManual", UNSET)

        invoice_dto = cls(
            id=id,
            workspace_id=workspace_id,
            invoice_context=invoice_context,
            provider_code=provider_code,
            series_id=series_id,
            invoice_number=invoice_number,
            invoice_series_code=invoice_series_code,
            cqt_code=cqt_code,
            status=status,
            reference_type=reference_type,
            reference_id=reference_id,
            reference_code=reference_code,
            invoice_date=invoice_date,
            tax_period=tax_period,
            buyer_name=buyer_name,
            buyer_tax_code=buyer_tax_code,
            buyer_address=buyer_address,
            buyer_phone=buyer_phone,
            buyer_email=buyer_email,
            buyer_id_no=buyer_id_no,
            buyer_id_type=buyer_id_type,
            subtotal=subtotal,
            vat_rate=vat_rate,
            vat_amount=vat_amount,
            total=total,
            currency=currency,
            payment_method_label=payment_method_label,
            error_message=error_message,
            cancel_reason=cancel_reason,
            issued_at=issued_at,
            created_at=created_at,
            updated_at=updated_at,
            branch_id=branch_id,
            buyer_contact_name=buyer_contact_name,
            sent_at=sent_at,
            invoice_date_manual=invoice_date_manual,
        )

        return invoice_dto


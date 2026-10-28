from typing import Literal

InvoiceDtoInvoiceContext = Literal['OperatorInvoice', 'SalesInvoice']

INVOICE_DTO_INVOICE_CONTEXT_VALUES: set[InvoiceDtoInvoiceContext] = { 'OperatorInvoice', 'SalesInvoice',  }

def check_invoice_dto_invoice_context(value: str) -> InvoiceDtoInvoiceContext:
    if value in INVOICE_DTO_INVOICE_CONTEXT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVOICE_DTO_INVOICE_CONTEXT_VALUES!r}")

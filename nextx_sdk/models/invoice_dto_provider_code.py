from typing import Literal

InvoiceDtoProviderCode = Literal['Bkav', 'Fpt', 'Misa', 'None', 'Viettel', 'Vnpt', 'WinInvoice']

INVOICE_DTO_PROVIDER_CODE_VALUES: set[InvoiceDtoProviderCode] = { 'Bkav', 'Fpt', 'Misa', 'None', 'Viettel', 'Vnpt', 'WinInvoice',  }

def check_invoice_dto_provider_code(value: str) -> InvoiceDtoProviderCode:
    if value in INVOICE_DTO_PROVIDER_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVOICE_DTO_PROVIDER_CODE_VALUES!r}")

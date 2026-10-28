from typing import Literal

InvoiceDtoStatus = Literal['ADJUSTED', 'ADJUSTED_AT_PROVIDER', 'CANCELLED', 'DELETED_AT_PROVIDER', 'DRAFT', 'ERROR', 'ISSUED', 'PENDING', 'REPLACED_AT_PROVIDER']

INVOICE_DTO_STATUS_VALUES: set[InvoiceDtoStatus] = { 'ADJUSTED', 'ADJUSTED_AT_PROVIDER', 'CANCELLED', 'DELETED_AT_PROVIDER', 'DRAFT', 'ERROR', 'ISSUED', 'PENDING', 'REPLACED_AT_PROVIDER',  }

def check_invoice_dto_status(value: str) -> InvoiceDtoStatus:
    if value in INVOICE_DTO_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVOICE_DTO_STATUS_VALUES!r}")

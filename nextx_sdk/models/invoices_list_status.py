from typing import Literal

InvoicesListStatus = Literal['ADJUSTED', 'ADJUSTED_AT_PROVIDER', 'CANCELLED', 'DELETED_AT_PROVIDER', 'DRAFT', 'ERROR', 'ISSUED', 'PENDING', 'REPLACED_AT_PROVIDER']

INVOICES_LIST_STATUS_VALUES: set[InvoicesListStatus] = { 'ADJUSTED', 'ADJUSTED_AT_PROVIDER', 'CANCELLED', 'DELETED_AT_PROVIDER', 'DRAFT', 'ERROR', 'ISSUED', 'PENDING', 'REPLACED_AT_PROVIDER',  }

def check_invoices_list_status(value: str) -> InvoicesListStatus:
    if value in INVOICES_LIST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVOICES_LIST_STATUS_VALUES!r}")

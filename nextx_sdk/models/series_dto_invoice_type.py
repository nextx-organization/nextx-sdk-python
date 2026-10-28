from typing import Literal

SeriesDtoInvoiceType = Literal['EXPORT', 'NON_VAT', 'VAT']

SERIES_DTO_INVOICE_TYPE_VALUES: set[SeriesDtoInvoiceType] = { 'EXPORT', 'NON_VAT', 'VAT',  }

def check_series_dto_invoice_type(value: str) -> SeriesDtoInvoiceType:
    if value in SERIES_DTO_INVOICE_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SERIES_DTO_INVOICE_TYPE_VALUES!r}")

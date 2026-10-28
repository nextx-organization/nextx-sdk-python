from typing import Literal

SeriesListProviderCode = Literal['Bkav', 'Fpt', 'Misa', 'None', 'Viettel', 'Vnpt', 'WinInvoice']

SERIES_LIST_PROVIDER_CODE_VALUES: set[SeriesListProviderCode] = { 'Bkav', 'Fpt', 'Misa', 'None', 'Viettel', 'Vnpt', 'WinInvoice',  }

def check_series_list_provider_code(value: str) -> SeriesListProviderCode:
    if value in SERIES_LIST_PROVIDER_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SERIES_LIST_PROVIDER_CODE_VALUES!r}")

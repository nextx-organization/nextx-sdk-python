from typing import Literal

SeriesDtoProviderCode = Literal['Bkav', 'Fpt', 'Misa', 'None', 'Viettel', 'Vnpt', 'WinInvoice']

SERIES_DTO_PROVIDER_CODE_VALUES: set[SeriesDtoProviderCode] = { 'Bkav', 'Fpt', 'Misa', 'None', 'Viettel', 'Vnpt', 'WinInvoice',  }

def check_series_dto_provider_code(value: str) -> SeriesDtoProviderCode:
    if value in SERIES_DTO_PROVIDER_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SERIES_DTO_PROVIDER_CODE_VALUES!r}")

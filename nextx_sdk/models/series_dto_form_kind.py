from typing import Literal

SeriesDtoFormKind = Literal['CashRegister', 'Normal']

SERIES_DTO_FORM_KIND_VALUES: set[SeriesDtoFormKind] = { 'CashRegister', 'Normal',  }

def check_series_dto_form_kind(value: str) -> SeriesDtoFormKind:
    if value in SERIES_DTO_FORM_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SERIES_DTO_FORM_KIND_VALUES!r}")

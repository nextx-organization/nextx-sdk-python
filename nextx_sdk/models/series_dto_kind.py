from typing import Literal

SeriesDtoKind = Literal['DeliveryNote', 'Sales', 'Ticket', 'Vat']

SERIES_DTO_KIND_VALUES: set[SeriesDtoKind] = { 'DeliveryNote', 'Sales', 'Ticket', 'Vat',  }

def check_series_dto_kind(value: str) -> SeriesDtoKind:
    if value in SERIES_DTO_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SERIES_DTO_KIND_VALUES!r}")

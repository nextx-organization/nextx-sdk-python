from typing import Literal

OutletDtoVisitFrequency = Literal['Biweekly', 'Daily', 'Monthly', 'Weekly']

OUTLET_DTO_VISIT_FREQUENCY_VALUES: set[OutletDtoVisitFrequency] = { 'Biweekly', 'Daily', 'Monthly', 'Weekly',  }

def check_outlet_dto_visit_frequency(value: str) -> OutletDtoVisitFrequency:
    if value in OUTLET_DTO_VISIT_FREQUENCY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OUTLET_DTO_VISIT_FREQUENCY_VALUES!r}")

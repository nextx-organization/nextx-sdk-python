from typing import Literal

OutletDtoOutletStatus = Literal['Active', 'Closed', 'Prospect', 'TempClosed']

OUTLET_DTO_OUTLET_STATUS_VALUES: set[OutletDtoOutletStatus] = { 'Active', 'Closed', 'Prospect', 'TempClosed',  }

def check_outlet_dto_outlet_status(value: str) -> OutletDtoOutletStatus:
    if value in OUTLET_DTO_OUTLET_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OUTLET_DTO_OUTLET_STATUS_VALUES!r}")

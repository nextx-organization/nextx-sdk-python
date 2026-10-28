from typing import Literal

CheckinLogDtoType = Literal['Field', 'Outlet']

CHECKIN_LOG_DTO_TYPE_VALUES: set[CheckinLogDtoType] = { 'Field', 'Outlet',  }

def check_checkin_log_dto_type(value: str) -> CheckinLogDtoType:
    if value in CHECKIN_LOG_DTO_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CHECKIN_LOG_DTO_TYPE_VALUES!r}")

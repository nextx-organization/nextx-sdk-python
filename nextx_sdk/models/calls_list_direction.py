from typing import Literal

CallsListDirection = Literal['inbound', 'outbound']

CALLS_LIST_DIRECTION_VALUES: set[CallsListDirection] = { 'inbound', 'outbound',  }

def check_calls_list_direction(value: str) -> CallsListDirection:
    if value in CALLS_LIST_DIRECTION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CALLS_LIST_DIRECTION_VALUES!r}")

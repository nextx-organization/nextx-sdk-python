from typing import Literal

PhoneNumbersListDirection = Literal['both', 'inbound', 'outbound']

PHONE_NUMBERS_LIST_DIRECTION_VALUES: set[PhoneNumbersListDirection] = { 'both', 'inbound', 'outbound',  }

def check_phone_numbers_list_direction(value: str) -> PhoneNumbersListDirection:
    if value in PHONE_NUMBERS_LIST_DIRECTION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PHONE_NUMBERS_LIST_DIRECTION_VALUES!r}")

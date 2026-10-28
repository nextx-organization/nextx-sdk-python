from typing import Literal

CallsListStatus = Literal['abandoned', 'answered', 'completed', 'failed', 'missed', 'ringing', 'voicemail']

CALLS_LIST_STATUS_VALUES: set[CallsListStatus] = { 'abandoned', 'answered', 'completed', 'failed', 'missed', 'ringing', 'voicemail',  }

def check_calls_list_status(value: str) -> CallsListStatus:
    if value in CALLS_LIST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CALLS_LIST_STATUS_VALUES!r}")

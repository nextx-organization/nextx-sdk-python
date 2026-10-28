from typing import Literal

AgentsListStatus = Literal['acw', 'available', 'offline', 'on_call', 'paused']

AGENTS_LIST_STATUS_VALUES: set[AgentsListStatus] = { 'acw', 'available', 'offline', 'on_call', 'paused',  }

def check_agents_list_status(value: str) -> AgentsListStatus:
    if value in AGENTS_LIST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AGENTS_LIST_STATUS_VALUES!r}")

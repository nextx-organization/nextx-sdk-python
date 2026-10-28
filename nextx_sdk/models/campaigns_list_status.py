from typing import Literal

CampaignsListStatus = Literal['active', 'cancelled', 'completed', 'draft', 'paused']

CAMPAIGNS_LIST_STATUS_VALUES: set[CampaignsListStatus] = { 'active', 'cancelled', 'completed', 'draft', 'paused',  }

def check_campaigns_list_status(value: str) -> CampaignsListStatus:
    if value in CAMPAIGNS_LIST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CAMPAIGNS_LIST_STATUS_VALUES!r}")

from typing import Literal

CampaignsListType = Literal['inbound', 'outbound']

CAMPAIGNS_LIST_TYPE_VALUES: set[CampaignsListType] = { 'inbound', 'outbound',  }

def check_campaigns_list_type(value: str) -> CampaignsListType:
    if value in CAMPAIGNS_LIST_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CAMPAIGNS_LIST_TYPE_VALUES!r}")

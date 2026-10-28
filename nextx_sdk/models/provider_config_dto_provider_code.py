from typing import Literal

ProviderConfigDtoProviderCode = Literal['Bkav', 'Fpt', 'Misa', 'None', 'Viettel', 'Vnpt', 'WinInvoice']

PROVIDER_CONFIG_DTO_PROVIDER_CODE_VALUES: set[ProviderConfigDtoProviderCode] = { 'Bkav', 'Fpt', 'Misa', 'None', 'Viettel', 'Vnpt', 'WinInvoice',  }

def check_provider_config_dto_provider_code(value: str) -> ProviderConfigDtoProviderCode:
    if value in PROVIDER_CONFIG_DTO_PROVIDER_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_CONFIG_DTO_PROVIDER_CODE_VALUES!r}")

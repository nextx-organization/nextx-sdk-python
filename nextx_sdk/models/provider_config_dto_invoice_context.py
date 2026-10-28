from typing import Literal

ProviderConfigDtoInvoiceContext = Literal['OperatorInvoice', 'SalesInvoice']

PROVIDER_CONFIG_DTO_INVOICE_CONTEXT_VALUES: set[ProviderConfigDtoInvoiceContext] = { 'OperatorInvoice', 'SalesInvoice',  }

def check_provider_config_dto_invoice_context(value: str) -> ProviderConfigDtoInvoiceContext:
    if value in PROVIDER_CONFIG_DTO_INVOICE_CONTEXT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_CONFIG_DTO_INVOICE_CONTEXT_VALUES!r}")

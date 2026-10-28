from typing import Literal

ProductDetailDtoKitPriceMode = Literal['AutoCalculate', 'Override']

PRODUCT_DETAIL_DTO_KIT_PRICE_MODE_VALUES: set[ProductDetailDtoKitPriceMode] = { 'AutoCalculate', 'Override',  }

def check_product_detail_dto_kit_price_mode(value: str) -> ProductDetailDtoKitPriceMode:
    if value in PRODUCT_DETAIL_DTO_KIT_PRICE_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRODUCT_DETAIL_DTO_KIT_PRICE_MODE_VALUES!r}")

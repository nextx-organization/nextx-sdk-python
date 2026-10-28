from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="LotExpiryReportDto")



@_attrs_define
class LotExpiryReportDto:
    

    lot_id: UUID | Unset = UNSET
    product_name: None | str | Unset = UNSET
    product_code: None | str | Unset = UNSET
    lot_number: None | str | Unset = UNSET
    expiry_date: datetime.date | None | Unset = UNSET
    days_to_expiry: int | None | Unset = UNSET
    available_quantity: float | Unset = UNSET
    status: None | str | Unset = UNSET
    branch_name: None | str | Unset = UNSET
    total_value: int | Unset = UNSET
    category_id: None | Unset | UUID = UNSET
    category_name: None | str | Unset = UNSET
    sku_code: None | str | Unset = UNSET
    selling_price: float | None | Unset = UNSET
    purchase_price: float | None | Unset = UNSET
    variant_id: None | Unset | UUID = UNSET
    variant_name: None | str | Unset = UNSET
    branch_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        lot_id: str | Unset = UNSET
        if not isinstance(self.lot_id, Unset):
            lot_id = str(self.lot_id)

        product_name: None | str | Unset
        if isinstance(self.product_name, Unset):
            product_name = UNSET
        else:
            product_name = self.product_name

        product_code: None | str | Unset
        if isinstance(self.product_code, Unset):
            product_code = UNSET
        else:
            product_code = self.product_code

        lot_number: None | str | Unset
        if isinstance(self.lot_number, Unset):
            lot_number = UNSET
        else:
            lot_number = self.lot_number

        expiry_date: None | str | Unset
        if isinstance(self.expiry_date, Unset):
            expiry_date = UNSET
        elif isinstance(self.expiry_date, datetime.date):
            expiry_date = self.expiry_date.isoformat()
        else:
            expiry_date = self.expiry_date

        days_to_expiry: int | None | Unset
        if isinstance(self.days_to_expiry, Unset):
            days_to_expiry = UNSET
        else:
            days_to_expiry = self.days_to_expiry

        available_quantity = self.available_quantity

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        branch_name: None | str | Unset
        if isinstance(self.branch_name, Unset):
            branch_name = UNSET
        else:
            branch_name = self.branch_name

        total_value = self.total_value

        category_id: None | str | Unset
        if isinstance(self.category_id, Unset):
            category_id = UNSET
        elif isinstance(self.category_id, UUID):
            category_id = str(self.category_id)
        else:
            category_id = self.category_id

        category_name: None | str | Unset
        if isinstance(self.category_name, Unset):
            category_name = UNSET
        else:
            category_name = self.category_name

        sku_code: None | str | Unset
        if isinstance(self.sku_code, Unset):
            sku_code = UNSET
        else:
            sku_code = self.sku_code

        selling_price: float | None | Unset
        if isinstance(self.selling_price, Unset):
            selling_price = UNSET
        else:
            selling_price = self.selling_price

        purchase_price: float | None | Unset
        if isinstance(self.purchase_price, Unset):
            purchase_price = UNSET
        else:
            purchase_price = self.purchase_price

        variant_id: None | str | Unset
        if isinstance(self.variant_id, Unset):
            variant_id = UNSET
        elif isinstance(self.variant_id, UUID):
            variant_id = str(self.variant_id)
        else:
            variant_id = self.variant_id

        variant_name: None | str | Unset
        if isinstance(self.variant_name, Unset):
            variant_name = UNSET
        else:
            variant_name = self.variant_name

        branch_id: None | str | Unset
        if isinstance(self.branch_id, Unset):
            branch_id = UNSET
        elif isinstance(self.branch_id, UUID):
            branch_id = str(self.branch_id)
        else:
            branch_id = self.branch_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if lot_id is not UNSET:
            field_dict["lotId"] = lot_id
        if product_name is not UNSET:
            field_dict["productName"] = product_name
        if product_code is not UNSET:
            field_dict["productCode"] = product_code
        if lot_number is not UNSET:
            field_dict["lotNumber"] = lot_number
        if expiry_date is not UNSET:
            field_dict["expiryDate"] = expiry_date
        if days_to_expiry is not UNSET:
            field_dict["daysToExpiry"] = days_to_expiry
        if available_quantity is not UNSET:
            field_dict["availableQuantity"] = available_quantity
        if status is not UNSET:
            field_dict["status"] = status
        if branch_name is not UNSET:
            field_dict["branchName"] = branch_name
        if total_value is not UNSET:
            field_dict["totalValue"] = total_value
        if category_id is not UNSET:
            field_dict["categoryId"] = category_id
        if category_name is not UNSET:
            field_dict["categoryName"] = category_name
        if sku_code is not UNSET:
            field_dict["skuCode"] = sku_code
        if selling_price is not UNSET:
            field_dict["sellingPrice"] = selling_price
        if purchase_price is not UNSET:
            field_dict["purchasePrice"] = purchase_price
        if variant_id is not UNSET:
            field_dict["variantId"] = variant_id
        if variant_name is not UNSET:
            field_dict["variantName"] = variant_name
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _lot_id = d.pop("lotId", UNSET)
        lot_id: UUID | Unset
        if isinstance(_lot_id,  Unset):
            lot_id = UNSET
        else:
            lot_id = UUID(_lot_id)




        def _parse_product_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_name = _parse_product_name(d.pop("productName", UNSET))


        def _parse_product_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_code = _parse_product_code(d.pop("productCode", UNSET))


        def _parse_lot_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lot_number = _parse_lot_number(d.pop("lotNumber", UNSET))


        def _parse_expiry_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiry_date_type_0 = datetime.date.fromisoformat(data)



                return expiry_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        expiry_date = _parse_expiry_date(d.pop("expiryDate", UNSET))


        def _parse_days_to_expiry(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        days_to_expiry = _parse_days_to_expiry(d.pop("daysToExpiry", UNSET))


        available_quantity = d.pop("availableQuantity", UNSET)

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_branch_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch_name = _parse_branch_name(d.pop("branchName", UNSET))


        total_value = d.pop("totalValue", UNSET)

        def _parse_category_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                category_id_type_0 = UUID(data)



                return category_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        category_id = _parse_category_id(d.pop("categoryId", UNSET))


        def _parse_category_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_name = _parse_category_name(d.pop("categoryName", UNSET))


        def _parse_sku_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sku_code = _parse_sku_code(d.pop("skuCode", UNSET))


        def _parse_selling_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        selling_price = _parse_selling_price(d.pop("sellingPrice", UNSET))


        def _parse_purchase_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        purchase_price = _parse_purchase_price(d.pop("purchasePrice", UNSET))


        def _parse_variant_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                variant_id_type_0 = UUID(data)



                return variant_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        variant_id = _parse_variant_id(d.pop("variantId", UNSET))


        def _parse_variant_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        variant_name = _parse_variant_name(d.pop("variantName", UNSET))


        def _parse_branch_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                branch_id_type_0 = UUID(data)



                return branch_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        branch_id = _parse_branch_id(d.pop("branchId", UNSET))


        lot_expiry_report_dto = cls(
            lot_id=lot_id,
            product_name=product_name,
            product_code=product_code,
            lot_number=lot_number,
            expiry_date=expiry_date,
            days_to_expiry=days_to_expiry,
            available_quantity=available_quantity,
            status=status,
            branch_name=branch_name,
            total_value=total_value,
            category_id=category_id,
            category_name=category_name,
            sku_code=sku_code,
            selling_price=selling_price,
            purchase_price=purchase_price,
            variant_id=variant_id,
            variant_name=variant_name,
            branch_id=branch_id,
        )

        return lot_expiry_report_dto


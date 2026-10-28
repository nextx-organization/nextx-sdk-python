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






T = TypeVar("T", bound="UnknownLotReportDto")



@_attrs_define
class UnknownLotReportDto:
    

    product_id: UUID | Unset = UNSET
    product_code: None | str | Unset = UNSET
    product_name: None | str | Unset = UNSET
    branch_id: None | Unset | UUID = UNSET
    remaining_quantity: float | Unset = UNSET
    sold_quantity: float | Unset = UNSET
    last_sold_at: datetime.datetime | None | Unset = UNSET
    category_id: None | Unset | UUID = UNSET
    category_name: None | str | Unset = UNSET
    sku_code: None | str | Unset = UNSET
    selling_price: float | None | Unset = UNSET
    purchase_price: float | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        product_id: str | Unset = UNSET
        if not isinstance(self.product_id, Unset):
            product_id = str(self.product_id)

        product_code: None | str | Unset
        if isinstance(self.product_code, Unset):
            product_code = UNSET
        else:
            product_code = self.product_code

        product_name: None | str | Unset
        if isinstance(self.product_name, Unset):
            product_name = UNSET
        else:
            product_name = self.product_name

        branch_id: None | str | Unset
        if isinstance(self.branch_id, Unset):
            branch_id = UNSET
        elif isinstance(self.branch_id, UUID):
            branch_id = str(self.branch_id)
        else:
            branch_id = self.branch_id

        remaining_quantity = self.remaining_quantity

        sold_quantity = self.sold_quantity

        last_sold_at: None | str | Unset
        if isinstance(self.last_sold_at, Unset):
            last_sold_at = UNSET
        elif isinstance(self.last_sold_at, datetime.datetime):
            last_sold_at = self.last_sold_at.isoformat()
        else:
            last_sold_at = self.last_sold_at

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


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if product_code is not UNSET:
            field_dict["productCode"] = product_code
        if product_name is not UNSET:
            field_dict["productName"] = product_name
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id
        if remaining_quantity is not UNSET:
            field_dict["remainingQuantity"] = remaining_quantity
        if sold_quantity is not UNSET:
            field_dict["soldQuantity"] = sold_quantity
        if last_sold_at is not UNSET:
            field_dict["lastSoldAt"] = last_sold_at
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

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _product_id = d.pop("productId", UNSET)
        product_id: UUID | Unset
        if isinstance(_product_id,  Unset):
            product_id = UNSET
        else:
            product_id = UUID(_product_id)




        def _parse_product_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_code = _parse_product_code(d.pop("productCode", UNSET))


        def _parse_product_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_name = _parse_product_name(d.pop("productName", UNSET))


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


        remaining_quantity = d.pop("remainingQuantity", UNSET)

        sold_quantity = d.pop("soldQuantity", UNSET)

        def _parse_last_sold_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_sold_at_type_0 = datetime.datetime.fromisoformat(data)



                return last_sold_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_sold_at = _parse_last_sold_at(d.pop("lastSoldAt", UNSET))


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


        unknown_lot_report_dto = cls(
            product_id=product_id,
            product_code=product_code,
            product_name=product_name,
            branch_id=branch_id,
            remaining_quantity=remaining_quantity,
            sold_quantity=sold_quantity,
            last_sold_at=last_sold_at,
            category_id=category_id,
            category_name=category_name,
            sku_code=sku_code,
            selling_price=selling_price,
            purchase_price=purchase_price,
        )

        return unknown_lot_report_dto


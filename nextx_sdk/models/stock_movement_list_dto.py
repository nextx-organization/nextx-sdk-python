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






T = TypeVar("T", bound="StockMovementListDto")



@_attrs_define
class StockMovementListDto:
    

    id: UUID | Unset = UNSET
    occurred_at: datetime.datetime | Unset = UNSET
    source: None | str | Unset = UNSET
    product_id: UUID | Unset = UNSET
    product_name: None | str | Unset = UNSET
    sku: None | str | Unset = UNSET
    movement_type: None | str | Unset = UNSET
    group: None | str | Unset = UNSET
    direction: None | str | Unset = UNSET
    quantity: float | Unset = UNSET
    before_quantity: float | None | Unset = UNSET
    after_quantity: float | None | Unset = UNSET
    branch_id: UUID | Unset = UNSET
    branch_name: None | str | Unset = UNSET
    reference_type: None | str | Unset = UNSET
    reference_id: None | Unset | UUID = UNSET
    reference_code: None | str | Unset = UNSET
    customer_code: None | str | Unset = UNSET
    customer_name: None | str | Unset = UNSET
    created_by_id: None | Unset | UUID = UNSET
    created_by_name: None | str | Unset = UNSET
    is_reversal: bool | Unset = UNSET
    unit_price: float | None | Unset = UNSET
    unit_cost: float | None | Unset = UNSET
    notes: None | str | Unset = UNSET
    category_id: None | Unset | UUID = UNSET
    category_name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        occurred_at: str | Unset = UNSET
        if not isinstance(self.occurred_at, Unset):
            occurred_at = self.occurred_at.isoformat()

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        product_id: str | Unset = UNSET
        if not isinstance(self.product_id, Unset):
            product_id = str(self.product_id)

        product_name: None | str | Unset
        if isinstance(self.product_name, Unset):
            product_name = UNSET
        else:
            product_name = self.product_name

        sku: None | str | Unset
        if isinstance(self.sku, Unset):
            sku = UNSET
        else:
            sku = self.sku

        movement_type: None | str | Unset
        if isinstance(self.movement_type, Unset):
            movement_type = UNSET
        else:
            movement_type = self.movement_type

        group: None | str | Unset
        if isinstance(self.group, Unset):
            group = UNSET
        else:
            group = self.group

        direction: None | str | Unset
        if isinstance(self.direction, Unset):
            direction = UNSET
        else:
            direction = self.direction

        quantity = self.quantity

        before_quantity: float | None | Unset
        if isinstance(self.before_quantity, Unset):
            before_quantity = UNSET
        else:
            before_quantity = self.before_quantity

        after_quantity: float | None | Unset
        if isinstance(self.after_quantity, Unset):
            after_quantity = UNSET
        else:
            after_quantity = self.after_quantity

        branch_id: str | Unset = UNSET
        if not isinstance(self.branch_id, Unset):
            branch_id = str(self.branch_id)

        branch_name: None | str | Unset
        if isinstance(self.branch_name, Unset):
            branch_name = UNSET
        else:
            branch_name = self.branch_name

        reference_type: None | str | Unset
        if isinstance(self.reference_type, Unset):
            reference_type = UNSET
        else:
            reference_type = self.reference_type

        reference_id: None | str | Unset
        if isinstance(self.reference_id, Unset):
            reference_id = UNSET
        elif isinstance(self.reference_id, UUID):
            reference_id = str(self.reference_id)
        else:
            reference_id = self.reference_id

        reference_code: None | str | Unset
        if isinstance(self.reference_code, Unset):
            reference_code = UNSET
        else:
            reference_code = self.reference_code

        customer_code: None | str | Unset
        if isinstance(self.customer_code, Unset):
            customer_code = UNSET
        else:
            customer_code = self.customer_code

        customer_name: None | str | Unset
        if isinstance(self.customer_name, Unset):
            customer_name = UNSET
        else:
            customer_name = self.customer_name

        created_by_id: None | str | Unset
        if isinstance(self.created_by_id, Unset):
            created_by_id = UNSET
        elif isinstance(self.created_by_id, UUID):
            created_by_id = str(self.created_by_id)
        else:
            created_by_id = self.created_by_id

        created_by_name: None | str | Unset
        if isinstance(self.created_by_name, Unset):
            created_by_name = UNSET
        else:
            created_by_name = self.created_by_name

        is_reversal = self.is_reversal

        unit_price: float | None | Unset
        if isinstance(self.unit_price, Unset):
            unit_price = UNSET
        else:
            unit_price = self.unit_price

        unit_cost: float | None | Unset
        if isinstance(self.unit_cost, Unset):
            unit_cost = UNSET
        else:
            unit_cost = self.unit_cost

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

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


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if occurred_at is not UNSET:
            field_dict["occurredAt"] = occurred_at
        if source is not UNSET:
            field_dict["source"] = source
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if product_name is not UNSET:
            field_dict["productName"] = product_name
        if sku is not UNSET:
            field_dict["sku"] = sku
        if movement_type is not UNSET:
            field_dict["movementType"] = movement_type
        if group is not UNSET:
            field_dict["group"] = group
        if direction is not UNSET:
            field_dict["direction"] = direction
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if before_quantity is not UNSET:
            field_dict["beforeQuantity"] = before_quantity
        if after_quantity is not UNSET:
            field_dict["afterQuantity"] = after_quantity
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id
        if branch_name is not UNSET:
            field_dict["branchName"] = branch_name
        if reference_type is not UNSET:
            field_dict["referenceType"] = reference_type
        if reference_id is not UNSET:
            field_dict["referenceId"] = reference_id
        if reference_code is not UNSET:
            field_dict["referenceCode"] = reference_code
        if customer_code is not UNSET:
            field_dict["customerCode"] = customer_code
        if customer_name is not UNSET:
            field_dict["customerName"] = customer_name
        if created_by_id is not UNSET:
            field_dict["createdById"] = created_by_id
        if created_by_name is not UNSET:
            field_dict["createdByName"] = created_by_name
        if is_reversal is not UNSET:
            field_dict["isReversal"] = is_reversal
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if unit_cost is not UNSET:
            field_dict["unitCost"] = unit_cost
        if notes is not UNSET:
            field_dict["notes"] = notes
        if category_id is not UNSET:
            field_dict["categoryId"] = category_id
        if category_name is not UNSET:
            field_dict["categoryName"] = category_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        _occurred_at = d.pop("occurredAt", UNSET)
        occurred_at: datetime.datetime | Unset
        if isinstance(_occurred_at,  Unset):
            occurred_at = UNSET
        else:
            occurred_at = datetime.datetime.fromisoformat(_occurred_at)




        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))


        _product_id = d.pop("productId", UNSET)
        product_id: UUID | Unset
        if isinstance(_product_id,  Unset):
            product_id = UNSET
        else:
            product_id = UUID(_product_id)




        def _parse_product_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_name = _parse_product_name(d.pop("productName", UNSET))


        def _parse_sku(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sku = _parse_sku(d.pop("sku", UNSET))


        def _parse_movement_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        movement_type = _parse_movement_type(d.pop("movementType", UNSET))


        def _parse_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group = _parse_group(d.pop("group", UNSET))


        def _parse_direction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        direction = _parse_direction(d.pop("direction", UNSET))


        quantity = d.pop("quantity", UNSET)

        def _parse_before_quantity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        before_quantity = _parse_before_quantity(d.pop("beforeQuantity", UNSET))


        def _parse_after_quantity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        after_quantity = _parse_after_quantity(d.pop("afterQuantity", UNSET))


        _branch_id = d.pop("branchId", UNSET)
        branch_id: UUID | Unset
        if isinstance(_branch_id,  Unset):
            branch_id = UNSET
        else:
            branch_id = UUID(_branch_id)




        def _parse_branch_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch_name = _parse_branch_name(d.pop("branchName", UNSET))


        def _parse_reference_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reference_type = _parse_reference_type(d.pop("referenceType", UNSET))


        def _parse_reference_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reference_id_type_0 = UUID(data)



                return reference_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        reference_id = _parse_reference_id(d.pop("referenceId", UNSET))


        def _parse_reference_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reference_code = _parse_reference_code(d.pop("referenceCode", UNSET))


        def _parse_customer_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_code = _parse_customer_code(d.pop("customerCode", UNSET))


        def _parse_customer_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_name = _parse_customer_name(d.pop("customerName", UNSET))


        def _parse_created_by_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_id_type_0 = UUID(data)



                return created_by_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        created_by_id = _parse_created_by_id(d.pop("createdById", UNSET))


        def _parse_created_by_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by_name = _parse_created_by_name(d.pop("createdByName", UNSET))


        is_reversal = d.pop("isReversal", UNSET)

        def _parse_unit_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        unit_price = _parse_unit_price(d.pop("unitPrice", UNSET))


        def _parse_unit_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        unit_cost = _parse_unit_cost(d.pop("unitCost", UNSET))


        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


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


        stock_movement_list_dto = cls(
            id=id,
            occurred_at=occurred_at,
            source=source,
            product_id=product_id,
            product_name=product_name,
            sku=sku,
            movement_type=movement_type,
            group=group,
            direction=direction,
            quantity=quantity,
            before_quantity=before_quantity,
            after_quantity=after_quantity,
            branch_id=branch_id,
            branch_name=branch_name,
            reference_type=reference_type,
            reference_id=reference_id,
            reference_code=reference_code,
            customer_code=customer_code,
            customer_name=customer_name,
            created_by_id=created_by_id,
            created_by_name=created_by_name,
            is_reversal=is_reversal,
            unit_price=unit_price,
            unit_cost=unit_cost,
            notes=notes,
            category_id=category_id,
            category_name=category_name,
        )

        return stock_movement_list_dto


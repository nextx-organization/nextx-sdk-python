from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="SupplierInfoRefDto")



@_attrs_define
class SupplierInfoRefDto:
    

    supplier_id: UUID | Unset = UNSET
    supplier_name: None | str | Unset = UNSET
    supplier_code: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        supplier_id: str | Unset = UNSET
        if not isinstance(self.supplier_id, Unset):
            supplier_id = str(self.supplier_id)

        supplier_name: None | str | Unset
        if isinstance(self.supplier_name, Unset):
            supplier_name = UNSET
        else:
            supplier_name = self.supplier_name

        supplier_code: None | str | Unset
        if isinstance(self.supplier_code, Unset):
            supplier_code = UNSET
        else:
            supplier_code = self.supplier_code


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if supplier_id is not UNSET:
            field_dict["supplierId"] = supplier_id
        if supplier_name is not UNSET:
            field_dict["supplierName"] = supplier_name
        if supplier_code is not UNSET:
            field_dict["supplierCode"] = supplier_code

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _supplier_id = d.pop("supplierId", UNSET)
        supplier_id: UUID | Unset
        if isinstance(_supplier_id,  Unset):
            supplier_id = UNSET
        else:
            supplier_id = UUID(_supplier_id)




        def _parse_supplier_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        supplier_name = _parse_supplier_name(d.pop("supplierName", UNSET))


        def _parse_supplier_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        supplier_code = _parse_supplier_code(d.pop("supplierCode", UNSET))


        supplier_info_ref_dto = cls(
            supplier_id=supplier_id,
            supplier_name=supplier_name,
            supplier_code=supplier_code,
        )

        return supplier_info_ref_dto


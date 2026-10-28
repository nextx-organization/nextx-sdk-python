from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="KitAvailabilityDto")



@_attrs_define
class KitAvailabilityDto:
    

    kit_sku_id: UUID | Unset = UNSET
    available_sets: float | None | Unset = UNSET
    component_count: int | Unset = UNSET
    limiting_component_sku_id: None | Unset | UUID = UNSET
    limiting_component_name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        kit_sku_id: str | Unset = UNSET
        if not isinstance(self.kit_sku_id, Unset):
            kit_sku_id = str(self.kit_sku_id)

        available_sets: float | None | Unset
        if isinstance(self.available_sets, Unset):
            available_sets = UNSET
        else:
            available_sets = self.available_sets

        component_count = self.component_count

        limiting_component_sku_id: None | str | Unset
        if isinstance(self.limiting_component_sku_id, Unset):
            limiting_component_sku_id = UNSET
        elif isinstance(self.limiting_component_sku_id, UUID):
            limiting_component_sku_id = str(self.limiting_component_sku_id)
        else:
            limiting_component_sku_id = self.limiting_component_sku_id

        limiting_component_name: None | str | Unset
        if isinstance(self.limiting_component_name, Unset):
            limiting_component_name = UNSET
        else:
            limiting_component_name = self.limiting_component_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if kit_sku_id is not UNSET:
            field_dict["kitSkuId"] = kit_sku_id
        if available_sets is not UNSET:
            field_dict["availableSets"] = available_sets
        if component_count is not UNSET:
            field_dict["componentCount"] = component_count
        if limiting_component_sku_id is not UNSET:
            field_dict["limitingComponentSkuId"] = limiting_component_sku_id
        if limiting_component_name is not UNSET:
            field_dict["limitingComponentName"] = limiting_component_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _kit_sku_id = d.pop("kitSkuId", UNSET)
        kit_sku_id: UUID | Unset
        if isinstance(_kit_sku_id,  Unset):
            kit_sku_id = UNSET
        else:
            kit_sku_id = UUID(_kit_sku_id)




        def _parse_available_sets(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        available_sets = _parse_available_sets(d.pop("availableSets", UNSET))


        component_count = d.pop("componentCount", UNSET)

        def _parse_limiting_component_sku_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                limiting_component_sku_id_type_0 = UUID(data)



                return limiting_component_sku_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        limiting_component_sku_id = _parse_limiting_component_sku_id(d.pop("limitingComponentSkuId", UNSET))


        def _parse_limiting_component_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        limiting_component_name = _parse_limiting_component_name(d.pop("limitingComponentName", UNSET))


        kit_availability_dto = cls(
            kit_sku_id=kit_sku_id,
            available_sets=available_sets,
            component_count=component_count,
            limiting_component_sku_id=limiting_component_sku_id,
            limiting_component_name=limiting_component_name,
        )

        return kit_availability_dto


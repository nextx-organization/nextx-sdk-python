from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="ContractRelationDto")



@_attrs_define
class ContractRelationDto:
    

    kind: None | str | Unset = UNSET
    contract_id: UUID | Unset = UNSET
    contract_code: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        contract_id: str | Unset = UNSET
        if not isinstance(self.contract_id, Unset):
            contract_id = str(self.contract_id)

        contract_code: None | str | Unset
        if isinstance(self.contract_code, Unset):
            contract_code = UNSET
        else:
            contract_code = self.contract_code


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if kind is not UNSET:
            field_dict["kind"] = kind
        if contract_id is not UNSET:
            field_dict["contractId"] = contract_id
        if contract_code is not UNSET:
            field_dict["contractCode"] = contract_code

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))


        _contract_id = d.pop("contractId", UNSET)
        contract_id: UUID | Unset
        if isinstance(_contract_id,  Unset):
            contract_id = UNSET
        else:
            contract_id = UUID(_contract_id)




        def _parse_contract_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contract_code = _parse_contract_code(d.pop("contractCode", UNSET))


        contract_relation_dto = cls(
            kind=kind,
            contract_id=contract_id,
            contract_code=contract_code,
        )

        return contract_relation_dto


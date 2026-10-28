from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.email_merge_variable_dto import EmailMergeVariableDto





T = TypeVar("T", bound="EmailMergeVariableGroupDto")



@_attrs_define
class EmailMergeVariableGroupDto:
    

    scope: None | str | Unset = UNSET
    label: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    variables: list[EmailMergeVariableDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.email_merge_variable_dto import EmailMergeVariableDto # noqa: PLC0415
        scope: None | str | Unset
        if isinstance(self.scope, Unset):
            scope = UNSET
        else:
            scope = self.scope

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        variables: list[dict[str, Any]] | None | Unset
        if isinstance(self.variables, Unset):
            variables = UNSET
        elif isinstance(self.variables, list):
            variables = []
            for variables_type_0_item_data in self.variables:
                variables_type_0_item = variables_type_0_item_data.to_dict()
                variables.append(variables_type_0_item)


        else:
            variables = self.variables


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if scope is not UNSET:
            field_dict["scope"] = scope
        if label is not UNSET:
            field_dict["label"] = label
        if source is not UNSET:
            field_dict["source"] = source
        if variables is not UNSET:
            field_dict["variables"] = variables

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.email_merge_variable_dto import EmailMergeVariableDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_scope(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scope = _parse_scope(d.pop("scope", UNSET))


        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))


        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))


        def _parse_variables(data: object) -> list[EmailMergeVariableDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                variables_type_0 = []
                _variables_type_0 = data
                for variables_type_0_item_data in (_variables_type_0):
                    variables_type_0_item = EmailMergeVariableDto.from_dict(variables_type_0_item_data)



                    variables_type_0.append(variables_type_0_item)

                return variables_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EmailMergeVariableDto] | None | Unset, data)

        variables = _parse_variables(d.pop("variables", UNSET))


        email_merge_variable_group_dto = cls(
            scope=scope,
            label=label,
            source=source,
            variables=variables,
        )

        return email_merge_variable_group_dto


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.series_dto_form_kind import check_series_dto_form_kind
from ..models.series_dto_form_kind import SeriesDtoFormKind
from ..models.series_dto_invoice_type import check_series_dto_invoice_type
from ..models.series_dto_invoice_type import SeriesDtoInvoiceType
from ..models.series_dto_kind import check_series_dto_kind
from ..models.series_dto_kind import SeriesDtoKind
from ..models.series_dto_provider_code import check_series_dto_provider_code
from ..models.series_dto_provider_code import SeriesDtoProviderCode
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="SeriesDto")



@_attrs_define
class SeriesDto:
    

    id: UUID | Unset = UNSET
    workspace_id: UUID | Unset = UNSET
    provider_config_id: UUID | Unset = UNSET
    provider_code: SeriesDtoProviderCode | Unset = UNSET
    template_no: None | str | Unset = UNSET
    series_code: None | str | Unset = UNSET
    full_code: None | str | Unset = UNSET
    invoice_type: SeriesDtoInvoiceType | Unset = UNSET
    kind: SeriesDtoKind | Unset = UNSET
    form_kind: SeriesDtoFormKind | Unset = UNSET
    has_tax_authority_code: bool | None | Unset = UNSET
    year: int | None | Unset = UNSET
    registered_at: datetime.date | Unset = UNSET
    from_number: int | Unset = UNSET
    current_number: int | Unset = UNSET
    is_active: bool | Unset = UNSET
    is_default: bool | Unset = UNSET
    notes: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        workspace_id: str | Unset = UNSET
        if not isinstance(self.workspace_id, Unset):
            workspace_id = str(self.workspace_id)

        provider_config_id: str | Unset = UNSET
        if not isinstance(self.provider_config_id, Unset):
            provider_config_id = str(self.provider_config_id)

        provider_code: str | Unset = UNSET
        if not isinstance(self.provider_code, Unset):
            provider_code = self.provider_code


        template_no: None | str | Unset
        if isinstance(self.template_no, Unset):
            template_no = UNSET
        else:
            template_no = self.template_no

        series_code: None | str | Unset
        if isinstance(self.series_code, Unset):
            series_code = UNSET
        else:
            series_code = self.series_code

        full_code: None | str | Unset
        if isinstance(self.full_code, Unset):
            full_code = UNSET
        else:
            full_code = self.full_code

        invoice_type: str | Unset = UNSET
        if not isinstance(self.invoice_type, Unset):
            invoice_type = self.invoice_type


        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind


        form_kind: str | Unset = UNSET
        if not isinstance(self.form_kind, Unset):
            form_kind = self.form_kind


        has_tax_authority_code: bool | None | Unset
        if isinstance(self.has_tax_authority_code, Unset):
            has_tax_authority_code = UNSET
        else:
            has_tax_authority_code = self.has_tax_authority_code

        year: int | None | Unset
        if isinstance(self.year, Unset):
            year = UNSET
        else:
            year = self.year

        registered_at: str | Unset = UNSET
        if not isinstance(self.registered_at, Unset):
            registered_at = self.registered_at.isoformat()

        from_number = self.from_number

        current_number = self.current_number

        is_active = self.is_active

        is_default = self.is_default

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id
        if provider_config_id is not UNSET:
            field_dict["providerConfigId"] = provider_config_id
        if provider_code is not UNSET:
            field_dict["providerCode"] = provider_code
        if template_no is not UNSET:
            field_dict["templateNo"] = template_no
        if series_code is not UNSET:
            field_dict["seriesCode"] = series_code
        if full_code is not UNSET:
            field_dict["fullCode"] = full_code
        if invoice_type is not UNSET:
            field_dict["invoiceType"] = invoice_type
        if kind is not UNSET:
            field_dict["kind"] = kind
        if form_kind is not UNSET:
            field_dict["formKind"] = form_kind
        if has_tax_authority_code is not UNSET:
            field_dict["hasTaxAuthorityCode"] = has_tax_authority_code
        if year is not UNSET:
            field_dict["year"] = year
        if registered_at is not UNSET:
            field_dict["registeredAt"] = registered_at
        if from_number is not UNSET:
            field_dict["fromNumber"] = from_number
        if current_number is not UNSET:
            field_dict["currentNumber"] = current_number
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if notes is not UNSET:
            field_dict["notes"] = notes
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

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




        _workspace_id = d.pop("workspaceId", UNSET)
        workspace_id: UUID | Unset
        if isinstance(_workspace_id,  Unset):
            workspace_id = UNSET
        else:
            workspace_id = UUID(_workspace_id)




        _provider_config_id = d.pop("providerConfigId", UNSET)
        provider_config_id: UUID | Unset
        if isinstance(_provider_config_id,  Unset):
            provider_config_id = UNSET
        else:
            provider_config_id = UUID(_provider_config_id)




        _provider_code = d.pop("providerCode", UNSET)
        provider_code: SeriesDtoProviderCode | Unset
        if isinstance(_provider_code,  Unset):
            provider_code = UNSET
        else:
            provider_code = check_series_dto_provider_code(_provider_code)




        def _parse_template_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template_no = _parse_template_no(d.pop("templateNo", UNSET))


        def _parse_series_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        series_code = _parse_series_code(d.pop("seriesCode", UNSET))


        def _parse_full_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        full_code = _parse_full_code(d.pop("fullCode", UNSET))


        _invoice_type = d.pop("invoiceType", UNSET)
        invoice_type: SeriesDtoInvoiceType | Unset
        if isinstance(_invoice_type,  Unset):
            invoice_type = UNSET
        else:
            invoice_type = check_series_dto_invoice_type(_invoice_type)




        _kind = d.pop("kind", UNSET)
        kind: SeriesDtoKind | Unset
        if isinstance(_kind,  Unset):
            kind = UNSET
        else:
            kind = check_series_dto_kind(_kind)




        _form_kind = d.pop("formKind", UNSET)
        form_kind: SeriesDtoFormKind | Unset
        if isinstance(_form_kind,  Unset):
            form_kind = UNSET
        else:
            form_kind = check_series_dto_form_kind(_form_kind)




        def _parse_has_tax_authority_code(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_tax_authority_code = _parse_has_tax_authority_code(d.pop("hasTaxAuthorityCode", UNSET))


        def _parse_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        year = _parse_year(d.pop("year", UNSET))


        _registered_at = d.pop("registeredAt", UNSET)
        registered_at: datetime.date | Unset
        if isinstance(_registered_at,  Unset):
            registered_at = UNSET
        else:
            registered_at = datetime.date.fromisoformat(_registered_at)




        from_number = d.pop("fromNumber", UNSET)

        current_number = d.pop("currentNumber", UNSET)

        is_active = d.pop("isActive", UNSET)

        is_default = d.pop("isDefault", UNSET)

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)




        series_dto = cls(
            id=id,
            workspace_id=workspace_id,
            provider_config_id=provider_config_id,
            provider_code=provider_code,
            template_no=template_no,
            series_code=series_code,
            full_code=full_code,
            invoice_type=invoice_type,
            kind=kind,
            form_kind=form_kind,
            has_tax_authority_code=has_tax_authority_code,
            year=year,
            registered_at=registered_at,
            from_number=from_number,
            current_number=current_number,
            is_active=is_active,
            is_default=is_default,
            notes=notes,
            created_at=created_at,
            updated_at=updated_at,
        )

        return series_dto


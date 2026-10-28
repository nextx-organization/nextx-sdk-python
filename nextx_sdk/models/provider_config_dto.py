from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.provider_config_dto_invoice_context import check_provider_config_dto_invoice_context
from ..models.provider_config_dto_invoice_context import ProviderConfigDtoInvoiceContext
from ..models.provider_config_dto_provider_code import check_provider_config_dto_provider_code
from ..models.provider_config_dto_provider_code import ProviderConfigDtoProviderCode
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.provider_config_dto_config_public_type_0 import ProviderConfigDtoConfigPublicType0





T = TypeVar("T", bound="ProviderConfigDto")



@_attrs_define
class ProviderConfigDto:
    

    id: UUID | Unset = UNSET
    workspace_id: UUID | Unset = UNSET
    branch_id: None | Unset | UUID = UNSET
    invoice_context: ProviderConfigDtoInvoiceContext | Unset = UNSET
    provider_code: ProviderConfigDtoProviderCode | Unset = UNSET
    display_name: None | str | Unset = UNSET
    is_active: bool | Unset = UNSET
    is_test_mode: bool | Unset = UNSET
    auto_issue_enabled: bool | Unset = UNSET
    auto_issue_hour: int | None | Unset = UNSET
    issuer_tax_code: None | str | Unset = UNSET
    issuer_name: None | str | Unset = UNSET
    issuer_address: None | str | Unset = UNSET
    issuer_phone: None | str | Unset = UNSET
    issuer_email: None | str | Unset = UNSET
    issuer_bank_name: None | str | Unset = UNSET
    issuer_bank_account: None | str | Unset = UNSET
    default_vat_rate: float | None | Unset = UNSET
    config_public: None | ProviderConfigDtoConfigPublicType0 | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.provider_config_dto_config_public_type_0 import ProviderConfigDtoConfigPublicType0 # noqa: PLC0415
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        workspace_id: str | Unset = UNSET
        if not isinstance(self.workspace_id, Unset):
            workspace_id = str(self.workspace_id)

        branch_id: None | str | Unset
        if isinstance(self.branch_id, Unset):
            branch_id = UNSET
        elif isinstance(self.branch_id, UUID):
            branch_id = str(self.branch_id)
        else:
            branch_id = self.branch_id

        invoice_context: str | Unset = UNSET
        if not isinstance(self.invoice_context, Unset):
            invoice_context = self.invoice_context


        provider_code: str | Unset = UNSET
        if not isinstance(self.provider_code, Unset):
            provider_code = self.provider_code


        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        is_active = self.is_active

        is_test_mode = self.is_test_mode

        auto_issue_enabled = self.auto_issue_enabled

        auto_issue_hour: int | None | Unset
        if isinstance(self.auto_issue_hour, Unset):
            auto_issue_hour = UNSET
        else:
            auto_issue_hour = self.auto_issue_hour

        issuer_tax_code: None | str | Unset
        if isinstance(self.issuer_tax_code, Unset):
            issuer_tax_code = UNSET
        else:
            issuer_tax_code = self.issuer_tax_code

        issuer_name: None | str | Unset
        if isinstance(self.issuer_name, Unset):
            issuer_name = UNSET
        else:
            issuer_name = self.issuer_name

        issuer_address: None | str | Unset
        if isinstance(self.issuer_address, Unset):
            issuer_address = UNSET
        else:
            issuer_address = self.issuer_address

        issuer_phone: None | str | Unset
        if isinstance(self.issuer_phone, Unset):
            issuer_phone = UNSET
        else:
            issuer_phone = self.issuer_phone

        issuer_email: None | str | Unset
        if isinstance(self.issuer_email, Unset):
            issuer_email = UNSET
        else:
            issuer_email = self.issuer_email

        issuer_bank_name: None | str | Unset
        if isinstance(self.issuer_bank_name, Unset):
            issuer_bank_name = UNSET
        else:
            issuer_bank_name = self.issuer_bank_name

        issuer_bank_account: None | str | Unset
        if isinstance(self.issuer_bank_account, Unset):
            issuer_bank_account = UNSET
        else:
            issuer_bank_account = self.issuer_bank_account

        default_vat_rate: float | None | Unset
        if isinstance(self.default_vat_rate, Unset):
            default_vat_rate = UNSET
        else:
            default_vat_rate = self.default_vat_rate

        config_public: dict[str, Any] | None | Unset
        if isinstance(self.config_public, Unset):
            config_public = UNSET
        elif isinstance(self.config_public, ProviderConfigDtoConfigPublicType0):
            config_public = self.config_public.to_dict()
        else:
            config_public = self.config_public

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
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id
        if invoice_context is not UNSET:
            field_dict["invoiceContext"] = invoice_context
        if provider_code is not UNSET:
            field_dict["providerCode"] = provider_code
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if is_test_mode is not UNSET:
            field_dict["isTestMode"] = is_test_mode
        if auto_issue_enabled is not UNSET:
            field_dict["autoIssueEnabled"] = auto_issue_enabled
        if auto_issue_hour is not UNSET:
            field_dict["autoIssueHour"] = auto_issue_hour
        if issuer_tax_code is not UNSET:
            field_dict["issuerTaxCode"] = issuer_tax_code
        if issuer_name is not UNSET:
            field_dict["issuerName"] = issuer_name
        if issuer_address is not UNSET:
            field_dict["issuerAddress"] = issuer_address
        if issuer_phone is not UNSET:
            field_dict["issuerPhone"] = issuer_phone
        if issuer_email is not UNSET:
            field_dict["issuerEmail"] = issuer_email
        if issuer_bank_name is not UNSET:
            field_dict["issuerBankName"] = issuer_bank_name
        if issuer_bank_account is not UNSET:
            field_dict["issuerBankAccount"] = issuer_bank_account
        if default_vat_rate is not UNSET:
            field_dict["defaultVatRate"] = default_vat_rate
        if config_public is not UNSET:
            field_dict["configPublic"] = config_public
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_config_dto_config_public_type_0 import ProviderConfigDtoConfigPublicType0 # noqa: PLC0415
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


        _invoice_context = d.pop("invoiceContext", UNSET)
        invoice_context: ProviderConfigDtoInvoiceContext | Unset
        if isinstance(_invoice_context,  Unset):
            invoice_context = UNSET
        else:
            invoice_context = check_provider_config_dto_invoice_context(_invoice_context)




        _provider_code = d.pop("providerCode", UNSET)
        provider_code: ProviderConfigDtoProviderCode | Unset
        if isinstance(_provider_code,  Unset):
            provider_code = UNSET
        else:
            provider_code = check_provider_config_dto_provider_code(_provider_code)




        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))


        is_active = d.pop("isActive", UNSET)

        is_test_mode = d.pop("isTestMode", UNSET)

        auto_issue_enabled = d.pop("autoIssueEnabled", UNSET)

        def _parse_auto_issue_hour(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        auto_issue_hour = _parse_auto_issue_hour(d.pop("autoIssueHour", UNSET))


        def _parse_issuer_tax_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issuer_tax_code = _parse_issuer_tax_code(d.pop("issuerTaxCode", UNSET))


        def _parse_issuer_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issuer_name = _parse_issuer_name(d.pop("issuerName", UNSET))


        def _parse_issuer_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issuer_address = _parse_issuer_address(d.pop("issuerAddress", UNSET))


        def _parse_issuer_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issuer_phone = _parse_issuer_phone(d.pop("issuerPhone", UNSET))


        def _parse_issuer_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issuer_email = _parse_issuer_email(d.pop("issuerEmail", UNSET))


        def _parse_issuer_bank_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issuer_bank_name = _parse_issuer_bank_name(d.pop("issuerBankName", UNSET))


        def _parse_issuer_bank_account(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issuer_bank_account = _parse_issuer_bank_account(d.pop("issuerBankAccount", UNSET))


        def _parse_default_vat_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        default_vat_rate = _parse_default_vat_rate(d.pop("defaultVatRate", UNSET))


        def _parse_config_public(data: object) -> None | ProviderConfigDtoConfigPublicType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_public_type_0 = ProviderConfigDtoConfigPublicType0.from_dict(data)



                return config_public_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProviderConfigDtoConfigPublicType0 | Unset, data)

        config_public = _parse_config_public(d.pop("configPublic", UNSET))


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




        provider_config_dto = cls(
            id=id,
            workspace_id=workspace_id,
            branch_id=branch_id,
            invoice_context=invoice_context,
            provider_code=provider_code,
            display_name=display_name,
            is_active=is_active,
            is_test_mode=is_test_mode,
            auto_issue_enabled=auto_issue_enabled,
            auto_issue_hour=auto_issue_hour,
            issuer_tax_code=issuer_tax_code,
            issuer_name=issuer_name,
            issuer_address=issuer_address,
            issuer_phone=issuer_phone,
            issuer_email=issuer_email,
            issuer_bank_name=issuer_bank_name,
            issuer_bank_account=issuer_bank_account,
            default_vat_rate=default_vat_rate,
            config_public=config_public,
            created_at=created_at,
            updated_at=updated_at,
        )

        return provider_config_dto


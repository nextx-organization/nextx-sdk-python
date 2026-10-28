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






T = TypeVar("T", bound="GoogleIntegrationDto")



@_attrs_define
class GoogleIntegrationDto:
    

    id: UUID | Unset = UNSET
    integration_type: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    google_account_email: None | str | Unset = UNSET
    scopes: list[str] | None | Unset = UNSET
    connected_at: datetime.datetime | Unset = UNSET
    token_expires_at: datetime.datetime | Unset = UNSET
    last_refreshed_at: datetime.datetime | None | Unset = UNSET
    selected_resource_id: None | str | Unset = UNSET
    selected_resource_name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        integration_type: None | str | Unset
        if isinstance(self.integration_type, Unset):
            integration_type = UNSET
        else:
            integration_type = self.integration_type

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        google_account_email: None | str | Unset
        if isinstance(self.google_account_email, Unset):
            google_account_email = UNSET
        else:
            google_account_email = self.google_account_email

        scopes: list[str] | None | Unset
        if isinstance(self.scopes, Unset):
            scopes = UNSET
        elif isinstance(self.scopes, list):
            scopes = self.scopes


        else:
            scopes = self.scopes

        connected_at: str | Unset = UNSET
        if not isinstance(self.connected_at, Unset):
            connected_at = self.connected_at.isoformat()

        token_expires_at: str | Unset = UNSET
        if not isinstance(self.token_expires_at, Unset):
            token_expires_at = self.token_expires_at.isoformat()

        last_refreshed_at: None | str | Unset
        if isinstance(self.last_refreshed_at, Unset):
            last_refreshed_at = UNSET
        elif isinstance(self.last_refreshed_at, datetime.datetime):
            last_refreshed_at = self.last_refreshed_at.isoformat()
        else:
            last_refreshed_at = self.last_refreshed_at

        selected_resource_id: None | str | Unset
        if isinstance(self.selected_resource_id, Unset):
            selected_resource_id = UNSET
        else:
            selected_resource_id = self.selected_resource_id

        selected_resource_name: None | str | Unset
        if isinstance(self.selected_resource_name, Unset):
            selected_resource_name = UNSET
        else:
            selected_resource_name = self.selected_resource_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if integration_type is not UNSET:
            field_dict["integrationType"] = integration_type
        if status is not UNSET:
            field_dict["status"] = status
        if google_account_email is not UNSET:
            field_dict["googleAccountEmail"] = google_account_email
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if connected_at is not UNSET:
            field_dict["connectedAt"] = connected_at
        if token_expires_at is not UNSET:
            field_dict["tokenExpiresAt"] = token_expires_at
        if last_refreshed_at is not UNSET:
            field_dict["lastRefreshedAt"] = last_refreshed_at
        if selected_resource_id is not UNSET:
            field_dict["selectedResourceId"] = selected_resource_id
        if selected_resource_name is not UNSET:
            field_dict["selectedResourceName"] = selected_resource_name

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




        def _parse_integration_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        integration_type = _parse_integration_type(d.pop("integrationType", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_google_account_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        google_account_email = _parse_google_account_email(d.pop("googleAccountEmail", UNSET))


        def _parse_scopes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scopes_type_0 = cast(list[str], data)

                return scopes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        scopes = _parse_scopes(d.pop("scopes", UNSET))


        _connected_at = d.pop("connectedAt", UNSET)
        connected_at: datetime.datetime | Unset
        if isinstance(_connected_at,  Unset):
            connected_at = UNSET
        else:
            connected_at = datetime.datetime.fromisoformat(_connected_at)




        _token_expires_at = d.pop("tokenExpiresAt", UNSET)
        token_expires_at: datetime.datetime | Unset
        if isinstance(_token_expires_at,  Unset):
            token_expires_at = UNSET
        else:
            token_expires_at = datetime.datetime.fromisoformat(_token_expires_at)




        def _parse_last_refreshed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_refreshed_at_type_0 = datetime.datetime.fromisoformat(data)



                return last_refreshed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_refreshed_at = _parse_last_refreshed_at(d.pop("lastRefreshedAt", UNSET))


        def _parse_selected_resource_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        selected_resource_id = _parse_selected_resource_id(d.pop("selectedResourceId", UNSET))


        def _parse_selected_resource_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        selected_resource_name = _parse_selected_resource_name(d.pop("selectedResourceName", UNSET))


        google_integration_dto = cls(
            id=id,
            integration_type=integration_type,
            status=status,
            google_account_email=google_account_email,
            scopes=scopes,
            connected_at=connected_at,
            token_expires_at=token_expires_at,
            last_refreshed_at=last_refreshed_at,
            selected_resource_id=selected_resource_id,
            selected_resource_name=selected_resource_name,
        )

        return google_integration_dto


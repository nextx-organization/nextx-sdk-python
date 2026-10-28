from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="FailureReasonDto")



@_attrs_define
class FailureReasonDto:
    

    reason_key: None | str | Unset = UNSET
    culprit: None | str | Unset = UNSET
    action_key: None | str | Unset = UNSET
    sip_code: int | None | Unset = UNSET
    sip_reason: None | str | Unset = UNSET
    hangup_cause: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        reason_key: None | str | Unset
        if isinstance(self.reason_key, Unset):
            reason_key = UNSET
        else:
            reason_key = self.reason_key

        culprit: None | str | Unset
        if isinstance(self.culprit, Unset):
            culprit = UNSET
        else:
            culprit = self.culprit

        action_key: None | str | Unset
        if isinstance(self.action_key, Unset):
            action_key = UNSET
        else:
            action_key = self.action_key

        sip_code: int | None | Unset
        if isinstance(self.sip_code, Unset):
            sip_code = UNSET
        else:
            sip_code = self.sip_code

        sip_reason: None | str | Unset
        if isinstance(self.sip_reason, Unset):
            sip_reason = UNSET
        else:
            sip_reason = self.sip_reason

        hangup_cause: None | str | Unset
        if isinstance(self.hangup_cause, Unset):
            hangup_cause = UNSET
        else:
            hangup_cause = self.hangup_cause


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if reason_key is not UNSET:
            field_dict["reasonKey"] = reason_key
        if culprit is not UNSET:
            field_dict["culprit"] = culprit
        if action_key is not UNSET:
            field_dict["actionKey"] = action_key
        if sip_code is not UNSET:
            field_dict["sipCode"] = sip_code
        if sip_reason is not UNSET:
            field_dict["sipReason"] = sip_reason
        if hangup_cause is not UNSET:
            field_dict["hangupCause"] = hangup_cause

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_reason_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason_key = _parse_reason_key(d.pop("reasonKey", UNSET))


        def _parse_culprit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        culprit = _parse_culprit(d.pop("culprit", UNSET))


        def _parse_action_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        action_key = _parse_action_key(d.pop("actionKey", UNSET))


        def _parse_sip_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sip_code = _parse_sip_code(d.pop("sipCode", UNSET))


        def _parse_sip_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sip_reason = _parse_sip_reason(d.pop("sipReason", UNSET))


        def _parse_hangup_cause(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hangup_cause = _parse_hangup_cause(d.pop("hangupCause", UNSET))


        failure_reason_dto = cls(
            reason_key=reason_key,
            culprit=culprit,
            action_key=action_key,
            sip_code=sip_code,
            sip_reason=sip_reason,
            hangup_cause=hangup_cause,
        )

        return failure_reason_dto


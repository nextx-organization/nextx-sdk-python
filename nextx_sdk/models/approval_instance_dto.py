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






T = TypeVar("T", bound="ApprovalInstanceDto")



@_attrs_define
class ApprovalInstanceDto:
    

    id: UUID | Unset = UNSET
    definition_id: UUID | Unset = UNSET
    definition_code: None | str | Unset = UNSET
    applicant_id: UUID | Unset = UNSET
    status: None | str | Unset = UNSET
    form_value: None | str | Unset = UNSET
    current_node_id: None | Unset | UUID = UNSET
    enrollment_id: None | Unset | UUID = UNSET
    created_at: datetime.datetime | Unset = UNSET
    definition_name: None | str | Unset = UNSET
    my_pending_task_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        definition_id: str | Unset = UNSET
        if not isinstance(self.definition_id, Unset):
            definition_id = str(self.definition_id)

        definition_code: None | str | Unset
        if isinstance(self.definition_code, Unset):
            definition_code = UNSET
        else:
            definition_code = self.definition_code

        applicant_id: str | Unset = UNSET
        if not isinstance(self.applicant_id, Unset):
            applicant_id = str(self.applicant_id)

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        form_value: None | str | Unset
        if isinstance(self.form_value, Unset):
            form_value = UNSET
        else:
            form_value = self.form_value

        current_node_id: None | str | Unset
        if isinstance(self.current_node_id, Unset):
            current_node_id = UNSET
        elif isinstance(self.current_node_id, UUID):
            current_node_id = str(self.current_node_id)
        else:
            current_node_id = self.current_node_id

        enrollment_id: None | str | Unset
        if isinstance(self.enrollment_id, Unset):
            enrollment_id = UNSET
        elif isinstance(self.enrollment_id, UUID):
            enrollment_id = str(self.enrollment_id)
        else:
            enrollment_id = self.enrollment_id

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        definition_name: None | str | Unset
        if isinstance(self.definition_name, Unset):
            definition_name = UNSET
        else:
            definition_name = self.definition_name

        my_pending_task_id: None | str | Unset
        if isinstance(self.my_pending_task_id, Unset):
            my_pending_task_id = UNSET
        elif isinstance(self.my_pending_task_id, UUID):
            my_pending_task_id = str(self.my_pending_task_id)
        else:
            my_pending_task_id = self.my_pending_task_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if definition_id is not UNSET:
            field_dict["definitionId"] = definition_id
        if definition_code is not UNSET:
            field_dict["definitionCode"] = definition_code
        if applicant_id is not UNSET:
            field_dict["applicantId"] = applicant_id
        if status is not UNSET:
            field_dict["status"] = status
        if form_value is not UNSET:
            field_dict["formValue"] = form_value
        if current_node_id is not UNSET:
            field_dict["currentNodeId"] = current_node_id
        if enrollment_id is not UNSET:
            field_dict["enrollmentId"] = enrollment_id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if definition_name is not UNSET:
            field_dict["definitionName"] = definition_name
        if my_pending_task_id is not UNSET:
            field_dict["myPendingTaskId"] = my_pending_task_id

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




        _definition_id = d.pop("definitionId", UNSET)
        definition_id: UUID | Unset
        if isinstance(_definition_id,  Unset):
            definition_id = UNSET
        else:
            definition_id = UUID(_definition_id)




        def _parse_definition_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        definition_code = _parse_definition_code(d.pop("definitionCode", UNSET))


        _applicant_id = d.pop("applicantId", UNSET)
        applicant_id: UUID | Unset
        if isinstance(_applicant_id,  Unset):
            applicant_id = UNSET
        else:
            applicant_id = UUID(_applicant_id)




        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_form_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        form_value = _parse_form_value(d.pop("formValue", UNSET))


        def _parse_current_node_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                current_node_id_type_0 = UUID(data)



                return current_node_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        current_node_id = _parse_current_node_id(d.pop("currentNodeId", UNSET))


        def _parse_enrollment_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                enrollment_id_type_0 = UUID(data)



                return enrollment_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        enrollment_id = _parse_enrollment_id(d.pop("enrollmentId", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_definition_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        definition_name = _parse_definition_name(d.pop("definitionName", UNSET))


        def _parse_my_pending_task_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                my_pending_task_id_type_0 = UUID(data)



                return my_pending_task_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        my_pending_task_id = _parse_my_pending_task_id(d.pop("myPendingTaskId", UNSET))


        approval_instance_dto = cls(
            id=id,
            definition_id=definition_id,
            definition_code=definition_code,
            applicant_id=applicant_id,
            status=status,
            form_value=form_value,
            current_node_id=current_node_id,
            enrollment_id=enrollment_id,
            created_at=created_at,
            definition_name=definition_name,
            my_pending_task_id=my_pending_task_id,
        )

        return approval_instance_dto


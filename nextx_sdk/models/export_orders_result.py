from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="ExportOrdersResult")



@_attrs_define
class ExportOrdersResult:
    

    job_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        job_id: str | Unset = UNSET
        if not isinstance(self.job_id, Unset):
            job_id = str(self.job_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if job_id is not UNSET:
            field_dict["jobId"] = job_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _job_id = d.pop("jobId", UNSET)
        job_id: UUID | Unset
        if isinstance(_job_id,  Unset):
            job_id = UNSET
        else:
            job_id = UUID(_job_id)




        export_orders_result = cls(
            job_id=job_id,
        )

        return export_orders_result


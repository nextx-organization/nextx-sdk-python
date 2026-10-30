from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.partner_agent_ref_request import PartnerAgentRefRequest





T = TypeVar("T", bound="PartnerTransferRequest")



@_attrs_define
class PartnerTransferRequest:
    

    to_agent: PartnerAgentRefRequest | Unset = UNSET
    to_queue_id: None | Unset | UUID = UNSET
    to_number: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.partner_agent_ref_request import PartnerAgentRefRequest # noqa: PLC0415
        to_agent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to_agent, Unset):
            to_agent = self.to_agent.to_dict()

        to_queue_id: None | str | Unset
        if isinstance(self.to_queue_id, Unset):
            to_queue_id = UNSET
        elif isinstance(self.to_queue_id, UUID):
            to_queue_id = str(self.to_queue_id)
        else:
            to_queue_id = self.to_queue_id

        to_number: None | str | Unset
        if isinstance(self.to_number, Unset):
            to_number = UNSET
        else:
            to_number = self.to_number


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if to_agent is not UNSET:
            field_dict["toAgent"] = to_agent
        if to_queue_id is not UNSET:
            field_dict["toQueueId"] = to_queue_id
        if to_number is not UNSET:
            field_dict["toNumber"] = to_number

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.partner_agent_ref_request import PartnerAgentRefRequest # noqa: PLC0415
        d = dict(src_dict)
        _to_agent = d.pop("toAgent", UNSET)
        to_agent: PartnerAgentRefRequest | Unset
        if isinstance(_to_agent,  Unset):
            to_agent = UNSET
        else:
            to_agent = PartnerAgentRefRequest.from_dict(_to_agent)




        def _parse_to_queue_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                to_queue_id_type_0 = UUID(data)



                return to_queue_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        to_queue_id = _parse_to_queue_id(d.pop("toQueueId", UNSET))


        def _parse_to_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        to_number = _parse_to_number(d.pop("toNumber", UNSET))


        partner_transfer_request = cls(
            to_agent=to_agent,
            to_queue_id=to_queue_id,
            to_number=to_number,
        )

        return partner_transfer_request


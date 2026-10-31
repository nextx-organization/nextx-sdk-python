from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.partner_agent_dto import PartnerAgentDto





T = TypeVar("T", bound="PartnerAgentStatusDto")



@_attrs_define
class PartnerAgentStatusDto:
    

    agent: PartnerAgentDto | Unset = UNSET
    status: None | str | Unset = UNSET
    since: datetime.datetime | None | Unset = UNSET
    registered: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.partner_agent_dto import PartnerAgentDto # noqa: PLC0415
        agent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.agent, Unset):
            agent = self.agent.to_dict()

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        since: None | str | Unset
        if isinstance(self.since, Unset):
            since = UNSET
        elif isinstance(self.since, datetime.datetime):
            since = self.since.isoformat()
        else:
            since = self.since

        registered = self.registered


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if agent is not UNSET:
            field_dict["agent"] = agent
        if status is not UNSET:
            field_dict["status"] = status
        if since is not UNSET:
            field_dict["since"] = since
        if registered is not UNSET:
            field_dict["registered"] = registered

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.partner_agent_dto import PartnerAgentDto # noqa: PLC0415
        d = dict(src_dict)
        _agent = d.pop("agent", UNSET)
        agent: PartnerAgentDto | Unset
        if isinstance(_agent,  Unset):
            agent = UNSET
        else:
            agent = PartnerAgentDto.from_dict(_agent)




        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_since(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                since_type_0 = datetime.datetime.fromisoformat(data)



                return since_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        since = _parse_since(d.pop("since", UNSET))


        registered = d.pop("registered", UNSET)

        partner_agent_status_dto = cls(
            agent=agent,
            status=status,
            since=since,
            registered=registered,
        )

        return partner_agent_status_dto


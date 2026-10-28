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






T = TypeVar("T", bound="DmsMyDayStopDto")



@_attrs_define
class DmsMyDayStopDto:
    

    id: UUID | Unset = UNSET
    route_stop_id: None | Unset | UUID = UNSET
    route_id: None | Unset | UUID = UNSET
    route_name: None | str | Unset = UNSET
    outlet_id: UUID | Unset = UNSET
    outlet_name: None | str | Unset = UNSET
    outlet_address: None | str | Unset = UNSET
    stop_sequence: int | Unset = UNSET
    status: None | str | Unset = UNSET
    checkin_at: datetime.datetime | None | Unset = UNSET
    checkout_at: datetime.datetime | None | Unset = UNSET
    skip_reason: None | str | Unset = UNSET
    order_count: int | Unset = UNSET
    checklist_score: float | None | Unset = UNSET
    gps_lat: float | None | Unset = UNSET
    gps_lng: float | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        route_stop_id: None | str | Unset
        if isinstance(self.route_stop_id, Unset):
            route_stop_id = UNSET
        elif isinstance(self.route_stop_id, UUID):
            route_stop_id = str(self.route_stop_id)
        else:
            route_stop_id = self.route_stop_id

        route_id: None | str | Unset
        if isinstance(self.route_id, Unset):
            route_id = UNSET
        elif isinstance(self.route_id, UUID):
            route_id = str(self.route_id)
        else:
            route_id = self.route_id

        route_name: None | str | Unset
        if isinstance(self.route_name, Unset):
            route_name = UNSET
        else:
            route_name = self.route_name

        outlet_id: str | Unset = UNSET
        if not isinstance(self.outlet_id, Unset):
            outlet_id = str(self.outlet_id)

        outlet_name: None | str | Unset
        if isinstance(self.outlet_name, Unset):
            outlet_name = UNSET
        else:
            outlet_name = self.outlet_name

        outlet_address: None | str | Unset
        if isinstance(self.outlet_address, Unset):
            outlet_address = UNSET
        else:
            outlet_address = self.outlet_address

        stop_sequence = self.stop_sequence

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        checkin_at: None | str | Unset
        if isinstance(self.checkin_at, Unset):
            checkin_at = UNSET
        elif isinstance(self.checkin_at, datetime.datetime):
            checkin_at = self.checkin_at.isoformat()
        else:
            checkin_at = self.checkin_at

        checkout_at: None | str | Unset
        if isinstance(self.checkout_at, Unset):
            checkout_at = UNSET
        elif isinstance(self.checkout_at, datetime.datetime):
            checkout_at = self.checkout_at.isoformat()
        else:
            checkout_at = self.checkout_at

        skip_reason: None | str | Unset
        if isinstance(self.skip_reason, Unset):
            skip_reason = UNSET
        else:
            skip_reason = self.skip_reason

        order_count = self.order_count

        checklist_score: float | None | Unset
        if isinstance(self.checklist_score, Unset):
            checklist_score = UNSET
        else:
            checklist_score = self.checklist_score

        gps_lat: float | None | Unset
        if isinstance(self.gps_lat, Unset):
            gps_lat = UNSET
        else:
            gps_lat = self.gps_lat

        gps_lng: float | None | Unset
        if isinstance(self.gps_lng, Unset):
            gps_lng = UNSET
        else:
            gps_lng = self.gps_lng


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if route_stop_id is not UNSET:
            field_dict["routeStopId"] = route_stop_id
        if route_id is not UNSET:
            field_dict["routeId"] = route_id
        if route_name is not UNSET:
            field_dict["routeName"] = route_name
        if outlet_id is not UNSET:
            field_dict["outletId"] = outlet_id
        if outlet_name is not UNSET:
            field_dict["outletName"] = outlet_name
        if outlet_address is not UNSET:
            field_dict["outletAddress"] = outlet_address
        if stop_sequence is not UNSET:
            field_dict["stopSequence"] = stop_sequence
        if status is not UNSET:
            field_dict["status"] = status
        if checkin_at is not UNSET:
            field_dict["checkinAt"] = checkin_at
        if checkout_at is not UNSET:
            field_dict["checkoutAt"] = checkout_at
        if skip_reason is not UNSET:
            field_dict["skipReason"] = skip_reason
        if order_count is not UNSET:
            field_dict["orderCount"] = order_count
        if checklist_score is not UNSET:
            field_dict["checklistScore"] = checklist_score
        if gps_lat is not UNSET:
            field_dict["gpsLat"] = gps_lat
        if gps_lng is not UNSET:
            field_dict["gpsLng"] = gps_lng

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




        def _parse_route_stop_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                route_stop_id_type_0 = UUID(data)



                return route_stop_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        route_stop_id = _parse_route_stop_id(d.pop("routeStopId", UNSET))


        def _parse_route_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                route_id_type_0 = UUID(data)



                return route_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        route_id = _parse_route_id(d.pop("routeId", UNSET))


        def _parse_route_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        route_name = _parse_route_name(d.pop("routeName", UNSET))


        _outlet_id = d.pop("outletId", UNSET)
        outlet_id: UUID | Unset
        if isinstance(_outlet_id,  Unset):
            outlet_id = UNSET
        else:
            outlet_id = UUID(_outlet_id)




        def _parse_outlet_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        outlet_name = _parse_outlet_name(d.pop("outletName", UNSET))


        def _parse_outlet_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        outlet_address = _parse_outlet_address(d.pop("outletAddress", UNSET))


        stop_sequence = d.pop("stopSequence", UNSET)

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_checkin_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                checkin_at_type_0 = datetime.datetime.fromisoformat(data)



                return checkin_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        checkin_at = _parse_checkin_at(d.pop("checkinAt", UNSET))


        def _parse_checkout_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                checkout_at_type_0 = datetime.datetime.fromisoformat(data)



                return checkout_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        checkout_at = _parse_checkout_at(d.pop("checkoutAt", UNSET))


        def _parse_skip_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        skip_reason = _parse_skip_reason(d.pop("skipReason", UNSET))


        order_count = d.pop("orderCount", UNSET)

        def _parse_checklist_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        checklist_score = _parse_checklist_score(d.pop("checklistScore", UNSET))


        def _parse_gps_lat(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        gps_lat = _parse_gps_lat(d.pop("gpsLat", UNSET))


        def _parse_gps_lng(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        gps_lng = _parse_gps_lng(d.pop("gpsLng", UNSET))


        dms_my_day_stop_dto = cls(
            id=id,
            route_stop_id=route_stop_id,
            route_id=route_id,
            route_name=route_name,
            outlet_id=outlet_id,
            outlet_name=outlet_name,
            outlet_address=outlet_address,
            stop_sequence=stop_sequence,
            status=status,
            checkin_at=checkin_at,
            checkout_at=checkout_at,
            skip_reason=skip_reason,
            order_count=order_count,
            checklist_score=checklist_score,
            gps_lat=gps_lat,
            gps_lng=gps_lng,
        )

        return dms_my_day_stop_dto


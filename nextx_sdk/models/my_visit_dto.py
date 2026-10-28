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






T = TypeVar("T", bound="MyVisitDto")



@_attrs_define
class MyVisitDto:
    

    date: datetime.date | Unset = UNSET
    outlet_id: UUID | Unset = UNSET
    outlet_name: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    gps_lat: float | None | Unset = UNSET
    gps_lng: float | None | Unset = UNSET
    route_id: UUID | Unset = UNSET
    route_code: None | str | Unset = UNSET
    visit_order: int | Unset = UNSET
    status: None | str | Unset = UNSET
    checkin_at: datetime.datetime | None | Unset = UNSET
    checkout_at: datetime.datetime | None | Unset = UNSET
    notes: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        outlet_id: str | Unset = UNSET
        if not isinstance(self.outlet_id, Unset):
            outlet_id = str(self.outlet_id)

        outlet_name: None | str | Unset
        if isinstance(self.outlet_name, Unset):
            outlet_name = UNSET
        else:
            outlet_name = self.outlet_name

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

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

        route_id: str | Unset = UNSET
        if not isinstance(self.route_id, Unset):
            route_id = str(self.route_id)

        route_code: None | str | Unset
        if isinstance(self.route_code, Unset):
            route_code = UNSET
        else:
            route_code = self.route_code

        visit_order = self.visit_order

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

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if date is not UNSET:
            field_dict["date"] = date
        if outlet_id is not UNSET:
            field_dict["outletId"] = outlet_id
        if outlet_name is not UNSET:
            field_dict["outletName"] = outlet_name
        if address is not UNSET:
            field_dict["address"] = address
        if gps_lat is not UNSET:
            field_dict["gpsLat"] = gps_lat
        if gps_lng is not UNSET:
            field_dict["gpsLng"] = gps_lng
        if route_id is not UNSET:
            field_dict["routeId"] = route_id
        if route_code is not UNSET:
            field_dict["routeCode"] = route_code
        if visit_order is not UNSET:
            field_dict["visitOrder"] = visit_order
        if status is not UNSET:
            field_dict["status"] = status
        if checkin_at is not UNSET:
            field_dict["checkinAt"] = checkin_at
        if checkout_at is not UNSET:
            field_dict["checkoutAt"] = checkout_at
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date,  Unset):
            date = UNSET
        else:
            date = datetime.date.fromisoformat(_date)




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


        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))


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


        _route_id = d.pop("routeId", UNSET)
        route_id: UUID | Unset
        if isinstance(_route_id,  Unset):
            route_id = UNSET
        else:
            route_id = UUID(_route_id)




        def _parse_route_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        route_code = _parse_route_code(d.pop("routeCode", UNSET))


        visit_order = d.pop("visitOrder", UNSET)

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


        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


        my_visit_dto = cls(
            date=date,
            outlet_id=outlet_id,
            outlet_name=outlet_name,
            address=address,
            gps_lat=gps_lat,
            gps_lng=gps_lng,
            route_id=route_id,
            route_code=route_code,
            visit_order=visit_order,
            status=status,
            checkin_at=checkin_at,
            checkout_at=checkout_at,
            notes=notes,
        )

        return my_visit_dto


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.checkin_log_dto_type import check_checkin_log_dto_type
from ..models.checkin_log_dto_type import CheckinLogDtoType
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="CheckinLogDto")



@_attrs_define
class CheckinLogDto:
    

    id: UUID | Unset = UNSET
    outlet_id: None | Unset | UUID = UNSET
    outlet_name: None | str | Unset = UNSET
    employee_id: UUID | Unset = UNSET
    employee_name: None | str | Unset = UNSET
    route_id: None | Unset | UUID = UNSET
    daily_plan_id: None | Unset | UUID = UNSET
    checkin_at: datetime.datetime | Unset = UNSET
    checkout_at: datetime.datetime | None | Unset = UNSET
    checkin_lat: float | None | Unset = UNSET
    checkin_lng: float | None | Unset = UNSET
    checkin_address: None | str | Unset = UNSET
    distance_from_outlet: float | None | Unset = UNSET
    is_valid: bool | Unset = UNSET
    invalid_reason: None | str | Unset = UNSET
    photo_key: None | str | Unset = UNSET
    photo_keys: list[str] | None | Unset = UNSET
    notes: None | str | Unset = UNSET
    type_: CheckinLogDtoType | Unset = UNSET
    photo_urls: list[str] | None | Unset = UNSET
    is_auto_closed: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        outlet_id: None | str | Unset
        if isinstance(self.outlet_id, Unset):
            outlet_id = UNSET
        elif isinstance(self.outlet_id, UUID):
            outlet_id = str(self.outlet_id)
        else:
            outlet_id = self.outlet_id

        outlet_name: None | str | Unset
        if isinstance(self.outlet_name, Unset):
            outlet_name = UNSET
        else:
            outlet_name = self.outlet_name

        employee_id: str | Unset = UNSET
        if not isinstance(self.employee_id, Unset):
            employee_id = str(self.employee_id)

        employee_name: None | str | Unset
        if isinstance(self.employee_name, Unset):
            employee_name = UNSET
        else:
            employee_name = self.employee_name

        route_id: None | str | Unset
        if isinstance(self.route_id, Unset):
            route_id = UNSET
        elif isinstance(self.route_id, UUID):
            route_id = str(self.route_id)
        else:
            route_id = self.route_id

        daily_plan_id: None | str | Unset
        if isinstance(self.daily_plan_id, Unset):
            daily_plan_id = UNSET
        elif isinstance(self.daily_plan_id, UUID):
            daily_plan_id = str(self.daily_plan_id)
        else:
            daily_plan_id = self.daily_plan_id

        checkin_at: str | Unset = UNSET
        if not isinstance(self.checkin_at, Unset):
            checkin_at = self.checkin_at.isoformat()

        checkout_at: None | str | Unset
        if isinstance(self.checkout_at, Unset):
            checkout_at = UNSET
        elif isinstance(self.checkout_at, datetime.datetime):
            checkout_at = self.checkout_at.isoformat()
        else:
            checkout_at = self.checkout_at

        checkin_lat: float | None | Unset
        if isinstance(self.checkin_lat, Unset):
            checkin_lat = UNSET
        else:
            checkin_lat = self.checkin_lat

        checkin_lng: float | None | Unset
        if isinstance(self.checkin_lng, Unset):
            checkin_lng = UNSET
        else:
            checkin_lng = self.checkin_lng

        checkin_address: None | str | Unset
        if isinstance(self.checkin_address, Unset):
            checkin_address = UNSET
        else:
            checkin_address = self.checkin_address

        distance_from_outlet: float | None | Unset
        if isinstance(self.distance_from_outlet, Unset):
            distance_from_outlet = UNSET
        else:
            distance_from_outlet = self.distance_from_outlet

        is_valid = self.is_valid

        invalid_reason: None | str | Unset
        if isinstance(self.invalid_reason, Unset):
            invalid_reason = UNSET
        else:
            invalid_reason = self.invalid_reason

        photo_key: None | str | Unset
        if isinstance(self.photo_key, Unset):
            photo_key = UNSET
        else:
            photo_key = self.photo_key

        photo_keys: list[str] | None | Unset
        if isinstance(self.photo_keys, Unset):
            photo_keys = UNSET
        elif isinstance(self.photo_keys, list):
            photo_keys = self.photo_keys


        else:
            photo_keys = self.photo_keys

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_


        photo_urls: list[str] | None | Unset
        if isinstance(self.photo_urls, Unset):
            photo_urls = UNSET
        elif isinstance(self.photo_urls, list):
            photo_urls = self.photo_urls


        else:
            photo_urls = self.photo_urls

        is_auto_closed = self.is_auto_closed


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if outlet_id is not UNSET:
            field_dict["outletId"] = outlet_id
        if outlet_name is not UNSET:
            field_dict["outletName"] = outlet_name
        if employee_id is not UNSET:
            field_dict["employeeId"] = employee_id
        if employee_name is not UNSET:
            field_dict["employeeName"] = employee_name
        if route_id is not UNSET:
            field_dict["routeId"] = route_id
        if daily_plan_id is not UNSET:
            field_dict["dailyPlanId"] = daily_plan_id
        if checkin_at is not UNSET:
            field_dict["checkinAt"] = checkin_at
        if checkout_at is not UNSET:
            field_dict["checkoutAt"] = checkout_at
        if checkin_lat is not UNSET:
            field_dict["checkinLat"] = checkin_lat
        if checkin_lng is not UNSET:
            field_dict["checkinLng"] = checkin_lng
        if checkin_address is not UNSET:
            field_dict["checkinAddress"] = checkin_address
        if distance_from_outlet is not UNSET:
            field_dict["distanceFromOutlet"] = distance_from_outlet
        if is_valid is not UNSET:
            field_dict["isValid"] = is_valid
        if invalid_reason is not UNSET:
            field_dict["invalidReason"] = invalid_reason
        if photo_key is not UNSET:
            field_dict["photoKey"] = photo_key
        if photo_keys is not UNSET:
            field_dict["photoKeys"] = photo_keys
        if notes is not UNSET:
            field_dict["notes"] = notes
        if type_ is not UNSET:
            field_dict["type"] = type_
        if photo_urls is not UNSET:
            field_dict["photoUrls"] = photo_urls
        if is_auto_closed is not UNSET:
            field_dict["isAutoClosed"] = is_auto_closed

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




        def _parse_outlet_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                outlet_id_type_0 = UUID(data)



                return outlet_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        outlet_id = _parse_outlet_id(d.pop("outletId", UNSET))


        def _parse_outlet_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        outlet_name = _parse_outlet_name(d.pop("outletName", UNSET))


        _employee_id = d.pop("employeeId", UNSET)
        employee_id: UUID | Unset
        if isinstance(_employee_id,  Unset):
            employee_id = UNSET
        else:
            employee_id = UUID(_employee_id)




        def _parse_employee_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        employee_name = _parse_employee_name(d.pop("employeeName", UNSET))


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


        def _parse_daily_plan_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                daily_plan_id_type_0 = UUID(data)



                return daily_plan_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        daily_plan_id = _parse_daily_plan_id(d.pop("dailyPlanId", UNSET))


        _checkin_at = d.pop("checkinAt", UNSET)
        checkin_at: datetime.datetime | Unset
        if isinstance(_checkin_at,  Unset):
            checkin_at = UNSET
        else:
            checkin_at = datetime.datetime.fromisoformat(_checkin_at)




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


        def _parse_checkin_lat(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        checkin_lat = _parse_checkin_lat(d.pop("checkinLat", UNSET))


        def _parse_checkin_lng(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        checkin_lng = _parse_checkin_lng(d.pop("checkinLng", UNSET))


        def _parse_checkin_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        checkin_address = _parse_checkin_address(d.pop("checkinAddress", UNSET))


        def _parse_distance_from_outlet(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        distance_from_outlet = _parse_distance_from_outlet(d.pop("distanceFromOutlet", UNSET))


        is_valid = d.pop("isValid", UNSET)

        def _parse_invalid_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        invalid_reason = _parse_invalid_reason(d.pop("invalidReason", UNSET))


        def _parse_photo_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        photo_key = _parse_photo_key(d.pop("photoKey", UNSET))


        def _parse_photo_keys(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                photo_keys_type_0 = cast(list[str], data)

                return photo_keys_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        photo_keys = _parse_photo_keys(d.pop("photoKeys", UNSET))


        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


        _type_ = d.pop("type", UNSET)
        type_: CheckinLogDtoType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = check_checkin_log_dto_type(_type_)




        def _parse_photo_urls(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                photo_urls_type_0 = cast(list[str], data)

                return photo_urls_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        photo_urls = _parse_photo_urls(d.pop("photoUrls", UNSET))


        is_auto_closed = d.pop("isAutoClosed", UNSET)

        checkin_log_dto = cls(
            id=id,
            outlet_id=outlet_id,
            outlet_name=outlet_name,
            employee_id=employee_id,
            employee_name=employee_name,
            route_id=route_id,
            daily_plan_id=daily_plan_id,
            checkin_at=checkin_at,
            checkout_at=checkout_at,
            checkin_lat=checkin_lat,
            checkin_lng=checkin_lng,
            checkin_address=checkin_address,
            distance_from_outlet=distance_from_outlet,
            is_valid=is_valid,
            invalid_reason=invalid_reason,
            photo_key=photo_key,
            photo_keys=photo_keys,
            notes=notes,
            type_=type_,
            photo_urls=photo_urls,
            is_auto_closed=is_auto_closed,
        )

        return checkin_log_dto


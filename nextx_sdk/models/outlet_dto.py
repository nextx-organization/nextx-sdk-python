from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.outlet_dto_outlet_status import check_outlet_dto_outlet_status
from ..models.outlet_dto_outlet_status import OutletDtoOutletStatus
from ..models.outlet_dto_visit_frequency import check_outlet_dto_visit_frequency
from ..models.outlet_dto_visit_frequency import OutletDtoVisitFrequency
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.outlet_assigned_rep_dto import OutletAssignedRepDto





T = TypeVar("T", bound="OutletDto")



@_attrs_define
class OutletDto:
    

    id: UUID | Unset = UNSET
    outlet_code: None | str | Unset = UNSET
    outlet_name: None | str | Unset = UNSET
    channel_code: None | str | Unset = UNSET
    outlet_status: OutletDtoOutletStatus | Unset = UNSET
    gps_lat: float | None | Unset = UNSET
    gps_lng: float | None | Unset = UNSET
    address: None | str | Unset = UNSET
    zone_id: None | Unset | UUID = UNSET
    branch_id: None | Unset | UUID = UNSET
    visit_frequency: OutletDtoVisitFrequency | Unset = UNSET
    owner_name: None | str | Unset = UNSET
    owner_phone: None | str | Unset = UNSET
    owner_email: None | str | Unset = UNSET
    last_checkin_at: datetime.datetime | None | Unset = UNSET
    assigned_rep_id: None | Unset | UUID = UNSET
    assigned_rep_code: None | str | Unset = UNSET
    assigned_rep_name: None | str | Unset = UNSET
    tier: None | str | Unset = UNSET
    rank: None | str | Unset = UNSET
    route_code: None | str | Unset = UNSET
    assigned_reps: list[OutletAssignedRepDto] | None | Unset = UNSET
    care_status_id: None | Unset | UUID = UNSET
    care_status_name: None | str | Unset = UNSET
    care_status_color: None | str | Unset = UNSET
    order_count: int | None | Unset = UNSET
    order_revenue: float | None | Unset = UNSET
    last_order_at: datetime.datetime | None | Unset = UNSET
    tax_code: None | str | Unset = UNSET
    duplicate_group: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.outlet_assigned_rep_dto import OutletAssignedRepDto # noqa: PLC0415
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        outlet_code: None | str | Unset
        if isinstance(self.outlet_code, Unset):
            outlet_code = UNSET
        else:
            outlet_code = self.outlet_code

        outlet_name: None | str | Unset
        if isinstance(self.outlet_name, Unset):
            outlet_name = UNSET
        else:
            outlet_name = self.outlet_name

        channel_code: None | str | Unset
        if isinstance(self.channel_code, Unset):
            channel_code = UNSET
        else:
            channel_code = self.channel_code

        outlet_status: str | Unset = UNSET
        if not isinstance(self.outlet_status, Unset):
            outlet_status = self.outlet_status


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

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        zone_id: None | str | Unset
        if isinstance(self.zone_id, Unset):
            zone_id = UNSET
        elif isinstance(self.zone_id, UUID):
            zone_id = str(self.zone_id)
        else:
            zone_id = self.zone_id

        branch_id: None | str | Unset
        if isinstance(self.branch_id, Unset):
            branch_id = UNSET
        elif isinstance(self.branch_id, UUID):
            branch_id = str(self.branch_id)
        else:
            branch_id = self.branch_id

        visit_frequency: str | Unset = UNSET
        if not isinstance(self.visit_frequency, Unset):
            visit_frequency = self.visit_frequency


        owner_name: None | str | Unset
        if isinstance(self.owner_name, Unset):
            owner_name = UNSET
        else:
            owner_name = self.owner_name

        owner_phone: None | str | Unset
        if isinstance(self.owner_phone, Unset):
            owner_phone = UNSET
        else:
            owner_phone = self.owner_phone

        owner_email: None | str | Unset
        if isinstance(self.owner_email, Unset):
            owner_email = UNSET
        else:
            owner_email = self.owner_email

        last_checkin_at: None | str | Unset
        if isinstance(self.last_checkin_at, Unset):
            last_checkin_at = UNSET
        elif isinstance(self.last_checkin_at, datetime.datetime):
            last_checkin_at = self.last_checkin_at.isoformat()
        else:
            last_checkin_at = self.last_checkin_at

        assigned_rep_id: None | str | Unset
        if isinstance(self.assigned_rep_id, Unset):
            assigned_rep_id = UNSET
        elif isinstance(self.assigned_rep_id, UUID):
            assigned_rep_id = str(self.assigned_rep_id)
        else:
            assigned_rep_id = self.assigned_rep_id

        assigned_rep_code: None | str | Unset
        if isinstance(self.assigned_rep_code, Unset):
            assigned_rep_code = UNSET
        else:
            assigned_rep_code = self.assigned_rep_code

        assigned_rep_name: None | str | Unset
        if isinstance(self.assigned_rep_name, Unset):
            assigned_rep_name = UNSET
        else:
            assigned_rep_name = self.assigned_rep_name

        tier: None | str | Unset
        if isinstance(self.tier, Unset):
            tier = UNSET
        else:
            tier = self.tier

        rank: None | str | Unset
        if isinstance(self.rank, Unset):
            rank = UNSET
        else:
            rank = self.rank

        route_code: None | str | Unset
        if isinstance(self.route_code, Unset):
            route_code = UNSET
        else:
            route_code = self.route_code

        assigned_reps: list[dict[str, Any]] | None | Unset
        if isinstance(self.assigned_reps, Unset):
            assigned_reps = UNSET
        elif isinstance(self.assigned_reps, list):
            assigned_reps = []
            for assigned_reps_type_0_item_data in self.assigned_reps:
                assigned_reps_type_0_item = assigned_reps_type_0_item_data.to_dict()
                assigned_reps.append(assigned_reps_type_0_item)


        else:
            assigned_reps = self.assigned_reps

        care_status_id: None | str | Unset
        if isinstance(self.care_status_id, Unset):
            care_status_id = UNSET
        elif isinstance(self.care_status_id, UUID):
            care_status_id = str(self.care_status_id)
        else:
            care_status_id = self.care_status_id

        care_status_name: None | str | Unset
        if isinstance(self.care_status_name, Unset):
            care_status_name = UNSET
        else:
            care_status_name = self.care_status_name

        care_status_color: None | str | Unset
        if isinstance(self.care_status_color, Unset):
            care_status_color = UNSET
        else:
            care_status_color = self.care_status_color

        order_count: int | None | Unset
        if isinstance(self.order_count, Unset):
            order_count = UNSET
        else:
            order_count = self.order_count

        order_revenue: float | None | Unset
        if isinstance(self.order_revenue, Unset):
            order_revenue = UNSET
        else:
            order_revenue = self.order_revenue

        last_order_at: None | str | Unset
        if isinstance(self.last_order_at, Unset):
            last_order_at = UNSET
        elif isinstance(self.last_order_at, datetime.datetime):
            last_order_at = self.last_order_at.isoformat()
        else:
            last_order_at = self.last_order_at

        tax_code: None | str | Unset
        if isinstance(self.tax_code, Unset):
            tax_code = UNSET
        else:
            tax_code = self.tax_code

        duplicate_group: int | None | Unset
        if isinstance(self.duplicate_group, Unset):
            duplicate_group = UNSET
        else:
            duplicate_group = self.duplicate_group


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if outlet_code is not UNSET:
            field_dict["outletCode"] = outlet_code
        if outlet_name is not UNSET:
            field_dict["outletName"] = outlet_name
        if channel_code is not UNSET:
            field_dict["channelCode"] = channel_code
        if outlet_status is not UNSET:
            field_dict["outletStatus"] = outlet_status
        if gps_lat is not UNSET:
            field_dict["gpsLat"] = gps_lat
        if gps_lng is not UNSET:
            field_dict["gpsLng"] = gps_lng
        if address is not UNSET:
            field_dict["address"] = address
        if zone_id is not UNSET:
            field_dict["zoneId"] = zone_id
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id
        if visit_frequency is not UNSET:
            field_dict["visitFrequency"] = visit_frequency
        if owner_name is not UNSET:
            field_dict["ownerName"] = owner_name
        if owner_phone is not UNSET:
            field_dict["ownerPhone"] = owner_phone
        if owner_email is not UNSET:
            field_dict["ownerEmail"] = owner_email
        if last_checkin_at is not UNSET:
            field_dict["lastCheckinAt"] = last_checkin_at
        if assigned_rep_id is not UNSET:
            field_dict["assignedRepId"] = assigned_rep_id
        if assigned_rep_code is not UNSET:
            field_dict["assignedRepCode"] = assigned_rep_code
        if assigned_rep_name is not UNSET:
            field_dict["assignedRepName"] = assigned_rep_name
        if tier is not UNSET:
            field_dict["tier"] = tier
        if rank is not UNSET:
            field_dict["rank"] = rank
        if route_code is not UNSET:
            field_dict["routeCode"] = route_code
        if assigned_reps is not UNSET:
            field_dict["assignedReps"] = assigned_reps
        if care_status_id is not UNSET:
            field_dict["careStatusId"] = care_status_id
        if care_status_name is not UNSET:
            field_dict["careStatusName"] = care_status_name
        if care_status_color is not UNSET:
            field_dict["careStatusColor"] = care_status_color
        if order_count is not UNSET:
            field_dict["orderCount"] = order_count
        if order_revenue is not UNSET:
            field_dict["orderRevenue"] = order_revenue
        if last_order_at is not UNSET:
            field_dict["lastOrderAt"] = last_order_at
        if tax_code is not UNSET:
            field_dict["taxCode"] = tax_code
        if duplicate_group is not UNSET:
            field_dict["duplicateGroup"] = duplicate_group

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.outlet_assigned_rep_dto import OutletAssignedRepDto # noqa: PLC0415
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_outlet_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        outlet_code = _parse_outlet_code(d.pop("outletCode", UNSET))


        def _parse_outlet_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        outlet_name = _parse_outlet_name(d.pop("outletName", UNSET))


        def _parse_channel_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel_code = _parse_channel_code(d.pop("channelCode", UNSET))


        _outlet_status = d.pop("outletStatus", UNSET)
        outlet_status: OutletDtoOutletStatus | Unset
        if isinstance(_outlet_status,  Unset):
            outlet_status = UNSET
        else:
            outlet_status = check_outlet_dto_outlet_status(_outlet_status)




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


        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))


        def _parse_zone_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                zone_id_type_0 = UUID(data)



                return zone_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        zone_id = _parse_zone_id(d.pop("zoneId", UNSET))


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


        _visit_frequency = d.pop("visitFrequency", UNSET)
        visit_frequency: OutletDtoVisitFrequency | Unset
        if isinstance(_visit_frequency,  Unset):
            visit_frequency = UNSET
        else:
            visit_frequency = check_outlet_dto_visit_frequency(_visit_frequency)




        def _parse_owner_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_name = _parse_owner_name(d.pop("ownerName", UNSET))


        def _parse_owner_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_phone = _parse_owner_phone(d.pop("ownerPhone", UNSET))


        def _parse_owner_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_email = _parse_owner_email(d.pop("ownerEmail", UNSET))


        def _parse_last_checkin_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_checkin_at_type_0 = datetime.datetime.fromisoformat(data)



                return last_checkin_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_checkin_at = _parse_last_checkin_at(d.pop("lastCheckinAt", UNSET))


        def _parse_assigned_rep_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                assigned_rep_id_type_0 = UUID(data)



                return assigned_rep_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        assigned_rep_id = _parse_assigned_rep_id(d.pop("assignedRepId", UNSET))


        def _parse_assigned_rep_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assigned_rep_code = _parse_assigned_rep_code(d.pop("assignedRepCode", UNSET))


        def _parse_assigned_rep_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assigned_rep_name = _parse_assigned_rep_name(d.pop("assignedRepName", UNSET))


        def _parse_tier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tier = _parse_tier(d.pop("tier", UNSET))


        def _parse_rank(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rank = _parse_rank(d.pop("rank", UNSET))


        def _parse_route_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        route_code = _parse_route_code(d.pop("routeCode", UNSET))


        def _parse_assigned_reps(data: object) -> list[OutletAssignedRepDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assigned_reps_type_0 = []
                _assigned_reps_type_0 = data
                for assigned_reps_type_0_item_data in (_assigned_reps_type_0):
                    assigned_reps_type_0_item = OutletAssignedRepDto.from_dict(assigned_reps_type_0_item_data)



                    assigned_reps_type_0.append(assigned_reps_type_0_item)

                return assigned_reps_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OutletAssignedRepDto] | None | Unset, data)

        assigned_reps = _parse_assigned_reps(d.pop("assignedReps", UNSET))


        def _parse_care_status_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                care_status_id_type_0 = UUID(data)



                return care_status_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        care_status_id = _parse_care_status_id(d.pop("careStatusId", UNSET))


        def _parse_care_status_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        care_status_name = _parse_care_status_name(d.pop("careStatusName", UNSET))


        def _parse_care_status_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        care_status_color = _parse_care_status_color(d.pop("careStatusColor", UNSET))


        def _parse_order_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        order_count = _parse_order_count(d.pop("orderCount", UNSET))


        def _parse_order_revenue(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        order_revenue = _parse_order_revenue(d.pop("orderRevenue", UNSET))


        def _parse_last_order_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_order_at_type_0 = datetime.datetime.fromisoformat(data)



                return last_order_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_order_at = _parse_last_order_at(d.pop("lastOrderAt", UNSET))


        def _parse_tax_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tax_code = _parse_tax_code(d.pop("taxCode", UNSET))


        def _parse_duplicate_group(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duplicate_group = _parse_duplicate_group(d.pop("duplicateGroup", UNSET))


        outlet_dto = cls(
            id=id,
            outlet_code=outlet_code,
            outlet_name=outlet_name,
            channel_code=channel_code,
            outlet_status=outlet_status,
            gps_lat=gps_lat,
            gps_lng=gps_lng,
            address=address,
            zone_id=zone_id,
            branch_id=branch_id,
            visit_frequency=visit_frequency,
            owner_name=owner_name,
            owner_phone=owner_phone,
            owner_email=owner_email,
            last_checkin_at=last_checkin_at,
            assigned_rep_id=assigned_rep_id,
            assigned_rep_code=assigned_rep_code,
            assigned_rep_name=assigned_rep_name,
            tier=tier,
            rank=rank,
            route_code=route_code,
            assigned_reps=assigned_reps,
            care_status_id=care_status_id,
            care_status_name=care_status_name,
            care_status_color=care_status_color,
            order_count=order_count,
            order_revenue=order_revenue,
            last_order_at=last_order_at,
            tax_code=tax_code,
            duplicate_group=duplicate_group,
        )

        return outlet_dto


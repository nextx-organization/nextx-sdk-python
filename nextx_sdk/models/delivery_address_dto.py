from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="DeliveryAddressDto")



@_attrs_define
class DeliveryAddressDto:
    

    customer_address_id: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    address_line: None | str | Unset = UNSET
    province: None | str | Unset = UNSET
    province_code: None | str | Unset = UNSET
    district: None | str | Unset = UNSET
    district_code: None | str | Unset = UNSET
    ward: None | str | Unset = UNSET
    ward_code: None | str | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        customer_address_id: None | str | Unset
        if isinstance(self.customer_address_id, Unset):
            customer_address_id = UNSET
        elif isinstance(self.customer_address_id, UUID):
            customer_address_id = str(self.customer_address_id)
        else:
            customer_address_id = self.customer_address_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        address_line: None | str | Unset
        if isinstance(self.address_line, Unset):
            address_line = UNSET
        else:
            address_line = self.address_line

        province: None | str | Unset
        if isinstance(self.province, Unset):
            province = UNSET
        else:
            province = self.province

        province_code: None | str | Unset
        if isinstance(self.province_code, Unset):
            province_code = UNSET
        else:
            province_code = self.province_code

        district: None | str | Unset
        if isinstance(self.district, Unset):
            district = UNSET
        else:
            district = self.district

        district_code: None | str | Unset
        if isinstance(self.district_code, Unset):
            district_code = UNSET
        else:
            district_code = self.district_code

        ward: None | str | Unset
        if isinstance(self.ward, Unset):
            ward = UNSET
        else:
            ward = self.ward

        ward_code: None | str | Unset
        if isinstance(self.ward_code, Unset):
            ward_code = UNSET
        else:
            ward_code = self.ward_code

        latitude: float | None | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: float | None | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if customer_address_id is not UNSET:
            field_dict["customerAddressId"] = customer_address_id
        if name is not UNSET:
            field_dict["name"] = name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if address_line is not UNSET:
            field_dict["addressLine"] = address_line
        if province is not UNSET:
            field_dict["province"] = province
        if province_code is not UNSET:
            field_dict["provinceCode"] = province_code
        if district is not UNSET:
            field_dict["district"] = district
        if district_code is not UNSET:
            field_dict["districtCode"] = district_code
        if ward is not UNSET:
            field_dict["ward"] = ward
        if ward_code is not UNSET:
            field_dict["wardCode"] = ward_code
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_customer_address_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                customer_address_id_type_0 = UUID(data)



                return customer_address_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        customer_address_id = _parse_customer_address_id(d.pop("customerAddressId", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))


        def _parse_address_line(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_line = _parse_address_line(d.pop("addressLine", UNSET))


        def _parse_province(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        province = _parse_province(d.pop("province", UNSET))


        def _parse_province_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        province_code = _parse_province_code(d.pop("provinceCode", UNSET))


        def _parse_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district = _parse_district(d.pop("district", UNSET))


        def _parse_district_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_code = _parse_district_code(d.pop("districtCode", UNSET))


        def _parse_ward(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ward = _parse_ward(d.pop("ward", UNSET))


        def _parse_ward_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ward_code = _parse_ward_code(d.pop("wardCode", UNSET))


        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))


        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))


        delivery_address_dto = cls(
            customer_address_id=customer_address_id,
            name=name,
            phone=phone,
            address_line=address_line,
            province=province,
            province_code=province_code,
            district=district,
            district_code=district_code,
            ward=ward,
            ward_code=ward_code,
            latitude=latitude,
            longitude=longitude,
        )

        return delivery_address_dto


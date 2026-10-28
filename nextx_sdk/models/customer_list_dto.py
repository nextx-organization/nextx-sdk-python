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

if TYPE_CHECKING:
  from ..models.customer_list_dto_custom_fields_type_0 import CustomerListDtoCustomFieldsType0





T = TypeVar("T", bound="CustomerListDto")



@_attrs_define
class CustomerListDto:
    

    id: UUID | Unset = UNSET
    customer_code: None | str | Unset = UNSET
    crm_contact_id: UUID | Unset = UNSET
    full_name: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    customer_type: None | str | Unset = UNSET
    customer_group_id: None | Unset | UUID = UNSET
    customer_group_name: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    total_debt: float | Unset = UNSET
    debt_limit: float | Unset = UNSET
    total_orders: int | Unset = UNSET
    total_revenue: float | Unset = UNSET
    total_purchase: float | Unset = UNSET
    last_order_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    avatar_key: None | str | Unset = UNSET
    avatar_url: None | str | Unset = UNSET
    price_list_id_override: None | Unset | UUID = UNSET
    total_points: int | Unset = UNSET
    gym_member_code: None | str | Unset = UNSET
    assigned_to: None | Unset | UUID = UNSET
    assigned_to_name: None | str | Unset = UNSET
    custom_fields: CustomerListDtoCustomFieldsType0 | None | Unset = UNSET
    notes: None | str | Unset = UNSET
    debt_days: int | None | Unset = UNSET
    linked_supplier_id: None | Unset | UUID = UNSET
    address: None | str | Unset = UNSET
    advance_remaining: float | Unset = UNSET
    net_debt: float | Unset = UNSET
    branch_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.customer_list_dto_custom_fields_type_0 import CustomerListDtoCustomFieldsType0 # noqa: PLC0415
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        customer_code: None | str | Unset
        if isinstance(self.customer_code, Unset):
            customer_code = UNSET
        else:
            customer_code = self.customer_code

        crm_contact_id: str | Unset = UNSET
        if not isinstance(self.crm_contact_id, Unset):
            crm_contact_id = str(self.crm_contact_id)

        full_name: None | str | Unset
        if isinstance(self.full_name, Unset):
            full_name = UNSET
        else:
            full_name = self.full_name

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        customer_type: None | str | Unset
        if isinstance(self.customer_type, Unset):
            customer_type = UNSET
        else:
            customer_type = self.customer_type

        customer_group_id: None | str | Unset
        if isinstance(self.customer_group_id, Unset):
            customer_group_id = UNSET
        elif isinstance(self.customer_group_id, UUID):
            customer_group_id = str(self.customer_group_id)
        else:
            customer_group_id = self.customer_group_id

        customer_group_name: None | str | Unset
        if isinstance(self.customer_group_name, Unset):
            customer_group_name = UNSET
        else:
            customer_group_name = self.customer_group_name

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        total_debt = self.total_debt

        debt_limit = self.debt_limit

        total_orders = self.total_orders

        total_revenue = self.total_revenue

        total_purchase = self.total_purchase

        last_order_at: None | str | Unset
        if isinstance(self.last_order_at, Unset):
            last_order_at = UNSET
        elif isinstance(self.last_order_at, datetime.datetime):
            last_order_at = self.last_order_at.isoformat()
        else:
            last_order_at = self.last_order_at

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        avatar_key: None | str | Unset
        if isinstance(self.avatar_key, Unset):
            avatar_key = UNSET
        else:
            avatar_key = self.avatar_key

        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        price_list_id_override: None | str | Unset
        if isinstance(self.price_list_id_override, Unset):
            price_list_id_override = UNSET
        elif isinstance(self.price_list_id_override, UUID):
            price_list_id_override = str(self.price_list_id_override)
        else:
            price_list_id_override = self.price_list_id_override

        total_points = self.total_points

        gym_member_code: None | str | Unset
        if isinstance(self.gym_member_code, Unset):
            gym_member_code = UNSET
        else:
            gym_member_code = self.gym_member_code

        assigned_to: None | str | Unset
        if isinstance(self.assigned_to, Unset):
            assigned_to = UNSET
        elif isinstance(self.assigned_to, UUID):
            assigned_to = str(self.assigned_to)
        else:
            assigned_to = self.assigned_to

        assigned_to_name: None | str | Unset
        if isinstance(self.assigned_to_name, Unset):
            assigned_to_name = UNSET
        else:
            assigned_to_name = self.assigned_to_name

        custom_fields: dict[str, Any] | None | Unset
        if isinstance(self.custom_fields, Unset):
            custom_fields = UNSET
        elif isinstance(self.custom_fields, CustomerListDtoCustomFieldsType0):
            custom_fields = self.custom_fields.to_dict()
        else:
            custom_fields = self.custom_fields

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        debt_days: int | None | Unset
        if isinstance(self.debt_days, Unset):
            debt_days = UNSET
        else:
            debt_days = self.debt_days

        linked_supplier_id: None | str | Unset
        if isinstance(self.linked_supplier_id, Unset):
            linked_supplier_id = UNSET
        elif isinstance(self.linked_supplier_id, UUID):
            linked_supplier_id = str(self.linked_supplier_id)
        else:
            linked_supplier_id = self.linked_supplier_id

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        advance_remaining = self.advance_remaining

        net_debt = self.net_debt

        branch_id: None | str | Unset
        if isinstance(self.branch_id, Unset):
            branch_id = UNSET
        elif isinstance(self.branch_id, UUID):
            branch_id = str(self.branch_id)
        else:
            branch_id = self.branch_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if customer_code is not UNSET:
            field_dict["customerCode"] = customer_code
        if crm_contact_id is not UNSET:
            field_dict["crmContactId"] = crm_contact_id
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if email is not UNSET:
            field_dict["email"] = email
        if customer_type is not UNSET:
            field_dict["customerType"] = customer_type
        if customer_group_id is not UNSET:
            field_dict["customerGroupId"] = customer_group_id
        if customer_group_name is not UNSET:
            field_dict["customerGroupName"] = customer_group_name
        if status is not UNSET:
            field_dict["status"] = status
        if total_debt is not UNSET:
            field_dict["totalDebt"] = total_debt
        if debt_limit is not UNSET:
            field_dict["debtLimit"] = debt_limit
        if total_orders is not UNSET:
            field_dict["totalOrders"] = total_orders
        if total_revenue is not UNSET:
            field_dict["totalRevenue"] = total_revenue
        if total_purchase is not UNSET:
            field_dict["totalPurchase"] = total_purchase
        if last_order_at is not UNSET:
            field_dict["lastOrderAt"] = last_order_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if avatar_key is not UNSET:
            field_dict["avatarKey"] = avatar_key
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if price_list_id_override is not UNSET:
            field_dict["priceListIdOverride"] = price_list_id_override
        if total_points is not UNSET:
            field_dict["totalPoints"] = total_points
        if gym_member_code is not UNSET:
            field_dict["gymMemberCode"] = gym_member_code
        if assigned_to is not UNSET:
            field_dict["assignedTo"] = assigned_to
        if assigned_to_name is not UNSET:
            field_dict["assignedToName"] = assigned_to_name
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if notes is not UNSET:
            field_dict["notes"] = notes
        if debt_days is not UNSET:
            field_dict["debtDays"] = debt_days
        if linked_supplier_id is not UNSET:
            field_dict["linkedSupplierId"] = linked_supplier_id
        if address is not UNSET:
            field_dict["address"] = address
        if advance_remaining is not UNSET:
            field_dict["advanceRemaining"] = advance_remaining
        if net_debt is not UNSET:
            field_dict["netDebt"] = net_debt
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.customer_list_dto_custom_fields_type_0 import CustomerListDtoCustomFieldsType0 # noqa: PLC0415
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_customer_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_code = _parse_customer_code(d.pop("customerCode", UNSET))


        _crm_contact_id = d.pop("crmContactId", UNSET)
        crm_contact_id: UUID | Unset
        if isinstance(_crm_contact_id,  Unset):
            crm_contact_id = UNSET
        else:
            crm_contact_id = UUID(_crm_contact_id)




        def _parse_full_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        full_name = _parse_full_name(d.pop("fullName", UNSET))


        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))


        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))


        def _parse_customer_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_type = _parse_customer_type(d.pop("customerType", UNSET))


        def _parse_customer_group_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                customer_group_id_type_0 = UUID(data)



                return customer_group_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        customer_group_id = _parse_customer_group_id(d.pop("customerGroupId", UNSET))


        def _parse_customer_group_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_group_name = _parse_customer_group_name(d.pop("customerGroupName", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        total_debt = d.pop("totalDebt", UNSET)

        debt_limit = d.pop("debtLimit", UNSET)

        total_orders = d.pop("totalOrders", UNSET)

        total_revenue = d.pop("totalRevenue", UNSET)

        total_purchase = d.pop("totalPurchase", UNSET)

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


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_avatar_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_key = _parse_avatar_key(d.pop("avatarKey", UNSET))


        def _parse_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url = _parse_avatar_url(d.pop("avatarUrl", UNSET))


        def _parse_price_list_id_override(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                price_list_id_override_type_0 = UUID(data)



                return price_list_id_override_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        price_list_id_override = _parse_price_list_id_override(d.pop("priceListIdOverride", UNSET))


        total_points = d.pop("totalPoints", UNSET)

        def _parse_gym_member_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gym_member_code = _parse_gym_member_code(d.pop("gymMemberCode", UNSET))


        def _parse_assigned_to(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                assigned_to_type_0 = UUID(data)



                return assigned_to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        assigned_to = _parse_assigned_to(d.pop("assignedTo", UNSET))


        def _parse_assigned_to_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assigned_to_name = _parse_assigned_to_name(d.pop("assignedToName", UNSET))


        def _parse_custom_fields(data: object) -> CustomerListDtoCustomFieldsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_fields_type_0 = CustomerListDtoCustomFieldsType0.from_dict(data)



                return custom_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CustomerListDtoCustomFieldsType0 | None | Unset, data)

        custom_fields = _parse_custom_fields(d.pop("customFields", UNSET))


        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


        def _parse_debt_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        debt_days = _parse_debt_days(d.pop("debtDays", UNSET))


        def _parse_linked_supplier_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                linked_supplier_id_type_0 = UUID(data)



                return linked_supplier_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        linked_supplier_id = _parse_linked_supplier_id(d.pop("linkedSupplierId", UNSET))


        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))


        advance_remaining = d.pop("advanceRemaining", UNSET)

        net_debt = d.pop("netDebt", UNSET)

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


        customer_list_dto = cls(
            id=id,
            customer_code=customer_code,
            crm_contact_id=crm_contact_id,
            full_name=full_name,
            phone=phone,
            email=email,
            customer_type=customer_type,
            customer_group_id=customer_group_id,
            customer_group_name=customer_group_name,
            status=status,
            total_debt=total_debt,
            debt_limit=debt_limit,
            total_orders=total_orders,
            total_revenue=total_revenue,
            total_purchase=total_purchase,
            last_order_at=last_order_at,
            created_at=created_at,
            avatar_key=avatar_key,
            avatar_url=avatar_url,
            price_list_id_override=price_list_id_override,
            total_points=total_points,
            gym_member_code=gym_member_code,
            assigned_to=assigned_to,
            assigned_to_name=assigned_to_name,
            custom_fields=custom_fields,
            notes=notes,
            debt_days=debt_days,
            linked_supplier_id=linked_supplier_id,
            address=address,
            advance_remaining=advance_remaining,
            net_debt=net_debt,
            branch_id=branch_id,
        )

        return customer_list_dto


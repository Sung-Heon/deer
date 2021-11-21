from ..extra_charge_policy.extra_charge_policy_interface import BaseExtraCharge
from ..dto import UserDTO
from ..const import OUTSIDE_CHARGE, FORBIDDEN_DISTRICT_CHARGE
from ...models import Area, ForbiddenArea
from django.contrib.gis.geos import Point


class OutsideDistrictExtraCharge(BaseExtraCharge):
    def calculate_extra_charge_amount(self, user: UserDTO):
        user_coords = Point(user.use_end_lat, user.use_end_lng)
        distance_extra_charge = user_coords.distance(self.area.boundary)
        self.extra_charge_amount = distance_extra_charge * OUTSIDE_CHARGE
        return self.extra_charge_amount

    def calculate_after_extra_charge(self, user: UserDTO, before_fare: int):
        return before_fare + self.calculate_extra_charge_amount(self, user)

    def policy_check(self, user: UserDTO) -> bool:
        user_coods = Point(user.use_end_lat, user.use_end_lng)
        area = Area.objects.get(id=user.use_deer.area_id)
        if not user_coods.within(area.boundary):
            self.area = area
            return True
        return False

    def get_name(self):
        return "구역 밖 주차 추가요금"


class ForbiddenDistrictExtraCharge(BaseExtraCharge):
    def calculate_extra_charge_amount(self):
        return FORBIDDEN_DISTRICT_CHARGE

    def calculate_after_extra_charge(self, user: UserDTO, before_fare: int):
        return before_fare + self.calculate_extra_charge_amount(self)

    def policy_check(self, user: UserDTO) -> bool:
        user_coods = Point(user.use_end_lat, user.use_end_lng)
        forbidden_area_list = ForbiddenArea.objects.filter(area_id=user.use_deer.area_id)
        for forbidden in forbidden_area_list:
            if user_coods.within(forbidden.boundary):
                return True
        return False

    def get_name(self):
        return "금지구역 주차 추가요금"

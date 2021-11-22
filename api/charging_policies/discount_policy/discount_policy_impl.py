from ..discount_policy.discount_policy_interface import BaseDiscount
from ..dto import UserDTO
from ..const import PARKING_ZONE_DISCOUNT_RATE, base_policy_const, REUSE_TIMEDELTA
from ...models import ParkingZone, UserRecords
from django.contrib.gis.geos import Point
from geopy import distance


class ParkingZoneDiscount(BaseDiscount):

    def calculate_discount_amount(self, user: UserDTO) -> int:
        minute = str(user.use_end_at - user.use_start_at).split(":")[1]
        before_discount = self.basic_rate + self.per_minute_rate * (int(minute))
        self.discount_amount = ((before_discount * PARKING_ZONE_DISCOUNT_RATE)//10) *10
        return int(self.discount_amount)

    def calculate_after_discount(self, user: UserDTO, before_fare) -> int:
        return before_fare - self.calculate_discount_amount(self, user)

    def policy_check(self, user: UserDTO) -> bool:
        parkingzones = ParkingZone.objects.filter(id=user.use_deer.area_id)
        user_coods = Point(user.use_end_lat, user.use_end_lng)
        for parkingzone in parkingzones:
            parkingzone_coods = parkingzone.center_lat_lng
            if distance.distance(parkingzone_coods, user_coods).m < parkingzone.radius:
                self.basic_rate = base_policy_const[user.use_deer.area_id]["basic_rate"]
                self.per_minute_rate = base_policy_const[user.use_deer.area_id]["per_minute_rate"]
                return True
        return False

    def get_name(self):
        return "parkingzone 할인"


class EarlyReuseDiscount(BaseDiscount):

    def calculate_discount_amount(self, user: UserDTO) -> int:
        return self.basic_rate

    def calculate_after_discount(self, user: UserDTO, before_fare: int) -> int:
        return before_fare - self.calculate_discount_amount(self, user)

    def policy_check(self, user: UserDTO) -> bool:
        if user.use_start_at.replace(tzinfo=None) - UserRecords.objects.filter(user_id=user.user_id).latest("end_at").end_at.replace(tzinfo=None) < REUSE_TIMEDELTA:
            self.basic_rate = base_policy_const[1]["basic_rate"]
            self.per_minute_rate = base_policy_const[1]["per_minute_rate"]
            return True
        return False

    def get_name(self):
        return "규정시간내 재이용 할인 "
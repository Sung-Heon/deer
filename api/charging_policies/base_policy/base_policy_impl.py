from .base_policy_interface import BasePricing
from ..dto import UserDTO

from ...models import User
from ..const import base_policy_const


class BasePricingImplement(BasePricing):
    """기본요금제 구현체"""
    def base_price_setting(self, deer_area_id: int):
        self.basic_rate = base_policy_const[deer_area_id]["basic_rate"]
        self.per_minute_rate = base_policy_const[deer_area_id]["per_minute_rate"]

    def calculate_fee(self, minute) -> int:
        minute = str(minute).split(":")[1]
        minute = int(minute)
        return self.basic_rate + minute * self.per_minute_rate

    def policy_check(self, user_dto: UserDTO) -> bool:
        if User.objects.get(id=user_dto.user_id).base_pricing_id == 1:
            return True
        return False

    def get_name(self):
        return f"{self.basic_rate}: 기본 요금, {self.per_minute_rate}: 분당 요금의 기본요금제"
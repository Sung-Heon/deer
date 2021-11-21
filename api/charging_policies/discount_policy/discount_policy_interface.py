from abc import ABC, abstractmethod
from ..dto import UserDTO


class BaseDiscount(ABC):

    @property
    def basic_rate(self):
        return self._basic_rate

    @basic_rate.setter
    def basic_rate(self, new_basic_rate):
        self._basic_rate = new_basic_rate

    @property
    def per_minute_rate(self):
        return self._per_minute_rate

    @per_minute_rate.setter
    def per_minute_rate(self,new_per_minute_rate):
        self._per_minute_rate =new_per_minute_rate

    @abstractmethod
    def calculate_discount_amount(self, user):
        pass

    @abstractmethod
    def calculate_after_discount(self, user: UserDTO, before_fare: int):
        pass

    @abstractmethod
    def policy_check(self, user: UserDTO):
        pass


    @abstractmethod
    def get_name(self):
        pass
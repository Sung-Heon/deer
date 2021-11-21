from abc import ABC, abstractmethod



class BasePricing(ABC):

    @property
    def basic_rate(self):
        return self._basic_rate

    @basic_rate.setter
    def basic_rate(self, new_basic_rate: int):
        self._basic_rate = new_basic_rate

    @property
    def per_minute_rate(self):
        return self._per_minute_rate

    @per_minute_rate.setter
    def per_minute_rate(self, new_per_minute_rate: int):
        self._per_minute_rate =new_per_minute_rate


    @abstractmethod
    def base_price_setting(self):
        pass

    @abstractmethod
    def calculate_fee(self, minute):
        pass

    @abstractmethod
    def get_name(self):
        pass
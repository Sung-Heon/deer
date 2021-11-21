from abc import ABC, abstractmethod


class BaseException(ABC):

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
    def per_minute_rate(self, new_per_minute_rate):
        self._per_minute_rate = new_per_minute_rate

    @abstractmethod
    def calculate_exception_change_amount(self):
        pass

    @abstractmethod
    def calculate_exception(self, before_fare):
        pass

    @abstractmethod
    def get_name(self):
        pass
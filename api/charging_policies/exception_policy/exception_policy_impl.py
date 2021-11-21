from ..const import EXCEPTION_TIMEDELTA
from ..exception_policy.exception_policy_interface import BaseException
from ..dto import UserDTO

class QuickReturnException(BaseException):

    def calculate_exception_change_amount(self, user:UserDTO, before_fare: int):
        return before_fare


    def calculate_exception(self, user:UserDTO, before_fare: int):
        return before_fare- self.calculate_exception_change_amount(self,user, before_fare)

    def policy_check(self, user: UserDTO) -> bool:
        if user.use_end_at - user.use_start_at < EXCEPTION_TIMEDELTA:
            return True
        return False

    def get_name(self):
        return "1분내 반납 예외"
import inspect
from functools import wraps
from typing import List



def inject_for_policy_check(func):

    from ..policy_checker.policy_checker_impl import PolicyCheckerImplement
    from ..policy_checker.policy_checker_interface import PolicyChecker
    from ..discount_policy.discount_policy_impl import ParkingZoneDiscount, EarlyReuseDiscount
    from ..discount_policy.discount_policy_interface import BaseDiscount
    from ..extra_charge_policy.extra_charge_policy_interface import BaseExtraCharge
    from ..extra_charge_policy.extra_charge_policy_impl import OutsideDistrictExtraCharge
    from ..extra_charge_policy.extra_charge_policy_impl import ForbiddenDistrictExtraCharge
    from ..exception_policy.exception_policy_interface import BaseException
    from ..exception_policy.exception_policy_impl import QuickReturnException

    from ..base_policy.base_policy_interface import BasePricing
    from ..base_policy.base_policy_impl import BasePricingImplement
    providers = {
        PolicyChecker: PolicyCheckerImplement,
        List[BaseDiscount]: [EarlyReuseDiscount , ParkingZoneDiscount],
        List[BaseExtraCharge] : [OutsideDistrictExtraCharge, ForbiddenDistrictExtraCharge],
        List[BaseException] : [QuickReturnException],
        List[BasePricing] : [BasePricingImplement]
    }

    @wraps(func)
    def wrapper(*args, **kwargs):
        annotations = inspect.getfullargspec(func).annotations
        for k, v in annotations.items():
            if v in providers:
                kwargs[k] = providers[v]

        return func(*args, **kwargs)

    return wrapper


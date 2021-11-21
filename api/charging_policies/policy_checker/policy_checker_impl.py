from ..policy_checker.policy_checker_interface import PolicyChecker
from ..dto import UserDTO

class PolicyCheckerImplement(PolicyChecker):
    def __init__(self, base_discounts):
        self.discount_policies = base_discounts


    def policy_check(self, user:UserDTO):
        discount_policy_for_user = []
        for policy in self.discount_policies:
            if policy.policy_check(policy, user):
                discount_policy_for_user.append(policy)

        return discount_policy_for_user
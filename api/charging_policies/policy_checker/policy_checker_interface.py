from abc import ABC, abstractmethod


class PolicyChecker(ABC):
    @abstractmethod
    def policy_check(self):
        pass
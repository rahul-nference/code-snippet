class ShippingCostCalculator:
    def __init__(self, type):
        self._type = type

    def calculate(self, order):
        if self._type == 'UPS':
            return order.weight * 1.0
        elif self._type == 'FedEx':
            return order.weight * 1.5
        else:
            return order.weight * 2.0
# can you guess what principle does this violate?


# better way to do this

from abc import ABC, abstractmethod

class ShippingCostStrategy(ABC):
    @abstractmethod
    def calculate(self, order):
        pass

class UPSStrategy(ShippingCostStrategy):
    def calculate(self, order):
        return order.weight * 1.0

class FedExStrategy(ShippingCostStrategy):
    def calculate(self, order):
        return order.weight * 1.5

class ShippingCostCalculator:
    def __init__(self, strategy: ShippingCostStrategy):
        self._strategy = strategy

    def calculate(self, order):
        return self._strategy.calculate(order)
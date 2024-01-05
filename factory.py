# Using factory method
from abc import ABC, abstractmethod

class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        pass

class CheesePizza(Pizza):
    def prepare(self):
        print("Preparing cheese pizza")

class PepperoniPizza(Pizza):
    def prepare(self):
        print("Preparing pepperoni pizza")


# Without factory method
class PizzaStore:
    def order_pizza(self, type):
        if type == 'cheese':
            return CheesePizza().prepare()
        elif type == 'pepperoni':
            return PepperoniPizza().prepare()
        else:
            return None
        

# with factory method
class PizzaFactory:
    def create_pizza(self, type):
        if type == 'cheese':
            return CheesePizza()
        elif type == 'pepperoni':
            return PepperoniPizza()
        else:
            return None

class PizzaStore:
    def __init__(self):
        self.factory = PizzaFactory()

    def order_pizza(self, type):
        pizza = self.factory.create_pizza(type)
        if pizza is not None:
            pizza.prepare()
        return pizza
    
#######################################################
# Bonus: abstract factory
from abc import ABC, abstractmethod

class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        pass

class NyCheesePizza(Pizza):
    def prepare(self):
        print("Preparing cheese pizza")

class NyPepperoniPizza(Pizza):
    def prepare(self):
        print("Preparing pepperoni pizza")
# and so on .....
class PizzaFactory(ABC):
    @abstractmethod
    def create_pizza(self, type):
        pass

class NewYorkPizzaFactory(PizzaFactory):
    def create_pizza(self, type):
        if type == 'cheese':
            return NyCheesePizza()
        elif type == 'pepperoni':
            return NyPepperoniPizza()
        else:
            return None

class ChicagoPizzaFactory(PizzaFactory):
    def create_pizza(self, type):
        if type == 'cheese':
            return ChicagoCheesePizza()
        elif type == 'pepperoni':
            return ChicagoPepperoniPizza()
        else:
            return None

class PizzaStore:
    def __init__(self, factory):
        self.factory = factory

    def order_pizza(self, type):
        pizza = self.factory.create_pizza(type)
        pizza.prepare()

new_york_store = PizzaStore(NewYorkPizzaFactory())
new_york_store.order_pizza('cheese')

chicago_store = PizzaStore(ChicagoPizzaFactory())
chicago_store.order_pizza('pepperoni')
    
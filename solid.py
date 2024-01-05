# SINGLE RESPONSIBILITY PRINCIPLE
# A class should have only one reason to change

# Violation
class User:
    def get_user(self, id):
        pass

    def save_user_details(self, user):
        pass

# Good
class User:
    def get_user(self, id):
        pass

class UserDB:
    def save_user_details(self, user):
        pass

#######################################################
# Open/Closed Principle
# code should be open for extension but closed for modification


# Violates Open/Closed Principle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class AreaCalculator:
    def calculate_rectangle_area(self, rectangle):
        return rectangle.width * rectangle.height # what happens if we add a circle class?
    


# Adheres to Open/Closed Principle
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

class AreaCalculator:
    def calculate(self, shape):
        return shape.area()


#######################################################
"""
The LSP states that 
'if S is a subtype of T, then objects of type T may be replaced with objects of type S
 without altering any of the desirable properties of the program'. 
 This means that a subclass should be able to do everything that its superclass can do.
 """
# Violates Liskov Substitution Principle
class Bird:
    def make_sound(self):
        pass

    def fly(self):
        pass

class Ostrich(Bird):
    def make_sound(self):
        print("Kweh")

    def fly(self):
        raise NotImplementedError("Ostriches can't fly")
    
# Adheres to Liskov Substitution Principle
class Bird:
    def make_sound(self):
        pass

class FlyingBird(Bird):
    def fly(self):
        pass

class Ostrich(Bird):
    pass


#######################################################
# Interface Segregation Principle (ISP): Clients should not be forced to depend on interfaces they do not use. 
# This means that a class should not have to implement methods it doesn't use.

# Violates Interface Segregation Principle
class Worker:
    def work(self):
        pass

    def eat(self):
        pass

class Human(Worker):
    def work(self):
        print("Human is working")

    def eat(self):
        print("Human is eating")

class Robot(Worker):
    def work(self):
        print("Robot is working")

    def eat(self):
        raise NotImplementedError("Robots can't eat")

# Adheres to Interface Segregation Principle
class Worker:
    def work(self):
        pass

class Eater:
    def eat(self):
        pass

class Human(Worker, Eater):
    def work(self):
        print("Human is working")

    def eat(self):
        print("Human is eating")

class Robot(Worker):
    def work(self):
        print("Robot is working")

#######################################################
# The Dependency Inversion Principle (DIP) states that high-level modules should not depend on low-level modules, 
# both should depend on abstractions. 
# Abstractions should not depend on details. Details should depend on abstractions.
        
# Violates Dependency Inversion Principle
class LightBulb:
    def turn_on(self):
        print("LightBulb: Bulb turned on...")

    def turn_off(self):
        print("LightBulb: Bulb turned off...")

class ElectricPowerSwitch:
    def __init__(self, light_bulb):
        self.light_bulb = light_bulb
        self.on = False

    def press(self):
        if self.on:
            self.light_bulb.turn_off()
            self.on = False
        else:
            self.light_bulb.turn_on()
            self.on = True

# Adheres to Dependency Inversion Principle
from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: Bulb turned on...")

    def turn_off(self):
        print("LightBulb: Bulb turned off...")

class ElectricPowerSwitch:
    def __init__(self, device):
        self.device = device
        self.on = False

    def press(self):
        if self.on:
            self.device.turn_off()
            self.on = False
        else:
            self.device.turn_on()
            self.on = True
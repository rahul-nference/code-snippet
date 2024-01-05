from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, temperature):
        pass

class AndroidDisplayElement(Observer):
    def update(self, temperature):
        print(f"Current temperature is {temperature}")

class AppleDisplayElement(Observer):
    def update(self, temperature):
        print(f"Current temperature is {temperature}")

class WeatherStation:
    def __init__(self):
        self.observers = []
        self.temperature = 0

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature)

    def set_temperature(self, temperature):
        self.temperature = temperature
        self.notify_observers()
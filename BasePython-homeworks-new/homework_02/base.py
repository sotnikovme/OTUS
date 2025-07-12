from abc import ABC
import exceptions

class Vehicle(ABC):
    weight = 1000
    started = None
    fuel = 0
    fuel_consumption = 40
    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def move(self, fuel, fuel_consumption):
        if self.fuel >= self.fuel_consumption:
            self.fuel -= self.fuel_consumption
        else:
            self.fuel += 40

    def start(self, started, fuel):
        try:
            if not self.started:
                if self.fuel > 0:
                    started = True
            else:
                if self.fuel > 0:
                    self.move()
        except:
               exceptions.LowFuelError()

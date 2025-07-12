from abc import ABC
import exceptions

class Vehicle(ABC):
    weight = 1000
    started = None
    fuel = 40
    fuel_consumption = 5
    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def move(self, dist):
        if self.fuel >= self.fuel_consumption * dist:
            raise exceptions.NotEnoughFuel
            self.fuel += 10
            print("NotEnoughFuel")
        else:
            self.fuel -= self.fuel_consumption * dist

    def start(self, started, fuel):
        if self.started != True:
            if self.fuel > 0:
                self.started = True

            else:
                raise exceptions.LowFuelError
                print('LowFuelError')
        return self
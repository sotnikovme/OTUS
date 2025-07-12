"""
создайте класс `Plane`, наследник `Vehicle`
"""
from base import Vehicle
from exceptions import CargoOverload
# from testing.test_homework_02.test_base import exceptions


class Plane(Vehicle):
    cargo = 10_000
    max_cargo = 15_000
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(self, weight, fuel, fuel_consumption)
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.max_cargo = max_cargo
    def load_cargo(self):
        if self.cargo > self.max_cargo:
            raise CargoOverload
        else:
            Vehicle.start()

    def remove_all_cargo(self):
        self.cargo = 10_000
        return self.cargo
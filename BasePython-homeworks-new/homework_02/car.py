"""
создайте класс `Car`, наследник `Vehicle`
"""
from base import Vehicle
from engine import Engin

class Car(Vehicle):
    engine = None
    def __init__(self, weight, fuel, fuel_consumption):
        super().__init__(self, weight, fuel, fuel_consumption)

    def set_engine(self):
        self.engine = Engin(volume=3, piston=6)

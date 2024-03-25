"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0, max_cargo=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, value):
        current_cargo = value + self.cargo
        if current_cargo <= self.max_cargo:
            self.cargo = current_cargo
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        result = self.cargo
        self.cargo = 0
        return result




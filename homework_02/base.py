from abc import ABC
from exceptions import LowFuelError
from exceptions import NotEnoughtFuel


class Vehicle(ABC):
    def __init__(self,weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance):
        waisted = distance * self.fuel_consumption
        if self.fuel >= waisted:
            self.fuel -= waisted
        else:
            raise NotEnoughtFuel




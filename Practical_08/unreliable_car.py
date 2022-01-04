"""
Practical 8: Question 2A
unreliable_car.py
UnreliableCar class
"""

from car import Car
import random

MINIMUM_THRESHOLD = 0
MAXIMUM_THRESHOLD = 100


class UnreliableCar(Car):
    """Represent an UnreliableCar object, a specialized version of a Car object that includes varying reliability."""

    def __init__(self, name, fuel, reliability):
        """
        Initialize an UnreliableCar instance,
        based on parent class Car.
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """
        Drive the UnreliableCar the same way as the Car,
        but also take account the unreliability threshold as well.
        """
        unreliability_threshold = random.uniform(MINIMUM_THRESHOLD, MAXIMUM_THRESHOLD)
        distance_driven = 0
        if unreliability_threshold < self.reliability:
            distance_driven = super().drive(distance)
        return distance_driven

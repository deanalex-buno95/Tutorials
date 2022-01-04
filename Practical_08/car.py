"""
Practical 8: Question 1A
car.py
Car class
"""


class Car:
    """Represent a Car object."""

    def __init__(self, name="Car", fuel=0):
        """
        Initialise a Car.
        """
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def add_fuel(self, amount):
        """
        Add amount to the car's fuel.
        """
        self.fuel += amount

    def drive(self, distance):
        """
        Drive the Car a given distance.
        Drive given distance if Car has enough fuel,
        or drive until the fuel runs out and return the distance actually driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance

    def __str__(self):
        """
        Display Car information.
        """
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"

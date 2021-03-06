"""
Practical 8: Question 1B
taxi.py
Taxi class
"""

from car import Car


class Taxi(Car):
    """Represent a Taxi object, a specialized version of a Car object that includes fare costs. """
    price_per_km = 1.23

    def __init__(self, name, fuel):
        """
        Initialize a Taxi instance,
        based on parent class Car.
        """
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def get_fare(self):
        """
        Return the price for the Taxi trip.
        """
        return round(self.price_per_km * self.current_fare_distance, 1)

    def start_fare(self):
        """
        Begin a new fare.
        """
        self.current_fare_distance = 0

    def drive(self, distance):
        """
        Drive the Taxi the same way as the Car,
        but also calculate the fare distance as well.
        """
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven

    def __str__(self):
        """
        Display Taxi information just like Car,
        but with the current fare distance.
        """
        return "{}, {}km on current fare, ${:.2f}/km".format(super().__str__(),
                                                             self.current_fare_distance,
                                                             self.price_per_km)

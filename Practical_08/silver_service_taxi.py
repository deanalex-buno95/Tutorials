"""
Practical 8, Question 3A
silver_service_taxi.py
SilverServiceTaxi class
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi object, a specialized version of a Taxi object that includes fanciness."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """
        Initialize a SilverServiceTaxi instance,
        based on parent class Taxi.
        """
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= self.fanciness

    def get_fare(self):
        """
        Return the price for the SilverServiceTaxi trip.
        """
        return super().get_fare() + self.flagfall

    def __str__(self):
        """
        Display SilverServiceTaxi information just like Taxi,
        but with the flag fall.
        """
        return "{} plus flag fall of ${:.2f}".format(super().__str__(), self.flagfall)

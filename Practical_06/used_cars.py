"""
Practical 6: Question 1B
used_cars.py
"""


# MODULES
from Practical_06.car import Car

# CONSTANTS
BORDER = "—" * 150


"""
PROGRAM
"""


def main():
    """Demo test code to show how to use car class."""
    print(BORDER)
    print("Practical 6: Question 1\ncar.py & used_cars.py")
    print(BORDER)
    print("Original:")
    my_car = Car(180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)
    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))
    print(BORDER)
    print("My modifications:")
    limo = Car(100)  # `Car` object, `limo`, initialized with 100 units of fuel (1)
    limo.add_fuel(20)  # `limo` with 20 units of fuel added (2)
    print(f"fuel = {limo.fuel}")  # `limo` with 120 units of fuel (3)
    limo.drive(115)  # `limo` drove 115km (4)
    print(f"odo = {limo.odometer}")  # `limo` have `odometer` value of 115 (5)
    print(BORDER)


main()

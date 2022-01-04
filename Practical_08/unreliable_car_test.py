"""
Practical 8: Question 2B
unreliable_car_test.py
"""

from unreliable_car import UnreliableCar

BORDER = "—" * 150


def main():
    """ Test the UnreliableCar class. """
    print(BORDER)
    print("Practical 8: Question 2\nunreliable_car_test.py")
    print(BORDER)
    print("Started…")
    great_wall_deer = UnreliableCar("Great Wall Deer", 100, 60)
    great_wall_deer.drive(40)
    print(great_wall_deer)
    great_wall_deer.add_fuel(20)
    print(great_wall_deer)
    great_wall_deer.drive(80)
    print(great_wall_deer)
    print("…Ended!")
    print(BORDER)


if __name__ == '__main__':
    main()

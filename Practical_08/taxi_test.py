"""
Practical 8: Question 1C
taxi_test.py
"""

from taxi import Taxi

BORDER = "—" * 150


def main():
    """ Test the Taxi class. """
    print(BORDER)
    print("Practical 8: Question 1\ntaxi_test.py")
    print(BORDER)
    print("Started…")
    prius_1 = Taxi("Prius 1", 100)
    prius_1.drive(40)
    print(prius_1)
    prius_1.start_fare()
    prius_1.drive(100)
    print(prius_1)
    print("…Ended!")
    print(BORDER)


if __name__ == '__main__':
    main()

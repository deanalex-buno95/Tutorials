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
    prius_1 = Taxi("Prius 1", 100, 1.23)  # (1) New Taxi
    prius_1.drive(40)  # (2) Drive 40km
    print(prius_1)  # (3) Print Taxi details
    prius_1.start_fare()  # (4A) Restart meter
    prius_1.drive(100)  # (4B) Drive another 100km
    print(prius_1)  # (5) Print Taxi details again
    print("…Ended!")
    print(BORDER)


if __name__ == '__main__':
    main()

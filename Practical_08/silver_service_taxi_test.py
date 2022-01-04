"""
Practical 8, Question 3B
silver_service_taxi_test.py
"""

from silver_service_taxi import SilverServiceTaxi

BORDER = "—" * 150


def main():
    """ Test the SilverServiceTaxi class. """
    print(BORDER)
    print("Practical 8, Question 3B\nsilver_service_taxi_test.py")
    print(BORDER)
    print("Started…")
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    super_taxi = SilverServiceTaxi("Super Taxi", 100, 2)
    print(hummer)
    print(super_taxi)
    hummer.drive(0)
    super_taxi.drive(18)
    print(f"${hummer.get_fare():.2f}")  # $4.50
    print(f"${super_taxi.get_fare():.2f}")  # $48.76 → $ $48.80
    print("…Ended!")
    print(BORDER)


if __name__ == '__main__':
    main()

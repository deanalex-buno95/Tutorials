"""
Practice:
test_date.py
"""


import datetime
from Practical_06.date import Date

NUMBER_OF_DAYS = 5


def main():
    """ Main function for testing. """
    print("Test begun…")
    empty_date = Date()  # 0/0/0
    print(empty_date)
    today = datetime.date.today()  # current date
    current_day = today.day
    current_month = today.month
    current_year = today.year
    date = Date(current_day, current_month, current_year)  # general date
    print(date)
    date.add_days(NUMBER_OF_DAYS)  # `NUMBER_OF_DAYS` of days later
    print(date)
    print("… Test ended!")


if __name__ == "__main__":
    main()

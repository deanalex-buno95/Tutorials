"""
Practice:
date.py
"""


import datetime


class Date:
    """ Date is class for any instance of a date. """
    def __init__(self, day=0, month=0, year=0):
        """ Constructor for Date. """
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        """ Display Date. """
        return f"{self.year}/{self.month}/{self.day}"

    def add_days(self, n):
        """ Add days to Date. """
        updated_date = datetime.date(self.year, self.month, self.day) + datetime.timedelta(days=n)
        self.day = updated_date.day
        self.month = updated_date.month
        self.year = updated_date.year

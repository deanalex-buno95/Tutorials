"""
Practical 3A:
guitar.py
"""


"""
CLASSES & FUNCTIONS
"""


class Guitar:
    """
    Represent a `Guitar` object
    """
    def __init__(self, name="", year=0, cost=0):
        """
        Instance of a `Guitar` object
        Parameters:
        name – name_str [str]
        year – year_int [int]
        cost – cost_float [float]
        """
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """
        Get `Guitar` object's `age` from parameter `Guitar.year`
        """
        return 2021 - self.year

    def is_vintage(self):
        """
        Check if the `Guitar` object is more than 50 years old
        """
        return self.get_age() > 50

    def __str__(self):
        """
        Display `Guitar` object information
        """
        return f"{self.name} ({self.year}) : ${self.cost}"

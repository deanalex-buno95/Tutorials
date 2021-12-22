"""
Practical 6: Question 2A
programming_language.py
"""


"""
CLASSES & FUNCTIONS
"""


class ProgrammingLanguage:
    """
    Represent a Programming Language (object)
    """

    def __init__(self, name, typing, reflection, year):
        """
        Instance of a Programming Language (object)
        Parameters:
        name: name_str [str]
        typing: 'Dynamic' or 'Static' [str]
        reflection: True (Yes) or False (No) [bool]
        year: year_int [int]
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """
        Check if the Programming Language is 'Dynamic'
        """
        return self.typing == "Dynamic"

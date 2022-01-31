"""
Practice:
person.py
"""


class Person:
    """ Person is a class that describes an instance of a person. """
    def __init__(self, first_name="", last_name="", age=0):
        """ Constructor for Person. """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_first_name(self):
        """ Getter for Person.first_name. """
        return self.first_name

    def get_last_name(self):
        """ Getter for Person.last_name. """
        return self.last_name

    def get_age(self):
        """ Getter for Person.age. """
        return self.age

    def set_first_name(self, new_first_name):
        """ Setter for Person.first_name. """
        self.first_name = new_first_name

    def set_last_name(self, new_last_name):
        """ Setter for Person.last_name. """
        self.last_name = new_last_name

    def set_age(self, new_age):
        """ Setter for Person.age. """
        self.age = new_age

    def __str__(self):
        """ Display Person. """
        return f"{self.get_last_name()}, {self.get_first_name()}. Age: {self.get_age()}."

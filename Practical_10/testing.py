"""
Practical 10:
Question 1
testing.py
"""


import doctest
from Practical_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    repeated_string = ""
    for i in range(n):
        # add repeated string
        repeated_string += s
        # deal with cases where it is not the last repeated string
        if i != n-1:
            repeated_string += " "
    return repeated_string


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # TODO: 1. fix the repeat_string function above so that it passes the failing test
    # Hint: "-".join(["yo", "yo"] -> "yo-yo"
    assert repeat_string("RGG", 8) == "RGG RGG RGG RGG RGG RGG RGG RGG"
    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    # TODO: 2. write assert statements to show if Car sets the fuel correctly
    # Note that Car's __init__ function sets the fuel in one of two ways:
    # using the value passed in or the default
    # You should test both of these
    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "Fuel is not 10"
    assert test_car.name == "Car", "This is not a regular car"


run_tests()

# TODO: 3. Uncomment the following line and run the doctests
# (PyCharm may see your >>> doctest comments and run doctests anyway.)
doctest.testmod()

# TODO: 4. Fix the failing is_long_word function
# (don't change the tests, change the function!)
assert(is_long_word("YAKUZA", 6)) is True

# TODO: 5. Write and test a function to format a phrase as a sentence,
# starting with a capital and ending with a single full stop.
# Important: start with a function header and just use pass as the body
# then add doctests for 3 tests:
# 'hello' -> 'Hello.'
# 'It is an ex parrot.' -> 'It is an ex parrot.'
# and one more you decide (one that is valid!)
# test this and watch the tests fail
# then write the body of the function so that the tests pass


def convert_string_to_sentence(string):
    """
    Convert a string to a complete sentence
    """
    sentence = ""
    for i in range(len(string)):
        if i == 0:
            sentence += string[i].upper()
        else:
            sentence += string[i].lower()
    if "." not in sentence:
        sentence += "."
    return sentence


assert convert_string_to_sentence("hello") == "Hello."
assert convert_string_to_sentence("It is an ex parrot.") == "It is an ex parrot."
assert convert_string_to_sentence("cheeseBurgers ARE Awesome") == "Cheeseburgers are awesome."

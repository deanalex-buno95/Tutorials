"""
Practical 3: Question 1
password_check.py
"""

# imports

# CONSTANTS
BORDER = "—" * 150

"""
FUNCTIONS
"""


def main():
    """ Create the main function to print the number of asterisks based on the length of the password from the user """
    print(BORDER)
    print("Practical 3: Question 1")
    print(BORDER)
    password = get_password("Your password: ")
    asterisks = get_asterisks(password)
    print(asterisks)
    print(BORDER)


def get_password(prompt):
    """ Get the password from the user """
    password = input(prompt)
    return password


def get_asterisks(password):
    """ Get the number of asterisks based on the length of password from the user """
    return len(password) * "⁕"


"""
FUNCTION CALL
"""


main()

"""
Practice:
sequences.py
"""

MENU = "1. Even numbers from x to y\n2. Odd numbers from x to y\n3. Squares from x to y\n4. Quit"
OPTIONS = [1, 2, 3, 4]
SENTINEL = -1


def main():
    """ Main function for the sequences menu. """
    x = get_number("Input the first number: ")  # first number
    y = get_number("Input the second number (larger than the first): ", x)  # second number
    run = 0  # run while loop for the menu
    while run != SENTINEL:
        pass


def get_number(prompt, first_number=None):
    """ Get first number or second number from the user. """
    run = 0  # run while loop for checking correct input
    while run != SENTINEL:
        try:  # input
            number = int(input(prompt))
        except ValueError:  # not an integer
            print("Invalid value! Try again!")
        else:
            if first_number is None:  # for getting the first number
                return number
            else:  # for getting the second number
                if number <= first_number:  # x <= y
                    print("The second number must be larger than the first! Try again!")
                else:
                    return number


if __name__ == "__main__":
    main()

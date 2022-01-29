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
        print(MENU)
        option = get_option()
        if option == 1:  # even numbers from x to y
            for i in range(x, y+1):
                if not is_odd(i):
                    print(i)
        elif option == 2:  # odd numbers from x to y
            for i in range(x, y+1):
                if is_odd(i):
                    print(i)
        elif option == 3:  # squares from x to y
            pass
        else:  # quit
            print("End of program…")
            run = SENTINEL


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
                if number <= first_number:  # y <= x
                    print("The second number must be larger than the first! Try again!")
                else:  # y > x
                    return number


def get_option():
    """ Get menu option from the user. """
    run = 0  # run while loop for checking correct input
    while run != SENTINEL:
        try:  # input
            option = int(input())
        except ValueError:  # not an integer
            print("Invalid value! Try again!")
        else:
            if option not in OPTIONS:  # option does not exist
                print("This option does not exist! Try again!")
            else:
                return option


def is_odd(number):
    """ Check if number is odd. """
    return number % 2 == 1


def get_squared_number(number):
    """ Get squared number from a number. """
    pass


if __name__ == "__main__":
    main()

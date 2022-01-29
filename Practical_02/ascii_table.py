"""
Practice
ascii_table.py
"""


LOWER = 33
UPPER = 127
SENTINEL = -1


def main():
    """ Main function for the program. """
    character_input = get_character()  # get character
    character_input_ascii_code = ord(character_input)  # get the respective ASCII code
    print(f"The ASCII code for {character_input} is {character_input_ascii_code}")
    ascii_code_input = get_ascii_code()  # get ASCII code
    ascii_code_input_character = chr(ascii_code_input)  # get the respective character
    print(f"The character for {ascii_code_input} is {ascii_code_input_character}")


def get_character():
    """ Get a character from the user. """
    run = 0
    while run != SENTINEL:
        character_input = input("Enter a character: ")
        if len(character_input) == 1:  # valid character
            return character_input
        else:  # invalid (empty or more than one character)
            print("Invalid input! Try again!")


def get_ascii_code():
    """ Get the ASCII code within a range from the user. """
    run = 0
    while run != SENTINEL:
        try:  # input
            ascii_code_input = int(input(f"Enter a number between {LOWER} and {UPPER}: "))
        except ValueError:  # not an integer
            print("Invalid value! Try again!")
        else:
            if LOWER <= ascii_code_input <= UPPER:  # ASCII code within range
                return ascii_code_input
            else:  # ASCII code out of range
                print(f"The number must be between {LOWER} and {UPPER}! Try again!")


if __name__ == "__main__":
    main()

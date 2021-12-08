"""
Practical 5: Question 2
hex_colours.py
"""

# CONSTANTS
BORDER = "—" * 150
NAME_TO_CODE = {"Red": "FF0000", "Orange": "FFA500", "Yellow": "FFFF00", "Lime": "00FF00", "Green": "008000",
                "Teal": "008080", "Blue": "0000FF", "Purple": "800080", "Magenta": "FF00FF", "Pink": "FFC0CB"}


"""
MAIN FUNCTION
"""


def main():
    """ Main function to get colour code from colour name input from dictionary 'NAME_TO_CODE' """
    print(BORDER)
    print("Practical 5: Question 2\nhex_colours.py")
    print(BORDER)
    colour_name = input("Name a colour: ").title()
    while colour_name != "":
        if colour_name in NAME_TO_CODE:
            print(f"{colour_name}: #{NAME_TO_CODE[colour_name]}")
        else:
            print("Invalid colour name!")
        colour_name = input("Name a colour: ").title()
    print(BORDER)


"""
RUN MAIN FUNCTION
"""

if __name__ == '__main__':
    main()

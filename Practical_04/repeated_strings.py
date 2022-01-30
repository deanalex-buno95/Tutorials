"""
Practice:
repeated_strings.py
"""


SENTINEL = -1


def main():
    """ Main function for the program. """
    strings = []  # collect all distinct strings
    repeated_strings = []  # collect strings that are entered more than once
    run = 0  # while loop for entering strings
    while run != SENTINEL:
        input_string = input("String: ").lower()  # lower case for standardization
        if not input_string:  # empty string, end while loop
            if not repeated_strings:  # no strings are repeated
                print("No repeated strings entered")
            else:  # display repeated strings
                print("Strings repeated: ", end="")
                for i in range(len(repeated_strings)):
                    repeated_string = repeated_strings[i]
                    if i != len(repeated_strings)-1:
                        repeated_string += ", "
                    print(repeated_string, end="")
            run = SENTINEL
        elif input_string in strings:  # string is repeated
            if input_string not in repeated_strings:  # repeated once
                repeated_strings.append(input_string)
        else:  # new string
            strings.append(input_string)


if __name__ == "__main__":
    main()

"""
Practical 4: Question 4
subject_reader.py
"""


# CONSTANTS
BORDER = "—" * 150
FILENAME = "subject_data.txt"


"""
FUNCTIONS
"""


def main():
    """ The main function to output data from 'subject_data.txt' """
    data = get_data()
    print(data)


def get_data():
    """ Read data from 'subject_data.txt' file that is formatted as: subject,lecturer,number of students """
    input_file = open(FILENAME)
    for line in input_file:
        print(line)
        print(repr(line))
        line = line.strip()
        parts = line.split(",")
        print(parts)
        print("-+-")


"""
PROGRAM
"""


main()

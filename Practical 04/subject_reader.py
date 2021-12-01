"""
Practical 4: Question 3
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
    display_data(data)


def get_data():
    """ Read data from 'subject_data.txt' file that is formatted as: subject,lecturer,number of students """
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # strip '\n'
        subject, lecturer, number_of_students = line.split(",")  # split line into multiple parts via ','
        data_row = [subject, lecturer, int(number_of_students)]  # each data row in a list
        data.append(data_row)  # append data row list into main data list
    input_file.close()
    return data


def display_data(data):
    """ Display data in terms of sentences """
    for subject, lecturer, number_of_students in data:
        print(f"{subject} is taught by {lecturer} and has {number_of_students} students.")


"""
PROGRAM
"""


main()

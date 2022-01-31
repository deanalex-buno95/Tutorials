"""
Practice:
dictionary_extension.py
"""


NUMBER_OF_PEOPLE = 5
CURRENT_YEAR = 2022


def main():
    """ Main function for program. """
    names = ["Jack", "Jill", "Harry"]
    dates_of_birth = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]
    date_of_birth_dictionary = get_date_of_birth_dictionary(names, dates_of_birth)
    age_dictionary = get_age_dictionary(names, dates_of_birth)
    print(f"Date-of-birth dictionary:\n{date_of_birth_dictionary}")
    print(f"Age dictionary:\n{age_dictionary}")


def get_date_of_birth_dictionary(name_list, date_of_birth_list):
    """ Get date-of-birth dictionary from two lists: name_list and dob_list. """
    date_of_birth_dictionary = {}
    for i in range(len(name_list)):
        name = name_list[i]
        date_of_birth_tuple = date_of_birth_list[i]
        date_of_birth_day = date_of_birth_tuple[0]
        date_of_birth_month = date_of_birth_tuple[1]
        date_of_birth_year = date_of_birth_tuple[2]
        date_of_birth = f"{date_of_birth_day}/{date_of_birth_month}/{date_of_birth_year}"
        date_of_birth_dictionary[name] = date_of_birth
    return date_of_birth_dictionary


def get_age_dictionary(name_list, date_of_birth_list):
    """ Get age dictionary from two lists: name_list and dob_list. """
    age_dictionary = {}
    for i in range(len(name_list)):
        name = name_list[i]
        date_of_birth_tuple = date_of_birth_list[i]
        date_of_birth_year = date_of_birth_tuple[2]
        age = CURRENT_YEAR - date_of_birth_year
        age_dictionary[name] = age
    return age_dictionary


if __name__ == "__main__":
    main()

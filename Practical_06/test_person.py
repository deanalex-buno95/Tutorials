"""
Practice:
test_person.py
"""


from Practical_06.person import Person


def main():
    """ Main program for testing. """
    print("Test begun…")
    empty_person = Person()  # test person with default parameters
    print(empty_person)  # ", . Age: 0."
    actual_person = Person("Lauri", "Törni", 46)  # test person with filled parameters
    print(actual_person)  # "Törni, Lauri. Age: 46."
    print(actual_person.get_first_name())  # "Lauri"
    print(actual_person.get_last_name())  # "Törni"
    print(actual_person.get_age())  # 46
    actual_person.set_first_name("Larry")  # change first name from "Lauri" to "Larry"
    actual_person.set_last_name("Thorne")  # change last name from "Törni" to "Thorne"
    actual_person.set_age(103)
    print(actual_person)  # "Thorne, Lauri. Age: 103"
    print("… Test ended!")


if __name__ == "__main__":
    main()

"""
Practical 6: Question 3B
guitar_test.py
"""


# MODULES
from Practical_06.guitar import Guitar

# BORDER
BORDER = "—" * 150


"""
PROGRAMS
"""


def main():
    """ Test `Guitar` class """
    print(BORDER)
    print("Practical 6: Question 3A\nguitar.py & guitar_test.py")
    print(BORDER)
    gibson_l5 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 100)
    print(f"{gibson_l5.name} get_age() – Expected 99. Got {gibson_l5.get_age()}.")
    print(f"{another_guitar.name} get_age() – Expected 8. Got {another_guitar.get_age()}.")
    print(f"{gibson_l5.name} is_vintage() – Expected True. Got {gibson_l5.is_vintage()}.")
    print(f"{another_guitar.name} is_vintage() – Expected False. Got {another_guitar.is_vintage()}.")
    print(BORDER)


if __name__ == '__main__':
    main()

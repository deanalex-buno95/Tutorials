"""
Practical 6: Question 3C
guitars.py
"""


# MODULES
from Practical_06.guitar import Guitar

# BORDER
BORDER = "—" * 150
SENTINEL = -1
VINTAGE_STRING = "(vintage)"


"""
PROGRAM
"""


def main():
    """
    Main program for adding guitars from users into a list
    """
    print(BORDER)
    print("Practical 6: Question 3B\nguitar.py & guitars.py")
    print(BORDER)
    print("My guitars!")
    guitar_list = []
    run = 0
    while run != SENTINEL:
        name = get_guitar_name()
        if name == "":
            run = SENTINEL
        else:
            year = get_guitar_year()
            cost = get_guitar_cost()
            added_guitar = Guitar(name, year, cost)
            print(added_guitar, "added.")
            guitar_list.append(added_guitar)
    print("…snip…")
    print("These are my guitars:")
    for i, guitar in enumerate(guitar_list, 1):
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {VINTAGE_STRING if guitar.is_vintage() else ''}")
    print(BORDER)


def get_guitar_name():
    """
    Get guitar name from user
    """
    return input("Name: ").title()


def get_guitar_year():
    """
    Get guitar year from user
    """
    run = 0
    while run != SENTINEL:
        try:
            year = int(input("Year: "))
            if year >= 0:
                return year
            print("Please input a valid year!")
        except ValueError:
            print("Please input a proper value!")


def get_guitar_cost():
    """
    Get guitar cost from user
    """
    run = 0
    while run != SENTINEL:
        try:
            cost = float(input("Cost: $"))
            if cost >= 0:
                return cost
            print("Please input a valid cost!")
        except ValueError:
            print("Please input a proper value!")


if __name__ == '__main__':
    main()

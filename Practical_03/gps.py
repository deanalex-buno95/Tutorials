"""
Practice:
gps.py
"""


import random


STARTING_POPULATION = 1000
MINIMUM_BORN_DECIMAL = 0.1
MAXIMUM_BORN_DECIMAL = 0.2
MINIMUM_DIED_DECIMAL = 0.05
MAXIMUM_DIED_DECIMAL = 0.25
NUMBER_OF_YEARS = 10


def main():
    """ Main function for the GPS program. """
    print(f"Welcome to the Gopher Population Simulator!\nStarting population: {STARTING_POPULATION}")
    current_population = STARTING_POPULATION  # initialize `current_population`
    for i in range(NUMBER_OF_YEARS):
        print(f"Year {i+1}\n")
        gophers_born = get_gophers_born(current_population)
        gophers_died = get_gophers_died(current_population)
        print(f"{gophers_born} gophers were born. {gophers_died} died.")
        current_population += (gophers_born - gophers_died)
        print(f"Population: {current_population}")


def get_gophers_born(current_population):
    """ Get gophers born. """
    gophers_born = round(current_population * random.uniform(MINIMUM_BORN_DECIMAL, MAXIMUM_BORN_DECIMAL))
    return gophers_born


def get_gophers_died(current_population):
    """ Get gophers died. """
    gophers_born = round(current_population * random.uniform(MINIMUM_DIED_DECIMAL, MAXIMUM_DIED_DECIMAL))
    return gophers_born


if __name__ == "__main__":
    main()

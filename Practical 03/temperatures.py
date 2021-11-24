"""
Practical 3: Question 2
temperatures.py
"""

# imports

# CONSTANTS
BORDER = "—" * 150
SENTINEL = -1
MENU = "Menu:\nC – Convert Celsius to Fahrenheit\nF – Convert Fahrenheit to Celsius\nQ – Quit"
CHOICES = ["C", "F", "Q"]

"""
Original Solution:
Practical 1: Question 1

MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"
print(MENU)
choice = input("Choice: ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print("Result: {:.2f}°F".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print("Result: {:.2f}°C".format(celsius))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
"""


"""
FUNCTIONS
"""


def main():
    """ Create the main function for a menu for temperature conversion """
    print(BORDER)
    print("Practical 3: Question 2")
    print(BORDER)
    run = 0
    while run != SENTINEL:
        print(MENU)
        print(BORDER)
        choice = get_choice("Select choice (C/H/Q): ")
        print(BORDER)
        if choice == "C":
            input_temperature = get_temperature("Input temperature in °C: ")
            converted_temperature = convert_temperature(input_temperature, "°C")
            print(f"{input_temperature:.2f}°C → {converted_temperature:.2f}°F")
        elif choice == "F":
            input_temperature = get_temperature("Input temperature in °F: ")
            converted_temperature = convert_temperature(input_temperature, "°F")
            print(f"{input_temperature:.2f}°F → {converted_temperature:.2f}°C")
        else:
            print("Program ended!")
            run = SENTINEL
        print(BORDER)


def get_choice(prompt):
    """ Get the menu choice from the user """
    run = 0
    while run != SENTINEL:
        choice = input(prompt).upper()
        if choice in CHOICES:
            return choice
        print("Invalid choice! Try again!")


def get_temperature(prompt):
    """ Get the temperature from the user """
    run = 0
    while run != SENTINEL:
        try:
            temperature_input = float(input(prompt))
            return temperature_input
        except ValueError:
            print("Invalid input! Try again!")


def convert_temperature(temperature_input, unit):
    """ Convert the temperature from the user to a different measurement """
    if unit == "°C":
        temperature_in_fahrenheit = temperature_input * 9.0 / 5 + 32
        return temperature_in_fahrenheit
    else:
        temperature_in_celsius = 5 / 9 * (temperature_input - 32)
        return temperature_in_celsius


"""
FUNCTION CALL
"""


main()

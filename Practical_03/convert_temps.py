"""
Practice:
convert_temps.py
"""


SENTINEL = -1
INPUT_TEXT_FILE = "temps_input.txt"
OUTPUT_TEXT_FILE = "temps_output.txt"
NUMBER_OF_TEMPERATURES = 3
MINIMUM_TEMPERATURE = -200
MAXIMUM_TEMPERATURE = 200
CELCIUS = "°C"
FAHRENHEIT = "°F"


def main():
    """ Main function for the program. """
    with open(INPUT_TEXT_FILE, "w") as input_file:  # create input file
        for i in range(NUMBER_OF_TEMPERATURES):
            temperature_input = get_temperature(f"Temperature {i}: ")
            new_line = str(temperature_input)
            if i != NUMBER_OF_TEMPERATURES-1:
                new_line += "\n"
            input_file.write(new_line)
    converted_temperatures = []  # the initial values are unconverted in °F, later in °C
    with open(INPUT_TEXT_FILE) as celcius_file:  # read input file
        lines = celcius_file.readlines()
        for line in lines:
            converted_temperatures.append(float(line.strip()))
    for i in range(len(converted_temperatures)):  # convert temperature in °F to °C
        fahrenheit_temperature = converted_temperatures[i]
        converted_temperatures[i] = convert_temperature(fahrenheit_temperature, FAHRENHEIT)
    with open(OUTPUT_TEXT_FILE, "w") as output_file:  # create output file
        for i in range(len(converted_temperatures)):
            new_line = str(converted_temperatures[i])
            if i != len(converted_temperatures)-1:
                new_line += "\n"
            output_file.write(new_line)


def get_temperature(prompt):
    """ Get the temperature from the user. """
    run = 0
    while run != SENTINEL:
        try:
            temperature_input = float(input(prompt))
        except ValueError:
            print("Invalid input! Try again!")
        else:
            if MINIMUM_TEMPERATURE <= temperature_input <= MAXIMUM_TEMPERATURE:
                return temperature_input
            else:
                print(f"Temperature must be between {MINIMUM_TEMPERATURE} and {MAXIMUM_TEMPERATURE}! Try again!")


def convert_temperature(temperature_input, unit):
    """ Convert the temperature from the user to a different measurement from the unit parameter. """
    if unit == CELCIUS:
        temperature_in_fahrenheit = temperature_input * 9.0 / 5 + 32
        return temperature_in_fahrenheit
    else:
        temperature_in_celsius = 5 / 9 * (temperature_input - 32)
        return temperature_in_celsius


if __name__ == '__main__':
    main()

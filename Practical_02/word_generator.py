"""
Practice
word_generator.py
"""


import random


VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
LETTERS = VOWELS + CONSONANTS
WILDCARDS = "%#*"
FORMAT_CHARACTERS = LETTERS + WILDCARDS
SENTINEL = -1
LOWER = 5
UPPER = 10


def get_word_format():
    """ Get word format from user. """
    run = 0
    while run != SENTINEL:
        input_format = input("Format: ").lower()
        valid_format = True
        for character in input_format:
            if character not in [char for char in FORMAT_CHARACTERS]:
                valid_format = False
        if valid_format:
            return input_format
        else:
            print("Invalid format! Try again!")


word_format = get_word_format()
word = ""
for format_char in word_format:
    if format_char == "%":
        word += random.choice(CONSONANTS)
    elif format_char == "#":
        word += random.choice(VOWELS)
    elif format_char == "*":
        word += random.choice(LETTERS)
    else:
        word += format_char
print(word)

random_word_format = ""
for i in range(random.randint(LOWER, UPPER+1)):
    random_word_format += random.choice(FORMAT_CHARACTERS)
print(f"Format: {random_word_format}")
random_word = ""
for format_char in random_word_format:
    if format_char == "%":
        random_word += random.choice(CONSONANTS)
    elif format_char == "#":
        random_word += random.choice(VOWELS)
    elif format_char == "*":
        random_word += random.choice(LETTERS)
    else:
        random_word += format_char
print(random_word)

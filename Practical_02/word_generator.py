"""
Practice
word_generator.py
"""


import random


VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
SENTINEL = -1


def get_word_format():
    """ Get word format from user. """
    run = 0
    while run != SENTINEL:
        input_format = input("Format: ").lower()
        valid_format = True
        for char in input_format:
            if char not in ["c", "v"]:
                valid_format = False
        if valid_format:
            return input_format
        else:
            print("Invalid format! Try again!")


word_format = get_word_format()
word = ""
for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)

print(word)

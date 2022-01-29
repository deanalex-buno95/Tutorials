"""
Practice
word_generator.py
"""


import random


VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def get_word_format():
    """ Get word format from user. """
    pass


word_format = get_word_format()
word = ""
for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)

print(word)

"""
Practical 6: Question 2B
languages.py
"""


# MODULES
from Practical_06.programming_language import ProgrammingLanguage


# CONSTANTS
BORDER = "—" * 150


"""
PROGRAM
"""


def main():
    """ Test code for languages """
    print(BORDER)
    print("Practical 6: Question 2\nprogramming_language.py & languages.py")
    print(BORDER)
    print("Part 1:")
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    languages_list = [ruby, python, visual_basic]
    for language in languages_list:
        print(language)
    print(BORDER)
    print("Part 2:")
    print("The dynamically typed languages are:")
    for language in languages_list:
        if language.is_dynamic():
            print(language.name)
    print(BORDER)


if __name__ == '__main__':
    main()

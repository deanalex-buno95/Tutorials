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
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)


if __name__ == '__main__':
    main()

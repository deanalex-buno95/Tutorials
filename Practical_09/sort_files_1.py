"""
Practical 9:
Question 3
sort_files_1.py
"""


def main():
    """
    Main function to change
    :return: None
    """
    pass


def get_extension(filename):
    """
    Get extension from filename
    :return: extension (type: str)
    """
    necessary_portion = filename[-5:]
    excess, extension = necessary_portion.split(".")
    return extension


if __name__ == '__main__':
    main()

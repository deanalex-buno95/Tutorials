"""
Practical 9:
Question 3
sort_files_1.py
"""


import os


def main():
    """
    Main function to change
    :return: None
    """
    os.chdir("FilesToSort")  # change to directory `FilesToSort`
    for directory_name, subdirectories, filenames in os.walk('.'):  # walk through the filenames in directory
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))
        for filename in filenames:  # loop each file name for moving files into created directories
            file_extension = get_extension(filename)
            print(filename, file_extension)


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

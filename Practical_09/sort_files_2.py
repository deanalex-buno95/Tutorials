"""
Practical 9:
Question 4
sort_files_2.py
"""


import os
import shutil

SENTINEL = -1


def main():
    """
    Main function to change
    :return: None
    """
    file_categories = []
    file_extensions_dictionary = {}
    os.chdir("FilesToSort")  # change to directory `FilesToSort`
    for filename in os.listdir('.'):
        if os.path.isdir(filename):  # ignore directories, just process files
            continue
        file_extension = get_extension(filename)  # get the extension
        if file_extension not in file_extensions_dictionary:  # extension not in dictionary
            directory_name = get_directory_name(file_extension)  # set directory name as value of extension
            file_categories.append(directory_name)
            try:  # first time
                os.mkdir(directory_name)
            except FileExistsError:  # subsequent times
                pass
            file_extensions_dictionary[file_extension] = directory_name
            print(f"Moving {filename} to {directory_name}")
            shutil.move(filename, f"{directory_name}/{filename}")
        else:  # extension in dictionary
            directory_name = file_extensions_dictionary[file_extension]
            print(f"Moving {filename} to {directory_name}")
            shutil.move(filename, f"{directory_name}/{filename}")

        '''
        try:  # new directory for new extension
            os.mkdir(file_extension)
        except FileExistsError:  # directory already exists
            pass
        print(f"Moving {filename} to {file_extension}")
        shutil.move(filename, f"{file_extension}/{filename}")
        '''


def get_extension(filename):
    """
    Get extension from filename
    :return: extension (type: str)
    """
    necessary_portion = filename[-5:]
    excess, extension = necessary_portion.split(".")
    return extension


def get_directory_name(file_extension):
    """
    Get directory name from user
    :param file_extension: string
    :return: directory_name (type: str)
    """
    run = 0
    while run != SENTINEL:
        directory_name = input(f"What category would you like to sort {file_extension} files into? ")
        if directory_name != "":
            return directory_name
        print("Invalid input!")


if __name__ == '__main__':
    main()

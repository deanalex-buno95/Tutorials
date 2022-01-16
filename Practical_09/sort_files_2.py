"""
Practical 9:
Question 4
sort_files_2.py
"""


import os
import shutil


def main():
    """
    Main function to change
    :return: None
    """
    file_directories = {}
    os.chdir("FilesToSort")  # change to directory `FilesToSort`
    for filename in os.listdir('.'):
        if os.path.isdir(filename):  # ignore directories, just process files
            continue
        file_extension = get_extension(filename)
        directory_name = get_directory_name(file_extension, file_directories)
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


def get_directory_name(file_extension, file_directories):
    """
    Get directory name from user
    :param file_extension: string
    :param file_directories: string
    :return: directory_name (type: str)
    """
    pass


if __name__ == '__main__':
    main()

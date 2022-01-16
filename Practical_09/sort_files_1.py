"""
Practical 9:
Question 3
sort_files_1.py
"""


import os
import shutil


def main():
    """
    Main function to change
    :return: None
    """
    os.chdir("FilesToSort")  # change to directory `FilesToSort`
    '''
    for directory_name, subdirectories, filenames in os.walk('.'):  # walk through the filenames in directory
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))
        for filename in filenames:  # loop each file name for moving files into created directories
            file_extension = get_extension(filename)
            print(f"Moving {filename} to {file_extension}")
            try:  # make a new directory
                os.mkdir(file_extension)
            except FileExistsError:  # directory already exists
                pass
            shutil.move(filename, f"/{file_extension}")
    '''
    for filename in os.listdir('.'):
        if os.path.isdir(filename):  # ignore directories, just process files
            continue
        file_extension = get_extension(filename)
        try:  # new directory for new extension
            os.mkdir(file_extension)
        except FileExistsError:  # directory already exists
            pass
        print(f"Moving {filename} to {file_extension}")
        shutil.move(filename, f"{file_extension}/{filename}")


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

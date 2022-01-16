"""
Practical 9:
Question 2
"""


# import shutil
import os


def main():
    """Main function for cleaning up file names."""

    # Starting directory
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir("Lyrics")

    # Walk
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))
        # Add a loop to rename the files
        for filename in filenames:
            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(full_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


# main()

import sys
import os

# https://pypi.org/project/in-place/
import in_place
import re


def main():
    print_header()
    if check_command_line_args():
        filename = get_data_file()
        change_in_place(filename)


def print_header():
    print("----------------------------------")
    print("   Format schedule for Excel")
    print("----------------------------------")


# https://www.pythonforbeginners.com/system/python-sys-argv
def print_command_line_args():
    print("Total args:", len(sys.argv))
    print("Available args:", sys.argv)


def check_command_line_args():
    if len(sys.argv) <= 1:
        print(
            "Missing argument! Specify target file name after script. It must be in same directory as script."
        )
        print("Example: schedule_formatter.py sample.txt")
        return False
    elif sys.argv[1] == "--help":
        print("This script formats copied schedule text to paste into spreadsheet.")
        print("Provide the name of the  target txt file after the script")
        print("Example: schedule_formatter.py sample.txt")
        return False
    elif sys.argv[1]:
        return True


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, sys.argv[1])


def change_in_place(filename):
    with in_place.InPlace(filename) as file:
        for line in file:
            # https://lzone.de/examples/Python%20re.sub
            # remove CT
            line = re.sub(" CT", "", line)
            # remove MDWY
            line = re.sub("MDWY - ", "", line)
            # remove last column
            line = re.sub(r"(.*)\t(.*)\t(.*)\t(.*)\t(.*)", r"\1\t\2\t\3\t\4", line)
            file.write(line)


if __name__ == "__main__":
    main()

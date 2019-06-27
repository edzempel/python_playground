import sys
import os

# https://pypi.org/project/in-place/
import in_place
import re


def main():
    print_header()
    if check_command_line_args():
        filename = get_data_file()
        print("Made", change_in_place(filename), "changes")


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
    change_count = 0
    with in_place.InPlace(filename) as file:
        for line in file:
            # https://lzone.de/examples/Python%20re.sub
            # remove CT
            line, n = re.subn(" CT", "", line)
            change_count += n
            # remove MDWY
            line, n = re.subn("MDWY - ", "", line)
            change_count += n
            # remove last column
            line, n = re.subn(r"(.*)\t(.*)\t(.*)\t(.*)\t(.*)", r"\1\t\2\t\3\t\4", line)
            change_count += n
            file.write(line)
    return change_count


if __name__ == "__main__":
    main()

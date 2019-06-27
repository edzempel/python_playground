import sys
import os


def main():
    print_header()
    # print_command_line_args()
    # print(get_data_file())
    if check_command_line_args():
        filename = get_data_file()
        file = load_file(filename)
        print(type(file))


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


def load_file(filename):
    with open(filename, "r", encoding="utf-8") as fin:
        return fin


def regex_swap_last_two_columns():
    pass


def regex_remove_extra_letters():
    pass


if __name__ == "__main__":
    main()

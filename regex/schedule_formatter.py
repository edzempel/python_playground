import sys
import os


def main():
    print_header()
    print_command_line_args()
    print(get_data_file())


def print_header():
    print("----------------------------------")
    print("   Format schedule for Excel")
    print("----------------------------------")


# https://www.pythonforbeginners.com/system/python-sys-argv
def print_command_line_args():
    print("Total args:", len(sys.argv))
    print("Available args:", sys.argv)


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, sys.argv[1])


def regex_swap_last_two_columns():
    pass


def regex_remove_extra_letters():
    pass


if __name__ == "__main__":
    main()

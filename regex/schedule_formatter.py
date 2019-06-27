import sys


def main():
    print_header()
    print_command_line_args()


def print_header():
    print("----------------------------------")
    print("   Format schedule for Excel")
    print("----------------------------------")


# https://www.pythonforbeginners.com/system/python-sys-argv
def print_command_line_args():
    print("Total args:", len(sys.argv))
    print("Available args:", sys.argv)


def regex_swap_last_two_columns():
    pass


def regex_remove_extra_letters():
    pass


if __name__ == "__main__":
    main()

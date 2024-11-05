#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        # Attempt to print the value as an integer
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        # Print the exception message to stderr
        print("Exception:", e, file=sys.stderr)
        return False

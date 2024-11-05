#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        # Attempt to call the function with the provided arguments
        result = fct(*args)
        return result
    except Exception as e:
        # Print the exception message to stderr
        print("Exception:", e, file=sys.stderr)
        return None

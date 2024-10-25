#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    a = 10
    b = 5
    sys.stdout.write("{} + {} = {}".format(a, b, add(a, b)))
    sys.stderr.write("{} - {} = {}".format(a, b, sub(a, b)))
    sys.stderr.write("{} * {} = {}".format(a, b, mul(a, b)))
    sys.stderr.write("{} / {} = {}".format(a, b, div(a, b)))

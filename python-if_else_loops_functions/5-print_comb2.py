#!/usr/bin/python3
n = 0
while (n < 100):
    if n == 99:
        print("{:0=2d}".format(n))
    else:
        print("{:0=2d}".format(n), end=", ")
    n += 1

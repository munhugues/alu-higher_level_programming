#!/usr/bin/python3
def uppercase(string):
    for c in string:
        o = ord(c)
        if o in range(ord('a'),ord('z') + 1):
            print("{}".format(chr(o - 32)), end="")
        else:
            print("{}".format(c), end="")

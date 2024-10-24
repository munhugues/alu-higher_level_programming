#!/usr/bin/python3
def uppercase(string):
    result = ""
    for c in string:
        o = ord(c)
        if o in range(ord('a'),ord('z') + 1):
            result += chr(ord(c) - 32)
        else:
            result += chr(c)
    print("{}".format(result), end="")
    print()

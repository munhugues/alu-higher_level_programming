#!/usr/bin/python3
for i in range(122, 96, -1):  # ASCII values of 'z' to 'a' are from 122 to 97
    if i % 2 == 0:
        print("{}".format(chr(i)), end="")  # Even: lowercase
    else:
        print("{}".format(chr(i - 32)), end="")  # Odd: uppercase (subtract 32 from ASCII to get uppercase)


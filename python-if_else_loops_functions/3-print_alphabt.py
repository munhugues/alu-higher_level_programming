#!/usr/bin/python3
for letter_code in range(ord('a'), ord('z')+1):
    letter = chr(letter_code)
    if letter in 'qe':
        continue
    else:
        print("{:c}".format(letter_code), end="")

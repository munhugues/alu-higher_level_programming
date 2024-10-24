#!/usr/bin/python3
def remove_char_at(string, n):
    tmp = ""
    for i, char in enumerate(string):
        if i == n:
            continue
        tmp += char
    return tmp

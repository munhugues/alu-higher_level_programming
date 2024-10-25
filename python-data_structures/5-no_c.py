#!/usr/bin/python3
def no_c(my_string):
    result = ''
    for n in my_string:
        if n == 'c' or n == 'C':
            continue
        result += n
    return result

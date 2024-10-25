#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    tot = len(my_list) - 1
    for i,n in enumerate(my_list):
        print("{:d}".format(my_list[tot - i]))

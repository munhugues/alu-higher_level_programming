#!/usr/bin/python3
"""Defining the class"""


class Square:
    """A class representing a square."""
    def __init__(self, size = 0):
        if type(size) != int:
            print("size must be an integer")

        elif size < 0:
            print("size must be >= 0")

        else:
            self.__size = size

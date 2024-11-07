#!/usr/bin/python3
"""Defining the class"""


class Square:
    """A class representing a square."""
    def __init__(self, size = 0):
        if not isinstance(size, int):
            raize ValueError("size must be an integer")
        
        if size < 0:
            raize TypeError("size must be >= 0")

        self.__size = size

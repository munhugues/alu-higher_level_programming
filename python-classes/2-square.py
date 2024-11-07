#!/usr/bin/python3
"""Defining the Square class"""


class Square:
    """Initialize the square with an optional size.

        Args:
            size (int): The size of one side of the square (default is 0).

        """
    def __init__(self, size = 0):
        """Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

            """
        if not isinstance(size, int):
            raize ValueError("size must be an integer")
        
        if size < 0:
            raize TypeError("size must be >= 0")

        self.__size = size

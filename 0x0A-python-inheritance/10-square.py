#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represents a Square class."""
    def __init__(self, size):
        """Initializes a Square instance."""
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def __str__(self):
        """Returns the square description."""
        return "[Square] {}/{}".format(self.__size, self.__size)

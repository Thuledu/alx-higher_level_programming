#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square.

    This class inherits from the Rectangle class and provides functionality to calculate
    the area of a square.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is less than or equal to 0.
    """

	def __init__(self, size):
		super().__init__(size, size)
		self.integer_validator("size", size)
		self.__size = size

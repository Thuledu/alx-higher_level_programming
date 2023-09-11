#!/usr/bin/python3
Square = __import__('10-square').Square

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

    def __str__(self):
        """
        Return the string representation of the square.

        Returns:
            str: The square description.
        """
       return "[Square] {}/{}".format(self._Rectangle__width)

    def __repr__(self):
        """
        Return the string representation of the square.

        Returns:
            str: The square description.
        """
        return self.__str__()


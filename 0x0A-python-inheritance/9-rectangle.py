#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.

    This class inherits from the BaseGeometry class and provides functionality to calculate
    the area of a rectangle.

    Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Raises:
        TypeError: If the width or height is not an integer.
        ValueError: If the width or height is less than or equal to 0.
    """

    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the string representation of the rectangle.

        Returns:
            str: The rectangle description.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def __repr__(self):
        """
        Return the string representation of the rectangle.

        Returns:
            str: The rectangle description.
        """
        return self.__str__()


#!/usr/bin/python3
"""The Python class MagicClass that does exactly the same as the Python bytecode"""
import math

class MagicClass:
    """
    This class represents a magic circle with a radius value.
    """

    def __init__(self, radius):
        """
        Initializes a MagicClass object with the given radius.

        Parameters:
        - radius: The radius of the magic circle.

        Raises:
        - TypeError: If the radius is not a number.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Calculates the area of the magic circle.

        Returns:
        - The area of the magic circle.
        """
        return 2 * math.pi * self.__radius ** 2

    def circumference(self):
        """
        Calculates the circumference of the magic circle.

        Returns:
        - The circumference of the magic circle.
        """
        return 2 * math.pi * self.__radius


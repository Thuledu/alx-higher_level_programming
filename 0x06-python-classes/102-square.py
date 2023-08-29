#!/usr/bin/python3
"""A class Square that defines a square by: (based on 4-square.py)"""
class Square:
    """
    Square class defines a square by its size.

    Attributes:
        size (float or int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a new instance of the Square class.
        area(self): Calculates and returns the area of the square.
        __eq__(self, other): Compares two Square instances for equality.
        __ne__(self, other): Compares two Square instances for inequality.
        __gt__(self, other): Checks if the area of the current square is greater than the area of another square.
        __ge__(self, other): Checks if the area of the current square is greater than or equal to the area of another square.
        __lt__(self, other): Checks if the area of the current square is less than the area of another square.
        __le__(self, other): Checks if the area of the current square is less than or equal to the area of another square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (float or int): The size of the square. Default is 0.
        """
        self.__size = 0
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (float or int): The size of the square.

        Raises:
            TypeError: If the provided size is not a number.
            ValueError: If the provided size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compares two Square instances for equality based on their areas.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Compares two Square instances for inequality based on their areas.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return not self.__eq__(other)

    def __gt__(self, other):
        """
        Checks if the area of the current square is greater than the area of another square.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the current square's area is greater, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """
        Checks if the area of the current square is greater than or equal to the area of another square.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the current square's area is greater or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False

    def __lt__(self, other):
        """
        Checks if the area of the current square is less than the area of another square.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the current square's area is less, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """
        Checks if the area of the current square is less than or equal to the area of another square.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the current square's area is less or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False


#!/usr/bin/python3
"""A class Square that defines a square by: (based on 6-square.py)"""
class Square:
    """
    This class represents a square.

    Attributes:
    - size: The size of the square.
    - position: The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square object with the given size and position.

        Parameters:
        - size: The size of the square (default: 0).
        - position: The position of the square (default: (0, 0)).

        Raises:
        - TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
        - ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
        - The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Parameters:
        - value: The size value to be set.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
        - The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Parameters:
        - value: The position value to be set.

        Raises:
        - TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(x, int) for x in value) or not all(x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        - The area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """
        Prints the square in stdout using the character '#'.

        If size is equal to 0, prints an empty line.
        """
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)


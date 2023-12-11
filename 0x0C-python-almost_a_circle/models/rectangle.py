#!/usr/bin/python3

# models/rectangle.py
"""
Rectangle module
"""

from models.base import Base

class Rectangle(Base):
    """
    Rectangle class that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for Rectangle class
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): x-coordinate of the rectangle
            y (int): y-coordinate of the rectangle
            id (int): id of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate the area of the rectangle
        Returns:
            int: area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Display the Rectangle instance with the character #
        """
        print("\n" * self.__y + "\n".join(" " * self.__x + "#" * self.__width for _ in range(self.__height)))

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle
        Returns:
            dict: dictionary representation of the Rectangle
        """
        return {'id': self.id, 'width': self.width, 'height': self.height, 'x': self.x, 'y': self.y}


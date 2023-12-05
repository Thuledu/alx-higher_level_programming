#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represents a Rectangle class."""
    def __init__(self, width, height):
        """Initializes a Rectangle instance."""
        super().__init__()
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)

    def area(self):
        """Calculates the area of the Rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the rectangle description."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

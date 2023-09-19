#!/usr/bin/python3

import unittest
from models import rectangle
Rectangle = rectangle.Rectangle
from models.base import Base

class Rectangle:
    """A class representing a rectangle."""

    def __init__(self, width, height, x, y, id):
        """
        Initialize a rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position.
            y (int): The y-coordinate of the rectangle's position.
            id (int): The unique identifier of the rectangle.

        Raises:
            TypeError: If width, height, x, or y is not an integer.
            ValueError: If width or height is less than or equal to 0,
                        or if x or y is less than 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self._width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self._height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle's position."""
        return self._x

    @x.setter
    def x(self, value):
        """
        Set the x-coordinate of the rectangle's position.

        Args:
            value (int): The x-coordinate of the rectangle's position.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self._x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle's position."""
        return self._y

    @y.setter
    def y(self, value):
        """
        Set the y-coordinate of the rectangle's position.

        Args:
            value (int): The y-coordinate of the rectangle's position.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self._y = value

     def area(self) -> int:
        """Return the area of the Rectangle."""
        return self._height * self._width

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self._width == 0 or self._height == 0:
            print("")
            return

        for _ in range(self._y):
            print("")
        for _ in range(self._height):
            for _ in range(self._x):
                print(" ", end="")
            for _ in range(self._width):
                print("#", end="")
            print("")

    def update(self, *args: int, **kwargs: int):
        """Update the Rectangle
        """
        attribute_map = {
            1: "height",
            2: "width"
            3: "x",
            4: "y"
        }

        for index, value in enumerate(args):
            attribute_name = attribute_map.get(index, None)
            if attribute_name is not None:
                setattr(self, attribute_name, value)

        for key, value in kwargs.items():
            if key in attribute_map.values():
                setattr(self, key, value)

    def to_dictionary(self) -> dict:
        """Return rectangle dictionary representation."""
        return {
            "height": self._height,
            "width": self._width,
            "x": self._x,
            "y": self._y
        }

    def __str__(self) -> str:
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.height, self.width)

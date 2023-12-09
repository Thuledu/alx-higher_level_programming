#!/usr/bin/python3

# models/square.py
"""
Square module
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for Square class
        Args:
            size (int): size of the square
            x (int): x-coordinate of the square
            y (int): y-coordinate of the square
            id (int): id of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for size attribute
        Returns:
            int: size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size attribute
        Args:
            value (int): size of the square
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the Square attributes based on the given arguments
        Args:
            *args: no-keyword arguments in the order (id, size, x, y)
            **kwargs: key-worded arguments
        """
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)


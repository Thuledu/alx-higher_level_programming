#!/usr/bin/python3
"""A class Square that defines a square by: (based on 3-square.py)"""
class Square:
    """
    A class that defines a square.
    
    Attributes:
        size (int): The size of the square.
    """
    
    def __init__(self, size=0):
        """
        Initializes a Square instance.
        
        Args:
            size (int, optional): The size of the square. Defaults to 0.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size
        
    @property
    def size(self):
        """
        Getter method for the size attribute.
        
        Returns:
            int: The size of the square.
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.
        
        Args:
            value (int): The size of the square.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        """
        Calculates the area of the square.
        
        Returns:
            int: The area of the square.
        """
        return self.size ** 2


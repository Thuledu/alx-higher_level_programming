#!/usr/bin/python3
"""An empty class Square that defines a square"""
class Square:
    """
    A class that defines a square.
    
    Attributes:
        size (int): The size of the square.
    """
    
    def __init__(self, size):
        """
        Initializes a Square instance with a given size.
        
        Args:
            size: The size of the square.
        """
        self.__size = size
    
    def area(self):
        """
        Calculates the area of the square.
        
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2


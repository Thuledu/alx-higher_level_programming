#!/usr/bin/python3
"""A class Square that defines a square by: (based on 5-square.py)"""
class Square:
    """
    A class that defines a square.
    
    Attributes:
        size (int): The size of the square.
        position (tuple): The position of the square.
    """
    
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance.
        
        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square. Defaults to (0, 0).
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
            TypeError: If position is not a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position
        
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
    
    @property
    def position(self):
        """
        Getter method for the position attribute.
        
        Returns:
            tuple: The position of the square.
        """
        return self.__position
    
    @position.setter
    def position(self, value):
        """
        Setter method for the position attribute.
        
        Args:
            value (tuple): The position of the square.
        
        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    
    def area(self):
        """
        Calculates the area of the square.
        
        Returns:
            int: The area of the square.
        """
        return self.size ** 2
    
    def my_print(self):
        """
        Prints the square with the character '#'.
        
        If size is equal to 0, prints an empty line.
        Uses position to determine the starting position of the square.
        Does not fill lines by spaces when position[1] > 0.
        """
        if self.size == 0:
            print()
            return
        
        for _ in range(self.position[1]):
            print()
        
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)


#!/usr/bin/python3

# models/base.py
"""
Base module
"""

class Base:
    """
    Base class for managing id attribute in future classes
    """
    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        """
        Constructor for Base class
        Args:
            id (int): if not None, assign the public instance attribute id with this argument value,
                      otherwise, increment __nb_objects and assign the new value to the public instance attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

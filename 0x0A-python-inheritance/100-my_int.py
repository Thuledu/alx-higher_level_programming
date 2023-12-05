#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""

class MyInt(int):
    """Represents a MyInt class."""
    def __eq__(self, other):
        """Defines the inverted equality operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Defines the inverted inequality operator."""
        return super().__eq__(other)

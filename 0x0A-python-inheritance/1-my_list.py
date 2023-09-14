#!/usr/bin/python3
class MyList(list):
    """
    A class that inherits from the built-in `list` class.

    This class provides an additional method `print_sorted()` that prints the list in ascending order.
    """
	 def print_sorted(self):
        """
        Prints the list in ascending order.
	"""
		print (sorted(self))

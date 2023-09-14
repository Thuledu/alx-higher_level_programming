#!/usr/bin/python3
class MyInt(int):
    """
    A class representing a rebel integer.

    This class inherits from the int class and inverts the == and != operators.

    """

	def __eq__(self, other):
        """
        Override the == operator to invert the behavior.

        Args:
            other (Any): The object to compare with.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
		return int(self) != int(other)

	def __ne__(self, other):
        """
        Override the != operator to invert the behavior.

        Args:
            other (Any): The object to compare with.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
		return int(self) == int(other)

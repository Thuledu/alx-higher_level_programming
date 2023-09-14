#!/usr/bin/python3
class BaseGeometry:
    """
    A base class representing geometry.
    This class can be used as a base class for defining different geometric shapes and operations.
    """
	def area(self):
        """
        Calculate the area of the geometry.

        Raises:
            Exception: This method is not implemented.
	"""
		raise Exception("area() is not implemented")


	def integer_validator(self, name, value):
        	"""
        	Validate the value to be an integer greater than 0.

       		 Args:
            	 name (str): The name of the value being validated.
            	 value: The value to be validated.

        	 Raises:
            	 TypeError: If the value is not an integer.
            	 ValueError: If the value is less than or equal to 0.
		 """
		if not isinstance(value, int):
			raise TypeError("{} must be an integer".format(name))
		if value <= 0:
            	 	raise ValueError("{} must be greater than 0".format(name))


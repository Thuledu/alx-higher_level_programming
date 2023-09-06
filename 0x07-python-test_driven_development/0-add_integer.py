#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
    a (int or float): The first integer to be added.
    b (int or float): The second integer to be added. Default value is 98.

    Returns:
    int: The addition of a and b.

    Raises:
    TypeError: If a or b is not an integer or float.
    """

    # Check if a and b are integers or floats
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    # Cast a and b to integers if they are floats
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    # Add the integers
    result = a + b

    return result


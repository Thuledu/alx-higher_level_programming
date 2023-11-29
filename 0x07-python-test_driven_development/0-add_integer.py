#!/usr/bin/python3

def add_integer(a: int, b: int = 98) -> int:
    """
    Adds two integers.

    Args:
        a (int or float): First integer or float.
        b (int or float, optional): Second integer or float. Defaults to 98.

    Raises:
        TypeError: If a or b is not an integer or float.

    Returns:
        int: The addition of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b


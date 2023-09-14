#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or if the object is an instance of a class that inherited from, the specified class.
    Args:
        obj: The object to check.
        a_class: The specified class to compare against.
    Returns:
        True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise False.
    """
	if isinstance(obj, a_class):
		return True
	return False

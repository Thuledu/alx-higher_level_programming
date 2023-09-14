#!/usr/bin/python3
def add_attribute(obj, attr_name, attr_value):
    """
    Add a new attribute to an object if it's possible.

    Args:
        obj (object): The object to add the attribute to.
        attr_name (str): The name of the attribute.
        attr_value (Any): The value of the attribute.

    Raises:
        TypeError: If the attribute was not successfully added to the object.
    """
	if not hasattr(obj, attr_name) or getattr(obj, attr_name) != attr_value:
		raise TypeError("can't add new attribute")
	setattr(obj, attr_name, attr_value)

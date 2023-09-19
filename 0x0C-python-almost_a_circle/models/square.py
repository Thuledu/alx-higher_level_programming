#!/usr/bin/python3

from models.rectangle import Rectangle

class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square."""
        attribute_mapping = {
            0: "id",
            1: "x",
            2: "y",
            3: "size"
        }

        if args:
            for i, arg in enumerate(args):
                attribute = attribute_mapping.get(i)
                if attribute is not None:
                    if attribute == "id" and arg is None:
                        self.__init__(self.x, self.y, self.size)
                    else:
                        setattr(self, attribute, arg)

        elif kwargs:
            for k, v in kwargs.items():
                attribute = attribute_mapping.get(k)
                if attribute is not None:
                    if attribute == "id" and v is None:
                        self.__init__(self.x, self.y, self.size)
                    else:
                        setattr(self, attribute, v)

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "x": self.x,
            "y": self.y,
            "size": self.width
        }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

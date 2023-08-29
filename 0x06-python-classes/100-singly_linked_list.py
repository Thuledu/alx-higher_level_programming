#!/usr/bin/python3
"""A class Node that defines a node of a singly linked list"""
class Node:
    """
    This class represents a node of a singly linked list.

    Attributes:
    - data: The data stored in the node.
    - next_node: The next node in the linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a Node object with the given data and next_node.

        Parameters:
        - data: The data to be stored in the node.
        - next_node: The next node in the linked list (default: None).

        Raises:
        - TypeError: If data is not an integer or next_node is not a Node object or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data stored in the node.

        Returns:
        - The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data stored in the node.

        Parameters:
        - value: The data value to be set.

        Raises:
        - TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next node in the linked list.

        Returns:
        - The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the linked list.

        Parameters:
        - value: The next node value to be set.

        Raises:
        - TypeError: If value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This class represents a singly linked list.

    Attributes:
    - head: The head node of the linked list.
    """

    def __init__(self):
        """
        Initializes a SinglyLinkedList object with an empty list.
        """
        self.head = None

    def __str__(self):
        """
        Returns a string representation of the linked list.
        """
        current = self.head
        result = ""
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the linked list (increasing order).

        Parameters:
        - value: The value to be inserted.

        Raises:
        - TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node


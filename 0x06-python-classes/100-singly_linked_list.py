#!/usr/bin/python3
"""A class Node that defines a node of a singly linked list"""
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        result = ""
        current_node = self.head
        while current_node:
            result += str(current_node.data) + "\n"
            current_node = current_node.next_node
        return result

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node and value > current_node.next_node.data:
                current_node = current_node.next_node
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node

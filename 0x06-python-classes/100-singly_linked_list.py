#!/usr/bin/python3
"""
This Module Defines A class For:
- Singly Linked List
- Node
"""


class Node:
    """ Node For Linked List Class """
    __data = 0
    __next_node = None

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Returns Node Data """
        return self.__data

    @data.setter
    def data(self, value):
        """ Sets the Node Data """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Returns The Next Node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Sets The Next Node """
        if type(value) is Node or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """ Single Linked List Class """

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """ inserts a new Node in the list (increasing order) """
        new = Node(value)

        if not self.__head or value < self.__head.data:
            new.next_node = self.__head
            self.__head = new
        else:
            current = self.__head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new.next_node = current.next_node
            current.next_node = new

    def __str__(self):
        """ Prints The Linked List """
        result = ""
        current = self.__head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.rstrip()

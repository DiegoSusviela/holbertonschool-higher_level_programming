#!/usr/bin/python3
"""asd"""


class Node:
    """node in singly linked
    Attributes:
        __data (int): data
        __next_node (Node): next node
    """
    def __init__(self, data, next_node=None):
        """Initializes
        Args:
            data (int): data
            next_node (Node): next node
        Returns:
            None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data
        Returns:
            data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """data
        Args:
            value (int): datastored
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """get next_node
        Returns:
           next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """__next_node
        Args:
            value (Node): next node
        Returns:
            None
        """
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __str__(self):
        """String
        Returns:
            Formatted string 
        """
        return str(self.__data)


class SinglyLinkedList:
    """Representer
    Attributes:
        __head (Node): head
    """
    def __init__(self):
        """Initializer
        Returns:
            None
        """
        self.__head = None

    def sorted_insert(self, value):
        """ new Node instance 
        Args:
            value (int): data stored
        Returns:
            None
        """
        new = Node(value)
        tmp = self.__head
        if tmp is None or tmp.data >= value:
            if tmp:
                new.next_node = tmp
            self.__head = new
            return
        while tmp.next_node is not None:
            if tmp.next_node.data >= value:
                break
            tmp = tmp.next_node
        new.next_node = tmp.next_node
        tmp.next_node = new

    def __str__(self):
        """String SinglyLinkedList 
        Returns:
            Formatted string representing the linked list
        """
        string = ""
        tmp = self.__head
        while tmp is not None:
            string += str(tmp)
            if tmp.next_node is not None:
                string += "\n"
            tmp = tmp.next_node
        return string

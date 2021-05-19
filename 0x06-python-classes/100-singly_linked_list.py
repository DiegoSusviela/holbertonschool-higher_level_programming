#!/usr/bin/python3


class Node:
    """asd"""
    def __init__(self, data, next_node=None):
        """asd"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """asd"""
        return self.__data

    @data.setter
    def data(self, value):
        """asd"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """asd"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """asd"""
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __str__(self):
        """asd"""
        return str(self.__data)


class SinglyLinkedList:
    """asd"""
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

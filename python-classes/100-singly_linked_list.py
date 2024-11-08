#!/usr/bin/python3


class Node:
    """A class that represents a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize the node with data and an optional next_node.

        Args:
            data (int): The data of the node.
            next_node (Node or None): The next node in the list (default is None).

        Raises:
            TypeError: If data is not an integer or next_node is not a Node object.
        """
        self.data = data  # Use the setter to validate data
        self.next_node = next_node  # Use the setter to validate next_node

    @property
    def data(self):
        """Get the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node with validation.

        Args:
            value (int): The new data value.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node with validation.

        Args:
            value (Node or None): The next node.

        Raises:
            TypeError: If value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class that represents a singly linked list."""

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.head = None

    def __str__(self):
        """Return a string representation of the list."""
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position.

        Args:
            value (int): The data value to insert in the list.
        """
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node


# Author: Ditrung Duong
# GitHub username: ditrungduong
# Date: 11/3/2022
# Description: Using recursive to create a linked list with various methods: add, remove , insert, reverse, display and convert
#to plain list

class Node:
    """
        Represents a node in a linked list
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
        A linked list implementation of the List ADT
        """

    def __init__(self):
        self._head = None

    def get_head(self):
        """Return first node in the list"""
        if self._head is not None:
            return self._head

    def rec_add(self, current, val):
        """
        Helper function to add a node containing val to the linked list
        """
        if current is None:  # If the list is empty or the current node is None
            current = Node(val)  # new_node = self.head = Node(val)
            return current  # Base case
        else:
            # Recursive to go through next item in the list
            current.next = self.rec_add(current.next, val)
            return current

    def add(self, val):
        """ Add a node containing val to the linked list"""
        self._head = self.rec_add(self._head, val)

    def display(self):
        """
        Prints out the values in the linked list
        """
        current = self._head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def rec_remove(self, current, val):
        """Helper function to remove the node containing val from the linked list
        """
        if current is None:  # If the list is empty
            return
        elif current.data == val:  # Base case if val found
            current = current.next
            return current
        else:
            # Recursive until value found
            current.next = self.rec_remove(current.next, val)
            return current

    def remove(self, val):
        """
        Removes the node containing val from the linked list
        """
        self._head = self.rec_remove(self._head, val)

    def is_empty(self):
        """
        Returns True if the linked list is empty,
        returns False otherwise
        """
        return self._head is None

    def rec_contains(self, current, key):
        """
        Helper function to return contain value
        """
        if current is None:  # If the list is empty
            return False
        if current.data == key:
            return True
        return self.rec_contains(current.next, key)

    def contains(self, key):
        """ Returns True if the list contains a Node with the value key, otherwise returns False """
        return self.rec_contains(self._head, key)

    def rec_insert(self, current, new_value, pos):
        """Helper function for insert"""

        if current is None and pos > 0:
            return current
        # Adding new value to the first pos of the list
        if pos == 0:
            temp = Node(new_value)
            temp.next = current
            return current
        if pos == 1:
            temp = Node(new_value)
            temp.next = current.next
            current.next = temp
            return current
        # Recursion to go down to 1
        self.rec_insert(current.next, new_value, pos - 1)
        return current

    def insert(self, new_value, pos):
        """Insert value of new data with position indication"""
        self._head = self.rec_insert(self._head, new_value, pos)

    def rec_reverse(self, current):
        """"
        Helper function to reverses the linked list
        """
        # If the list is empty
        if current is None or current.next is None:
            return current
        if current is not None:
            # Recursive to the end of the list
            head_pos = self.rec_reverse(current.next)
            # Working backward the call stack to assign value
            current.next.next = current
            # Assigning each item in the call stack None to make it the end of the line
            current.next = None
        return head_pos

    def reverse(self):
        """Return the linked list"""
        self._head = self.rec_reverse(self._head)

    def rec_to_plain_list(self, current):
        """
        Helper function to return a regular Python list containing the same values, in the same order, as the linked list
        """
        if current is None:
            # Base case returning an empty list
            result = list()
            return result
        if current is not None:
            return [current.data] + self.rec_to_plain_list(current.next)

    def to_plain_list(self):
        """
        Return a regular Python list containing the same values, in the same order, as the linked list
        """
        return self.rec_to_plain_list(self._head)




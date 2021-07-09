"""
Singly linked list data structure implementation
"""


class Node:
    """
    The Node class represents an item in the Singly linked list. It holds the
    data of the current node and a pointer to the next node
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:
    """
    The linked list class builds the data structure by using nodes and traverses
    the list starting from the head node. The head node doesn't hold data but
    marks the starting point of the linked list
    """

    def __init__(self):
        self.head = Node(None)
        self.size = 0

    """
    The Append method inserts items at the end of the linked list. It traverse the 
    list until it gets to the last node which has the next point=None and inserts 
    the new node at the end
    """

    def Append(self, data):
        New_node = Node(data)
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = New_node

    """
    The pop method traverses the linked list to find the last element and removes 
    it from the linked list
    """

    def Pop(self):
        prev = None
        cur_node = self.head
        while cur_node.next is not None:
            prev = cur_node
            cur_node = cur_node.next
        cur_node.data = None
        prev.next = None

    """
    The size method returns the number of elements in the linked list
    """

    def Size(self):
        cur_node = self.head
        while cur_node.next != 0:
            cur_node = cur_node.next
            self.size += 1
        return self.size

    """
    Is_empty return True if the linked list is empty
    """

    def Is_empty(self):
        if self.size == 0:
            return True

    """
    String representation of the linked list
    """

    def __str__(self):
        elements = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            elements.append(cur_node.data)
        return f"{elements}"

"""
Stack data structure implementation
"""


class Stack:
    """
    The stack can have a maximum number of element specified the user. If the
     maxsize attribute is not specified the stack can take an arbitrary number of elements.
     This stack is implemented using the built in python list
    """

    def __init__(self):
        self.maxsize = 0
        self.items = []

    """
    The push method take an input item and push it to the top of the stack. if the maxsize
    of the stack is specified, it checks the whether the stack is full before pushing
    """

    def push(self, item):
        if self.maxsize == 0:
            self.items.append(item)
        else:
            if len(self.items) != self.maxsize:
                self.items.append(item)
            else:
                print("Stack full")

    """
    The pop method removes the item at the top of the stack and returns it
    """

    def pop(self):
        return self.items.pop()

    """
    The peek method returns the item on top of the stack. 
    """

    def peek(self):
        return self.items[-1]

    """
    The Is_empty method checks if the stack is empty and returns True if it is
    """

    def Is_empty(self):
        if not self.items:
            return True

    """
    The size method returns the number of elements in the stack
    """

    def size(self):
        return len(self.items)

    """
    The maxsize method is used to specify the maximum size of the stack
    """

    def Maxsize(self, maxsize):
        self.maxsize = maxsize

    """
    The Is_full method returns True is the stack is full.
    """

    def Is_full(self):
        if len(self.items) == self.maxsize:
            return True

    """
    String representation of the stack
    """

    def __str__(self):
        return f"{self.items}"

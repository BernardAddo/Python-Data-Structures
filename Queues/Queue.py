"""
Queue data structure implementation
"""


class Queue:
    """
    The Queue can have a maximum number of element specified the user. If the
     maxsize attribute is not specified the Queue can take and arbitrary number of elements.
     This Queue is implemented using the built in python list
    """

    def __init__(self):
        self.maxsize = 0
        self.items = []

    """
    The enqueue method first checks whether the queue is full. If not, it adds an item
    to the back of the queue
    """

    def enqueue(self, item):
        if self.maxsize == 0:
            self.items.insert(0, item)
        else:
            if len(self.items) != self.maxsize:
                self.items.insert(0, item)
            else:
                print("Queue is full")

    """
    The dequeue method remove and item from the front of the queue and returns it
    """

    def dequeue(self):
        return self.items.pop()

    """
    The peek method returns the element at the front of the queue
    """

    def peek(self):
        return self.items[-1]

    """
    The size method returns the number of element in the queue 
    """

    def size(self):
        return len(self.items)

    """
    The Is_empty return True if the queue is empty
    """

    def Is_empty(self):
        if not self.items:
            return True

    """
    The maxsize method specifies the maximum size of the queue
    """

    def Maxsize(self, maxsize):
        self.maxsize = maxsize

    """
    The Is_full method returns True if the Queue is full
    """

    def Is_full(self):
        if len(self.items) == self.maxsize:
            return True

    """
    The string representation of the Queue
    """

    def __str__(self):
        return f"{self.items}"

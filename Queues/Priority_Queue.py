"""
Priority Queue data structure implementation
"""


class PriorityQueue:
    """
    The priority queue returns items based on their priority. In this implementation, the greater
    the number, the higher its priority. Items added to the queue are also arranged based on its
    priority
    """
    def __init__(self):
        self.items = []

    """
    Items are added to the queue based on it priority. The enqueue method compares items in the 
    queue as inserts the new item accordingly
    """
    def enqueue(self, item):
        if not self.items:
            self.items.append(item)
        elif item < self.items[-1]:
            self.items.append(item)
        else:
            for x in range(len(self.items)):
                if item < self.items[x]:
                    continue
                else:
                    self.items.insert(x, item)
                    break
    """
    The Dequeue method removes the item with the highest priority in the queue 
    """
    def dequeue(self):
        return self.items.pop(0)

    """
    The peek method returns the item with the highest priority
    """
    def peek(self):
        return self.items[0]

    """
    The size method returns the size of the priority queue
    """
    def size(self):
        return len(self.items)

    """
    Is_empty returns True if the priority queue is empty
    """
    def Is_empty(self):
        if not self.items:
            return True

    """
    The string representation of the priority queue
    """
    def __str__(self):
        return f"{self.items}"

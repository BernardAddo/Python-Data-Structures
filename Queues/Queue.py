class Queue:
    def __init__(self):
        self.maxsize = 0
        self.items = []

    def enqueue(self, item):
        if self.maxsize == 0:
            self.items.insert(0, item)
        else:
            if len(self.items) != self.maxsize:
                self.items.insert(0, item)
            else:
                print("Queue is full")

    def dequeue(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def Is_empty(self):
        if not self.items:
            return True

    def Maxsize(self,maxsize):
        self.maxsize=maxsize

    def Is_full(self):
        if len(self.items) == self.maxsize:
            return True

    def __str__(self):
        return f"{self.items}"

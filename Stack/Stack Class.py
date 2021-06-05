class Stack:
    def __init__(self):
        self.maxsize = 0
        self.items = []

    def push(self, item):
        if self.maxsize == 0:
            self.items.append(item)
        else:
            if len(self.items) != self.maxsize:
                self.items.append(item)
            else:
                print("Stack full")

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.item[-1]

    def Is_empty(self):
        if not self.items:
            return True

    def size(self):
        return len(self.items)

    def Maxsize(self, maxsize):
        self.maxsize = maxsize

    def Is_full(self):
        if len(self.items) == self.maxsize:
            return True

    def __str__(self):
        return f"{self.items}"


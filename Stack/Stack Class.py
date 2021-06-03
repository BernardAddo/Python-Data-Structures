class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.item[-1]

    def Is_empty(self):
        if not self.items:
            return True
        else:
            return False

    def size(self):
        return len(self.item)

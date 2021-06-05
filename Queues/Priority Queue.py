class PriorityQueue:
    def __init__(self):
        self.items = []

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

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def Is_empty(self):
        if not self.items:
            return True

    def __str__(self):
        return f"{self.items}"


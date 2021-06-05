class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = Node(None)
        self.size = 0

    def Append(self, data):
        New_node = Node(data)
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = New_node

    def Pop(self):
        last_element = 0
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            last_element = cur_node.data
        return last_element

    def Insert(self):
        pass

    def Remove(self, index):
        pass

    def Size(self):
        cur_node = self.head
        while cur_node.next != 0:
            cur_node = cur_node.next
            self.size += 1
        return self.size

    def Is_empty(self):
        if self.size == 0:
            return True

    def __str__(self):
        elements = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            elements.append(cur_node.data)
        return f"{elements}"

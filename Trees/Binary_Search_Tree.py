"""
Binary Search Tree(BST) data structure implementation
"""


class Node:
    """
    The BST in made of of nodes. Each node could have a left child which is
    also a node or a right child
    """
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BST:
    """
    The first node in a BST is the root node and traversal of the tree starts
    from the root node
    """
    def __init__(self):
        self.root = None

    """
    The Insert method traverses the BST and compares the value of nodes with the 
    data to be added in order to insert the new node
    """
    def Insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert(data, self.root)
    """
    The insert methode is a helper method for the Insert method that get called recursively
    in order to insert the new node
    """
    def insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self.insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self.insert(data, cur_node.right)
        else:
            print("No duplicates allowed")

    """
    The search take a data input and traverses the true to find the data. if the data is found
    it returns "Found" if not, it returns "Not Found"
    """
    def Search(self, data):
        if self.root is not None:
            if self.find(data, self.root):
                print("Found")
            else:
                print("Not found")
        else:
            return None

    """
    The find method is a helper method for the Search method. it gets called recursively to find
    the inputted data  
    """
    def find(self, data, cur_node):
        if data < cur_node.data and cur_node.left:
            return self.find(data, cur_node.left)
        elif data > cur_node.data and cur_node.right:
            return self.find(data, cur_node.right)
        if data == cur_node.data:
            return True

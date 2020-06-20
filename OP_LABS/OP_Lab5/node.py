class Node:   # Node for our abstract syntax tree
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
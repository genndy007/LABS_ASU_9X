from node import Node

class AbstractSyntaxTree:
    def __init__(self, root=None):
        self.root = root

    def tree_generator(self, phrase):
        stack = []   # This is gonna be stack
        # Checking every symbol
        for symbol in phrase:
            # If it's an operator
            if symbol in '+-*/=':
                node = Node(symbol)
                node.right = stack.pop()  # Make node
                node.left = stack.pop()   # have
                stack.append(node)        # children
            # If it's a number
            else:    
                node = Node(symbol)
                stack.append(node)
        # Set root node
        node = stack.pop()
        self.root = node

    def exp_calc(self, root):
        if not root:   # If tree is empty
            return 0
        if not root.left and not root.right:   # If we get a number node
            val = float(root.value)
            return val

        value_left = self.exp_calc(root.left)
        value_right = self.exp_calc(root.right)
        
        operator = root.value
        # Checking arithmetic operation if node is operational
        if operator == '+':
            return value_left + value_right
        if operator == '-':
            return value_left - value_right
        if operator == '*':
            return value_left * value_right
        if operator == '/':
            return value_left / value_right
        if operator == '=':
            vars[str(value_left)] = value_right
            return
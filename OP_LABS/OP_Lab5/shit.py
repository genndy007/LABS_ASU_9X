def is_operator(c):
    if (c == '+' or c == '-' or c == '*'
        or c == '/' or c == '^'): 
        return True
    else: 
        return False
def evaluate_condition(condition, variables):
    for v in variables:
        if v in condition:
            condition = condition.replace(v, str(variables[v]))
    return eval(condition)
def parse_equation(equation):
    OPERATORS = ['+', '-', '/', '*', '(', ')']
    result = ''
    for char in equation:
        if char in OPERATORS:
            char = ' ' + char + ' '
        result += char
    while '  ' in result:
        result = result.replace('  ', ' ')
    return result.strip()
   
def shunting_yard(sentence):
        op = {'+': 1, '-':1, '*': 2, '/':2}
        stack = []
        formula = []
        for token in sentence:
            if token in op: 
                while stack and stack[-1] != "(" and op[token] <= op[stack[-1]]:
                    formula.append(stack.pop())
                stack.append(token)
            elif token == ")":
                while stack:
                    x = stack.pop()
                    if x == "(":
                        break
                    formula.append(x)
            elif token == "(":
                stack.append(token)
            else:
                formula.append(token)
        while stack:
            formula.append(stack.pop())
        return formula

class Parser:
    def __init__(self, filename):
        self.filename = filename
    def parse_expression(self):
        variables = dict()
        expressions = []
        conditions = []
        with open(self.filename, "r") as file:
            data = file.read().splitlines()
        global isif
        isif = False
        for x in data:
            if "if" in x:
                isif = True
        if isif:
            for x in range(len(data)):
                if "if" in data[x]:
                    c = data[x].replace("if","")[:-1].strip()
                    expressions.append(data[x+1].strip()[:-1])
                    conditions.append(c)
                if "else if" in data[x]:
                    c = data[x].replace("else if","")[:-1].strip()
                    expressions.append(data[x+1][:-1].strip())
                    conditions.append(c)
                if "else" in data[x]:
                    expressions.append(data[x+1].strip()[:-1])
                if "=" in data[x]:
                    d = data[x].split(" ")
                    variables[d[0].strip()] = float(d[2].replace(";", ""))
            for x in range(len(conditions)):
                conditions[x] = evaluate_condition(conditions[x], variables)
            try:
                expression = expressions[conditions.index(True)]
            except ValueError:
                expression = expressions[-1]
            expression = parse_equation(expression)
            return (expression, variables)
        else:
            expression = data[-1].replace(";", "")
            for x in range(len(data)-1):
                row = data[x].replace(";", "").split(" ")
                variables[row[0]] = row[2]
            expression = parse_equation(expression)
            return (expression, variables)
    def tranform_expression(self, expression, variables):
        for var in variables:
            while var in expression:
                expression = expression.replace(var, str(variables[var]))
        return shunting_yard(expression.split(" "))
    
class Node:
    def __init__(self,value,right=None, left=None):
        self.right = right
        self.left = left
        self.value = value

class AST:
    root = None
    def create_tree(self, sentence):
        stack = []
        for char in sentence:
            if not is_operator(char):
                node = Node(char)
                stack.append(node)
            else:
                node = Node(char)
                child1 = stack.pop()
                child2= stack.pop()
                node.right = child1
                node.left = child2
                stack.append(node)
        node = stack.pop()
        self.root = node
    
    def calculate_exp(self, root):
       if not root:
           return 0
       if(not root.left and not root.right):
           return float(root.value)
       l_val = self.calculate_exp(root.left)
       r_val = self.calculate_exp(root.right)
       if root.value =="+":
           return l_val+r_val
       if root.value =="-":
           return l_val-r_val
       if root.value == "*":
           return l_val*r_val
       if root.value =="/":
           return l_val/r_val

filename = "notacode.txt"      
parser = Parser(filename)
expression, variables = parser.parse_expression()
exp = parser.tranform_expression(expression, variables)
print(expression)
tree = AST()
tree.create_tree(exp)
print("Result: " + str(tree.calculate_exp(tree.root)))
from parser import Parser
from ast import AbstractSyntaxTree
import sys

input_name = sys.argv[1]  # Getting filename from cli
p = Parser(input_name)    # Creating a parser
exp, vars = p.parse()     # Getting an expression and variables with their values
exp = p.transform_exp(exp, vars)   # Get phrase thorugh shunting yard

tree = AbstractSyntaxTree()   # Initiating a tree
tree.tree_generator(exp)      # Filling it with nodes containing numbers or operators
print(f"Result: {tree.exp_calc(tree.root)}")   # Getting result of last line
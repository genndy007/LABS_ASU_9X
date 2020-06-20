from shunting_yard import shunting_yard_algorithm


def parse_equation(equation):  # Simple equation parser that makes equation look like el<space>el<space>...
    operators = '-+/*()'
    result = ''
    for symbol in equation:  # Check every symbol
        if symbol in operators:
            symbol = f" {symbol} "
        result += symbol

    while '  ' in result:  # Replace double spaces
        result = result.replace('  ', ' ')
    
    result = result.strip()
    return result 


class Parser:    # Parser for a file
    def __init__(self, name_file):
        self.name_file = name_file

    def parse(self):
        vars = dict()
        data = list()
        # Get 'code'
        file = open(self.name_file)
        for line in file:    # Reading phrases from text file 
            data.append(line.strip())
        file.close()
        # Getting rid of semicolons
        exp = data[-1].replace(';', '')
        for pos in range(len(data) - 1):
            line = data[pos].replace(';', '').split()
            vars[line[0]] = line[2]   # Pushing all variables to a dictionary

        exp = parse_equation(exp)
        return exp, vars

    def transform_exp(self, exp, vars):  # Changing variables in phrase into numbers
        for v in vars:
            while v in exp:
                exp = exp.replace(v, f"{vars[v]}")
        return shunting_yard_algorithm(exp.split())
def shunting_yard_algorithm(phrase):
    formula = list()  # Formula we are going to return
    stack = list()    # This list is going to be stack
    arithmetics = {'-': 0, '+': 0, '/': 1, '*': 1}  # All arithmetic operations
    for symbol in phrase:   # Checking every symbol
        # Checking if it's arithmetic operation
        if symbol in arithmetics:
            while len(stack) > 0 and stack[-1] != '(' and arithmetics[symbol] <= arithmetics[stack[-1]]:
                operator = stack.pop()
                formula.append(operator)
            stack.append(symbol)
        # If it's parenthesis
        elif symbol == '(':
            stack.append(symbol)
        # If it's other parenthesis
        elif symbol == ')':
            while len(stack) > 0:
                element = stack.pop()
                if element == '(': break
                formula.append(element)
        # If it's a number
        else:
            formula.append(symbol)
    # When there is no new elements to observe
    while len(stack) > 0:
        element = stack.pop()
        formula.append(element)
    return formula


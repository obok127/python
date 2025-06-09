def shunting_yard(tokens):
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    left_associative = {'+': True, '-':True,'*': True, '/':True, '^':False}

    output = []
    operator_stack = []

    for token in tokens:
        if token.isdigit():
            output.append(token)

        elif token in precedence:
            while (operator_stack and
                   operator_stack[-1] != '(' and
                   (precedence[operator_stack[-1]])> precedence[token] or
                   (precedence[operator_stack[-1]]== precedence[token] and
                    left_associative[token])):
                output.append(operator_stack.pop())
            operator_stack.append(token)

        elif token == '(':
            operator_stack.append(token)

        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())

            if operator_stack and operator_stack[-1]=='(':
                operator_stack.pop()

            else:
                raise ValueError("Mismatched parentheses")
            
    while operator_stack:
        if operator_stack[-1] in '()':
            raise ValueError("Mismatched parentheses")
        output.append(operator_stack.pop())
    
    return ' '.join(output)
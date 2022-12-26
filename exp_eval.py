# CSC 202 Project 2
# Nicole Arcolino

from stack_array import Stack

# You do not need to change this class
class PostfixFormatException(Exception):
    pass

operators = ["^", "**", "*", "/", "+", "-", "<<", ">>"]

operators_right = ["**", "^"]

operator_precedence = {
    "(": 1,
    "**":10,
    "^": 10,
    "*": 9,
    "/": 9,
    "+": 8,
    "-": 8,
    ">>": 7,
    "<<": 7
}

def handle_input(expression):
    tokens = []
    words = expression.split(" ")
    for i in words:
        if i in operators:
            tokens.append(i)
        else:
            tokens.append(to_a_number(i))
    return tokens


def to_a_number(token):
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            raise(PostfixFormatException(f"Invalid token"))

def is_a_number(token):
    try:
        int(token)
        return True
    except ValueError:
        try:
            float(token)
            return True
        except ValueError:
            return False

def calculate(operator, num1, num2):
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num2 - num1
    if operator == "/":
        if num1 == 0:
            raise ValueError
        return num2/num1
    if operator == "**":
        return num1 ** num2
    if operator == "*":
        return num1 * num2
    if operator == "<<":
        return num2 << num1
    if operator == ">>":
        return num2 >> num1
    else:
        return num1 ** num2

def postfix_eval(input_str):
    '''Evaluates a postfix expression
    
    Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** >> << or numbers.
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed
    DO NOT USE PYTHON'S EVAL FUNCTION!!!'''
    stack = Stack(30)
    tokens = handle_input(input_str)
    for token in tokens:
        if token in operators:
            try:
                num1 = stack.pop()
            except IndexError:
                raise PostfixFormatException("Insufficient operands")
            if num1 not in operators:
                try:
                    num2 = stack.peek()
                except IndexError:
                    raise PostfixFormatException("Insufficient operands")
                if num2 not in operators:
                    num2 = stack.pop()
                    stack.push(calculate(token, num1, num2))
            else:
                stack.push(num1)
        else:
            stack.push(token)
    if stack.size() > 1:
        raise PostfixFormatException("Too many operands")
    return stack.peek()


def infix_to_postfix(input_str):
    '''Converts an infix expression to an equivalent postfix expression

    Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << parentheses ( ) or numbers
    Returns a String containing a postfix expression '''
    operator_stack = Stack(30)
    postfix = []
    infix = input_str.split()
    for token in infix:
        # print(operator_stack.items)
        if is_a_number(token):
            postfix.append(token)
        elif token == "(":
            operator_stack.push(token)
        elif token == ")":
            num1 = operator_stack.pop()
            while num1 != "(":
                postfix.append(num1)
                num1 = operator_stack.pop()
        elif token in operators:
            while not operator_stack.is_empty() and ((token in operators_right and operator_precedence[token] <
                                                      operator_precedence[operator_stack.peek()]) or
                                                     (token not in operators_right and
                                                      operator_precedence[operator_stack.peek()] >=
                                                      operator_precedence[token])):
                try:
                    postfix.append(operator_stack.pop())
                except IndexError:
                    raise PostfixFormatException("Insufficient operands")
            operator_stack.push(token)
        else:
            raise (PostfixFormatException(f"Invalid token"))
    while not operator_stack.is_empty():
        postfix.append(operator_stack.pop())
    return " ".join(postfix)


def prefix_to_postfix(input_str):
    '''Converts a prefix expression to an equivalent postfix expression
    
    Input argument:  a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << or numbers
    Returns a String containing a postfix expression (tokens are space separated)'''
    operator_stack = Stack(30)
    tokens = handle_input(input_str)
    postfix = ''
    tokens = tokens[::-1]
    for token in tokens:
        if token not in operators:
            operator_stack.push(str(token))
        elif token in operators:
            try:
                o1 = operator_stack.pop()
            except IndexError:
                raise PostfixFormatException("Insufficient operands")
            try:
                o2 = operator_stack.pop()
            except IndexError:
                raise PostfixFormatException("Insufficient operands")
            result_postfix = o1 + " " + o2 + " " + token
            operator_stack.push(result_postfix)
        else:
            raise (PostfixFormatException("Invalid token"))
    if operator_stack.size() > 1:
        raise PostfixFormatException("Too many operands")
    return operator_stack.pop()



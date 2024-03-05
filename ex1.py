import sys

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        if self.top is None:
            self.top = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        return self.top.data if self.top is not None else None

    def is_empty(self):
        return self.top is None

def parse_sexpr(tokens):
    stack = Stack()

    while tokens:
        token = tokens.pop(0)
        if token.isdigit():
            stack.push(int(token))
        elif token in ['+', '-', '*', '/']:
            operands = []
            while not stack.is_empty() and isinstance(stack.peek(), int):
                operands.append(stack.pop())
            if token == '+':
                stack.push(sum(operands))
            elif token == '-':
                stack.push(operands[0] - sum(operands[1:]))
            elif token == '*':
                result = 1
                for operand in operands:
                    result *= operand
                stack.push(result)
            elif token == '/':
                stack.push(operands[0] / operands[1])
        elif token == '(':
            # Start a new recursive call to parse the sub-expression
            stack.push(parse_sexpr(tokens))
        elif token == ')':
            # End the current recursive call and return the result
            if not stack.is_empty():
                return stack.pop()

    # Return the result of the entire expression
    if not stack.is_empty():
        return stack.pop()
    else:
        return None

if len(sys.argv) > 1:
    expr = [i for i in sys.argv[1]]
    print(expr)
    result = parse_sexpr(expr)
    print(result)
else:
    print("No command line parameter provided")

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

def parse_expression(it):
    numbers = Stack()
    operators = Stack()

    for token in it:
        if token.isdigit():
            numbers.push(int(token))
        elif token in ['+', '-', '*', '/']:
            operators.push(token)
        elif token == '(':
            numbers.push(parse_expression(it))
        elif token == ')':
            break

    while not operators.is_empty():
        operator = operators.pop()
        num2 = numbers.pop() # num2 should is first due to the nature of stacks being LIFO
        num1 = numbers.pop()
        if operator == '+':
            numbers.push(num1 + num2)
        elif operator == '-':
            numbers.push(num1 - num2)
        elif operator == '*':
            numbers.push(num1 * num2)
        elif operator == '/':
            numbers.push(num1 / num2)

    return numbers.pop()

if len(sys.argv) > 1:
    expr = iter(sys.argv[1])
    result = parse_expression(expr)
    print(result)
else:
    print("No command line parameter provided")

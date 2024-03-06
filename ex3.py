class LinkedList_Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList_Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        if self.top is None:
            self.top = LinkedList_Node(data)
        else:
            new_node = LinkedList_Node(data)
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
    
class Array_Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1] if self.stack else None

    def is_empty(self):
        return not self.stack
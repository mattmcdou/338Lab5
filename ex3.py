import random
import timeit

def generate_tasks():
    tasks = [] # 10000 tasks within this array
    for _ in range(10000):
        task = 'push' if random.random() < 0.7 else 'pop'
        tasks.append(task)
    return tasks

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

Array_Stack_times = []
LinkedList_Stack_times = []

for _ in range(100):
    tasks = generate_tasks()

    array_stack = Array_Stack()
    start_time = timeit.default_timer()
    for task in tasks:
        if task == 'push':
            array_stack.push(1)
        else:  # task == 'pop'
            if not array_stack.is_empty():
                array_stack.pop()
    end_time = timeit.default_timer()
    Array_Stack_times.append(end_time - start_time)

    linkedlist_stack = LinkedList_Stack()
    start_time = timeit.default_timer()
    for task in tasks:
        if task == 'push':
            linkedlist_stack.push(1)
        else:  # task == 'pop'
            if not linkedlist_stack.is_empty():
                linkedlist_stack.pop()
    end_time = timeit.default_timer()
    LinkedList_Stack_times.append(end_time - start_time)

print("Average time for array stack implementation: ", sum(Array_Stack_times) / len(Array_Stack_times))
print("Average time for linked list stack Implementation: ", sum(LinkedList_Stack_times) / len(LinkedList_Stack_times))

import matplotlib.pyplot as plt

plt.hist(Array_Stack_times, bins=50, alpha=0.75, label='Array Stack')
plt.hist(LinkedList_Stack_times, bins=50, alpha=0.75, label='Linked List Stack')

plt.legend(loc='upper right')
plt.title('Task Execution Times for Array and Linked List Stack Implementations')
plt.xlabel('Time (s)')
plt.ylabel('Number of Occurrences')

plt.savefig("ex3.png")

'''
Q5) The array stack implementation is faster than the linked list stack implementation. This is because 
the array stack implementation has O(1) time complexity for push and pop operations, since it simply
has to add and remove elements to and from the END of the internal array, which does not require any traversal or
swapping of elements. 

Meanwhile, the linked list implementation of a stack has O(1) time complexity for push and pop operations, however,
it has to execute about 3 assignment/swapping operations to push and pop elements. This is because the linked list 
stack implementation has to create a new node and assign the next pointer to the top of the stack, and then reassign 
the top pointer to the new node. Similarly, when popping an element, the top pointer has to be reassigned to the 
next node in the stack. This results in execution times of given tasks approximately 3-4x slower than the array stack,
as depicted in ex3.png.
'''
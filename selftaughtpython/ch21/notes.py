# Example 1:
# Stacks


class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        last = len(self.items)-1
        return self.items[last]
    
    def size(self):
        return len(self.items)

# Create a new stack 

stack = Stack()
# it will be empty 
print(stack.is_empty()) 

# so let's add something to it
secondstack = Stack()
stack.push(1)
print(stack.is_empty())

# now let's remove something from it (because why the hell not) 
item = stack.pop()
print(item)
print(stack.is_empty())

# let's start over and use peek to look at the stacks contents and get the stack size 
thirdstack = Stack()

for i in range(0, 6):
    thirdstack.push(i)

print(thirdstack.peek())
print(thirdstack.size())

# Example 2
# Reversing a string with a stack

class Stack: 
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        last = len(self.items)-1
        return self.items[last]
    
    def size(self):
        return len(self.items)

stack = Stack()
for c in "Hello":
    stack.push(c)

reverse = ""

for i in range(len(stack.items)):
    reverse += stack.pop()

print(reverse)

# Example 3 
# Queue 

class Queue: 
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

# create a new empty queue 
a_queue = Queue()
print(a_queue.is_empty())

# let's add some stuff and check the queue size
a_queue = Queue()

for i in range(5):
    a_queue.enqueue(i)

print(a_queue.size())

# now let's remove each item from the queue 

a_queue = Queue()

for i in range(5):
    a_queue.enqueue(i)

for i in range(5):
    print(a_queue.dequeue())

print()

print(a_queue.size())

# Example 4
# ticket queue 

import time 
import random

from numpy import r_ 

class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def simulate_line(self, till_show, max_time):
        pq = Queue()
        tix_sold = []

        for i in range(100):
            pq.enqueue("person" + str(i))
        t_end = time.time() + till_show 
        now = time.time()
        while now < t_end and not pq.is_empty():
            now = time.time()
            r = random.randint(0, max_time)
            time.sleep(r)
            person = pq.dequeue()
            print(person)
            tix_sold.append(person)

        return tix_sold

queue = Queue()
sold = queue.simulate_line(5, 1)
print(sold)


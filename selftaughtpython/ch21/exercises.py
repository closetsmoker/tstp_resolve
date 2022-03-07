# 1. Reverse the string "yesterday" using a stack. 

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
for a in "yesterday":
    stack.push(a)

reverse = ""

for q in range(len(stack.items)):
    reverse += stack.pop()

print(reverse)

# 2. Use a stack to create a new list with the items in the following list reversed: [1, 2, 3, 4, 5]

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

forward = [1, 2, 3, 4, 5]
reverse = []

stack = Stack()

# this technically works but I don't think this was the goal 
# for a in range(1, 6):
#     stack.push(a)

for item in forward:
    stack.push(item)

# print the stack for the hell of it 
print(stack)

for q in range(len(stack.items)):
    reverse.append(stack.pop())

print(reverse)
# Write a Python class that simulates a Stack. The class should implement methods like push, pop, peek 
# (the last two methods should return None if no element is present in the stack).

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item): #adds an item to the top of the stack.
        self.stack.append(item)

    def pop(self): #removes and returns the top element of the stack
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self): #returns the top element of the stack without removing it
        if not self.is_empty():
            return self.stack[-1]
        return None  # Return None if the stack is empty

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print("Element ", my_stack.pop(), " was removed")  # Pop the top element (3)
print("The element from the top of the stack is:", my_stack.peek(), ". We didn't remove it")  # Peek at the top element (2)
print("The satck has dimension ", my_stack.size())  # Get the size of the stack (2)
print("Element ", my_stack.pop(), " was removed")  # Pop another element (2)
print("Element ", my_stack.pop(), " was removed")  # Pop the last element (1)
print("Element ", my_stack.pop(), " was removed")  # Try to pop from an empty stack (returns None)

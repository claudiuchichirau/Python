# Write a Python class that simulates a Queue. The class should implement methods like push, pop, peek (the last two methods 
# should return None if no element is present in the queue).

class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item): #adds an item to the queue.
        self.queue.append(item)

    def pop(self): #removes and returns the first element of the queue
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def peek(self): #returns the first element of the queue without removing it
        if not self.is_empty():
            return self.queue[0]
        return None

    def is_empty(self):
        return len(self.queue) == 0


my_queue = Queue()
my_queue.push(1)
my_queue.push(2)
my_queue.push(3)

print("Element ", my_queue.pop(), " was removed")  # Pop (1)
print("The element from the top of the stack is:", my_queue.peek(), ". We didn't remove it")  # Peek (2)
print("The element from the top of the stack is:", my_queue.peek(), ". We didn't remove it")  # Peek (2)
print("Element ", my_queue.pop(), " was removed")  # Pop another element (2)
print("Element ", my_queue.pop(), " was removed")  # Pop the last element (1)
print("Element ", my_queue.pop(), " was removed")  # Try to pop from an empty stack (returns None)

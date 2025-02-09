class Stack:
    def __init__(self):
        # Initialize an empty list to use as the stack
        self.stack = []

    def push(self, value):
        # Add an element to the top of the stack
        self.stack.append(value)

    def pop(self):
        # Remove and return the top element of the stack
        # If the stack is empty, print a message and return None
        if not self.stack:
            print("Stack is empty!")
            return
        return self.stack.pop()

    def peek(self):
        # Return the top element of the stack without removing it
        # If the stack is empty, print a message and return None
        if not self.stack:
            print("Stack is empty!")
            return
        return self.stack[-1]

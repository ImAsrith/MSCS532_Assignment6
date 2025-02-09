class Queue:
    def __init__(self):
        # Initialize an empty list to represent the queue
        self.queue = []

    def enqueue(self, value):
        # Add an element to the end of the queue
        self.queue.append(value)

    def dequeue(self):
        # Remove and return the element from the front of the queue
        # If the queue is empty, print a message and return None
        if not self.queue:
            print("Queue is empty!")
            return
        return self.queue.pop(0)

    def peek(self):
        # Return the element at the front of the queue without removing it
        # If the queue is empty, print a message and return None
        if not self.queue:
            print("Queue is empty!")
            return
        return self.queue[0]
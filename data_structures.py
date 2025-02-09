from dsa import Array, Matrix, Stack, Queue, SinglyLinkedList

def test_data_structures():
    # Testing Array
    print("Testing Array:")
    arr = Array(5)  # Create an array of size 5
    arr.insert(0, 10)  # Insert 10 at index 0
    arr.insert(1, 20)  # Insert 20 at index 1
    print("Array at index 0:", arr.of(0))  # Print value at index 0
    arr.delete(0)  # Delete value at index 0
    print("Array after deletion:", arr.of(0))  # Print value at index 0 after deletion
    arr.printArray()  # Print the entire array

    # Testing Matrix
    print("\nTesting Matrix:")
    matrix = Matrix(2, 2)  # Create a 2x2 matrix
    matrix.insert(0, 0, 5)  # Insert 5 at position (0,0)
    matrix.insert(0, 1, 10)  # Insert 10 at position (0,1)
    matrix.insert(1, 0, 15)  # Insert 15 at position (1,0)
    matrix.insert(1, 1, 20)  # Insert 20 at position (1,1)
    print("Matrix at (0,1):", matrix.of(0, 1))  # Print value at position (0,1)
    matrix.printMatrix()  # Print the entire matrix

    # Testing Stack
    print("\nTesting Stack:")
    stack = Stack()  # Create a stack
    stack.push(10)  # Push 10 onto the stack
    stack.push(20)  # Push 20 onto the stack
    print("Stack Peek:", stack.peek())  # Peek at the top of the stack
    stack.pop()  # Pop the top value from the stack
    print("Stack Peek after Pop:", stack.peek())  # Peek at the top of the stack after pop

    # Testing Queue
    print("\nTesting Queue:")
    queue = Queue()  # Create a queue
    queue.enqueue(10)  # Enqueue 10 into the queue
    queue.enqueue(20)  # Enqueue 20 into the queue
    print("Queue Peek:", queue.peek())  # Peek at the front of the queue
    queue.dequeue()  # Dequeue the front value from the queue
    print("Queue Peek after Dequeue:", queue.peek())  # Peek at the front of the queue after dequeue

    # Testing Linked List
    print("\nTesting Linked List:")
    linked_list = SinglyLinkedList()  # Create a singly linked list
    linked_list.insert_at_beginning(10)  # Insert 10 at the beginning of the list
    linked_list.insert_at_end(20)  # Insert 20 at the end of the list
    linked_list.traverse()  # Traverse and print the list
    linked_list.delete(10)  # Delete the node with value 10
    linked_list.traverse()  # Traverse and print the list again

if __name__ == "__main__":
    test_data_structures()  # Run the test function

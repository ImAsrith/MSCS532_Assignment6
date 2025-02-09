class Node:
    def __init__(self, value=None):
        self.value = value  # Initialize the node's value
        self.next = None  # Initialize the next pointer to None

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list to None

    def insert_at_beginning(self, value):
        new_node = Node(value)  # Create a new node with the given value
        new_node.next = self.head  # Point the new node's next to the current head
        self.head = new_node  # Update the head to be the new node

    def insert_at_end(self, value):
        new_node = Node(value)  # Create a new node with the given value
        if not self.head:  # If the list is empty
            self.head = new_node  # Set the new node as the head
            return
        last = self.head  # Start from the head
        while last.next:  # Traverse to the end of the list
            last = last.next
        last.next = new_node  # Set the last node's next to the new node

    def delete(self, value):
        temp = self.head  # Start from the head
        if temp and temp.value == value:  # If the head node is to be deleted
            self.head = temp.next  # Update the head to the next node
            temp = None  # Free the old head
            return
        prev = None
        while temp and temp.value != value:  # Traverse the list to find the node to delete
            prev = temp
            temp = temp.next
        if not temp:  # If the value was not found
            print("Node not found!")
            return
        prev.next = temp.next  # Unlink the node from the list
        temp = None  # Free the node

    def traverse(self):
        temp = self.head  # Start from the head
        while temp:  # Traverse the list
            print(temp.value, end=" -> ")  # Print the current node's value
            temp = temp.next  # Move to the next node
        print("None")  # Indicate the end of the list

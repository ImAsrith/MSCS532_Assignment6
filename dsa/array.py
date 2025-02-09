class Array:
    def __init__(self, size):
        # Initialize the array with the given size
        self.size = size
        self.arr = [None] * size

    def insert(self, index, value):
        # Insert value at the specified index
        if index >= self.size:
            print("Index out of range!")
            return
        self.arr[index] = value

    def delete(self, index):
        # Delete value at the specified index
        if index >= self.size:
            print("Index out of range!")
            return
        self.arr[index] = None

    def of(self, index):
        # Retrieve value at the specified index
        if index >= self.size:
            print("Index out of range!")
            return
        return self.arr[index]

    def printArray(self):
        # Print the entire array
        for i in range(self.size):
            print(self.arr[i], end=" ")
        print()

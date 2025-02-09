class Matrix:
    """
    A class to represent a matrix.

    Attributes
    ----------
    rows : int
        Number of rows in the matrix.
    cols : int
        Number of columns in the matrix.
    matrix : list of list
        2D list to store matrix elements.

    Methods
    -------
    __init__(rows, cols):
        Initializes the matrix with the given number of rows and columns.
    insert(row, col, value):
        Inserts a value at the specified row and column in the matrix.
    of(row, col):
        Retrieves the value at the specified row and column in the matrix.
    printMatrix():
        Prints the matrix in a formatted way.
    """
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[None] * cols for _ in range(rows)]

    def insert(self, row, col, value):
        if row >= self.rows or col >= self.cols:
            print("Index out of range!")
            return
        self.matrix[row][col] = value

    def of(self, row, col):
        if row >= self.rows or col >= self.cols:
            print("Index out of range!")
            return
        return self.matrix[row][col]
    def printMatrix(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.matrix[i][j], end=" ")
            print()
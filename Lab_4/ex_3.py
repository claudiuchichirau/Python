# Write a Python class that simulates a matrix of size NxM, with N and M provided at initialization. 
# The class should provide methods to access elements (get and set methods) and some methematical functions such as transpose, 
# matrix multiplication and a method that allows iterating through all elements form a matrix an apply a transformation over them 
# (via a lambda function).

class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.data = [[0 for _ in range(m)] for _ in range(n)]

    def get(self, i, j):
        if 0 <= i < self.n and 0 <= j < self.m:
            return self.data[i][j]
        return None

    def set(self, i, j, value):
        if 0 <= i < self.n and 0 <= j < self.m:
            self.data[i][j] = value

    def transpose(self):
        transposed = Matrix(self.m, self.n)
        for i in range(self.n):
            for j in range(self.m):
                transposed.set(j, i, self.get(i, j))
        return transposed

    def multiply(self, other):
        if self.m != other.n:
            return None  # Matrix multiplication is not possible
        result = Matrix(self.n, other.m)
        for i in range(self.n):
            for j in range(other.m):
                total = 0
                for k in range(self.m):
                    total += self.get(i, k) * other.get(k, j)
                result.set(i, j, total)
        return result

    def iterate(self):
        for i in range(self.n):
            for j in range(self.m):
                yield self.get(i, j)

# Example usage:
matrix = Matrix(3, 2)
matrix.set(0, 0, 1)
matrix.set(0, 1, 2)
matrix.set(1, 0, 3)
matrix.set(1, 1, 4)
matrix.set(2, 0, 5)
matrix.set(2, 1, 6)

print("Display first matrix:")
for element in matrix.iterate():
    print(element)

# Transpose the matrix
transposed_matrix = matrix.transpose()

# Multiply the matrix by its transpose
result_matrix = matrix.multiply(transposed_matrix)

print("\n Display multiplied matrix:")
# Iterate through all elements and print the transformed matrix
for element in result_matrix.iterate():
    print(element)

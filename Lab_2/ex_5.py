# Write a function that receives as parameter a matrix and will return the matrix obtained 
# by replacing all the elements under the main diagonal with 0 (zero).

def replace_with_zero(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    result_matrix = matrix.copy()

    for row in range(num_rows):
        for col in range(num_cols):
            if col < row:
                result_matrix[row][col] = 0

    return result_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = replace_with_zero(matrix)
for row in result:
    print(row)


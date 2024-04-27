def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

original_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed_matrix = transpose_matrix(original_matrix)
for row in transposed_matrix:
    print(row)

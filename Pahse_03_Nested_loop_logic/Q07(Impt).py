# Print a matrix, then calculate and display the sum of each row and the sum of each column.

matrix = [[1,2,3],[4,5,6],[7,8,9]]
num_rows = len(matrix)
num_cols = len(matrix[0])
for i in range(num_rows):
    sum_of_row = sum(matrix[i])
    print(f"Sum of row : {sum_of_row}")
for i in range(num_cols):
    sum_of_cols = 0
    for j in range(num_rows):
        sum_of_cols += matrix[j][i]
    print (f"Sum of column : {sum_of_cols}")






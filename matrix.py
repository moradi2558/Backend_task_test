def set_zeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
 
    zero_positions = [(i, j) for i in range(rows) for j in range(cols) if matrix[i][j] == 0]
    

    for i, j in zero_positions:

        for col in range(cols):
            matrix[i][col] = 0

        for row in range(rows):
            matrix[row][j] = 0
            
    return matrix


matrix = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
output = set_zeroes(matrix)
print(output) 
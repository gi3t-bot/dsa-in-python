# Brute Force
def marking_infinity(matrix, row, col):
    rows = len(matrix)
    cols = len(matrix[0])
    
    for i in range(rows):
        if matrix[i][col] != 0:
            matrix[i][col] = float("inf")

    for j in range(cols):
        if matrix[row][j] != 0:
            matrix[row][j] = float("inf")
            
            
    return matrix
                            
    
def setZeros(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    # iterating and looking for 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                marking_infinity(matrix, i , j)
                
                
    # iterating and marking infinity to 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == float("inf"):
                matrix[i][j] = 0
    
    
    
    # printing the matrix             
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end=" ")
            
        print()
                
                
                
matrix = [[7, 9, 2, 3], [10, 9, 0, 10], [29, 0, 5, 5], [4, 14, 3, 7]]
setZeros(matrix)



# Optimal solution
def setZeros(matrix):
    
    rows = len(matrix)
    cols = len(matrix[0])

    row_track = [0] * rows
    col_track = [0] * cols

    # looking for 0's
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                row_track[i] = -1
                col_track[j] = -1
                
    # assigning 0's
    for i in range(rows):
        for j in range(cols):
            if row_track[i] == -1 or col_track[j] == -1:
                matrix[i][j] = 0
            
    # printing the matrix             
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end=" ")
            
        print()
                
                
                
matrix = [[7, 9, 2, 3], [10, 9, 0, 10], [29, 0, 5, 5], [4, 14, 3, 7]]
setZeros(matrix)            

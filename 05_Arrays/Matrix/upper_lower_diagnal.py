# Upper triangle
matrix = [[5, 20, 3] , [7, 10, 9] , [1, -52, 6]]

rows = len(matrix)
cols = len(matrix[0])

for i in range(rows):
    for j in range(cols):
        if j >= i :
            print(matrix[i][j], end = " ")
            
        else:
            print("*", end = " ")
    
    print()


# Lower triangle
matrix = [[5, 20, 3] , [7, 10, 9] , [1, -52, 6]]

rows = len(matrix)
cols = len(matrix[0]) 

for i in range(rows):
    for j in range(cols):
        if j <= i :
            print(matrix[i][j], end = " ")
            
        else:
            print("*", end = " ")
    
    print()


# Diagonal
matrix = [[5, 20, 3] , [7, 10, 9] , [1, -52, 6]]

rows = len(matrix)
cols = len(matrix[0])

for i in range(rows):
    for j in range(cols):
        if j == i :
            print(matrix[i][j], end = " ")
            
        else:
            print("*", end = " ")
    
    print()


# Opposite Diagonal
matrix = [[5, 20, 3] , [7, 10, 9] , [1, -52, 6]]

rows = len(matrix)
cols = len(matrix[0])

for i in range(rows):
    for j in range(cols):
        if j + i == 2 :
            print(matrix[i][j], end = " ")
            
        else:
            print("*", end = " ")
    
    print()
# Brute force
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

n = len(matrix)
result = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        result[j][n-1-i] = matrix[i][j]
        
# printing the matrix             
for i in range(n):
    for j in range(n):
        print(result[i][j], end=" ")
        
    print() 
    


# Optimal solution
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = len(matrix)

# transpose of a matrix
for i in range(n):
    for j in range(i+1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
# printing the matrix             
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
        
    print()
        
for i in range(n):
    matrix[i].reverse()
    
# printing the matrix             
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
        
    print() 
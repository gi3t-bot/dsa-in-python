
matrix = [[5, 20, 3] , [7, 10, 9] , [1, -52, 6]]

rows = len(matrix)
cols = len(matrix[0])

for i in range(cols):
    for j in range(rows):
        print(matrix[j][i], end = " ")
            
    print()
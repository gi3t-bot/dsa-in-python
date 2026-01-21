# Brute Force
import math

n = 7
result = []

for i in range(n):
    row = []
    col = 0
    
    while col <= i:
        val = math.factorial(i) // (math.factorial(col) * math.factorial(i - col))
        row.append(val)
        
        col += 1
        
    result.append(row)
    
    
print(result)



# Optimal Solution
n = 7
result = []

for i in range(n):
    row = []
    col = 0
    
    while col <= i:
        if col == 0 or col == i:
            row.append(1)
            
        else:
            val = result[i-1][col-1] + result[i-1][col]
            
            row.append(val)
            
        col += 1
        
    result.append(row)
    
print(result)
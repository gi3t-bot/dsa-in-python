# Brute Force 
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

n = len(arr)
maximum = float("-inf")


for i in range(n):
    total = 0
    for j in range(i, n):
        total += arr[j]
        
        maximum = max(total, maximum)
    
    
print(maximum)


# Optimal Solution or Kadane's Algorithm
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

n = len(arr)
maximum = float("-inf")
total = 0

for i in range(n):
    total += arr[i]
    maximum = max(total, maximum)
    
    if total < 0:
        total = 0
        
print(maximum)
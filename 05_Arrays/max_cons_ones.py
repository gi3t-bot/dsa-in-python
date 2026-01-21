# Optimal Solution 
arr = [1, 1, 0, 1, 1, 0, 1, 1, 1, 1]
n = len(arr)
count = max_count = 0

for i in range(n) :
    if arr[i] == 1:
        count += 1
        
    else:
        max_count = max(count, max_count)
        count = 0
        
print(max(max_count, count))

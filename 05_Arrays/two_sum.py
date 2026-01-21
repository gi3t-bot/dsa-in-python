# Brute Force 
arr = [8, 1, 6, 2, 7, 3]
target = 7
n = len(arr)

for i in range(n-1):
    for j in range(i+1, n):
        if arr[i] + arr[j] == target:
            print(i , j)
            


# Optimal Solution
arr = [8, 1, 6, 2, 7, 3]
target = 7
n = len(arr)

freq = {}

for i in range(n):
    need = target - arr[i]
    
    if need in freq:
        print(i , freq[need])
        
    else:
        freq[arr[i]] = i
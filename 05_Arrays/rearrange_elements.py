# Brute Force
arr = [3,1,-2,-5,2,-4]
n = len(arr)

pos = []
neg = []

for i in range(n):
    if arr[i] < 0:
        neg.append(arr[i])
    
    else:
        pos.append(arr[i])  

for i in range(n//2):
    arr[2*i] = pos[i]
    arr[(2 * i) + 1] = neg[i]
    
print(arr)
    
    
# Optimal Solution
arr = [3,1,-2,-5,2,-4]
n = len(arr)

hash_map = [0] * n

positive_position = 0
negative_position = 1

for i in range(n):
    if arr[i] > 0:
        hash_map[positive_position] = arr[i]
        positive_position += 2
        
    else:
        hash_map[negative_position] = arr[i]
        negative_position += 2
        
print(hash_map)
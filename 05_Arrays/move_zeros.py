# Brute Force 
arr = [1,3,2,0,6,5,0,0,9,8,5]

n = len(arr)
temp = []

for i in arr:
    if i != 0:
        temp.append(i)


temp_len = len(temp)
for i in range(temp_len):
    arr[i] = temp[i]
    
for i in range(temp_len, n):
    arr[i] = 0
    
print(arr)


# Optimal Solution 

def move_zero(arr, i , n):
    
    # finding the position of first zero 
    while i < n:
        if arr[i] == 0:
            break
        
        i += 1

    # incase of no 0 in the array then do this
    if i == n:
        return arr
    
    j = i + 1
    
    while j < n:
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            
        j += 1
        
    return arr
             
arr = [1, 3, 2, 0, 6, 5, 0, 0, 9, 8, 0, 5]

i = 0
n = len(arr)
print(move_zero(arr, i , n))
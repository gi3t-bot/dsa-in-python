arr = [4, 5, 3, 6, 5, 6, 7, 7, 8, 3, 3, 9, 6, 1, 2]

n = len(arr)

for i in range(1, n):
    key = arr[i]
    j = i - 1
    
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -= 1
        
    arr[j+1] = key 
    
print(arr)
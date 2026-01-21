# bubble sort if the array is unsorted
arr = [9, 8, 7, 5, 3, 5, 7, 8, 9, 3, 5, 4, 4, 2, 1]
n = len(arr) - 2

for i in range(n, -1, -1):
    for j in range(i+1):
        if arr[j+1] < arr[j]:
            arr[j], arr[j+1] = arr[j+1] , arr[j]
        
print(arr)



# bubble sort if the array is sorted
arr = [9, 8, 7, 5, 3, 5, 7, 8, 9, 3, 54, 4, 2, 1]
n = len(arr) - 2

for i in range(n, -1, -1):
    is_swap = False
    for j in range(i+1):
        if arr[j+1] < arr[j]:
            arr[j], arr[j+1] = arr[j+1] , arr[j]   
            is_swap = True
            
    if is_swap == False:
        break 
    
print(arr)
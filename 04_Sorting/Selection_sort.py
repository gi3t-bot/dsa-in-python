arr = [9, 8, 7, 5, 3, 5, 7, 8, 9, 3, 54, 4, 2, 1]

for i in range(len(arr)):
    for j in  range(i+1, len(arr)):
        if arr[j] < arr[i]:
            arr[i] , arr[j] = arr[j] , arr[i]
            
print(arr)

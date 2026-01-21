# Step-2 Merging the array
def merger(left, right):
    result = []
    i = j = 0
    n = len(left)
    m = len(right)
    
    while i < n and j < m:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1 

        else:
            result.append(right[j])
            j += 1
            
    if i < n :
        while i < n :
            result.append(left[i])
            i += 1
            
    if j < m :
        while j < m:
            result.append(right[j])
            j += 1

    return result


# Step-1 Dividing the array
def divide_arr(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_arr = arr[ : mid]
    right_arr = arr[mid : ]
    
    left = divide_arr(left_arr)
    right = divide_arr(right_arr)
    
    return merger(left, right)


arr = [3,2,4,5,6,7,4,5,3,1,7,8,9,6,4,2]
print(divide_arr(arr))
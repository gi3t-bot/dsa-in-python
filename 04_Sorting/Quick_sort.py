def partition(arr, low, high):
    pivot = arr[(low + high) // 2]     # Middle pivot for stability
    i = low
    j = high
    
    while i <= j:
        
        while arr[i] < pivot:          # <--|
            i += 1                     #    |_____ finding out the position of i and j 
        while arr[j] > pivot:          #    |
            j -= 1                     # <--|  
            
        if i <= j:                             # <--|
            arr[i], arr[j] = arr[j], arr[i]    #    |_____ swapping the values at i and j if i < j
            i += 1                             #    |
            j -= 1                             # <--|
                                                 
    return i, j


def quick_sort(arr, low, high):
    if low < high:
        left, right = partition(arr, low, high)
        quick_sort(arr, left, high)     # Sorting for the right section
        quick_sort(arr, low, right)     # sorting for the left section
    return arr


# test
arr = [6, 3, 2, 1, 4, 9, 7]
print(quick_sort(arr, 0, len(arr)-1))

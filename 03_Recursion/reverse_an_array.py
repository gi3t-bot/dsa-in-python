# using recursion 
def reverse(arr, left, right):
    if left > right:
        return arr
    
    arr[left], arr[right] = arr[right], arr[left]
       
    return reverse(arr, left+1, right-1)
    
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverse(arr,0,9)



# using while loop 
def reverse(arr, l , r):
    while l < r:
        arr[l], arr[r] =  arr[r], arr[l]
        
        l += 1
        r -= 1
    
    return arr

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverse(arr,0,9)
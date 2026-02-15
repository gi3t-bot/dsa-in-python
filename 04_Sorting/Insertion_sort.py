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


# Another way for insertion sort
nums = [3, 5, 6, 4, 7, 4, 8, 9, 4, 2]

n = len(nums)

for i in range(1, n):
    if nums[i] >= nums[i-1]:
        continue
    
    else:
        temp = nums[i]
        j = i - 1
        
        while j >= 0 and nums[j] > temp:
            nums[j+1] = nums[j]
            j -= 1
            
        nums[j+1] = temp
    
print(nums)

# Upper bound = smallest index of an element, nums[mid] > target = also tells the position where the target must be placed if it is not present in the array

nums = [1, 1, 1, 2, 3, 3, 5, 5, 6, 7, 9, 12, 12, 13]
target = 4

n = len(nums)
low = 0 
high = n - 1
ub = n

while low <= high:
    mid = (low + high) // 2
    
    if nums[mid] > target:
        ub = mid
        high = mid - 1
        
    else:
        low = mid + 1
        
print(ub)
 
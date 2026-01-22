nums = [-1, 0, 3, 5, 9, 12]
target = 9

n = len(nums)
low = 0
high = n - 1
  
while low <= high:
    mid = (low + high)//2
    
    if nums[mid] == target:
        print(mid)
        break
        
    elif nums[mid] > target:
        high = mid - 1
        
    else:
        low = mid + 1
        
    
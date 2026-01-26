nums = [1, 2, 2, 2, 3, 3, 4, 5, 7, 7, 8, 8, 10]
target = 1

n = len(nums)
low = 0 
high = n - 1

start = -1

# lower bound of the target
while low <= high:
    mid = (low + high) // 2
    
    if nums[mid] >= target:
        start = mid
        high = mid - 1
        
    else:
        low = mid + 1
        
if start == -1 or nums[start] != target:
    print("[-1, -1]")
    
else:
    end = n
    low = 0 
    high = n - 1

    # upper bound of the target

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] > target:
            end = mid
            high = mid - 1

        else:
            low = mid + 1

    print([start, end - 1])
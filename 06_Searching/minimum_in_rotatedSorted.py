# Brute Force
nums = [4, 5, 6, 7, 0, 1, 2]

minimum = float("inf")

for i in nums:
    if i < minimum:
        minimum = i
        
print(minimum)


# Optimal solution
nums = [4, 5, 6, 7, 0, 1, 2]

minimum = float("inf")
n = len(nums)
low = 0 
high = n - 1

while low <= high:
    mid = (low + high) // 2
    
    if nums[mid] < nums[high]:
        minimum = min(minimum, nums[mid])
        high = mid - 1
        
    else:
        minimum = min(minimum, nums[low])
        low = mid + 1
        
print(minimum)
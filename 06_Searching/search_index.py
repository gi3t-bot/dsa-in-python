# Brute Force
nums = [1, 3, 5, 6, 8, 10, 12, 15, 18, 21]
target = 2

n = len(nums)
position = n

for i in range(n):
    if nums[i] > target:
        position = i 
        break
        
print(position)



# Optimal solution
nums = [1, 3, 5, 6, 8, 10, 12, 15, 18, 21]
target = 2

n = len(nums)
low = 0 
high = n - 1

position = n

while low <= high:
    mid = (low + high) // 2
    
    if nums[mid] >= target:
        position = mid
        high = mid - 1
        
    else:
        low = mid + 1
        
print(position)

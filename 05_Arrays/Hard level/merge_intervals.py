# Optimal Solution
intervals = [[1, 3], [8, 10], [15, 18], [2, 6]]

intervals.sort()

result = []

for nums in intervals:
    
    if not result:
        result.append(nums)
        
    else:
        last = result[-1]
        
        if nums[0] <= last[1]:
            last[1] = max(nums[1], last[1])
            
        else:
            result.append(nums)
            
print(result)
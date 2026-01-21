# Brute Force 
nums = [1, 2, 3, 2, 3, 2, 4, 3, 5, 1, 2, 1, 2, 3, 2, 4, 3, 4, 5, 3, 3, 2, 2, 3, 2, 3]
target = 8
n = len(nums)
result = set()

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            for l in range(k+1, n):
                if nums[i] + nums[j] + nums[k] + nums[l] == target:
                    temp = [nums[i], nums[j], nums[k], nums[l]]
                    temp.sort()
                    
                    result.add(tuple(temp))
                    
print([list(t) for t in result])




# Better Solution
nums = [1, 2, 3, 2, 3, 2, 4, 3, 5, 1, 2, 1, 2, 3, 2, 4, 3, 4, 5, 3, 3, 2, 2, 3, 2, 3]
target = 8
n = len(nums)
result = set()

for i in range(n):
    for j in range(i + 1, n):
        my_set = set()
        for k in range(j + 1, n):
            fourth = target - (nums[i] + nums[j] + nums[k])

            if fourth in my_set:
                temp = [nums[i], nums[j], nums[k], fourth]
                temp.sort()
                result.add(tuple(temp))

            my_set.add(nums[k])

print([list(t) for t in result])



# Optimal Solution
nums = [1, 2, 3, 2, 3, 2, 4, 3, 5, 1, 2, 1, 2, 3, 2, 4, 3, 4, 5, 3, 3, 2, 2, 3, 2, 3]
nums.sort()
n = len(nums)
target = 8
result = []

for i in range(n):
    if i > 0 and nums[i] == nums[i-1]:
        continue
    
    for j in range(i+1, n):
        if j > i+1 and nums[j] == nums[j-1]:
            continue
        
        k = j + 1
        l = n - 1
        
        while k < l:
            total = nums[i] + nums[j] + nums[k] + nums[l]
            
            if total < target:
                k += 1
                
            elif total > target:
                l -= 1
                
            else:
                temp = [nums[i], nums[j], nums[k], nums[l]]
                
                result.append(temp)
                k += 1
                l -= 1
                
                while k < l and nums[k] == nums[k-1]:
                    k += 1
                    
                while k < l and nums[l] == nums[l+1]:
                    l -= 1
                    
print(result)
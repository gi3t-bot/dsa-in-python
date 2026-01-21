# Brute Force 
nums = [-1, 0, 1, 2, -1, -4]

n = len(nums)
my_set = set()

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if nums[i] + nums[j] + nums[k] == 0:
                temp = [nums[i], nums[j], nums[k]]
                temp.sort()
                
                my_set.add(tuple(temp))
                
print([list(t) for t in my_set])


# Better Solution
nums = [-1, 0, 1, 2, -1, -4]

n = len(nums)
result = set()

for i in range(n):
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    
    my_set = set()
    for j in range(i+1, n):
        third = -(nums[i] + nums[j])
        
        if third in my_set:
            temp = [nums[i], nums[j], third]
            temp.sort()
            
            result.add(tuple(temp))
            
        my_set.add(nums[j])
        
print([list(t) for t in result])



# Optimal Solution
nums = [-1, 0, 1, 2, -1, -4]

n = len(nums)
result = []
nums.sort()

for i in range(n):
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    
    j = i + 1
    k = n - 1
    
    while j < k:
        total = nums[i] + nums[j] + nums[k]
        
        # checking if total is <0 or >0 or =0
        if total < 0 :
            j += 1
            
        elif total > 0:
            k -= 1
            
        else:
            temp = [nums[i], nums[j], nums[k]]
            result.append(temp)
            j += 1
            k -= 1
            
            # skipping the duplicates
            while j < k and nums[j] == nums[j-1]:
                j += 1
                
            while j < k and nums[k] == nums[k+1]:
                k -= 1
                
print(result)
    

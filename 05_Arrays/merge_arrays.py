# Merge two sorted arrays (with duplicates)
arr  = [1, 2, 2, 4, 7, 7, 9, 12]
nums = [1, 2, 3, 3, 4, 4, 8, 9, 9, 15]


result = []

i = j = 0
n = len(arr)
m = len(nums)

while i < n and j < m:
    if arr[i] < nums[j]:
        result.append(arr[i])
        i += 1
        
    else:
        result.append(nums[j])
        j += 1
        
        
if i < n:
    while i < n:
        result.append(arr[i])
        i += 1
        
if j < m:
    while j < m:
        result.append(nums[j])
        j += 1
        

print(result)

# Merge two sorted arrays (without duplicates)
arr  = [1, 2, 2, 4, 7, 7, 9, 12]
nums = [1, 2, 3, 3, 4, 4, 8, 9, 9, 15]


result = []

i = j = 0
n = len(arr)
m = len(nums)

while i < n and j < m:
    if arr[i] == nums[j]:
        if not result or result[-1] != arr[i]:
            result.append(arr[i])
        i += 1
        j += 1

        
    elif arr[i] < nums[j]:
        if not result or result[-1] != arr[i]:
            result.append(arr[i])
        i += 1
        
    else:
        if not result or result[-1] != nums[j]:
            result.append(nums[j])
        j += 1
    
if i < n:
    while i < n:
        if result[-1] != arr[i]:
            result.append(arr[i])
        i += 1

if j < m:
    while j < m:
        if result[-1] != nums[j]:
            result.append(nums[j])
        j += 1


print(result)

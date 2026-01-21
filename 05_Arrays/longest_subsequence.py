# Better solution
arr = [1, 99, 101, 98, 2, 5, 3, 100, 1, 1]

if not arr:
    print("0")
    
arr.sort()    
count = 1
max_length = 1

for i in range(1, len(arr)):
    if arr[i] == arr[i-1]:
        continue
    
    elif arr[i] - arr[i - 1] == 1:
        count += 1
        
    else:
        count = 1
        
    max_length = max(count, max_length)
    
print(max_length)



# Optimal solution
arr = [1, 99, 101, 98, 2, 5, 3, 100, 1, 1]

nums_set = set(arr)
max_length = 0

for nums in nums_set:
    if nums - 1 not in nums_set:
        current = nums
        count = 1
        
        while current + 1 in nums_set:
            count += 1
            current += 1
            
        max_length = max(count, max_length)
        
print(max_length)

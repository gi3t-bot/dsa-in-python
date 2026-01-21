# brute force
arr = [3,12,24,33,44,55,63,74,62,55,76,87,98,79,64,35,5]

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            arr[i] , arr[j] = arr[j], arr[i]
            
print(arr[-2])



# without sorting(Better solution)
arr = [3,12,24,33,44,55,63,74,62,55,76,87,98,79,64,35,5]

largest = float("-inf")
s_largest = float("-inf")

for i in range(len(arr)):
    largest = max(largest, arr[i])
    
for i in range(len(arr)):
    if arr[i] > s_largest and arr[i] != largest:
        s_largest = arr[i]
        
print(s_largest)



# without sorting (Optimal solution)
arr = [3,1,4,2,6,9,7,5]

largest = float("-inf")
s_largest = float("-inf")

for i in range(len(arr)):
    if arr[i] > largest:
        largest, s_largest = arr[i], largest
    
    if arr[i] > s_largest and arr[i] < largest:
        s_largest = arr[i]
        
print(s_largest)



# same as optimal approach just another way to write it 
arr = [3,12,24,33,44,55,63,74,62,55,76,87,98,79,64,35,5]

largest = float("-inf")
second = float("-inf")

for x in arr:
    if x > largest:
        second = largest
        largest = x
    elif x > second:
        second = x

print(second)
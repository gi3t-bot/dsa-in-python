# My method 
arr = [3,12,24,33,44,55,63,74,62,55,76,87,98,79,64,35,5]

arr.sort()

print(arr[-1])


# Another method 
arr = [3,12,24,33,44,55,63,74,62,55,76,87,98,79,64,35,5]
largest = arr[0]

for i in range (1, len(arr)):
    if arr[i] > largest:
        largest = arr[i]
        
print(largest)
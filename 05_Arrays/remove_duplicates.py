# not using inplace 
arr = [1,1,2,2,3,3,3,4,4,5,6,6,7,8,8,9,9,9,9]

unique = []

for i in arr:
    if i not in unique:
        unique.append(i)
        
        
print(len(unique))

# using inplace (Brute force)
arr = [1,1,2,2,3,3,3,4,4,5,6,6,7,8,8,9,9,9,9]

freq_map = {}

for i in arr:
    freq_map[i] = freq_map.get(i, 0)
    
j = 0
for k in freq_map:
    arr[j] = k
    j += 1

print(j)
print(arr[:j])


# using inplace (Optimal approach) I made it 
arr = [1,1,2,2,3,3,3,4,4,5,6,6,7,8,8,9,9,9,9]

point = 0

for i in range(1, len(arr)):
    if arr[i] != arr[point]:
        arr[point + 1] = arr[i]
        
        point += 1
        
print(point + 1)
print(arr[:point+1])


arr = [9,8,7,5,4,3,2,2,1]

i = 0
asc = True
desc = True

while i < len(arr)-1:
    
    if arr[i] > arr[i+1]:
        asc = False
        
    if (arr[i+1] > arr[i]):
        desc = False
        
    i += 1
    
if asc:
    print("Sorted Ascending")
elif desc:
    print("Sorted Descending")
else:
    print("Not Sorted")

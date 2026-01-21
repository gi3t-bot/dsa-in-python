# Better solution
arr = [9,6,4,2,3,5,7,0,1]
n = len(arr)
freq = {}

for i in range(n+1):
        freq[i] = 0
        
for i in freq.keys():
    if i in arr:
        freq[i] += 1 
    
for key, val in freq.items():
    if val == 0:
        print(key)
        
# Optimal solution (using sum feature)
arr = [9,6,4,2,3,5,7,0,1]
n = len(arr)
arr_sum = 0
sum = 0

for i in range(n+1):
    sum += i
    
for i in arr:
    arr_sum += i
    
print(sum - arr_sum) 

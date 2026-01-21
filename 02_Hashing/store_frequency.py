# method 1
nums = [5,6,6,7,8,5,2,3,1,3,5,7,9,9,6,3]

freq = {}

for i in nums:
    if i in freq.keys():
        freq[i] += 1
        
    else:
        freq[i] = 1
        
print(freq)


# method 2 

nums = [5,6,6,7,8,5,2,3,1,3,5,7,9,9,6,3]

freq = {}

for i in nums:
    freq[i] = freq.get(i, 0) + 1
    
print(freq)
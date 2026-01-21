# Brute force 
nums = [2, 3, 2, 1 ,2 ,3 ,4 ,3 ,2 ,3 ,2 ,3 ,3 ,3 ,3 ,2 ,2 ,1 ,2 ,3 ,3 ,3 ,3 ,2 ,3 ,3]

freq = {}
n = len(nums)
result = []

for i in nums:
    freq[i] = freq.get(i, 0) + 1
    
limit = n // 3

for k , v in freq.items():
    if v > limit:
        result.append(k)
        
print(result)
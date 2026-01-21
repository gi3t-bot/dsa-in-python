arr = [2, 2, 1, 1, 1, 2, 2]

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1
    
for key, value in freq.items():
    if value > len(arr) // 2:
        print("The majority element: ", key)
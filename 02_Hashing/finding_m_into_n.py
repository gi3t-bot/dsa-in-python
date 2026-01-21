# brute force
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

freq = {}
for i in m:
    count = 0
    for x in n:
        if x == i:
            count += 1
            
    freq[i] = count
            
print(freq)

# Hashmap

n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

hash_map = [0] * (len(n) + 1)

for i in n:
    hash_map[i] += 1
    
for j in m:
    print(j, end=":")
    if j < 1 or j > 10:
        print("0")
        
    else:
        print(hash_map[j])
        
        
# Hashmap using dictionary

n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

freq = {}

for i in n:
    freq[i] = freq.get(i, 0) + 1
    
for j in m:
    print(j, end=":") # for printing the values of keys
    print(freq.get(j , 0)) # for getting the values of the key[j] and returning 0 as default
    
    
# Character hashing

s = ['g', 'a', 'q', 'm', 'b', 'p', 's', 'g', 'z', 'a', 'l', 'v', 'k', 't', 'f', 'c', 'm', 'x', 'a', 'r', 'g', 'e', 'd', 'y', 'o', 'q']

q = ['a', 'e', 'i', 'o', 'u']

freq = [0] * 26

for ch in s:
    ascii_value = ord(ch)
    index = ascii_value - 97
    freq[index] += 1
    
    
for ch in q:
    ascii_value = ord(ch)
    index = ascii_value - 97
    
    print(freq[index])
    
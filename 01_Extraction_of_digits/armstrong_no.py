n = 153
count = 0
num = n

while num > 0:
    count += 1
    num //= 10

# print(count)

new_num = n 
result = 0   
while new_num > 0:
    ld = new_num % 10
    result += ld ** count
    new_num //= 10 
    
print(result == n)
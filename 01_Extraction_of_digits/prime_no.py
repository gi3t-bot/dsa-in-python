num = 1
count = 0
for i in range(2, (num//2 + 1)):
    if num % i == 0:
        count += 1
        
if count == 0:
    print("Prime No")

else:
    print("Not a prime")
    

num = 10
# is_prime = False

for i in range(2, num):
    if num % i == 0:
        print("not prime")
        break
        
    else:
        print("prime")
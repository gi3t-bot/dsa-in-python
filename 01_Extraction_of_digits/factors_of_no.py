# my method (brute force)
n = 121
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")
print("")

# better solution
n = 121
factors = []

for i in range(1, n//2 + 1):
    if n % i == 0:
        factors.append(i)
    
factors.append(n)
print(factors)


# optimal solution(what I thought)
n = 121
factors = []
i = 1

while i not in factors:
    if n % i == 0:
        factors.append(i)
        num = n // i
        factors.append(num)
        
    i += 1

print(list(set(factors)))


# optimal solution(what Sir taught)
from math import sqrt
n = 121
factors = []

for i in range(1, int(sqrt(n)) + 1):
    if n % i == 0:
        factors.append(i)
        if n//i != i:
            factors.append(n//i)
        
print(sorted(factors))
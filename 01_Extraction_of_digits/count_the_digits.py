# my method
num = 123456
count = 0

while num > 0:    
    count += 1
    num //= 10
    
print(count)



# Another method (best approach)
from math import *
num = 123456
print(int(log10(num)+1))
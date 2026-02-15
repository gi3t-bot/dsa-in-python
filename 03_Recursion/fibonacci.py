def fib(num):
    if num == 0 or num == 1:
        return num
    
    return fib(num - 1) + fib(num - 2)


fib(7)


fibo = []
n = 5
i = -1
j = 1

for _ in range(n):
    add = i + j
    fibo.append(add)
    i, j = j , add 
    
print(fibo)
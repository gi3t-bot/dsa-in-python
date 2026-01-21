def factorial(n):
    if n == 1:
        return 1
    
    return n * factorial(n-1)


factorial(4)



def factorialNumbers(n):
    i = 1
    
    if i > n:
        return 1
    
    print(i)    
    i += 1
    factorialNumbers(n-1)




def factorialNumbers(n):
        num = 1
        for i in range(1, n+1):
            num *= i
            print(num)


factorialNumbers(4)
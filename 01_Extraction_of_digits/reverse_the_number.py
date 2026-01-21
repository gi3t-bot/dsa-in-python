num = 67394758

while num > 0:
    last_digit = num % 10
    print(last_digit, end="")
    
    num //= 10

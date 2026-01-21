# Brute Force
arr = [7, 1, 5, 3, 6, 4, 8]
n = len(arr)
profit = 0
max_profit = 0

for i in range(n):
    for j in range(i+1, n):
        profit = arr[j] - arr[i]
        max_profit = max(profit, max_profit)
        

print(max_profit)


# Optimal Solution
arr = [7, 1, 5, 3, 6, 4]
n = len(arr)
min_price = arr[0]
max_profit = 0

for i in range(n):
    if arr[i] < min_price:
        min_price = arr[i]   
    
    else:
        profit = arr[i] - min_price
        max_profit = max(max_profit, profit)

print(max_profit)
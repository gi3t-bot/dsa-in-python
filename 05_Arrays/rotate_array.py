# Rotate array by 1 place
arr = [1,2,3,4,5,6,7]
n = len(arr)

arr = arr[n-1:] + arr[:n-1]

print(arr)



# Another method for rotation by 1 place
arr = [1,2,3,4,5,6,7]
n = len(arr)
temp = arr[n-1]

for i in range(n-2, -1, -1):
    arr[i + 1] = arr[i]

arr[0] = temp

print(arr)


# Rotating array by k places (using slicing)
arr = [1,2,3,4,5,6,7]
n = len(arr)
k = 4
     
arr = arr[n-k:] + arr[:n-k]

print(arr)


# Optimal Solution
# Rotating array by k places (without using slicing)

def reverse(arr, l, r):
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

arr = [1,2,3,4,5,6,7]
n = len(arr)
k = 5 % n

# reverse whole array
reverse(arr, 0, n-1)

# reverse first k elements
reverse(arr, 0, k-1)

# reverse remaining elements
reverse(arr, k, n-1)

print(arr)


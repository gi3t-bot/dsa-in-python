nums = [3, 4, 4, 4, 8, 9, 9, 10, 12, 12, 14, 15]
target = 6

n = len(nums)
floor = ceil = -1

low = 0
high = n - 1

# finding the floor
while low <= high:
    mid = (low + high) // 2

    if nums[mid] <= target:
        floor = mid
        low = mid + 1
    else:
        high = mid - 1

low = 0
high = n - 1

# finding the ceil
while low <= high:
    mid = (low + high) // 2

    if nums[mid] >= target:
        ceil = mid
        high = mid - 1
    else:
        low = mid + 1

print(
    nums[floor] if floor != -1 else -1,
    nums[ceil] if ceil != -1 else -1
)

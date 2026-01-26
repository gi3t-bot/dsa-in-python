nums = [45, 48, 52, 55, 59, 63, 67, 71, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 1, 4, 7, 10, 14, 18, 22, 26, 30, 35, 40]
target = 3

n = len(nums)
low = 0
high = n - 1

found = False

while low <= high:
    mid = (low + high) // 2

    if nums[mid] == target:
        print(mid)
        found = True
        break

    if nums[mid] <= nums[high]:
        if nums[mid] <= target <= nums[high]:
            low = mid + 1
        else:
            high = mid - 1
    else:
        if nums[low] <= target <= nums[mid]:
            high = mid - 1
        else:
            low = mid + 1

if not found:
    print("-1")

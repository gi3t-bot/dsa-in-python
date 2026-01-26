nums = [45, 48, 52, 55, 59, 63, 67, 71, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 1, 4, 7, 10, 14, 18, 22, 26, 30, 35, 40]
target = 4

low = 0
high = len(nums) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if nums[mid] == target:
        found = True
        break

    # handle duplicates
    if nums[low] == nums[mid] == nums[high]:
        low += 1
        high -= 1
        continue

    # if right half is sorted
    if nums[mid] <= nums[high]:
        if nums[mid] < target <= nums[high]:
            low = mid + 1
        else:
            high = mid - 1

    # if left half is sorted
    else:
        if nums[low] <= target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1

print(found)

# Method-1

def largestSumAfterKNegations(nums, k):
    nums.sort()
    n = len(nums)
    i = 0

    while(i < n and k  >0):
        if nums[i] < 0:
            nums[i] = -nums[i]
            k -= 1
            i += 1
        elif nums[i] >= 0:
            break
    if k % 2 == 1:
        return sum(nums) - 2 * (min(nums))
    else:
        return sum(nums)

# Time Complexity : O(nlogn)
# Space Complexity : O(1)
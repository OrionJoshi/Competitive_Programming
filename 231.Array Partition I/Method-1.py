# Method-1

def arrayPairSum(nums):
    nums.sort(reverse = True)
    totalSum = 0
    idx = 0

    while idx < len(nums):
        totalSum += nums[idx + 1]
        idx += 2

    return totalSum

# Time Complexity : O(nlogn)
# Space Complexity : O(1)
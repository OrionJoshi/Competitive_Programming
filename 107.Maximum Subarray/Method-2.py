# Method-2

def maxSubArray(nums):
    maxSumAtIndex = [None for x in nums]
    maxSumAtIndex[0] = nums[0]
    i = 1

    for num in nums[1:]:
        maxSumAtIndex[i] = max(num, maxSumAtIndex[i - 1] + num)
        i += 1

    return max(maxSumAtIndex)

# Time Complexity : O(n)
# Space Complexity : O(n)
# Method-1

def findMiddleIndex(nums):
    leftSum = 0
    rightSum = sum(nums)

    for i in range(len(nums)):
        rightSum  -= nums[i]
        if leftSum == rightSum:
            return i
        leftSum += nums[i]

    return -1

# Time Complexity : O(n)
# Space Complexity : O(1)
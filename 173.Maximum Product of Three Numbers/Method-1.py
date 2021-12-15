# Method-1 Sorting

def maximumProduct(nums):
    length = len(nums)
    nums.sort()
    firstMul = nums[0] * nums[1]* nums[length - 1]
    secondMul = nums[length - 3] * nums[length - 2] * nums[length - 1]

    return max(firstMul, secondMul)

# Time Complexity : O(nlogn)
# Space Complexity : O(1)
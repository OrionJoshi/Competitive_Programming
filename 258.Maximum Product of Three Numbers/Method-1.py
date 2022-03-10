# Method-1

def maximumProduct(nums):
    nums.sort()

    return max(nums[0] * nums[1] * nums[-1], nums[-3] * nums[-2] * nums[-1])

# Time Complexity : O(nlogn)
# Space Complexity : O(1)
# Method-1 Sorting

def maxProductDifference(nums):
  nums.sort()
  return nums[-1]*nums[-2] - nums[0]*nums[1]

# Time Complexity : O(nlogn)
# Assuming best sorting used
# space Complexity : O(1)

# Input: nums = [5,6,2,7,4]
# Output: 34
# Explanation: We can choose indices 1 and 3 for the first pair (6, 7)
# and indices 2 and 4 for the second pair (2, 4).
# The product difference is (6 * 7) - (2 * 4) = 34.
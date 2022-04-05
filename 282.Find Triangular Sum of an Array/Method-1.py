# Method-1

def triangularSum(nums):
    n = len(nums)
    while n > 0:
      for i in range(n-1):
        nums[i] = (nums[i] + nums[i+1]) % 10
      n -= 1
    return nums[0]

# Time Complexity : O(n)
# Space Complexity : O(1)
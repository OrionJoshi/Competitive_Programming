# Method-1

def firstMissingPositive(nums):
  for i in range(len(nums)):
    if nums[i] < 0:
      nums[i] = 0
  
  for i in range(len(nums)):
    currValue = abs(nums[i])
    if currValue <= len(nums) and currValue > 0:
      if nums[currValue - 1] > 0:
        nums[currValue - 1] *= -1
      elif nums[currValue - 1] == 0:
        nums[currValue - 1] = -1 * (len(nums) + 1)

  for i in range(1,len(nums) + 1):
    if nums[i - 1] >= 0:
      return i
      
  return len(nums) + 1

# Time Complexity : O(n)
# Space Complexity : O(1)
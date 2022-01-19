# Method-1 Using Sorting and pointer

def threeSum(nums):
  res = []
  nums.sort()
  
  for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i - 1]:
      continue
    
    left = i + 1
    right = len(nums) - 1
    
    while left < right:
      currSum =   nums[i] + nums[left] + nums[right]
        
      if currSum < 0:
        left += 1
      elif currSum > 0:
        right -= 1
      else:
        res.append([nums[i], nums[left], nums[right]])
        left += 1
        
        while left < right and nums[left - 1] == nums[left]:
          left += 1
                  
  return res

# Time Complexity : O(n^2)
# Space Complexity : O(1)

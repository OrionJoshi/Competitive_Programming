# Method-1

def duplicateZeros(nums):
    length = len(nums)
    ptr = 0
    result = []
    while(length > len(result)):
      if nums[ptr] == 0:
          result += [0, 0]
      else:
          result.append(nums[ptr])
      ptr += 1
    return result

# Time Complexity  : O(n)
# Space Complexity : O(n)

# Input: nums = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
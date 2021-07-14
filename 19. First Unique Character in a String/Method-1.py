# Method-1 Using Hash Map
def firstUniqueCharacter(str):
  strLen = len(str)
  nums = {}  # empty hash
  for i in range(strLen):
    if str[i] not in nums:
      nums[str[i]] = 1
    else:
      nums[str[i]] += 1

  for i in range(len(str)):
    if(nums[str[i]] == 1):
      return i

  return -1

# Time Complexity : O(n)
# Space Complexity : O(n)
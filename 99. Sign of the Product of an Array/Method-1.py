def arraySign(nums):

  numNeg = 0
  numZero = 0

  for num in nums:

    if num < 0:
      numNeg += 1

    elif num == 0:
      numZero += 1

  if numZero > 0:
    return 0

  if numNeg % 2 == 0:
    return 1

  return -1

# Time Complexity : O(n)
# Space Complexity : O(1)

#  Input: nums = [-1,-2,-3,-4,3,2,1]
#  Output: 1
#  Explanation: The product of all values
#  in the array is 144, and signFunc(144) = 1
# Method-1 Using Kadanes Algorithm (Dynamic programming)

def kadanesAlgorithm(array):
  maxAtThisPoint = array[0]
  finalMax = array[0]

  for num in array[1:]:
    maxAtThisPoint = max(num, maxAtThisPoint + num)
    finalMax = max(finalMax, maxAtThisPoint)

  return finalMax

# Time Complexity : O(n)
# Space Complexity : O(1)
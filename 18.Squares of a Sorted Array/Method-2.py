# Method-2 Using pointer

def sqrtSortedList(lst):
  leftIdx = 0
  rightIdx = len(lst) -1

  # Sorting elements ignoring signs
  while leftIdx < rightIdx:
    leftSqrt = pow(lst[leftIdx], 2) 
    rightSqrt = pow(lst[rightIdx], 2)

    if leftSqrt > rightSqrt:
      lst[leftIdx], lst[rightIdx] = lst[rightIdx], lst[leftIdx]
    rightIdx -= 1
  
  # squaring all the elements
  for i in range(len(lst)):
    lst[i] **= 2
  return lst;

# # Time Complexity : O(n)
# # Space Complexity : O(1)
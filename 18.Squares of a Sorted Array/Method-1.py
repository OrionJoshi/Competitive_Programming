# Method-1 Using sorting technique

def sqrtOfSortedList(lst):
  # square all elements
  for x in range(0, len(lst)):
    lst[x] = pow(lst[x], 2)
  
  # sort the resulted array
  lst.sort() # Assuming best sorting technique
  
  return lst

# Time Complexity : O(nlog)
# Space Complexity : O(1)

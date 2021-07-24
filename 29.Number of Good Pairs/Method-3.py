# Method-3
from itertools import combinations
 
def noOfGoodPairs(lst):

  comb = combinations(lst, 2)
  count = 0

  for i, j in list(comb):
      if i == j:
          count += 1
  return count

# Time Complexity : O(n^2)
# Space Complexity : O(1)

# Method-1

import math

def isPowerOfFour(n):
  return math.ceil(math.log(n, 4)) == math.floor((math.log(n, 4))) if n > 0 else False

# Time Complexity : O(1)
# Space Complexity : O(1)
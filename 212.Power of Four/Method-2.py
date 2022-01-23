# Method-2

import math

def isPowerOfFour(n):
  return math.log(n, 4) == int(math.log(n, 4)) if n > 0 else False

# Time Complexity : O(1)
# Space Complexity : O(1)
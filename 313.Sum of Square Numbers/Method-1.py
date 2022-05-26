# Method-1

import math

def judgeSquareSum(c):
    if c < 3:
        return True
    
    low = 0
    high = int(math.sqrt(c))
    
    while low <= high:
        val = low * low + high * high
        if val == c:
            return True
        elif val < c:
            low += 1
        else:
            high -= 1
    
    return False

# Time Complexity : O(nlogn)
# Space Complexity : O(1)
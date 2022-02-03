# Method-2 Brute Force

import math

def minEatingSpeed(piles, h):
    maxNum = max(piles)
    for i in range(1, maxNum + 1):
        currHour = 0
        for j in range(len(piles)):
            currHour += math.ceil(piles[j] / i)
            
        if currHour <= h:
            return i
            
    return -1

# Time Complexity : O(max(piles) * n)
# Space Complexity : O(1)